# Project Workflow Dashboard Acceptance

Date: 2026-09-16

Template: `templates/project-workflow-dashboard.html`
Project Context fixture: `templates/project-workflow-context.example.json`

## Status

Initial Project Context binding implemented and browser-checked for the static dashboard template.

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

Given `templates/project-workflow-context.example.json`, when the dashboard is served over local HTTP, it populates the hero, health list, Project Context fields, execution map, skill matrix, workflow sequence, usage gauge, evidence ledger, prompts and footer from fixture data.

## Browser Checks

- In-app browser at `http://127.0.0.1:8765/templates/project-workflow-dashboard.html?binding=2` loaded the populated JSON fixture into hero, checkpoint, health, execution map, context fields, modules, evidence, prompts and footer.
- In-app browser current viewport reported no horizontal overflow.
- Tabs opened: Overview, Context, Modules, Workflow, Health, Evidence, Prompts.
- Action lens changed to Review.
- Checkpoint refresh routed to Health and updated the checkpoint pill.
- Copy prompt button showed `Copied`.
- Scratchpad Save locally and Clear updated visible state.
- Chrome headless 390 by 844 screenshot checked the first mobile viewport after binding; hero copy wraps without clipping and primary buttons fit.

## Remaining Checks

- A future packaging pass should decide whether the JSON fixture stays as an example only or becomes part of a documented template API.
