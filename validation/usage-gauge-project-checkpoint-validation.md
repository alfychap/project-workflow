# Usage Gauge and Project Checkpoint Validation

Date: 2026-09-16
Scope: `skills/usage-gauge/SKILL.md`, `skills/usage-gauge/references/measurement.md`, `skills/project-checkpoint/SKILL.md`, `templates/project-workflow-dashboard.html`

## Summary

Status: pass after minor alignment edits.

Usage Gauge and Project Checkpoint now match the accepted Project Workflow documentation and representative examples. Usage Gauge preserves a tiny qualitative forecast, includes the accepted Light/Moderate/Heavy/Intense/Extreme levels, and keeps forecasts separate from measurement. Project Checkpoint preserves a compact continuation format and merges Working Set concerns into one checkpoint artifact.

## Usage Gauge

Result: pass.

Representative expectations checked:

- Explicit `/tokens`, direct usage-gauge requests, "How expensive will this task be?", and materially high-cost execution should activate the gauge.
- Incidental mentions of "tokens" should not create noisy activation.
- Bounded answer or rewrite maps to Light.
- Focused reasoning or a small bounded sequence maps to Moderate.
- Meaningful multi-file analysis or verification maps to Heavy.
- Substantial multi-file implementation or research maps to Intense.
- Unusually broad multimodal, research and implementation scope maps to Extreme.

Evidence:

- `skills/usage-gauge/SKILL.md` defines the forecast as qualitative intensity, not exact accounting.
- `skills/usage-gauge/SKILL.md` keeps default explicit output tiny: intensity, likely cost driver, and one practical optimization.
- `skills/usage-gauge/SKILL.md` now includes the accepted Extreme level and pre-work warning behavior for Heavy, Intense, and Extreme work.
- `skills/usage-gauge/references/measurement.md` keeps measured usage distinct from forecasts, treats missing telemetry as unavailable rather than zero, avoids repeated polling, and prevents unsupported task-level attribution.
- `templates/project-workflow-dashboard.html` presents Usage Gauge as qualitative and sample-driven rather than as a live quota calculator.

Residual risk:

- A deterministic ledger collector and historical validation are still pending before plugin packaging. This validation only covers the written skill contract and static template example.

## Project Checkpoint

Result: pass.

Representative expectations checked:

- "checkpoint", "continue", "fresh chat", "handoff", "resume", and "what's next" should activate the skill for ongoing projects.
- The skill should preserve the smallest useful project state rather than rereading full chats or producing a long recap.
- Working Set belongs inside the checkpoint and should not become a separate artifact unless explicitly requested.
- The output should identify project, phase, status, approved decisions, working set, ignored items, current task, next action, and a fresh-chat prompt only when useful.

Evidence:

- `skills/project-checkpoint/SKILL.md` defines compact activation and explicitly excludes quick questions, casual explanations, one-off rewrites, and tasks with no ongoing project state.
- `skills/project-checkpoint/SKILL.md` requires settled decisions, current status, working files, next action, ignored/out-of-scope items, and blockers when useful.
- `skills/project-checkpoint/SKILL.md` keeps optional fields optional and prohibits full file contents, long chat history, and repeated architecture explanations.
- `templates/project-workflow-dashboard.html` now labels the copyable checkpoint example as "Checkpoint", matching the accepted dashboard terminology.

Residual risk:

- Real Project Context binding remains future work. The current template is a static renderer with sample copy.

## Validation Commands

```sh
git diff --check
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

for path in [
    Path("templates/project-workflow-dashboard.html"),
    Path("examples/alfydd/alfydd-project-status-dashboard.html"),
]:
    Parser().feed(path.read_text())
    print(f"parsed {path}")
PY
rg -n "Extreme|One-Sentence Checkpoint|Light to Extreme|PROJECT CHECKPOINT|qualitative" \
  skills/usage-gauge skills/project-checkpoint templates validation docs handoff
```
