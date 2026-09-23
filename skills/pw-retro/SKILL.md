---
name: pw-retro
description: Review a completed or unusually difficult phase for concrete workflow improvements. Use after major, failed, repeatedly corrected, or unusually expensive work; do not run after every task or reopen the product decision itself.
---

# 🔄 PW Retro

Review primary evidence from the completed phase and identify improvements for future runs. Focus on unnecessary reads, repeated validation, routing mistakes, ambiguous instructions, missing automation, avoidable agent or tool use, useful guardrails, and instructions that created overhead.

For each finding, state the evidence, consequence, and smallest repair. Distinguish one-off friction from a repeatable pattern. Prefer deterministic checks for mechanical mistakes and concise guidance for judgment calls. Do not propose new infrastructure without a demonstrated recurring cost.

Return only the highest-value findings, ordered by impact, plus one recommended change to apply first. `pw-workflow-health` covers ongoing state; Retro covers lessons after the work.
