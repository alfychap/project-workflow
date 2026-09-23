---
name: pw-workflow-health
description: Evaluate the health of an ongoing project workflow from existing evidence and module outputs. Use when work is drifting, repetitive, blocked, unusually costly, or explicitly audited; do not run after every task.
---

# 🩺 PW Workflow Health

Evaluate whether the current workflow is helping the project move reliably with reasonable overhead. Aggregate available evidence; do not rerun every specialist or become a second analysis engine.

Review only the dimensions supported by current evidence:

- scope clarity and settled decisions;
- status and checkpoint freshness;
- evidence quality and unresolved blockers;
- fit of the execution surface, tools, and skills;
- repeated reads, validation loops, or context leakage;
- artifact and repository organization;
- handoff readiness and next-action clarity.

For each material finding, report `Healthy`, `Attention`, or `Problem`, cite the evidence, and give one repair action. Distinguish observation from inference and label unavailable evidence. Prefer the single repair with the highest expected benefit.

`pw-project-status` owns what is true now, `pw-retro` owns lessons after completed work, and `pw-usage-gauge` owns usage forecasting. Workflow Health may summarize their outputs without duplicating them.
