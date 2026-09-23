---
name: pw-implement
description: Execute an approved implementation or settled specification with focused edits and proportional validation. Use when requirements and acceptance criteria are ready; do not use it to resolve design ambiguity or perform unrelated refactors.
---

# ⚙️ PW Implement

Implement the authorized work from the current spec, tickets, or explicit request. Treat approved decisions as settled. Inspect the smallest relevant working set, reuse existing patterns, preserve unrelated user changes, and stop on a genuine blocker.

Make the smallest complete change that satisfies the acceptance criteria. Avoid unrelated cleanup, parallel infrastructure, and speculative extensibility. Run the focused checks that demonstrate changed behavior; broaden only after a failure or unresolved risk. Review the final diff for scope, correctness, and accidental files.

Report what changed, the checks and results, material limitations, and the next Git action when useful. Do not commit, publish, deploy, or message others unless that action is authorized by the request or established workflow.
