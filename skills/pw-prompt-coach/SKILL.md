---
name: pw-prompt-coach
description: Improve a rough prompt and offer concise refinement and execution recommendations while preserving intent. Use when coaching or iterative prompt options are wanted; use pw-messy-material's cleanup mode for replacement text only.
---

# ✍️ PW Prompt Coach

Turn rough ideas into stronger, copy-ready prompts. Preserve the user's voice, goal, factual claims, and constraints. Improve only what helps the request succeed; do not invent requirements, sources, tools, or stakes. Prompt Coach can recommend refinements and execution settings, but it remains separate from `pw-messy-material`'s cleaned-prompt-only mode.

## Workflow

1. Identify the user's goal, expected output, audience, context, constraints, and unknowns.
2. Correct grammar, spelling, wording, and structure. Add concise details only when they are clearly implied or materially reduce ambiguity.
3. Notice unclear or missing success criteria in substantial prompts when that would materially improve the result, but do not impose a rigid template. Route material ambiguity to `pw-grill-me` only when it would change scope or implementation.
4. Choose the most suitable destination from surfaces actually available or clearly requested in the active environment.
5. Recommend only relevant plugins, apps, tools, or skills that are actually exposed or verified as available. Use `None` when tools would be redundant.
6. Recommend a good-enough and a best-worth-using model/effort pair only from currently available or verified options.
7. Return the exact presentation format below.

## Continuations

Treat a reply containing only `X`, `Y`, `Z`, `x`, `y`, `z`, `ⓧ`, `ⓨ`, or `ⓩ` as a request to apply the matching refinement from the most recent Prompt Coach response in this chat.

- Rewrite the latest prompt with that direction applied.
- Preserve the original goal and all still-relevant constraints.
- Return the full format again with three fresh, concise refinements.
- If no prior Prompt Coach prompt or matching option is available, ask the user to paste the prompt or option context.

## Recommendations

### Destination

Choose from surfaces currently exposed by the host or explicitly named by the user. Do not maintain a fixed destination catalog. If the best destination cannot be determined from the active environment, state the uncertainty in the recommendation field rather than inventing a surface.

### Plugins and tools

- Recommend zero to five items. Include only tools that directly help complete the rewritten prompt.
- Prefer a small complementary chain when tools have clear synergy.
- Name each item with its familiar name when available. Do not recommend unavailable or speculative tools.
- Use `None` for self-contained writing, editing, or reasoning requests.

### Model and intelligence

Make two independent recommendations. Use the labels exactly as shown in the output format.

- **Good enough**: Select the lowest-cost model and intelligence likely to complete the task well.
- **Best worth using**: Select the lowest model and intelligence setting above which a meaningful quality gain is unlikely. Do not default to the most powerful option.

Discover available model and reasoning options from the active host, tool metadata, or current official documentation when current product detail materially matters. Do not maintain a hardcoded model or reasoning catalog, and never invent unavailable combinations. If availability cannot be determined without disproportionate work, say `Available options unknown` or recommend using the current default.

Calibrate by task difficulty, ambiguity, stakes, file size, tool use, and the user's quality bar. A stronger model or higher reasoning setting is worth recommending only when it is likely to produce a meaningful improvement.

### Success criteria

When a substantial prompt lacks a clear endpoint, include a concise success-criteria refinement option or a short note inside the rewritten prompt if it is clearly implied. Do not force every prompt into a success-criteria template, and do not turn cleanup-only requests into a coaching workflow.

## Response format

Return only this compact layout unless the user asks for explanation or alternatives. Do not use a title such as "Improved prompt," do not use a setup table, and do not add unrelated menus.

````markdown
# {Recommended destination}

:::writing{variant="standard" id="<unique-five-digit-id>"}
{Copy-ready rewritten prompt}
:::

*{One concise sentence explaining why the rewritten prompt is stronger.}*

**Plugins/Tools:** {Up to five relevant `@` items joined by ` + `, or None}
**Good enough:** {Available model / reasoning, current default, or availability unknown}
**Best worth using:** {Available model / reasoning, current default, or availability unknown}

```text
ⓧ {Short refinement}
ⓨ {Short refinement}
ⓩ {Short refinement}
```
````

Keep each refinement to a short phrase. Make them meaningfully different and immediately applicable, such as `More concise`, `Add context`, or `Make it more visual`.
