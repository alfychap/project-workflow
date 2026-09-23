---
name: pw-router
description: Choose the smallest useful Project Workflow specialist or short sequence for a request. Use when routing is unclear or the user asks which PW skill to use; direct specialist invocation remains valid without it.
---

# 🧭 PW Router

Route to the minimum useful specialist. Do not analyze the project again when the selected skill already owns the work, and do not run an entire chain automatically.

## Routing

- meaningful ambiguity → `pw-grill-me`
- ambiguity tied to durable docs or terminology → `pw-grill-with-docs`
- disorganized supplied material → `pw-messy-material`
- evidence-backed current state → `pw-project-status`
- compact durable continuation state → `pw-project-checkpoint`
- settled discussion that needs one implementation authority → `pw-to-spec`
- surface, model, reasoning, tool, plugin, or skill choice → `pw-execution-planner`
- approved implementation-ready work → `pw-implement`
- unresolved design question suited to a cheap experiment → `pw-prototype`
- transfer to another context or surface → `pw-handoff`
- completed work with material execution lessons → `pw-retro`
- confusing prior explanation → `pw-wait-what`
- project or repository organization → `pw-project-structure`
- prompt coaching and refinement options → `pw-prompt-coach`
- qualitative usage forecast or cost warning → `pw-usage-gauge`
- ongoing workflow diagnosis → `pw-workflow-health`
- render or interact with PW outputs → `pw-dashboard`

Useful sequences include `pw-grill-me → pw-to-spec → pw-implement`, `pw-project-checkpoint → pw-handoff`, and `pw-prototype → pw-to-spec → pw-implement`. Advance only when the next phase is actually needed and authorized.

When installed separately, discover which `pw-*` skills are available before routing. If a specialist is absent, name the missing skill and use the closest bounded fallback. Never make the router a prerequisite for direct invocation.
