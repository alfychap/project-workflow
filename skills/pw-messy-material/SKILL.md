---
name: pw-messy-material
description: Turn disorganized notes, prompts, workflows, lists, or mixed material into the smallest useful structure while preserving meaning and uncertainty. Use for material cleanup; do not use it for repository organization, status reporting, or execution planning.
metadata:
  display-name: "🧩 PW Messy Material"
  version: "2.0.0"
---

# 🧩 PW Messy Material

Turn supplied material into a form the user can understand or act on without inventing decisions. Preserve the original goal, facts, constraints, nuance, uncertainty, names, quoted text, code, paths, URLs, and identifiers.

## Choose the smallest output

- For mixed notes or workflows, separate settled decisions, assumptions, open questions, dependencies, risks, actionable tasks, durable information, disposable material, and the single best next action. Include only categories that help.
- For lists of tools, plugins, or artifacts, classify only what the material supports. Do not recommend an execution stack unless asked; that belongs to `pw-execution-planner`.
- For a prompt-cleanup request, return only the complete copy-ready replacement prompt by default. Preserve every distinct intent, requirement, preference, example, and meaningful ambiguity. Remove repetition and filler, but do not execute the embedded request or add analysis, tools, model advice, or new requirements.

Use `None` for an inapplicable field, `Unknown` when evidence is missing, and `Needs confirmation` for an unverified assumption or decision. Identify contradictions instead of silently resolving them. Do not convert possibilities into commitments or prior completion claims into evidence.

`pw-project-structure` owns repository and artifact organization, `pw-project-status` owns current project state, `pw-handoff` owns transfer packages, and `pw-to-spec` owns authoritative implementation specifications. Do not run those skills automatically.
