---
layout: "default"
title: "Trust taxonomy"
nav_order: 2
has_children: true
permalink: "/docs/taxonomy/"
---
# Trust taxonomy

Use four distinct concepts in one connected model: moments provide human context, tasks specify operational work, ceremonies coordinate interactions, and patterns capture reusable design solutions. Use patterns as the main unit of UX guidance.

## The four definitions

| Concept | Recommended meaning | Boundary |
| --- | --- | --- |
| Trust moment | A trust-relevant situation or episode within a human journey. | May recur or span phases; it is not necessarily a whole journey phase. |
| Trust task | The ToIP architectural unit of trust-related work; retain the formal definition below. | A human goal or UI action is not automatically a Layer 3 protocol task. |
| Trust ceremony | A coordinated interaction with participants, roles, channels, rules and outcomes. | In the DTG Trust Tasks profile it composes several tasks; ritual and high friction are optional. |
| Trust pattern | A reusable solution to a recurring human trust-experience problem in a stated context, with rationale and limits. | May use several components and screens; it is more than a named activity or badge. |

### ToIP definition of trust task

“A specific task that involves establishing, verifying, or maintaining trust relationships or exchanging verifiable messages or verifiable data that can be performed on behalf of a trust application by a trust task protocol at Layer 3 of the ToIP stack.” [A1]({{ '/docs/references/#a1' | relative_url }})

The moment and pattern definitions above are recommendations for this catalogue. The ceremony definition reconciles the broader security meaning with the narrower DTG composition model. They are not presented as four official ToIP glossary entries. [A3–A7]({{ '/docs/references/#a3' | relative_url }})

### Naming the design work

HDX is the catalogue label used for human experience design in digital trust. The ToIP community’s official Human Trust Experience name and HTX abbreviation remain unchanged. The catalogue title does not imply ToIP endorsement. [A10]({{ '/docs/references/#a10' | relative_url }})

## Relationships and classification

These concepts form a network of relationships, not four successive steps or additional layers of the ToIP stack. Keep human goals, protocol operations and design guidance distinguishable.

| Relationship | Meaning |
| --- | --- |
| Moment provides context for work | The situation explains why a person needs understanding, evidence, control or a decision. Background tasks may have no visible human moment. |
| Ceremony composes tasks | In the DTG profile, several tasks form a coordinated process. It may branch, pause, retry or involve parallel participants. |
| Pattern guides an interaction or ceremony | A pattern can address one decision or a whole ceremony structure. A ceremony pattern is reusable guidance for designing that process. |
| Pattern uses components | Controls, summaries and status messages implement parts of the solution. A screenshot records one implementation. |
| Records have many links | One pattern can apply to several moments; one ceremony can use several patterns. Avoid one-to-one mapping assumptions. |

### A short classification test

| Example | Classify it as |
| --- | --- |
| An unexpected request for money | A situation or trust moment. |
| Decide whether to act on the request | A human goal or decision. |
| Exchange a request-bound confirmation | Candidate operational work; link a real specification before claiming task conformance. |
| Coordinate an independent check with a known contact | A ceremony description. |
| Independently confirm an unexpected high-risk request | A pattern when its context, solution, failure paths and limits are documented. |
| A contact button or verification badge | A component; its appearance establishes no evidence by itself. |

### Separate authority from evidence

The glossary was reviewed as Public Review Draft 01 and the DTG Trust Tasks specification as Working Draft 0.7.0. Official provenance does not make every statement final. Likewise, community endorsement, implementation and user evaluation are separate facts. [A1]({{ '/docs/references/#a1' | relative_url }}), [A3]({{ '/docs/references/#a3' | relative_url }})

A valid cryptographic proof does not establish every claim’s truth, the requester’s current authority or the safety of the requested action. Pattern guidance must explain the actual scope of the evidence. [A11]({{ '/docs/references/#a11' | relative_url }})

## How to derive the pattern list

Derive patterns from recurring human problems, then check coverage against the moments and operational examples. The proposed 18 families are the organizing index; individual patterns are the design deliverables.

**1 Collect concrete scenarios.** For each case, record the actor, trigger, goal, uncertainty, possible harm and available evidence. Include ordinary use, refusal, interruption and adverse cases.

**2 Separate the concepts.** Tag the moment; identify the human decision; describe the ceremony; link any actual task specification. Keep unknown protocol mappings explicit.

**3 Identify the reusable solution.** State what the person must be able to understand or do and the behavior that enables it. A category such as “delegation” does not yet specify a solution.

**4 Set the boundary.** Keep one coherent problem and solution together. Split when a different actor, obligation, threat or recovery route materially changes the behavior. Screen count is not the criterion.

**5 Group and link.** Assign the closest family, retain the source moment IDs and link related patterns. Resolve duplicates before adding categories. Permit multiple links instead of forcing exclusive classification.

**6 Specify and evaluate.** Complete the catalogue template, prototype the interaction and test relevant states. Record findings and limits before promoting reuse claims. [A6]({{ '/docs/references/#a6' | relative_url }}), [A7]({{ '/docs/references/#a7' | relative_url }})

### One derivation example

| Input or decision | Result |
| --- | --- |
| Scenario | A message claims to be from a family member and requests urgent money. |
| Human problem | The person needs to establish whether the known contact made this exact request. |
| Relevant context | T4–T7; T9 if compromise is suspected. Threat: impersonation or account compromise. |
| Reusable solution | Confirm the exact request through an established route independent of the suspicious message, with unresolved and refusal outcomes. |
| Catalogue record | P18.01 in P18 Fraud and abuse resistance. [The worked pattern]({{ '/docs/patterns/p18-01/' | relative_url }}) contains the completed specification. |

### Recommended handoff to designers

Use the 18 families for navigation and prioritization. Commission named patterns beneath them, each with a problem, context, core behavior, states, evidence requirements and evaluation plan. A screen may combine several patterns; a pattern may span several screens.

Start with request comprehension and disclosure, limited agent authority, and independent confirmation of unexpected requests. Judge outcomes by understanding, appropriate decisions, accessibility and burden—not by increased confidence or completion alone.

## Related pages

[13 moments and coverage inputs]({{ '/docs/taxonomy/moments/' | relative_url }}) · [18-family catalogue]({{ '/docs/patterns/' | relative_url }}) · [Sources and draft status]({{ '/docs/references/' | relative_url }})
