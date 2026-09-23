#!/usr/bin/env python3
"""Local deterministic state validation, event reduction and visual rendering."""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(state):
    return hashlib.sha256(json.dumps(state, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def validate(s):
    require(isinstance(s, dict), 'State must be an object')
    require(s.get('version') == 1, 'Unsupported version')
    require(isinstance(s.get('session'), str) and 1 <= len(s['session']) <= 100, 'Missing session')
    require(type(s.get('revision')) is int and s['revision'] >= 0, 'Invalid revision')
    require(s.get('phase') in ('interview', 'review', 'approved'), 'Invalid phase')
    require(s.get('layout') in ('focus', 'board'), 'Invalid layout')
    require(isinstance(s.get('goal'), str) and len(s['goal']) <= 6000, 'Invalid goal')
    ds = s.get('decisions')
    require(isinstance(ds, list) and len(ds) <= 60, 'Invalid decisions')
    ids = [d.get('id') for d in ds if isinstance(d, dict)]
    require(len(ids) == len(ds) and all(isinstance(x, str) and x for x in ids) and len(set(ids)) == len(ids), 'Duplicate or invalid decision IDs')
    for d in ds:
        require(d.get('status') in ('open', 'answered', 'deferred'), 'Invalid decision status')
        require(isinstance(d.get('label'), str) and isinstance(d.get('answer', ''), str), 'Invalid decision text')
        require(d['status'] != 'answered' or bool(d.get('answer', '').strip()), 'Answered decision needs an answer')
        require(isinstance(d.get('depends_on', []), list) and all(x in ids and x != d['id'] for x in d.get('depends_on', [])), 'Invalid dependency')
    def visit(key, trail):
        require(key not in trail, 'Cyclic dependency')
        for parent in next(d for d in ds if d['id'] == key).get('depends_on', []):
            visit(parent, trail | {key})
    for key in ids:
        visit(key, set())
    for key in ('assumptions', 'sources'):
        require(isinstance(s.get(key), list) and all(isinstance(x, str) for x in s[key]), 'Invalid ' + key)
    q = s.get('question')
    if s['phase'] == 'interview':
        require(isinstance(q, dict) and q.get('id') in ids, 'Question must match a decision')
        require(all(isinstance(q.get(k), str) and q[k].strip() for k in ('title', 'why')), 'Question needs title and why')
        require(isinstance(q.get('options'), list) and len(q['options']) <= 3, 'Use at most three options')
        for o in q['options']:
            require(isinstance(o, dict) and isinstance(o.get('label'), str) and bool(o['label'].strip()) and isinstance(o.get('detail', ''), str), 'Invalid option')
    b = s.get('brief')
    if b is not None:
        require(isinstance(b, dict) and isinstance(b.get('outcome'), str), 'Invalid brief')
        for k in ('included', 'excluded', 'checks', 'unresolved'):
            require(isinstance(b.get(k), list) and all(isinstance(x, str) for x in b[k]), 'Invalid brief ' + k)
    if s['phase'] in ('review', 'approved'):
        require(b is not None, 'Review requires brief')
    if s['phase'] == 'approved':
        require(approvable(s), 'Unresolved blocking decisions')
        require(s.get('approval') == {'revision': s['revision'], 'brief_digest': digest(b)}, 'Approval does not match brief')
    else:
        require(s.get('approval') is None, 'Approval must be cleared outside approved phase')
    require(len(json.dumps(s)) < 120000, 'State too large')
    return s


def approvable(s):
    return bool(s.get('brief') and s['brief']['outcome'].strip() and s['brief']['included'] and s['brief']['checks']) and all(d['status'] == 'answered' for d in s['decisions'] if d.get('blocking', True))


def apply_event(state, event):
    validate(state)
    require(isinstance(event, dict), 'Event must be an object')
    require(event.get('session') == state['session'] and event.get('revision') == state['revision'] and event.get('state_digest') == digest(state), 'Stale or mismatched widget; use latest state')
    s = copy.deepcopy(state)
    action = event.get('action')
    require(action in ('answer', 'defer', 'edit', 'review', 'approve'), 'Unknown action')
    if action == 'approve':
        require(s['phase'] == 'review' and approvable(s), 'Brief is not ready for approval')
        require(event.get('brief_digest') == digest(s['brief']), 'Stale brief')
        s['revision'] += 1
        s['phase'] = 'approved'
        s['approval'] = {'revision': s['revision'], 'brief_digest': digest(s['brief'])}
        return validate(s)
    if action == 'review':
        require(s.get('brief') is not None, 'Host must prepare a current brief first')
        s['phase'] = 'review'
    else:
        key = event.get('question_id')
        require(key in [d['id'] for d in s['decisions']], 'Unknown decision')
        if action in ('answer', 'defer'):
            require(s['phase'] == 'interview' and key == s['question']['id'], 'Not the current question')
        d = next(d for d in s['decisions'] if d['id'] == key)
        answer = event.get('answer', '').strip() if isinstance(event.get('answer', ''), str) else ''
        require(action != 'answer' or 0 < len(answer) <= 6000, 'Answer is empty or too long')
        new_status = {'answer': 'answered', 'defer': 'deferred', 'edit': 'open'}[action]
        changed = d.get('answer', '') != answer or d['status'] != new_status
        if changed:
            affected = {key}
            while True:
                more = {x['id'] for x in s['decisions'] if any(p in affected for p in x.get('depends_on', []))}
                if more <= affected:
                    break
                affected |= more
            for x in s['decisions']:
                if x['id'] in affected - {key}:
                    x.update(status='open', answer='')
        d.update(status=new_status, answer=answer if action == 'answer' else '')
        s['phase'] = 'interview'
        # The host must author the next adaptive question; no canned branch here.
        if action == 'edit' and (not s.get('question') or key != s['question']['id']):
            s['question'] = {'id': key, 'title': 'How would you revise ' + d['label'] + '?', 'why': 'Dependent decisions will be checked again.', 'options': []}
        s['brief'] = None
    s['approval'] = None
    s['revision'] += 1
    return validate(s)


def render(s):
    validate(s)
    packet = {'state': s, 'state_digest': digest(s), 'brief_digest': digest(s['brief']) if s.get('brief') else None, 'approvable': approvable(s)}
    data = json.dumps(packet, ensure_ascii=False).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    template = (Path(__file__).resolve().parent.parent / 'assets/widget.html').read_text()
    return template.replace('__GRILL_STATE__', data)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['validate', 'render', 'apply'])
    p.add_argument('state', type=Path)
    p.add_argument('--event', type=Path)
    p.add_argument('--out', type=Path)
    a = p.parse_args()
    try:
        s = validate(json.loads(a.state.read_text()))
        if a.command == 'validate':
            print(digest(s))
            return
        require(a.out is not None, '--out is required')
        if a.command == 'render':
            output = render(s)
        else:
            require(a.event is not None, '--event is required')
            output = json.dumps(apply_event(s, json.loads(a.event.read_text())), ensure_ascii=False, indent=2) + '\n'
        a.out.parent.mkdir(parents=True, exist_ok=True)
        temporary = a.out.with_name(a.out.name + '.tmp')
        temporary.write_text(output)
        temporary.replace(a.out)
        print(a.out.resolve())
    except (ValueError, OSError, KeyError, TypeError, RecursionError) as e:
        p.exit(2, str(e) + '\n')


if __name__ == '__main__':
    main()
