# Usage Gauge and Project Checkpoint Validation

Date: 2026-09-16
Scope: `skills/pw-usage-gauge/SKILL.md`, `skills/pw-usage-gauge/references/measurement.md`, `skills/pw-project-checkpoint/SKILL.md`, `skills/pw-dashboard/assets/project-workflow-dashboard.html`

## Summary

Status: pass after minor alignment edits.

Usage Gauge and Project Checkpoint now match the accepted Project Workflow documentation and representative examples. Usage Gauge preserves a tiny qualitative forecast, includes the accepted Light/Moderate/Heavy/Intense/Extreme levels, and keeps forecasts separate from measurement. Project Checkpoint preserves a compact continuation format and merges Working Set concerns into one checkpoint artifact.

## Usage Gauge

Result: pass.

Representative expectations checked:

- Explicit `/tokens`, direct usage-gauge requests, "How expensive will this task be?", and materially high-cost execution should activate the gauge.
- Incidental mentions of "tokens" should not create noisy activation.
- Bounded answer or rewrite maps to Light.
- Focused reasoning or a small bounded sequence maps to Moderate.
- Meaningful multi-file analysis or verification maps to Heavy.
- Substantial multi-file implementation or research maps to Intense.
- Unusually broad multimodal, research and implementation scope maps to Extreme.

Evidence:

- `skills/pw-usage-gauge/SKILL.md` defines the forecast as qualitative intensity, not exact accounting.
- `skills/pw-usage-gauge/SKILL.md` keeps default explicit output tiny: intensity, likely cost driver, and one practical optimization.
- `skills/pw-usage-gauge/SKILL.md` includes the accepted Extreme level and pre-work warning behavior for Heavy, Intense, and Extreme work.
- `skills/pw-usage-gauge/references/measurement.md` keeps measured usage distinct from forecasts, treats missing telemetry as unavailable rather than zero, avoids repeated polling, and prevents unsupported task-level attribution.
- `skills/pw-dashboard/assets/project-workflow-dashboard.html` presents Usage Gauge as qualitative and sample-driven rather than as a live quota calculator.

Residual risk:

- The portable skill contract is validated, but no deterministic collector or historical calibration dataset is bundled. Measurement therefore depends on telemetry available in the active surface and otherwise falls back to a qualitative forecast.

## Project Checkpoint

Result: pass.

Representative expectations checked:

- "checkpoint", "continue", "fresh chat", "handoff", "resume", and "what's next" should activate the skill for ongoing projects.
- The skill should preserve the smallest useful project state rather than rereading full chats or producing a long recap.
- Working Set belongs inside the checkpoint and should not become a separate artifact unless explicitly requested.
- The output should identify project, phase, status, approved decisions, working set, ignored items, current task, next action, and a fresh-chat prompt only when useful.

Evidence:

- `skills/pw-project-checkpoint/SKILL.md` defines compact activation and explicitly excludes quick questions, casual explanations, one-off rewrites, and tasks with no ongoing project state.
- `skills/pw-project-checkpoint/SKILL.md` requires settled decisions, current status, working files, next action, do-not-revisit items, and blockers.
- `skills/pw-project-checkpoint/SKILL.md` keeps optional fields optional and prohibits full file contents, long chat history, and repeated architecture explanations.
- `skills/pw-dashboard/assets/project-workflow-dashboard.html` labels the copyable example as "Checkpoint", matching the accepted terminology.

Residual risk:

- The dashboard binds the bundled Project Context fixture. Supplying current project outputs remains the caller's responsibility; the plugin does not claim a background data connection.

## Validation Commands

```sh
git diff --check
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

for path in [
    Path("skills/pw-dashboard/assets/project-workflow-dashboard.html"),
    Path("examples/alfydd/alfydd-project-status-dashboard.html"),
]:
    Parser().feed(path.read_text())
    print(f"parsed {path}")
PY
rg -n "Extreme|One-Sentence Checkpoint|Light to Extreme|PROJECT CHECKPOINT|qualitative" \
  skills/pw-usage-gauge skills/pw-project-checkpoint skills/pw-dashboard validation docs handoff
```
