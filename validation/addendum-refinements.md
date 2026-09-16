# Addendum Refinements Validation

Purpose: preserve the accepted implementation refinements for Execution Planner, Prompt Cleanup, and Prompt Coach as concrete behavior checks.

## Execution Planner

Input scenario:

> How should I run a multi-file local repository review that may need tools and a stronger model?

Expected behavior:

- Discover capabilities exposed in the active environment before recommending a surface, model, reasoning level, tools, plugins, or skills.
- Do not use a hardcoded model or reasoning catalog.
- Do not recommend unavailable or unverified model/reasoning combinations.
- Separate "Good enough" from "Best worth using."
- Explain when a stronger option is not worth the additional usage.
- Keep usage forecasting out of scope except for qualitative tradeoffs.

Failure examples:

- Recommends a named model or reasoning level that is not exposed or verified.
- Lists every available tool as recommended merely because it exists.
- Defaults to the strongest model or highest reasoning without task-specific justification.

## Prompt Cleanup

Input scenario:

> Clean this prompt:
> "go through /Users/me/archive and check whether the PDFs named in my spreadsheet are backed up in Drive. Preserve weird filenames, don't delete anything, note uncertainty, and if the sheet has a Notes column keep it. I might have duplicates. Return CSV."

Expected behavior:

- Return only the complete cleaned replacement prompt by default, preferably in one raw text code block.
- Preserve every distinct intent, requirement, constraint, preference, uncertainty, path, named entity, output format, and meaningful nuance.
- Improve organization and wording without adding requirements.
- Do not critique the prompt, recommend a model, suggest a workflow, or execute the prompt.

Failure examples:

- Adds model/tool recommendations without being asked.
- Drops "don't delete anything," duplicate handling, path details, or uncertainty.
- Adds a new backup strategy or output fields not implied by the source prompt.

## Prompt Coach

Input scenario:

> Help me improve a prompt for a substantial project handoff, but I am not sure how to define done.

Expected behavior:

- Preserve Prompt Coach's coaching-oriented output and refinement options.
- Notice unclear or missing success criteria when it would materially improve the prompt.
- Offer success-criteria refinement without forcing a rigid universal template.
- Do not collapse into Prompt Cleanup's cleaned-prompt-only output.
- Recommend surfaces, tools, plugins, skills, models, or reasoning levels only when available or verified.

Failure examples:

- Returns only a cleaned prompt when the user asked for coaching.
- Forces every prompt into the same success-criteria template.
- Uses a stale fixed model table or invents unavailable tools.
