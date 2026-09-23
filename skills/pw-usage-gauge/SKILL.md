---
name: pw-usage-gauge
description: Forecast task resource intensity qualitatively, warn before unusually expensive work, and audit major usage waste when useful. Use for /tokens, usage questions, or clear high-cost work; never present rough estimates as measured allowance use.
---

# 📊 PW Usage Gauge

Help the user understand and reduce Work/Codex allowance consumption. Focus on warning and practical optimization, not exact accounting. Forecast execution intensity, not an invented token budget or quota percentage. `/tokens` is a conversational trigger when this skill is available, not a registered host command.

## Cheap forecast

Use already available context. Do not scan files, fetch histories, browse, or invoke other skills merely to classify a request. Consider model/effort when known, material to process, expected output, retrieval breadth, tool iterations and repeated context. Prompt length or tool count alone does not determine cost. Distinguish required processing from avoidable repetition; never label all long history wasteful or assume caching is absent.

- 🟢 Light: a bounded answer or rewrite with little execution.
- 🟡 Moderate: focused reasoning or a small, bounded sequence of steps.
- 🟠 Heavy: substantial material or several meaningful execution/verification steps.
- 🔴 Intense: broad research, large analysis or sustained implementation with substantial iteration.
- 🚨 Extreme: unusually broad multimodal, research and implementation scope where the work should be split or explicitly approved.

These are relative qualitative forecasts, not calibrated allowance bands. Do not call Light free or negligible. Do not assign a high level solely because work involves coding, tools or a long prompt.

When explicitly invoked, show only the intensity, biggest likely cost driver, and one practical optimization:

```text
🟠 Heavy — likely cost driver: reading prior chats and repo files.
Optimization: use the latest Project Checkpoint and limit reads to the working set.
```

Otherwise omit trivial turns and show the gauge only when it helps a real execution decision. Preserve the user's required coverage and quality; offer narrower scope as a choice, not a silent substitution. Do not rewrite the user's prompt unless asked.

## Before costly execution

Heavy, Intense and Extreme work get a compact pre-work warning when the user has not already authorized that scope after a warning. Name the main driver and one lower-cost path. Honor existing approval; do not repeatedly gate the same work. A material scope expansion can justify a new warning. The initial prompt has already been processed; this warning protects subsequent execution only.

Do not estimate context-window percentages. Mention context only when it contributes meaningfully and identify the evidence or uncertainty. Do not switch models, surfaces, tools or scope without the appropriate user direction.

## Post-Session Audit

After unusually expensive sessions, give a tiny audit only when it is useful:

```text
Biggest cost driver: [tool loops / repo discovery / long chat history / validation / documentation]
Necessary: [what was justified]
Avoidable: [what could be reduced next time]
Next time: [one practical improvement]
```

Do not show this audit for normal small tasks.

## Measured Usage

Keep forecasts, measured token counters and observed account allowance changes visibly distinct. Collect only when the user requests measurement or when a concrete telemetry workflow is already part of the task. Load [measurement.md](references/measurement.md) for collection or a requested usage check. Do not claim account-wide monitoring or background collection just because this skill exists.

By default, avoid raw counts in the headline. Missing telemetry means unavailable, not zero. Never convert tokens, context occupancy or API/credit prices directly into a Plus weekly/five-hour percentage. Never claim a particular file, instruction or skill caused a measured share without component-level evidence.
