---
name: pw-to-spec
description: Convert sufficiently settled discussion into one concise authoritative implementation spec. Use at a Design-to-Build transition or when approved decisions are scattered; do not reopen settled decisions or implement the spec.
---

# 📋 PW To Spec

Synthesize existing approved decisions into an implementation-ready source of truth. Read only the current discussion, latest checkpoint, and directly relevant code or docs needed to remove contradiction. Do not interview unless a genuine blocker remains; route material ambiguity to `pw-grill-me`.

Include the problem and intended behavior, scope and exclusions, constraints, affected components, acceptance criteria, validation seams, unresolved blockers, and the implementation entry point. Prefer existing seams and repository vocabulary. Reference stable files rather than copying them, and avoid code snippets or paths likely to become stale unless exact placement is itself settled.

Create or update the project's established spec location when the request authorizes a saved artifact; otherwise return copy-ready spec text. Do not publish to an issue tracker unless requested. End with a clear readiness state: `Ready`, `Ready with stated assumptions`, or `Blocked`.
