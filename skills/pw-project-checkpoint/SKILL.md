---
name: pw-project-checkpoint
description: Preserve compact durable continuation state for ongoing work. Use at meaningful milestones, before major builds or context switches, when context is repetitive, or when the user asks to checkpoint; skip trivial tasks.
---

# 💾 PW Project Checkpoint

Preserve the smallest useful project state so future turns can continue without rereading full chats, repositories, long documents, or already-approved decisions.

## Use When

Use this skill when the user says "checkpoint", "save the current state", "continue", "fresh chat", "handoff", or "resume"; when context is becoming repetitive or heavy; when a meaningful milestone finishes; before a major build phase; or when work will switch chats, agents, or surfaces.

Do not use it for quick questions, casual explanations, one-off rewrites, tasks with no ongoing project state, or full project summaries where a compact checkpoint is enough.

## Core Behavior

Prefer a compact checkpoint over a recap. Treat approved decisions as settled. Do not redesign, re-explain, or repeat unchanged history unless new evidence requires it.

Read only what is needed to update the checkpoint. Reuse already available context and stable project files. When source material is large, extract only settled decisions, current status, working files, next action, ignored/out-of-scope items, and blockers.

Merge the working set into the checkpoint. Do not create a separate Working Set artifact unless the user explicitly asks for one.

## Output Format

```text
PROJECT CHECKPOINT

Project: [name]
Phase: [Explore / Plan / Design / Build / Verify / Deploy / Maintain / Archive]
Status: [current state in 1-2 lines]
Settled decisions: [approved decisions]
Working set: [files/artifacts relevant now]
Do not revisit: [stable, out-of-scope, or already-settled items]
Current task: [what is being done now]
Blockers: [only material blockers]
Next: [single best continuation]

Continuation/handoff seed:
[compact next-context prompt, only if useful]
```

Optional fields: `Risks`, `Recent changes`, `Validation`, and `Git state`. Include them only when useful. Reference artifacts by path or URL instead of copying their contents.

## Token Rules

Keep checkpoints short. Prefer bullets over paragraphs. Do not include full file contents, long chat history, or repeated architecture explanations. Do not reread stable sources unless needed to update the checkpoint.

## Success Criteria

A good checkpoint answers what the project is, what has already been approved, what matters now, what should be ignored, and what happens next.
