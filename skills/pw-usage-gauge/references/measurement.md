# Usage measurement contract

Approved collection policy: automatically collect for Heavy, Intense and Extreme tasks when this skill is active and telemetry is available. Light/Moderate tasks use forecasts only unless the user requests measurement. This is an agent workflow, not a background service or a guaranteed host hook.

## Collection workflow

1. Before substantial execution, take one available account-limit snapshot and one bounded current-task token snapshot. Record the timestamp and whether any task work already occurred. A late baseline covers only the remaining interval, not the entire task.
2. At the end of execution, take one matching snapshot pair. Do not repeatedly poll for a percentage change. The final response may not yet be included in local counters; mark that boundary explicitly.
3. Save the minimal observations and comparison in the active project's `work/usage-gauge/` directory when a writable project is available. Use a distinct task/interval identifier and retain source references. Without writable storage, report available measurements without claiming a saved ledger.
4. Follow the accounting rules below. A compact postflight line can report an observed change, but never silently assign the entire account delta to the task. If the baseline or comparable endpoint is missing, report partial telemetry rather than inventing a delta.
5. Reuse snapshots for the same interval. No recursive log inventory, transcript rereading or extra model calls solely to power the gauge. If a source is unavailable, fall back without repeatedly retrying it.

A deterministic collector and historical calibration remain optional future enhancements. They are not required for portable plugin packaging because the skill already records available snapshots through the agent workflow and falls back to qualitative forecasts when telemetry is unavailable.

Use bounded local telemetry and account snapshots where supported. A portable skill must fall back to qualitative guidance when telemetry is unavailable. Do not imply that local logs cover ChatGPT Work, other devices, deleted sessions or the whole account.

For each observation retain task identity, source, timestamp, model/mode when available, forecast, counters, window durations/reset identities, and coverage limitations. Store only necessary metadata by default, not conversation bodies or credentials.

Token accounting must distinguish cumulative from latest-request fields. Deduplicate repeated events; do not sum cumulative totals. Detect counter resets, truncated logs, forks and missing intervals. Verify whether cached input is included in input and reasoning in output before arithmetic; do not double count subsets. Mark incomplete task totals as partial, and do not treat the latest pre-final event as a completed-turn total.

An allowance delta is the later used-percent minus the earlier used-percent within the same limit/window/reset identity. Report percentage points, not percent of remaining capacity. Invalid or crossed windows have no comparable delta. Roundoff, delayed updates, concurrent tasks and other account activity limit attribution. A zero displayed change is not proof of zero cost. Unknown concurrency is not confirmed isolation.

Keep measured account changes separate from task attribution. Single-task observations with stable windows and complete timestamps support stronger association, not an official task invoice. Do not proportionally allocate account usage by raw tokens across models or tasks.

Empirical forecasting needs multiple comparable completed observations, stratified by model/mode and task type, with sample size and uncertainty disclosed. Until there is enough clean evidence, retain qualitative levels. Published credit rates may support a clearly labeled comparison proxy after current verification; they do not reveal the included Plus budget denominator.

Avoid continuous AI polling to measure AI costs. Prefer deterministic collection and compact summaries. An HTML report renders recorded snapshots; it is not live unless a working data connection is actually present.
