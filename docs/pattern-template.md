---
layout: "default"
title: "Pattern template"
nav_order: 4
permalink: "/docs/pattern-template/"
---
# Pattern template

Create one record for one coherent problem and reusable solution. The ten fields below condense the original study’s schema. Use prose for explanation, a small state table for branching, and linked screens for implementations.

| Field | What the author supplies |
| --- | --- |
| 1 Record | Stable ID and verb-led title; family; version; owner; date; publication, implementation and evaluation status. |
| 2 Context and problem | Actor, trigger, goal, vulnerability and recurring difficulty; preconditions; when to use and when not to use. |
| 3 Solution and rationale | Core interaction behavior, meaningful choices and safe exits; why the solution addresses the problem. |
| 4 Flow and states | Entry condition, sequence or branches, evidence states, outcomes, interruptions and recovery routes. |
| 5 UI and content | What the person sees and can do; example wording; components and screen references. Separate evidence from visual styling. |
| 6 Assurance and dependencies | Required evidence and services; source, binding, freshness and status; what the evidence does not establish. |
| 7 Linked concepts | Moment IDs; task and ceremony references with versions where known; related patterns and implementation examples. |
| 8 Accessibility and privacy | Accessible alternatives, cognitive burden and stressful use; data minimization, disclosure and retention decisions. |
| 9 Evaluation | Threat and legitimate scenarios, methods, success criteria, findings and limitations. Distinguish a plan from completed research. |
| 10 Operations and economics | Responsible roles; support and escalation; delivery constraints, expected benefit, burden and costs; unresolved decisions. |

## Record maturity separately

Publication: proposed or endorsed. Implementation: not implemented or deployed in a named context. Evaluation: untested, evaluated in a stated context, or supported across several contexts. Record the evidence behind each status. “Candidate” is shorthand for proposed guidance awaiting evaluation; it is not a separate pattern type. [C1]({{ '/docs/references/#c1' | relative_url }})

## Minimum design package

Deliver the completed record, an interaction flow, a prototype covering material states, and an evaluation plan. Reuse existing components. Do not create a separate screen merely to represent each catalogue field.

## Create a new entry

Start from the [worked example]({{ '/docs/patterns/p18-01/' | relative_url }}) or [copy the blank Markdown starter]({{ '/docs/pattern-starter.txt' | relative_url }}). Save a new entry under `docs/patterns/`, choose an unused child ID and update the catalogue index. See [Contribute]({{ '/docs/contributing/' | relative_url }}) for browser editing.
