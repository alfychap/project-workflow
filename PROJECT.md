# Project Workflow

Create a low-overhead set of reusable skills that clarify prompts, organize projects, show evidence-based status and help explain Work/Codex usage. Refine and validate the skills first, then the shared HTML dashboard, and package them as a plugin last.

## Confirmed decisions

- Usage Gauge replaces token-estimate-header's guessed context percentage with qualitative intensity, the biggest likely cost driver and one practical optimization. Measurements remain distinct from forecasts.
- Usage Gauge is warning-first and lightweight: use fuzzy levels, pre-work warnings for Heavy/Intense work and tiny post-session audits only after unusually expensive sessions.
- Project Checkpoint merges the old Working Set idea into one compact callable/auto-trigger skill for continuing work without rereading full history.
- Prompt Cleanup and Prompt Coach remain separate. Cleanup returns faithful replacement text; Coach retains recommendations and X/Y/Z refinements.
- Execution Planner is capability-based rather than catalog-based. It discovers currently available surfaces, models, reasoning levels, tools, plugins and skills before distinguishing good-enough from best-worth-using recommendations.
- Messy Material splits into Prompt Cleanup and Project Structure. Project Status retains its evidence-based execution map, blockers, controls and next action; detailed model/surface/usage analysis belongs in focused utilities.
- Project Structure creates or updates at least a concise PROJECT.md from the discussion and relevant existing material. It reuses existing artifacts and suggests additional ones only for a clear purpose. A proposed workspace tree does not move files.
- Save working material in this folder. Installed originals remain the baseline during refinement.

## Current state

Draft skill instructions exist for [Usage Gauge](skills/usage-gauge/SKILL.md), [Project Checkpoint](skills/project-checkpoint/SKILL.md), [Prompt Cleanup](skills/prompt-cleanup/SKILL.md), [Execution Planner](skills/execution-planner/SKILL.md) and [Project Structure](skills/project-structure/SKILL.md). The accepted addendum checks are captured in [validation/addendum-refinements.md](validation/addendum-refinements.md). Usage Gauge and Project Checkpoint validation is captured in [validation/usage-gauge-project-checkpoint-validation.md](validation/usage-gauge-project-checkpoint-validation.md). These are not installed replacements yet.

The usage measurement contract is written; a deterministic ledger collector and historical validation remain pending. The bundled skill validator has not run successfully because its Python environment lacks PyYAML.

Installed baselines for Messy Material, Project Status, Prompt Coach and Token Estimate Header are now copied under their original names in `skills/`, including supporting assets and agent metadata. `skills/BASELINE-MANIFEST.json` records import provenance and hashes; [BACKUPS.md](BACKUPS.md) records coverage and snapshot limits. The earlier Drive/Notion snapshot lacks these imports and still needs a manual refresh.

Project Status refinement and the plugin package remain unfinished. The latest Alfydd dashboard HTML has been recovered from Google Drive and saved as [examples/alfydd/alfydd-project-status-dashboard.html](examples/alfydd/alfydd-project-status-dashboard.html). A generalized dashboard template now lives at [templates/project-workflow-dashboard.html](templates/project-workflow-dashboard.html), with desktop/iPhone static-template browser QA recorded in [validation/dashboard-template-static-review.md](validation/dashboard-template-static-review.md). Initial Project Context binding uses [templates/project-workflow-context.example.json](templates/project-workflow-context.example.json) and has bound-fixture browser checks in [validation/project-workflow-dashboard-acceptance.md](validation/project-workflow-dashboard-acceptance.md).

## Completion criteria

- Skills have distinct activation and output boundaries and preserve user requirements in representative examples.
- Gauge forecasts are cheap; measured reports handle unavailable telemetry, cumulative counters, resets and concurrent activity without claiming exact task charges.
- Structure creates or updates a useful brief without unnecessary artifacts; Status completion claims have evidence.
- The actual dashboard template reflects finished skill outputs and passes meaningful desktop/mobile layout and interaction checks.
- Package and installation checks happen after skill/dashboard refinement and ledger validation.

## Sources and next work

[PLAN.md](PLAN.md) tracks the approved sequence; [RESEARCH.md](RESEARCH.md) records source conversations, telemetry evidence and limitations. The accepted consolidated blueprint is [docs/project-workflow-v1-accepted-blueprint.md](docs/project-workflow-v1-accepted-blueprint.md), and the implementation handoff prompt is [handoff/codex-implementation-handoff.md](handoff/codex-implementation-handoff.md). Interview decisions are stored in work/grill-me/state.json.

Next: continue the remaining skill refinements in the approved sequence, validate the usage ledger and finalize plugin packaging.
