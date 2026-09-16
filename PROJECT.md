# Project Workflow

Create a low-overhead set of reusable skills that clarify prompts, organize projects, show evidence-based status and help explain Work/Codex usage. Refine and validate the skills first, then the shared HTML dashboard, and package them as a plugin last.

## Confirmed decisions

- Usage Gauge replaces token-estimate-header's guessed context percentage with qualitative intensity, meaningful drivers and practical savings. Measurements remain distinct from forecasts.
- Collect bounded before/after telemetry automatically for Heavy, Intense and Extreme tasks when the skill is active and telemetry is available. Smaller tasks collect only when requested. No background polling is implied.
- Prompt Cleanup and Prompt Coach remain separate. Cleanup returns faithful replacement text; Coach retains recommendations and X/Y/Z refinements.
- Messy Material splits into Prompt Cleanup and Project Structure. Project Status retains its evidence-based execution map, blockers, controls and next action; detailed model/surface/usage analysis belongs in focused utilities.
- Project Structure creates or updates at least a concise PROJECT.md from the discussion and relevant existing material. It reuses existing artifacts and suggests additional ones only for a clear purpose. A proposed workspace tree does not move files.
- Save working material in this folder. Installed originals remain the baseline during refinement.

## Current state

Draft skill instructions exist for [Usage Gauge](skills/usage-gauge/SKILL.md), [Prompt Cleanup](skills/prompt-cleanup/SKILL.md) and [Project Structure](skills/project-structure/SKILL.md). These are not installed or behaviorally validated replacements.

The usage measurement contract is written; a deterministic ledger collector and historical validation remain pending. The bundled skill validator has not run successfully because its Python environment lacks PyYAML.

Project Status, focused model/surface utilities, the final HTML template and plugin package remain unfinished. The latest actual HTML must still be obtained and inspected; the source conversation alone is not the artifact.

## Completion criteria

- Skills have distinct activation and output boundaries and preserve user requirements in representative examples.
- Gauge forecasts are cheap; measured reports handle unavailable telemetry, cumulative counters, resets and concurrent activity without claiming exact task charges.
- Structure creates or updates a useful brief without unnecessary artifacts; Status completion claims have evidence.
- The actual dashboard template reflects finished skill outputs and passes meaningful desktop/mobile layout and interaction checks.
- Package and installation checks happen after skill/dashboard refinement and ledger validation.

## Sources and next work

[PLAN.md](PLAN.md) tracks the approved sequence; [RESEARCH.md](RESEARCH.md) records source conversations, telemetry evidence and limitations. Interview decisions are stored in work/grill-me/state.json.

Next: validate Usage Gauge's instructions and representative measurement behavior, then continue the remaining skill refinements in the approved sequence.
