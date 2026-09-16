---
name: rp-messy-material-to-useful-structure
description: Turn messy notes, prompts, workflows, tool lists, plugin lists, or mixed material into a concise, useful structure with decisions, uncertainties, actionable tasks, durable vs temporary information, tool recommendations, handoffs, and a single best next step.
metadata:
  display-name: "RP-Messy Material to Useful Structure"
version: "1.0.0"
---

Use this skill when the user invokes `@RP-Messy Material to Useful Structure` or asks to turn disorganized material into a useful structure.

# Messy Material → Useful Structure

## Material

`[PASTE NOTES, PROMPT, WORKFLOW, TOOL LIST, PLUGIN LIST, OR MIXED MATERIAL HERE]`

## Scope

- **Estimated scope:** `[Tiny / Small / Medium / Large / Complex]`
- **Reason:** `[Brief explanation]`
- **Response level:** `[Concise / Structured / Detailed]`

Use the smallest sufficient response. Do not inflate scope because the input is long.

## Main Ideas

`[Summarize the central goals, themes, constraints, intended outcome, and meaningful ambiguity.]`

## Decisions and Uncertainties

### Settled Decisions

- `[Explicit or sufficiently established decision]`

### Assumptions

- `[Unconfirmed belief or premise affecting the plan]`
- **Status:** `[Needs confirmation / Confirmed]`

### Missing Information

- `[Information required for accurate interpretation or execution]`
- **Blocking:** `[Yes / No]`

### Dependencies

- `[Prerequisite, person, system, file, input, or decision]`
- **Blocking:** `[Yes / No]`

### Unresolved Choices

- `[Decision still requiring selection]`
- **Blocking:** `[Yes / No]`

### Material Risks

- `[Risk that could materially affect outcome, effort, quality, timing, or reversibility]`

`[Omit genuinely inapplicable subsections or write Not applicable.]`

## Actionable Tasks

|Priority|Task|Dependency|Expected output|Suggested surface/tool|
|---|---|---|---|---|
|`[Now / Next / Later]`|`[Verb-led task]`|`[None or prerequisite]`|`[Specific result]`|`[Surface/tool or None]`|

`[Include only concrete, useful tasks. If none: No actionable task is justified from the available material.]`

Use a specialized surface only when necessary. Available options include:

- `Chat`, `Work`, `Codex`, `Codex CLI`, `Codex IDE`
- `Gemini`, `Gemini Spark`, `Gemini Notebook`
- `Antigravity`, `Antigravity CLI`
- `Search`, `Deep Research`, `Create Image`, `Visualize`, `Product Design`, `Data Analytics`, `Sites`

## Durable and Temporary Material

### Durable Material

|Item|Why it is durable|Recommended destination|
|---|---|---|
|`[Requirement, decision, principle, process, specification, workflow, constraint, or stable context]`|`[Reason]`|`[Notion / ChatGPT Library / Google Drive / Figma / GitHub / Supabase / Other / None]`|

`[If none: No long-term reference is justified.]`

### Temporary or Disposable Material

- `[Outdated, redundant, speculative, abandoned, superseded, low-value, interaction-only, or discardable material]`

`[If none: Not applicable.]`

## Tools, Plugins, and Artifacts

|Item|Classification|Purpose|Justification|Timing|Recommended surface|
|---|---|---|---|---|---|
|`[Tool, plugin, file, document, workflow, or artifact]`|`[Keep / Clarify / Remove / Research further / Not needed]`|`[Purpose]`|`[Brief reason]`|`[Now / Later / Never]`|`[Surface or None]`|

`[If none: No additional tools, plugins, or artifacts are needed.]`

## Destination and Handoff

### Canonical Destinations

|Item|Destination|Reason|
|---|---|---|
|`[Important item]`|`[Notion / ChatGPT Library / Google Drive / Reminders / Figma / GitHub / Supabase / Nowhere]`|`[Capability or persistence reason]`|

`[If none: No material requires long-term storage.]`

### Handoff

- **Handoff recommended:** `[Yes / No]`
- **Destination:** `[Surface or None]`
- **Reason:** `[Capability, token, persistence, collaboration, or workflow advantage]`
- **What to transfer:** `[Minimum context: objective, completed work, decisions, constraints, dependencies, files, and exact next task]`
- **What should remain here:** `[Non-duplicated context]`

`[If no handoff: No handoff is recommended.]`

## Minimal Workflow

Use only the steps that apply.

### Tiny or Small

1. `[Clarify the goal]`
2. `[Complete the task]`
3. `[Save or discard the result]`

### Medium

1. `[Define the objective]`
2. `[Separate decisions from questions]`
3. `[Identify dependencies]`
4. `[Complete necessary work]`
5. `[Validate the result]`
6. `[Store durable outputs]`
7. `[Discard temporary material]`

### Large or Complex

1. `[Define objective and success criteria]`
2. `[Separate facts, decisions, assumptions, and questions]`
3. `[Identify dependencies, ownership, and material risks]`
4. `[Create only necessary artifacts]`
5. `[Execute each stage in the best surface]`
6. `[Validate outputs against requirements]`
7. `[Record durable decisions and reusable results]`
8. `[Prepare a minimal handoff if needed]`
9. `[Discard temporary, redundant, or superseded material]`

## Recommended Next Step

- **Best next step:** `[Single concrete action]`
- **Why:** `[Brief justification]`

`[If none: No further action is justified from the available material.]`

## Processing Rules

- Preserve the original goal, meaning, constraints, nuance, uncertainty, names, labels, code, paths, URLs, identifiers, and quoted text.
- Separate facts, interpretations, assumptions, decisions, questions, tasks, durable information, and temporary material when useful.
- Do not invent structure, tasks, dependencies, owners, dates, tools, destinations, or completed work.
- Do not turn speculation into fact or possibilities into commitments.
- Identify contradictions and missing information rather than silently resolving them.
- Recommend tools, artifacts, destinations, or handoffs only when they materially improve capability, accuracy, effort, persistence, collaboration, or execution.
- Prefer existing tools, one canonical destination, minimal handoffs, reuse, simplification, and completion.
- Use `None` for an inapplicable field, `Unknown` for insufficient information, and `Needs confirmation` for unverified assumptions or decisions.
- Keep the response proportional to scope and omit genuinely inapplicable sections.

