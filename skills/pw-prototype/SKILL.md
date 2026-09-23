---
name: pw-prototype
description: Build the cheapest useful experiment for an unresolved design question. Use when interaction, UI, or state behavior is easier to judge than describe; do not silently promote prototype architecture to production.
---

# 🧪 PW Prototype

State the hypothesis or question first, then create the smallest runnable artifact that can answer it. Reuse the project's existing runtime and patterns when cheap. Keep state local and temporary unless persistence is the question being tested.

Mark the artifact clearly as a prototype. Skip production abstractions, broad error handling, and tests that do not help answer the question. Expose the relevant state and make the comparison or walkthrough easy to run.

Conclude with the evidence observed, the decision supported, and one of `Promote the validated decision`, `Revise`, or `Discard`. Production work belongs to `pw-to-spec` and `pw-implement`; never merge prototype code into production by implication.
