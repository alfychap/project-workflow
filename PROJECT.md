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

The v0.2.0 implementation is on `codex/pw-v1-expansion`. All 18 PW skills and standalone `teach` pass the bundled skill validator; plugin validation, dashboard browser checks, and archive integrity checks pass. The stale root `plugin.json` and `.tmp.driveupload/` upload cache are excluded from Git; `.codex-plugin/plugin.json` is the canonical manifest.

The implementation is still uncommitted, and `origin/main` contains newer instruction-only commits. The local Codex installation still exposes the published v0.1.0 skill set. Drive, Notion, and ChatGPT account copies have not been refreshed for v0.2.0.

## Definition of done

- Expected PW inventory exists and each skill validates.
- Router references only valid PW skills and superseded skill directories are absent.
- Dashboard loads without JavaScript errors; new action cards and existing interactions work.
- Plugin validation and archive checks pass.
- Third-party attribution remains present in the repository, plugin package, and each separately installable derived skill.

## Next action

Review and commit the v0.2.0 diff, rebase the branch onto `origin/main`, run targeted validation, and push. Then reinstall the local plugin with a cache-busted version and verify the new skills in a fresh Codex task. Refresh ChatGPT account and external backup copies separately.
