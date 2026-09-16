# Codex Handoff: Project Workflow v1 Implementation

Use this prompt in a fresh Codex task when implementation continues.

```text
We are implementing the Project Workflow plugin in `/Users/alfyos/Project Workflow Plugin`.

Start by reading:

- `docs/project-workflow-v1-accepted-blueprint.md`
- `PROJECT.md`
- `PLAN.md`
- `BACKUPS.md`
- `RESEARCH.md`

Acceptance boundary:

- The user approves the Project Workflow v1 architecture from the planning chats.
- The user explicitly does not approve the two "final suggestions before implementation" from the prior chat as v1 requirements.
- Do not add an ADR folder requirement or formal module-contract requirement as blockers.
- The user approves the Usage Gauge/token skill direction: qualitative Light/Moderate/Heavy/Intense/Extreme intensity, tiny default output, main usage driver, one useful savings hint, no normal context percentage, and no fake five-hour/weekly quota percentage.

Current backup state:

- The last completed GitHub checkpoint before the consolidation/addendum pass was `origin/main` / `main`, commit `3865b76ddc7c2473e1e8c97c014f67970a3ae169`.
- Check current Git history before claiming GitHub coverage for newer consolidation and addendum files.
- Baseline skills and current drafts are in the repo.
- Drive/Notion snapshots are older point-in-time copies and are not automatic sync.
- The recovered dashboard example is at `examples/alfydd/alfydd-project-status-dashboard.html`.

Primary implementation goal:

Turn Project Workflow into a cohesive plugin package with focused skills plus a reusable HTML dashboard template. Do not create a super-skill.

Module boundaries:

- Project Blueprint is the canonical long-form project artifact.
- Project Context is the compact shared structured project state, not a skill.
- Project Status owns evidence-based state, execution map, blockers, progress, project controls, checkpoints, and next action.
- Prompt Cleanup owns faithful prompt replacement text, clarity, structure, redundancy removal, and context reduction.
- Usage Gauge owns qualitative usage intensity, likely driver, practical saving hint, and expensive-work warnings.
- Execution Planner owns surface, model, reasoning, tool, plugin, skill, and execution recommendations.
- Project Structure owns folders, artifact placement, docs, naming, Git workflow, checkpoints, archive strategy, and concise PROJECT.md creation/update.
- Prompt Coach remains separate and should not be merged into Prompt Cleanup.
- Workflow Health is an aggregator, not a duplicate analysis engine.
- Dashboard renders Project Context and module outputs; it is not a source of truth.

Additional accepted refinements:

- Execution Planner must be capability-based, not name-catalog-based. Discover exposed models, reasoning levels, surfaces, tools, plugins and skills; then distinguish "Good enough" from "Best worth using" without inventing unavailable combinations.
- Prompt Cleanup's default response is only the complete cleaned replacement prompt, preferably as raw text in one copyable code block. Do not add critique, execution planning, model recommendations, workflow guidance, project-management machinery or explanations unless asked.
- Prompt Cleanup must preserve every distinct intent, requirement, constraint, preference, example, uncertainty, named entity, path, URL and meaningful nuance without adding requirements or executing the cleaned prompt.
- Prompt Coach may notice unclear or missing success criteria in substantial prompts when useful, but should not impose a rigid template or merge into Prompt Cleanup.

Next implementation sequence:

1. Inspect the repo and confirm the working tree state.
2. Finish/validate `skills/usage-gauge/SKILL.md` and `skills/usage-gauge/references/measurement.md`.
3. Refine Prompt Cleanup and Project Structure against the accepted boundaries.
4. Refine Project Status so it stays evidence-based and visual-first.
5. Create `templates/project-workflow-dashboard.html` by generalizing the recovered Alfydd dashboard example, not by hardcoding Alfydd.
6. Validate the dashboard in desktop and iOS-sized browser viewports.
7. Update docs only where they reflect completed implementation.

Important:

- Preserve installed baseline copies.
- Do not reorganize files just because a tree is proposed.
- Do not claim Drive/Notion backup coverage unless refreshed.
- Do not claim package completion until dashboard, skills, and validation are actually done.
- Before a coherent milestone commit, review the diff and run relevant checks.
```
