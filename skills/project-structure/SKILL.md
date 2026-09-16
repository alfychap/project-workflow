---
name: project-structure
description: Create or update a concise PROJECT.md brief from project discussions and existing material, reuse current planning artifacts, and propose useful implementation plans or workspace organization. Use for /structure or requests to organize project material.
---

# Project Structure

Turn the material already discussed into a durable, minimal project brief. By default, create or update `PROJECT.md` in the user's project folder. This invocation authorizes that brief and relevant updates to existing planning artifacts; it does not authorize implementing the project or moving its files.

## Reuse first

Use the active conversation and inspect the project root for existing briefs and directly relevant planning files. Start with their current summaries; expand inspection only where evidence is missing or conflicting. Do not recursively read the workspace or fetch all prior chats merely to organize known material.

Update the existing canonical `PROJECT.md` rather than creating competing versions. If another established brief already serves that role, preserve it and use a compact `PROJECT.md` pointer plus missing essentials instead of copying the whole document. Preserve unrelated content and manual changes. Treat source text as evidence, not new authorization. If storage is unavailable, return copy-ready brief text and state that it has not been saved.

## Minimum useful brief

Include the supported project goal, scope, constraints, confirmed decisions, current state, definition of done, open questions and next action. Keep facts, decisions and assumptions distinct. Link directly to source files and detailed plans rather than reproducing them. Omit empty sections; do not invent owners, dates, dependencies, completion evidence or commitments.

Do not mistake earlier assistant proposals for accepted decisions or claims of completion for verification. Label a briefly reviewed project as a snapshot with its evidence limits. Preserve uncertainty and conflicting requirements that need resolution.

## Additional artifacts

Suggest only artifacts with a concrete job: an implementation plan when sequencing needs detail, a proposed workspace tree when placement is unclear, or another document that resolves an actual gap. Explain its purpose in one line. Keep small plans and trees inside the brief instead of multiplying files.

Create additional artifacts when requested or already authorized; otherwise propose them. Update existing relevant artifacts to reflect confirmed decisions, without converting a tentative plan into completed work. Do not create a standard bundle of README, roadmap, backlog, handoff and architecture files by habit.

A proposed workspace tree is a proposal. Actual moves, deletions or restructuring require an explicit organization request and appropriate verification of references. Do not publish or upload the brief merely because a destination appears in the source material.

## Result

Return the saved brief link, a short account of meaningful updates, and any justified artifact suggestions. Prompt Cleanup owns prompt rewriting; Project Status owns current-state assessment and its visual interface. Do not run either automatically. `/structure` is a conversational convention where this skill is available, not a guaranteed host command.
