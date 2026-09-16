---
name: usage-gauge
description: Give a compact forecast of task resource intensity, warn before unusually expensive execution, and explain measured usage when telemetry is available. Use for /tokens, usage-gauge requests, or clear high-cost work.
---

# Usage Gauge

Help the user understand and reduce Work/Codex allowance consumption. Forecast execution intensity, not an invented token budget or quota percentage. `/tokens` is a conversational trigger when this skill is available, not a registered host command.

## Cheap forecast

Use already available context. Do not scan files, fetch histories, browse, or invoke other skills merely to classify a request. Consider model/effort when known, material to process, expected output, retrieval breadth, tool iterations and repeated context. Prompt length or tool count alone does not determine cost. Distinguish required processing from avoidable repetition; never label all long history wasteful or assume caching is absent.

- 🟢 Light: a bounded answer or rewrite with little execution.
- 🟡 Moderate: focused reasoning or a small, bounded sequence of steps.
- 🟠 Heavy: substantial material or several meaningful execution/verification steps.
- 🔴 Intense: broad research, large analysis or sustained implementation with substantial iteration.
- 🚨 Extreme: unusually large scope combining several major drivers, such as exhaustive retrieval, multimodal processing and repeated revision.

These are relative qualitative forecasts, not calibrated allowance bands. Do not call Light free or negligible. Do not assign a high level solely because work involves coding, tools or a long prompt.

When explicitly invoked, show one line: `🟠 Heavy · Forecast: multi-file analysis and verification`. Otherwise omit trivial turns and show the gauge only when it helps a real execution decision. Add at most one saving suggestion when supported: `💡 Start with the existing checkpoint; inspect relevant changes first.` Preserve the user's required coverage and quality; offer narrower scope as a choice, not a silent substitution.

## Before costly execution

Heavy work gets a compact advisory, not an automatic interruption. For Intense/Extreme work, when a meaningful lower-cost alternative exists and the user has not already authorized that scope after a warning, explain the main driver and offer `Continue as requested` or `Optimize first` before costly execution. Honor existing approval; do not repeatedly gate the same work. A material scope expansion can justify a new warning. The initial prompt has already been processed; this warning protects subsequent execution only.

Do not estimate context-window percentages. Mention context only when it contributes meaningfully and identify the evidence or uncertainty. Do not switch models, surfaces, tools or scope without the appropriate user direction.

## Measured usage

Keep forecasts, measured token counters and observed account allowance changes visibly distinct. Automatically collect for Heavy, Intense and Extreme tasks when this skill is active and telemetry is available. For Light/Moderate tasks, collect only when the user requests measurement. Load [measurement.md](references/measurement.md) for collection or a requested usage check. Do not claim account-wide monitoring or background collection just because this skill exists.

By default, avoid raw counts in the headline. A measured report may show the dominant supported driver and the account change with its attribution limitation. Missing telemetry means unavailable, not zero. Never convert tokens, context occupancy or API/credit prices directly into a Plus weekly/five-hour percentage. Never claim a particular file, instruction or skill caused a measured share without component-level evidence.

Do not add a postflight report to every small reply. Surface one when requested or when collected evidence reveals a useful discrepancy from the forecast. Detailed history and accounting belong in the optional ledger, not this entrypoint.
