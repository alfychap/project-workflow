# Approved sequence

Recorded from the user's Grill Me answer, 2026-09-16.

1. Finish token-estimate-header → usage-gauge first, following the approved forecast, evidence and low-overhead direction.
2. Refine Messy Material into Prompt Cleanup and Project Structure; trim Project Status to evidence-based state, execution map, blockers and next action. Preserve the approved separation of surface/model guidance into focused utilities.
3. Once the skills are finished, refine and verify the reusable HTML dashboard template against their outputs.
4. Validate the Codex usage ledger and gauge before plugin packaging.
5. Package the refined skills and dashboard as Project Workflow.

The approval covers the direction above; it is not a claim of completed implementation. Working files live here. Installed originals remain the comparison baseline while refinement is underway.

## Current work

- Approved: Project Structure creates or updates a minimal PROJECT.md, reuses existing artifacts, and suggests additional useful artifacts rather than generating a bundle. The actual workspace is not reorganized merely by proposing a tree.
- Project Structure draft and this project's PROJECT.md are saved.

- Approved: keep Prompt Cleanup and Prompt Coach as two distinct skills. Cleanup returns lean replacement text; Coach retains recommendations and its X/Y/Z menu. Installed Prompt Coach remains unchanged during refinement.
- Prompt Cleanup draft saved with stricter default output: only the complete cleaned replacement prompt, preferably in one copyable raw-text block. It does not execute a pasted request unless execution is separately requested.

- Approved: Execution Planner is capability-based, not a hardcoded model/reasoning catalog. It discovers exposed surfaces, models, reasoning levels, tools, plugins and skills, then distinguishes good-enough from best-worth-using configurations without inventing unsupported combinations.
- Execution Planner draft saved in `skills/execution-planner/SKILL.md`.
- Addendum validation fixture saved in `validation/addendum-refinements.md`.
- Representative addendum validation saved in `validation/addendum-validation-results.md`.

- Usage Gauge instructions updated in `skills/usage-gauge/SKILL.md` to use fuzzy levels, biggest likely cost driver, one practical optimization, Heavy/Intense pre-work warning and tiny post-session audits only when useful.
- Project Checkpoint drafted in `skills/project-checkpoint/SKILL.md`; it merges Working Set into a compact continuation checkpoint and treats approved decisions as settled.
- Usage Gauge and Project Checkpoint validation saved in `validation/usage-gauge-project-checkpoint-validation.md`; the gauge now includes the accepted Extreme level and the dashboard checkpoint label matches the accepted terminology.
- Measurement integrity contract drafted; collector not implemented. Measurement remains distinct from forecast and is not part of the lightweight default gauge.
- Latest Alfydd dashboard HTML sourced from Google Drive and saved under `examples/alfydd/` as a design seed. Generalized static dashboard template saved at `templates/project-workflow-dashboard.html`; desktop/iPhone rendering and interactions are recorded in `validation/dashboard-template-static-review.md`. Next bind the template to real Project Context outputs before packaging.

## Accepted blueprint

- Consolidated accepted v1 blueprint saved at `docs/project-workflow-v1-accepted-blueprint.md`.
- Codex implementation handoff saved at `handoff/codex-implementation-handoff.md`.
- Explicit exclusion: do not treat the earlier ADR-folder suggestion or formal module-contract suggestion as accepted v1 blockers.
