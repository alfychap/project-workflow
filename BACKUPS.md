# Backup status

Verified 2026-09-16. The local working copy is `/Users/alfyos/Project Workflow Plugin`.

## Current status (2026-09-23)

The detailed audit below is a historical record of the 2026-09-16 snapshot. The v0.2.0 plugin implementation and dashboard browser/mobile QA are now complete locally, but the implementation branch is still uncommitted and unpublished. Drive and Notion still need a new point-in-time snapshot after the v0.2.0 commit. The root `plugin.json` is a stale v0.1.0 upload manifest and `.tmp.driveupload/` is a local upload cache; both are excluded from Git. The canonical plugin manifest is `.codex-plugin/plugin.json`.

## Destinations and coverage

- GitHub: https://github.com/alfychap/project-workflow (`origin`, branch `main`). The previously published commit was `3fc277007f73d4a029c33cc4d5123a5ee77fa7b7`, containing 16 files. All 16 matched the local working files byte for byte before this audit. The local branch initially had no commit/index despite having fetched remote history; it was attached to the existing remote history without replacing working files.
- This verification commit adds the four missing installed source directories, their provenance manifest, and this audit. Its parent is the previous snapshot commit above. Use `git rev-parse HEAD` and `git ls-remote origin refs/heads/main` to compare the current local and published commits; a commit cannot embed its own final hash. Push confirmation is reported separately after the push succeeds.
- Google Drive folder: https://drive.google.com/drive/folders/1pU9ZBYw5hgSj55dnsaDAS8qZG_Tz1bat
- Existing Drive ZIP: https://drive.google.com/file/d/1eAhT7rrTZ6WPPb-_G9vdEVhofTyChVwQ/view . The live folder listing reports `project-workflow-2026-09-16.zip`, 23,633 bytes, modified 2026-09-16 09:45:36 UTC. It predates these additions. The connector metadata did not expose a remote checksum, so remote ZIP bytes were not independently verified.
- Notion development and backup page: https://app.notion.com/p/3dd03ed1b24a81668b02f77db8ea5792?pvs=204 . The page records the previous GitHub commit, a 16-file ZIP attachment, its matching Drive link and SHA-256 `0b5d2a2308727fee7206260b06f8aed2693553b3d06c6f3b5374f6ba750148b9`. The local ZIP has that exact SHA-256; every archived file matches its internal manifest and the previous GitHub commit. The Notion attachment bytes were not independently downloaded.

**Drive and Notion still reference the earlier 16-file snapshot and do not cover the four newly imported source directories.** They were inspected, not refreshed, during this audit. A new ZIP upload and Notion snapshot update are required for those destinations to cover this verification commit.

## Skill inventory and naming

All paths below are repository-relative. Imported sources retain their original directory names and complete supporting files (excluding OS metadata and Python caches). `skills/BASELINE-MANIFEST.json` records each imported file's installed source path, size and SHA-256 at import. Installed originals were not modified.

| Skill or artifact | Repository path | Earlier GitHub/ZIP snapshot | Current verification |
| --- | --- | --- | --- |
| Messy Material baseline | `skills/rp-messy-material-to-useful-structure/` | Missing | Imported `SKILL.md` |
| Project Status baseline | `skills/rp-project-status/` | Missing | Imported `SKILL.md` and `README.md` |
| Prompt Coach | `skills/prompt-coach/` | Missing | Imported `SKILL.md`, `agents/openai.yaml`, `assets/icon.svg` |
| Token Estimate Header baseline | `skills/token-estimate-header/` | Missing | Imported `SKILL.md` and `agents/openai.yaml` |
| Usage Gauge draft | `skills/usage-gauge/` | Present | Existing `SKILL.md` and `references/measurement.md` retained |
| Prompt Cleanup draft | `skills/prompt-cleanup/SKILL.md` | Present | Retained |
| Project Structure draft | `skills/project-structure/SKILL.md` | Present | Retained |
| Project plan and brief | `PLAN.md`, `PROJECT.md` | Present | Retained; brief updated with baseline coverage |
| Accepted blueprint and handoff | `docs/project-workflow-v1-accepted-blueprint.md`, `handoff/codex-implementation-handoff.md` | Missing | Added after the backup audit |
| Alfydd dashboard example | `examples/alfydd/alfydd-project-status-dashboard.html` | Missing | Recovered from Google Drive file `1PACjZ4yzxp-JJ7YZ4uLDLj-pEN6DaD14` |
| Reusable dashboard template | `templates/project-workflow-dashboard.html` | Missing | Created from Alfydd design seed; static review passed, browser/mobile QA pending |
| Evidence and interview | `RESEARCH.md`, `work/grill-me/` | Present | Retained |

Usage Gauge is the planned successor to Token Estimate Header, not a byte-identical rename. Prompt Cleanup and Project Structure are the planned split of Messy Material. Prompt Coach remains a separate skill, not an alias for Prompt Cleanup. Project Status is now present as the installed baseline; its planned refinement is still unfinished. No additional PLAN.md or PROJECT.md files exist inside the four imported source directories.

## Synchronization boundary

GitHub commits/pushes, Drive ZIP uploads and Notion attachments/pages are **manual, point-in-time snapshots, not automatic sync**. Editing this repo does not update installed `~/.codex/skills`, GitHub, Drive or Notion. Pushing GitHub does not refresh Drive or Notion. The local project folder remains the working copy.

At the time of this 2026-09-16 audit, the existing ZIP omitted `.git`, `backups/`, OS metadata and environment files and contained a SHA-256 manifest. The accepted blueprint, handoff prompt, recovered Alfydd dashboard example and reusable dashboard template had been added after the last backup audit. The ledger, focused utilities, browser/mobile dashboard QA and final plugin package were not claimed as implemented in that snapshot; see the current-status note above for the later v0.2.0 state.
