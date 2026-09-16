---
name: rp-project-status
description: Generate a visual-first, evidence-based project status interface for resuming, reviewing, or handing off active work. Use when the user invokes this project-status workflow. Default to an in-conversation interactive Execution Map rather than a deliverable artifact.
metadata:
  display-name: "RP-Project Status"
  version: "1.0.1"
---

# RP-Project Status

Review the project as it currently exists. Return a clear, lightweight, visual-first status interface in the conversation for resuming, reviewing, or handing off active work. Do not create a standalone document, PDF, spreadsheet, presentation, or other artifact unless asked.

Use concise, evidence-based entries. Distinguish confirmed facts from judgments, explicitly identify uncertainty, and never invent information to fill gaps. Prior claims of completion are not verification; use current evidence where available and label anything not checked.

## Core output principle

Preserve the information requirements below, not rigid section boundaries. Consolidate related information into visual components whenever that improves scanability, reduces duplication, or makes project relationships easier to understand.

The default output should feel like a temporary project interface rather than a conventional report.

## Status vocabulary

Use one icon plus one status word when status is useful:
- ✅ Complete
- 🔄 Active
- 🟡 Partial
- ⚠️ Review
- ⛔ Blocked
- ○ Pending
- ➖ Not needed

Complete requires supporting evidence. Pending is not failure. Use only statuses that apply. Do not repeat a full legend unless needed.

## Canonical visual layout

For active multi-stage projects, prefer this four-region hierarchy:

1. Project Header
2. Execution Map
3. Project Controls
4. Single Best Next Step

Do not mechanically force all four regions when the project is simple, finished, or lacks meaningful structure.

### 1. Project Header

Use a compact, glanceable visual header that combines the most important identity and state information.

Include, when supported by evidence:
- Overall Status
- Current Phase or active work area
- Next Action
- Goal
- Main Risk
- Definition of Done

Prefer compact cards or one grouped visual surface over a long prose section. Keep this readable above the fold on iPhone when possible.

### 2. Execution Map — canonical primary visualization

For projects with meaningful stages, dependencies, milestones, sequential work, or distinct work areas, render an in-conversation interactive Execution Map as the primary visualization.

When the current ChatGPT surface exposes an app-style/in-conversation interactive UI capability, USE IT. Do not substitute a Markdown table, ASCII diagram, Mermaid diagram, or prose description while that capability is available.

The expected interaction pattern is:
- approximately 3–8 evidence-supported nodes derived from the actual project;
- short labels and status indicators;
- visible directional arrows when sequence/dependency is meaningful;
- completed/current/future/blocked/deferred states visually distinct;
- current or most important active node selected by default;
- tapping/clicking a node updates ONE shared detail panel below the map.

The shared detail panel contains only applicable fields:
- Purpose
- Current State
- Exit Condition
- Tasks
- Evidence / Uncertainty
- Blocker
- Dependency
- Next Action

For Tasks, distinguish verified completed work from unfinished work. Interactions are inspection-only: they must never approve work, mutate files, publish, or claim to alter real project state.

When meaningful work is intentionally deferred, show a compact strip below the map:
`Later: [item] · [item] · [item]`

Responsive requirements:
- tap/click, never hover-only;
- iPhone-first readability;
- short node labels;
- one shared detail panel;
- horizontal flow when comfortable;
- local horizontal scrolling or vertical adaptation on narrow screens rather than tiny text;
- no wide dashboard chrome.

Adaptive map selection:
- sequential work → execution flow;
- dependencies → dependency flow;
- branching decision → branching flow;
- parallel workstreams → compact workstream flow;
- simple/nearly finished project → omit map and use concise visual status.

Never invent phases or relationships merely to populate the map.

Fallback ONLY when true interactive rendering is unavailable:
1. equivalent supported interactive visualization;
2. code-rendered static flowchart;
3. compact text-arrow flow.

Do not rely on raw Mermaid on iOS. Do not use image generation for exact status diagrams.

### 3. Project Controls

Merge decision/handoff, execution review, and execution recommendations into one compact interactive area when useful.

Preferred interaction: three tappable lenses sharing one detail panel:
- 🚦 Decide
- 🔬 Review
- ⚡ Execute

#### 🚦 Decide
Include only decisions materially affecting scope, safety, cost, direction, or implementation. If none are needed, say “Nothing currently.”

If a real decision creates distinct paths, a compact branching decision visual may be used as the supporting visualization.

Include a minimal Handoff Note when another person, chat, model, or surface may resume work. Preserve only what is required to continue accurately: objective, completed work, decisions, constraints, dependencies, files, and exact next task.

#### 🔬 Review
Use:
- Worked
- Watch
- Change

Focus only on important evidence-based observations about execution/methodology, prompt quality, scope drift, model/reasoning choices, plugins/skills/tools, surface/platform choice, blind spots, over-engineering, meaningful token leakage, and context-heavy chat problems.

Do not repeat minor/already-covered issues. Mention token/context/over-engineering only with meaningful evidence. Keep judgment fair and actionable.

#### ⚡ Execute
Combine execution recommendations here rather than creating separate Best Surface/Tool and Best Agent sections.

Include only useful recommendations for the next step:
- Best surface/tool
- Purpose
- Token-frugal model/intelligence recommendation
- Quality-balanced model/intelligence recommendation
- When stronger reasoning is justified
- Destination/handoff surface

For actual OpenAI model recommendations, verify current names/capabilities using official OpenAI documentation when web access is available. If verification is unavailable, disclose that rather than inventing names/access. Do not automatically choose the strongest model/highest reasoning.

## Visual budget

Default:
- 1 primary visual: Execution Map
- 0–1 supporting visual: usually a branching decision gate or genuinely different relationship visual

The report should be visual-heavy, but additional visuals are justified only when they reveal materially different relationships. Never repeat the same information in a diagram, table, and prose.

## Single Best Next Step

End with one high-emphasis callout:
- one specific actionable next step;
- brief evidence-based justification;
- recommended surface/tool when useful.

This is the final visual endpoint. Do not add a redundant conclusion afterward.

## Internal self-review

Before returning the report, internally review:
- Readability
- Evidence integrity
- Usefulness
- Proportionality
- Visual overload
- Whether the Execution Map reflects real structure
- Whether completion claims have evidence

Do not expose a self-review score unless the user is testing, auditing, or revising this skill.

## Output rules

- Keep the report limited to actual state and next useful action.
- Prefer visual relationships over repeated heading → paragraph blocks.
- Preserve critical information outside hidden interactions: Overall Status, Current Phase, Main Blocker when present, and Single Best Next Step remain visible without tapping.
- Treat diagrams and interactive components as status snapshots, not live project-management systems.
- Label mocks clearly; never mix invented evidence with real completion claims.
- Do not add tracking, databases, roadmaps, or project-management overhead for simple/finished work.
- Do not force visualization where no meaningful relationship exists.
- Default behavior is an in-conversation status interface, NOT an artifact/template deliverable.
