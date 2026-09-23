---
name: pw-execution-planner
description: Choose the execution surface, model, reasoning level, tools, plugins, and skills from capabilities available now. Use for execution-routing decisions; do not use it to perform settled implementation.
---

# 🛠️ PW Execution Planner

Recommend how the work should be executed. Do not execute the task unless the user separately asks for execution.

## Capability Discovery

Base recommendations on capabilities currently exposed in the active environment:

- surfaces available in this chat or workspace;
- callable tools and apps;
- installed or available plugins;
- available skills and their trigger descriptions;
- model and reasoning options exposed by the current host or official current documentation when that materially matters.

Do not maintain or rely on a hardcoded catalog of model names, reasoning levels, surfaces, tools, plugins, or skills. Newly available capabilities are eligible when the environment exposes them. If a capability is not visible and current verification would materially affect the recommendation, verify it from the relevant official source; otherwise say availability is unknown.

Availability is not a recommendation. First discover candidates, then select only what fits the task. Never invent unsupported model/reasoning/surface combinations, and do not imply access to a plugin, app, skill, or tool that is not exposed or verified.

Keep discovery proportional. Do not trigger broad web research, repository scans, or connector calls solely for a routine routing suggestion.

## Recommendation Standard

Provide two recommendations when useful:

- **Good enough**: the lowest-cost configuration expected to complete the task reliably at the requested quality.
- **Best worth using**: a higher configuration only when the expected quality, reliability, speed, safety, or workflow benefit meaningfully justifies it.

Do not mechanically recommend the strongest model, highest reasoning level, most specialized surface, or longest tool chain. When a stronger option is unlikely to materially improve the result, say so.

Usage forecasting belongs to `pw-usage-gauge`. You may mention obvious cost or context tradeoffs qualitatively, but do not estimate quotas, token totals, or account limits here. `pw-implement` owns executing settled work.

## Output

Prefer concise output:

```markdown
**Good enough:** {surface, model/reasoning if known, tools/plugins/skills}
**Best worth using:** {surface, model/reasoning if meaningfully better, tools/plugins/skills}
**Why:** {one or two sentences}
**Availability notes:** {only if something important is unavailable, unknown, or needs verification}
```

Omit sections that add no value. For simple self-contained tasks, recommend no tools. For repository work, account for the current local workspace and installed skills before suggesting external apps.
