---
name: pw-project-status
description: Report the evidence-backed current state, phase, blockers, execution map, and next action for active work. Use to resume or review a project; do not use it to create durable checkpoints, transfer packages, retrospectives, or execution plans.
metadata:
  display-name: "📍 PW Project Status"
  version: "2.0.0"
---

# 📍 PW Project Status

Review the project as it currently exists and return a clear, visual-first status interface. Use only current evidence. Distinguish confirmed facts from judgments, label uncertainty, and never treat an earlier completion claim as verification.

## Current-state output

Include only supported fields:

- overall status and current phase;
- goal and definition of done;
- verified completed work;
- active work and exit condition;
- blockers, risks, dependencies, and evidence gaps;
- a 3–8 node execution map when real stages or dependencies exist;
- one concrete next action.

Use one icon plus one status word when useful: `✅ Complete`, `🔄 Active`, `🟡 Partial`, `⚠️ Review`, `⛔ Blocked`, `○ Pending`, or `➖ Not needed`. Completion requires evidence. Do not repeat a full legend unless it helps.

For meaningful stages, render an in-conversation interactive execution map when the surface supports it. Keep critical state visible outside hidden interactions. Otherwise use the smallest supported flow or compact text-arrow map. Never invent phases merely to populate a visual, and do not create a standalone artifact unless asked.

End with one highlighted next action and the evidence supporting it. Omit empty sections and avoid repeating the same fact in a diagram, table, and prose.

## Ownership boundaries

Use the latest checkpoint as an input when available, but `pw-project-checkpoint` owns durable continuation state. `pw-handoff` owns transfer packages, `pw-execution-planner` owns surface/model/tool choices, `pw-retro` owns lessons from completed work, and `pw-dashboard` owns the reusable HTML presentation layer. Do not run those analyses inside status.
