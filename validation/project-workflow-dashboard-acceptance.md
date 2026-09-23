# Project Workflow Dashboard Acceptance

Date: 2026-09-17

Template: `skills/pw-dashboard/assets/project-workflow-dashboard.html`
Project Context fixture: `skills/pw-dashboard/assets/project-workflow-context.example.json`

## Status

Project Context binding and the v0.2 PW action cards are implemented and browser-checked in the canonical `pw-dashboard` asset.

The dashboard now exposes `window.ProjectWorkflowDashboard.render(context)` and attempts to load `project-workflow-context.example.json` when served from the template directory. If loading is unavailable, the static fallback copy remains usable.

## Acceptance Cases

### Minimal Project Context

Given a minimal Project Context with only identity and summary fields, when `ProjectWorkflowDashboard.render(context)` runs, optional cards backed by missing arrays or objects are hidden instead of showing empty filler.

Covered renderer paths:

- `health.items`
- `workflowInputs`
- `executionMap`
- `context`
- `definitionOfDone`
- `skillOutputs`
- `moduleActions`
- `sequence`
- `workflowHealth`
- `usageGauge`
- `evidence`
- `prompts`

### Canonical Blueprint Reference

Given an existing canonical blueprint, when the dashboard renders the main brief and evidence ledger, it references source files such as `docs/project-workflow-v1-accepted-blueprint.md` and `PROJECT.md` rather than duplicating the full artifacts.

### Usage Gauge Output

Given Usage Gauge output, when Workflow Health renders, it summarizes the qualitative usage concern from Project Context. It does not independently rerun Usage Gauge or calculate token/account percentages.

### Project Status Separation

Given ordinary chat status output, rich dashboard construction is not required. The dashboard remains a renderer/interactor for compact Project Context and module outputs.

### Execution Planner Separation

Given an execution-planning request, Execution Planner owns model, surface, tool, plugin and skill routing. The dashboard displays the routed summary when present; it does not maintain a hardcoded model or reasoning catalog.

### Populated Fixture

Given the bundled Project Context fixture, when the dashboard is served over local HTTP, it populates the hero, health list, Project Context fields, execution map, skill matrix, nine contextual PW action cards, workflow sequence, usage gauge, evidence ledger, prompts and footer from fixture data.

## Browser Checks

- Playwright loaded `skills/pw-dashboard/assets/project-workflow-dashboard.html` through local HTTP with no page or console errors.
- The populated fixture rendered all nine requested `moduleActions`; each action button was bound to the existing copy interaction.
- The new Update Checkpoint action clicked successfully.
- Rendering a minimal context with an empty `moduleActions` array hid the PW Actions card.
- In-app browser current viewport reported no horizontal overflow.
- Tabs opened: Overview, Context, Modules, Workflow, Health, Evidence, Prompts.
- Action lens changed to Review.
- Checkpoint refresh routed to Health and updated the checkpoint pill.
- Copy prompt button showed `Copied`.
- Scratchpad Save locally and Clear updated visible state.
- Chrome headless 390 by 844 screenshot checked the first mobile viewport after binding; hero copy wraps without clipping and primary buttons fit.
- The current 390 by 844 Playwright viewport reported no horizontal overflow after the v0.2 changes.

The fixture remains an example input owned by `pw-dashboard`, not a second source of truth or a formal cross-module API.
