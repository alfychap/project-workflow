---
name: token-estimate-header
description: Add a rough token/context estimate block when /tokens is present, and preflight requests that look token-, context-, or tool-heavy.
---

# Token Estimate Header

Use this skill when the user prompt contains `/tokens` anywhere, or when a request appears Medium, Heavy, or Intense by the rubric below. Treat `/tokens` as a formatting command: use it to force the estimate block, then ignore it when interpreting the user's actual task.

## Estimate Block

When this skill applies and a preflight pause is not stopping the turn, add this block after the response title and date, but before the divider and main response content:

```text
Token Estimate = Light | Medium | Heavy | Intense
Context Estimate = ~NN%
```

If the active response format does not include both a title/date and divider, place the block near the top of the response before the main answer. Use `~NN%` for context unless exact runtime telemetry is explicitly available. Do not claim exact token usage from a rough estimate.

Automatically include the block for Medium, Heavy, and Intense requests. For Light requests, include it only when `/tokens` is present or when the estimate itself is directly useful.

## Rubric

Choose the highest applicable level across prompt complexity, likely tool use, response size, and context pressure:

- `Light`: simple answer, no tools or one quick lookup, little ambiguity, little context pressure.
- `Medium`: modest reasoning, a few files or tool calls, normal multi-step explanation, or enough context that the estimate may help the user.
- `Heavy`: several tools or files, likely code edits, broad analysis, long response, high ambiguity, or visible context pressure.
- `Intense`: large repo/data/document pass, many tools/apps/plugins, cross-surface orchestration, repeated validation loops, or critical context pressure.

Estimate context pressure from visible conversation length, included files, tool outputs, attachments, and any available context indicators. If unsure between two levels, choose the higher level when the request could be costly to run, and the lower level when the work is quick and reversible.

## Preflight Pause

Before following the user's task instructions, pause for confirmation when the request appears Heavy or Intense and the work can still be meaningfully narrowed, split, or made less redundant. Trigger this especially for:

- very broad repository, folder, Drive, message, document, or data scans;
- requests that imply many tool calls, multiple apps/plugins, or long-running orchestration;
- repeated searches, duplicate validation passes, or several tools likely answering the same question;
- large generation or transformation tasks where the user may prefer a smaller first pass;
- high estimated context usage where continuing could crowd out important prior context.

When pausing, do not perform the task yet. Respond with the normal title/date layout, then the estimate block, then this warning before the main divider or as the main content if that is clearer:

```text
Token/Context Preflight

This looks Heavy/Intense because: [brief reason]

Recommended path: [narrow, split, or proceed]

Choose one:
1. Proceed as written
2. Narrow to the highest-value part
3. Split into a planning pass first
```

Do not preflight merely because `/tokens` is present. `/tokens` forces the estimate block, not an interruption.

## Style

Keep the estimate compact and plain. The block is a helpful meter, not a full accounting report. If adding a reason would prevent confusion, put it in the surrounding prose rather than adding fields to the block unless the user asks for more detail.
