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

- Usage Gauge core instructions drafted in skills/usage-gauge/SKILL.md.
- Measurement integrity contract drafted; collector not implemented.
- Approved collection: Heavy/Intense/Extreme automatically when the skill is active and telemetry is available; smaller tasks only on explicit measurement requests. Use bounded before/after observations, not background polling.
- Latest Alfydd dashboard HTML sourced from Google Drive and saved under `examples/alfydd/` as a design seed. Later: generalize it into `templates/project-workflow-dashboard.html`, inspect supporting resources of the original skills, validate representative behavior and dashboard desktop/mobile interactions before packaging.

## Accepted blueprint

- Consolidated accepted v1 blueprint saved at `docs/project-workflow-v1-accepted-blueprint.md`.
- Codex implementation handoff saved at `handoff/codex-implementation-handoff.md`.
- Explicit exclusion: do not treat the earlier ADR-folder suggestion or formal module-contract suggestion as accepted v1 blockers.
