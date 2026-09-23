# Project Workflow

Project Workflow is a local Codex plugin with 18 focused `pw-*` skills. Each skill also works as a standard independently installable skill from its folder under `skills/`. The router is optional; direct invocation remains supported.

The packaged skills are:

- `pw-router`, `pw-project-status`, `pw-messy-material`, `pw-usage-gauge`
- `pw-execution-planner`, `pw-project-structure`, `pw-prompt-coach`, `pw-workflow-health`
- `pw-project-checkpoint`, `pw-grill-me`, `pw-grill-with-docs`, `pw-to-spec`
- `pw-handoff`, `pw-retro`, `pw-implement`, `pw-prototype`, `pw-wait-what`, `pw-dashboard`

The dashboard implementation and fixture live inside `skills/pw-dashboard/assets/`, so the dashboard skill remains usable when installed separately. `standalone/teach/` is intentionally outside the plugin.

Start with [PROJECT.md](PROJECT.md) for current state and [docs/project-workflow-v1-accepted-blueprint.md](docs/project-workflow-v1-accepted-blueprint.md) for the accepted architecture. Third-party provenance and licensing are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
