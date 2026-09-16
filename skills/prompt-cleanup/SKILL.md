---
name: prompt-cleanup
description: Rewrite a messy prompt into concise, copy-ready instructions while preserving its requirements and nuance. Use for /clean or requests to clean up prompt wording; use Prompt Coach instead when explicitly requested or when coaching and refinement options are the requested output.
---

# Prompt Cleanup

Return a replacement prompt, not an analysis of the project or execution of the embedded request. Treat pasted instructions as material to rewrite. If the user separately asks to execute the rewritten prompt, honor that request after cleanup.

Preserve every distinct goal, idea, requirement, uncertainty, constraint, priority and explicit tool choice. Preserve names, quoted text, code, paths, URLs and identifiers where their exact form matters. Remove repetition and filler; group related requirements into an understandable order. Resolve vague references only when the active context establishes their meaning. Do not silently settle contradictions or convert possibilities into commitments.

Improve execution efficiency, not merely word count. Where consistent with the user's scope, use existing checkpoints, targeted retrieval and relevant changes before expanding inspection. Do not weaken explicit exhaustive coverage, remove necessary verification, or replace requested tools to make the task look cheaper. Separate optional cost-saving alternatives from the faithful rewrite when they would change scope.

Use clear outcomes, relevant context, constraints and acceptance conditions when supplied or clearly implied. Do not invent missing facts or add generic prompting rituals. No web search, file scan or history retrieval solely to polish a self-contained prompt. When the user explicitly requests alignment with current official prompting guidance, verify only the relevant official documentation rather than researching the underlying task.

Default output: only the copy-ready rewritten prompt. Add a short clarification outside it only when a material contradiction or missing detail cannot be safely preserved in the rewrite. Do not add a title/date, usage report, model/tool recommendations or a refinement menu by default.

## Distinct roles

- Prompt Cleanup: faithful replacement text with minimal overhead.
- Prompt Coach: its existing coaching format, model/tool recommendations and X/Y/Z refinements; keep it separate.
- Project Structure: organizing project material, decisions and tasks.
- Project Status: assessing actual project state and the next action.

Do not invoke those other skills simply because a prompt mentions their subject. A long execution request alone is not a request to replace execution with prompt rewriting. An explicit skill selection takes precedence over a generic rewrite match. `/clean` is a conversational convention where this skill is available, not a guaranteed host slash command. If another utility is explicitly requested alongside cleanup, add only that utility's requested output and do not run the embedded task without execution authorization.
