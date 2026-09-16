# Project Workflow — discovery notes

Status: planning interview; no plugin implementation or installation yet.
Date: 2026-09-16

## User direction

- Rework token-estimate-header to explain and anticipate meaningful five-hour/weekly usage, with low overhead.
- Rework custom workflow skills and package them in a Project Workflow plugin.
- Include a reusable Project Status HTML dashboard as a combined deliverable for larger projects.
- Save project material in this folder.
- Use Grill Me to resolve consequential design choices.

## Verified evidence

- Account usage tool reports Plus, five-hour 54% used and weekly 93% used at the initial check. This is account-wide, not task-specific.
- Current local task log exposes token_count events with cumulative and latest input, cached-input, output, reasoning-output and total-token fields, plus rate-limit snapshots.
- One earlier local session from today also contains these token fields (8 events). Historical local analysis is feasible for retained logs; coverage across other devices and cloud Work is unverified.
- Installed token-estimate-header currently asks for approximate context percentages and qualitative intensity, and has a heavy-task preflight rule. It does not implement a measured historical ledger.
- Official pricing documentation confirms model, context, reasoning, retrieval, tools and caching affect usage; prompt length alone is insufficient. Plus current usage is available through the dashboard and CLI /status. Enterprise analytics are distinct. No official per-task Plus allowance ledger or fixed token-to-percentage formula was established.
- Source: https://learn.chatgpt.com/docs/pricing (checked 2026-09-16).

## Source conversations

- Test skill activation — 6aaa4cfc-20fc-83e9-a32d-4dce93cb955c: prefer emoji intensity levels, actionable warnings and low overhead over raw token counts and unexplained context percentages.
- Compare Workflow Skills — 6aaa5512-95d4-83ea-a5cd-7b09ec99bbc4: proposed prompt cleanup, project status, structure, surface/model selection and usage skills under one router. Prior assistant suggestions are not approved implementation decisions.
- Project Status HTML — 6aa48264-06d4-83ea-80de-bbc6cf1308b8: evidence-linked execution map, Decide/Review/Execute views, scratchpad, handoff and concise prompts. The Drive artifact `alfydd-project-status-dashboard.html` was fetched from https://drive.google.com/file/d/1PACjZ4yzxp-JJ7YZ4uLDLj-pEN6DaD14/view and saved locally at `examples/alfydd/alfydd-project-status-dashboard.html`; Drive metadata reported `text/html`, 26,231 bytes, modified 2026-09-16T06:55:20.265Z.

## Proposed measurement design (not approved)

1. Cheap preflight: qualitative forecast, main likely driver and one saving suggestion. A skill cannot prevent the cost of reading its initial prompt.
2. Local deterministic collector: use per-event counters or deduplicated cumulative deltas; never sum cumulative totals. Verify cached and reasoning fields as subsets before calculating weighted measures.
3. Observed allowance change: before/after snapshot with timestamps, window reset identity, concurrency and missing-coverage flags. Never call an account delta an exact task charge.
4. Calibrated forecast: compare completed tasks within model/mode cohorts; show ranges only with sufficient clean observations. Credit/API rates can be a labeled comparison proxy, not a Plus allowance conversion.
5. Dashboard: separate measured, inferred and unavailable values. Avoid rereading entire transcripts merely to render it.

## Open decision

Prioritize a Codex-first measured tracker, an equally cross-surface qualitative gauge, or the complete workflow bundle before deeper usage measurement. Recommendation: Codex-first tracker with portable skill instructions and explicit fallback elsewhere.
