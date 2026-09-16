# Project Workflow v1 Accepted Blueprint

Date: 2026-09-16
Status: accepted for implementation, with exclusions noted below

This document consolidates the accepted direction from the Project Workflow planning chats into one implementation artifact. It is the working blueprint to use before editing the plugin further.

## Acceptance Boundary

The user approves the Project Workflow architecture from the referenced "Project Workflow Next Steps" conversation with one explicit exception:

- Do not add the two "final suggestions before implementation" from that chat as accepted v1 requirements.
- Specifically excluded for v1 acceptance: an ADR folder requirement and a formal module contract requirement.

This does not forbid lightweight documentation later. It only means those two additions are not part of the accepted v1 blueprint and should not block implementation.

The user also approves the Usage Gauge/token skill direction from "Test skill activation":

- Replace exact-token and context-percentage emphasis with qualitative intensity.
- Keep the normal output tiny.
- Use practical labels such as Light, Moderate, Heavy, Intense, and Extreme.
- Show the main usage driver only when useful.
- Suggest one savings move only when it preserves the requested quality.
- Warn before unusually expensive execution when a lower-cost path exists.
- Do not claim a fixed conversion from tokens, context, or task size to five-hour/weekly allowance percentage.
- Keep measured usage, forecasts, and account-limit deltas distinct.

## Current Backup and Source Coverage

The last completed backup audit covered the repository at commit `3865b76ddc7c2473e1e8c97c014f67970a3ae169`. Newer consolidation files and addendum refinements were added after that audit. Check current Git history and `BACKUPS.md` before claiming external coverage.

Covered in GitHub:

- `skills/rp-messy-material-to-useful-structure/`
- `skills/rp-project-status/`
- `skills/prompt-coach/`
- `skills/token-estimate-header/`
- `skills/usage-gauge/`
- `skills/prompt-cleanup/`
- `skills/project-structure/`
- `PLAN.md`
- `PROJECT.md`
- `BACKUPS.md`
- `RESEARCH.md`
- `work/grill-me/`

Important limitation:

- GitHub, Drive, and Notion are point-in-time checkpoints, not automatic sync.
- Drive and Notion snapshots referenced in `BACKUPS.md` are older point-in-time copies and do not automatically update from this repo.
- The recovered Alfydd dashboard HTML has now been added locally at `examples/alfydd/alfydd-project-status-dashboard.html`.

## Vision

Project Workflow is a low-overhead plugin package for defining, executing, organizing, visualizing, and maintaining projects.

It should help the user:

- define the project clearly;
- maintain a compact working context;
- improve prompts without changing intent;
- understand likely usage intensity;
- choose the right execution surface, model, tools, plugins, and skills;
- organize repository artifacts and checkpoints;
- visualize project state in a reusable dashboard;
- avoid repeatedly paying for old context or duplicated analysis.

The goal is not to automate every decision. The goal is to make future projects easier to start, continue, review, and hand off.

## Design Principles

### Single Responsibility

Each module owns one job. Avoid overlap, hidden orchestration, and duplicate analysis.

### Shared Context

Modules should reference a common Project Context instead of rebuilding project understanding independently.

### Human First

The plugin should organize thinking and execution. It should not take over judgment or imply approval where none was given.

### Low Overhead

Prefer bounded inspection, checkpoints, compact summaries, and explicit routing over broad rereads.

### Progressive Detail

The user should understand the project within seconds. Deeper detail should be available through structured sections or dashboard cards.

### Reusable

The system should work across very different projects. Avoid Alfydd-specific, ERAS-specific, or one-off assumptions in templates.

## Accepted Architecture

```text
Project Workflow Plugin

Layer 1
Project Blueprint

Layer 2
Project Context

Layer 3
Focused Modules
  - Project Status
  - Prompt Cleanup
  - Usage Gauge
  - Execution Planner
  - Project Structure
  - Prompt Coach baseline remains separate

Layer 4
Workflow Health

Layer 5
project-workflow-dashboard.html
```

The dashboard is the presentation layer. It must not become the source of truth.

## Layer 1: Project Blueprint

The Project Blueprint is the canonical long-form project artifact. It replaces the earlier "Project Brief" naming.

