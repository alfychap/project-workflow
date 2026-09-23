# Project Workflow

## Goal

Provide one packaged Project Workflow plugin plus independently installable `pw-*` skills. Keep each module focused, preserve compact context and evidence, and keep `teach` standalone.

## Confirmed decisions

- The plugin exposes exactly 18 `pw-*` skills; `pw-router` is optional and direct invocation works without it.
- Project Status, Project Checkpoint, Handoff, Execution Planner, Implement, Project Structure, To Spec, Grill Me, Grill With Docs, Retro, Workflow Health, and Dashboard retain separate ownership.
- The user's custom Grill Me implementation is the source for `pw-grill-me`.
- Retained Matt Pocock skills are adapted to PW boundaries with MIT attribution preserved.
- The dashboard renders Project Context and module outputs. It does not duplicate specialist analysis or become a source of truth.
- `teach` stays under `standalone/teach/` and is not discoverable through the plugin.

## Current state

The v0.2.0 implementation is committed on `codex/pw-v1-expansion`. All 18 PW skills and standalone `teach` pass the bundled skill validator; plugin validation, dashboard browser checks, and archive integrity checks pass. The stale root `plugin.json` and `.tmp.driveupload/` upload cache are excluded from Git; `.codex-plugin/plugin.json` is the canonical manifest.

The v0.2.1 package adds the user's Drive icon as the plugin logo and composer icon. The local Codex installation is enabled with all 18 skills and the new icon; the cached icon matches the Drive PNG by SHA-256. ChatGPT account and iOS Work availability still require account-side installation and verification.

## Definition of done

- Expected PW inventory exists and each skill validates.
- Router references only valid PW skills and superseded skill directories are absent.
- Dashboard loads without JavaScript errors; new action cards and existing interactions work.
- Plugin validation and archive checks pass.
- Third-party attribution remains present in the repository, plugin package, and each separately installable derived skill.

## Next action

Publish the v0.2.1 icon package and make it available for account-side installation. Verify ChatGPT Work on iOS separately from the local Codex installation.
