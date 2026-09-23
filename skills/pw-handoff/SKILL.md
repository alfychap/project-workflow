---
name: pw-handoff
description: Create a compact task-specific continuation package for another chat, agent, model, surface, or session. Use for context transfers or pressure; prefer referencing the latest checkpoint instead of duplicating it.
---

# 🤝 PW Handoff

Prepare only what the destination needs to continue a specific next task. Start from the latest `pw-project-checkpoint` when available and reference existing specs, commits, diffs, and artifacts rather than copying them.

Include destination and purpose, checkpoint reference, settled decisions, exact working set, validation already completed, blockers or risks, permissions or privacy boundaries, and the first concrete next action. Add a paste-ready continuation prompt when useful. Tailor capability notes to the named destination and label unknown availability.

Redact secrets and avoid moving private material to an external service without authorization. `pw-project-checkpoint` owns durable project state; this skill owns the transfer package for one context.