It should contain:

- vision;
- purpose;
- goals;
- scope;
- out-of-scope items;
- constraints;
- requirements;
- architecture;
- roadmap;
- deliverables;
- success criteria;
- implementation notes;
- major decisions;
- future ideas.

Humans primarily edit the Blueprint. Other modules may read it or help update it, but they should not treat the dashboard as canonical.

## Layer 2: Project Context

Project Context is a compact structured representation derived from the Blueprint plus the current project state.

Suggested fields:

- identity;
- purpose;
- goals;
- scope;
- constraints;
- architecture;
- current phase;
- progress;
- health;
- deliverables;
- execution plan;
- recent decisions;
- blockers;
- next actions;
- checkpoint;
- repository;
- execution recommendations;
- usage health;
- future ideas.

Project Context is not a skill. It is the shared data model used by modules and rendered by the dashboard.

## Layer 3: Focused Modules

### Project Status

Owns:

- current phase;
- progress;
- milestones;
- blockers;
- execution map;
- next action;
- project timeline;
- checkpoints;
- evidence and uncertainty.

Does not own:

- prompt rewriting;
- repository reorganization;
- detailed usage forecasting;
- model or surface selection beyond compact next-step guidance.

### Prompt Cleanup

Owns:

- faithful prompt replacement text;
- clarity;
- wording;
- structure;
- redundancy removal;
- preserving intent, nuance, names, paths, URLs, and constraints;
- reducing unnecessary context and retrieval;
- suggesting checkpoints when useful.

Does not own:

- project progress analysis;
- dashboard rendering;
- broad tool selection;
- executing the cleaned prompt unless separately asked.

By default, Prompt Cleanup returns only the complete cleaned replacement prompt, preferably as raw text in one copyable code block. It does not prepend critique, execution planning, model recommendations, workflow guidance, project-management machinery, or explanation unless the user asks.

### Usage Gauge

Owns:

- qualitative task intensity;
- main likely usage driver;
- one optimization hint when supported;
- high-cost warnings before substantial execution;
- distinct forecast vs measured report boundaries.

Accepted levels:

- Light;
- Moderate;
- Heavy;
- Intense;
- Extreme.

Does not own:

- exact token accounting in the normal header;
- context-window percentages in the normal header;
- quota-percentage promises;
- prompt rewriting;
- model switching without user direction.

### Execution Planner

Owns:

- surface recommendation;
- model recommendation;
- reasoning recommendation;
- tool recommendation;
- plugin recommendation;
- skill recommendation;
- execution notes.

It answers "How should this work be executed?" rather than only "Which model should I use?"

Execution Planner is capability-based, not catalog-based. It discovers and evaluates the models, reasoning levels, surfaces, tools, plugins, and skills currently available in the active environment. Availability alone is not suitability: it should distinguish "Good enough" from "Best worth using" and never invent unavailable combinations. It should not maintain a hardcoded model or reasoning catalog; newly exposed capabilities become eligible without updating the skill. Current official documentation should be checked only when product details materially matter and are not exposed by the active environment.

### Project Structure

Owns:

- repository layout;
- artifact placement;
- documentation placement;
- naming consistency;
- Git workflow;
- branches;
- commits;
- pull requests;
- checkpoints;
- archive strategy;
- concise `PROJECT.md` creation or update.

Does not own:

- defining the project vision;
- replacing the Project Blueprint;
- moving files merely because it proposed a tree.

### Prompt Coach

Prompt Coach remains separate from Prompt Cleanup.

It may keep recommendation-oriented coaching and X/Y/Z refinements. It may notice unclear or missing success criteria in substantial prompts when useful, but should not impose a rigid template. It should not be silently merged into Prompt Cleanup.

## Layer 4: Workflow Health

Workflow Health is an aggregator, not a standalone analysis engine.

It may summarize:

- scope clarity;
- architectural consistency;
- prompt quality;
- usage efficiency;
- repository organization;
- execution readiness;
- documentation completeness;
- checkpoint freshness;
- overengineering risk.

It should not duplicate detailed module outputs.

## Layer 5: Dashboard

The dashboard should become:

