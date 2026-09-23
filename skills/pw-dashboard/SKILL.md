---
name: pw-dashboard
description: Render and interact with Project Workflow module outputs in the bundled HTML dashboard. Use to create, refresh, preview, or inspect the dashboard; modules own analysis and the dashboard hides inapplicable content.
---

# 🖥️ PW Dashboard

Use `assets/project-workflow-dashboard.html` as the canonical implementation and `assets/project-workflow-context.example.json` as the fixture. Reuse its visual system and interaction patterns. Do not rebuild the dashboard or turn it into a reasoning engine.

Populate compact Project Context and module outputs, then call `window.ProjectWorkflowDashboard.render(context)` or serve the asset beside a JSON file named `project-workflow-context.example.json`. Keep the blueprint, checkpoint, spec, and module outputs as the sources of truth. Hide empty or inapplicable cards.

Represent specialist outputs with `moduleActions` entries where useful:

- checkpoint freshness, next action, and create/update prompt;
- unresolved Grill Me decisions and clarification prompt;
- documentation or terminology conflicts for Grill With Docs;
- spec readiness and generate/update prompt;
- handoff destination, checkpoint reference, and preview prompt;
- latest retro findings and improvement;
- implementation readiness or blocker plus acceptance criteria;
- prototype hypothesis, status, and promote-or-discard decision;
- a small contextual Explain This action for Wait What.

Dashboard actions may switch views, update local display state, save local scratch text, or copy a prompt. They do not approve work, mutate canonical project files, or claim specialist analysis has run.

When changing the asset, update the existing fixture and validation path. Verify that it loads without JavaScript errors, its new interactions work, relevant existing interactions still work, and missing optional content remains hidden. Preserve mobile tap behavior and avoid hover-only controls.