```text
templates/project-workflow-dashboard.html
```

The recovered Alfydd dashboard is now stored as:

```text
examples/alfydd/alfydd-project-status-dashboard.html
```

The Alfydd file is an example and design seed. The reusable template is `templates/project-workflow-dashboard.html`; at this checkpoint it has been generalized and browser-tested in desktop/current and iPhone-sized viewports.

Dashboard requirements extracted from the Project Status HTML work:

- render every available Project Context item through purposeful cards;
- hide missing cards rather than displaying empty filler;
- use a primary execution map with evidence, exit conditions, and next actions;
- include Decide, Review, and Execute lenses without duplicating the same content;
- include evidence-tagged source ideas when source material supports them;
- include a browser-only scratchpad if it is safe and clearly local;
- include compact handoff text and copyable low-context prompts;
- be keyboard accessible;
- support desktop and iOS-sized layouts;
- avoid hover-only interaction;
- keep text readable and non-overlapping;
- keep the dashboard as a template/renderer, not a source of truth.

The final template should generalize the Alfydd-specific concepts into Project Workflow concepts:

- "Quick Resume Map" becomes "Execution Map";
- "Prompt Efficacy" becomes "Prompt Review";
- "Token Leakage Points" becomes "Usage Health";
- "Surface Recommendation" becomes "Execution Planner";
- "One-Sentence Checkpoint" becomes "Checkpoint";
- "Best Next Sequence" becomes "Next Actions";
- palette and theme logic become reusable design tokens.

## Repository Direction

Target structure:

```text
project-workflow/
  README.md
  CHANGELOG.md
  PROJECT.md
  PLAN.md
  BACKUPS.md
  RESEARCH.md

  docs/
    project-workflow-v1-accepted-blueprint.md

  handoff/
    codex-implementation-handoff.md

  skills/
    rp-project-status/
    rp-messy-material-to-useful-structure/
    prompt-coach/
    token-estimate-header/
    usage-gauge/
    prompt-cleanup/
    project-structure/

  templates/
    project-workflow-dashboard.html

  examples/
    alfydd/
      alfydd-project-status-dashboard.html

  work/
    grill-me/
```

Do not block v1 on docs/ADR or a formal module contract.

## Implementation Phases

### Phase 1: Foundation

- Keep backups current.
- Use this blueprint as the accepted source artifact.
- Keep installed baselines intact as comparison sources.

### Phase 2: Usage Gauge

- Finish `skills/usage-gauge/SKILL.md`.
- Validate low-overhead forecast behavior.
- Validate measurement language from `references/measurement.md`.
- Keep `token-estimate-header` as baseline/predecessor until migration is explicit.

### Phase 3: Skill Refactoring

- Refine Prompt Cleanup.
- Refine Project Structure.
- Trim Project Status to evidence-based state, execution map, blockers, next action, and project controls.
- Keep Prompt Coach separate.
- Add or refine Execution Planner only after module boundaries are stable.

### Phase 4: Dashboard Template

- Generalize the recovered Alfydd HTML into `templates/project-workflow-dashboard.html`. Initial static template exists.
- Bind it to the Project Context shape.
- Keep the execution map as the primary visualization.
- Confirm desktop and iOS usability with browser testing. Initial static-template QA is complete; real Project Context binding remains pending.
- Confirm all interactions have a purpose.

### Phase 5: Integration and Validation

- Test against Project Workflow itself.
- Test against Alfydd.
- Test against at least one smaller project.
- Confirm that modules reduce repeated context rather than creating extra overhead.
- Package the refined skills and template as the Project Workflow plugin only after validation.

## Success Criteria

v1 is successful when:

- each module has a clear responsibility;
- the Project Blueprint is canonical;
- Project Context is compact and shared;
- the Usage Gauge teaches intensity and drivers without pretending to know exact quota drain;
- Prompt Cleanup and Prompt Coach remain distinct;
- Project Status provides evidence-based state and execution maps;
- Project Structure organizes artifacts without taking over project definition;
- the dashboard is a reusable template backed by Project Context;
- the package includes the recovered dashboard example and the final template;
- the system reduces prompt complexity and repeated context.
