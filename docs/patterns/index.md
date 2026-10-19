---
layout: "default"
title: "HDX pattern catalogue"
nav_order: 3
has_children: true
permalink: "/docs/patterns/"
---
# HDX pattern catalogue

Use this catalogue to select a human trust problem, define a reusable interaction and brief a prototype. The 18 families organize the work. They are not 18 finished patterns or 18 required screens.

[Use the pattern template]({{ '/docs/pattern-template/' | relative_url }}) or read [P18.01, the completed example]({{ '/docs/patterns/p18-01/' | relative_url }}). Definitions and derivation are in the [taxonomy analysis]({{ '/docs/taxonomy/' | relative_url }}).

<p align="center">
  <img src="images/HDX pattern catalogue_ 18 trust families.png"
       alt="HDX pattern catalogue"
       width="900">
</p>

## Family index

| Family | Initial patterns to develop | Moments |
| --- | --- | --- |
| <a id="p01"></a>**P01 Invitations and entry** | Review invitation origin and consequences before accepting. | T1, T4 |
| <a id="p02"></a>**P02 Relationship formation and recognition** | Confirm the intended counterpart; recognize an established relationship later. | T1, T10, T4 |
| <a id="p03"></a>**P03 Custody and recovery readiness** | Set up a recovery route; check readiness; recover when a method is unavailable. | T3, T9 |
| <a id="p04"></a>**P04 Credential receipt and acceptance** | Preview a credential and its limits; handle an offer that cannot be accepted. | T2 |
| <a id="p05"></a>**P05 Responsible peer assertions** | Review the exact claim, audience and responsibility before vouching. | T11, T8 |
| <a id="p06"></a>**P06 Evidence scope and counterparty assurance** | Explain exactly what was checked and what remains unresolved. | T4, T2, T10 |
| <a id="p07"></a>**P07 Safe transitions between channels** | Identify the destination; preserve request context; resume a failed handoff. | T4, T7 |
| <a id="p08"></a>**P08 Understandable requests** | Explain the requested action, recipient, purpose and consequences. | T5 |
| <a id="p09"></a>**P09 Personas and correlation control** | Choose an identity context; explain when an action links information. | T12, T8 |
| <a id="p10"></a>**P10 Meaningful choice and minimum disclosure** | Distinguish required and optional information; support refusal and alternatives. | T6, T5 |
| <a id="p11"></a>**P11 Consequential action confirmation** | Review the exact commitment; correct details; renew approval after material change. | T6, T7 |
| <a id="p12"></a>**P12 Outcomes and durable records** | Distinguish pending from completed; retrieve an understandable record. | T7, T8 |
| <a id="p13"></a>**P13 Bounded delegation and standing access** | Grant limited authority; inspect its use; pause or stop access. | T13, T8, T9 |
| <a id="p14"></a>**P14 Shared authority and independent approval** | Review a shared request; track approvals; handle disagreement or absence. | T13, T7, T9 |
| <a id="p15"></a>**P15 Change notices and accumulated state** | Explain a material change; distinguish a historical notice from current status. | T8, T13, T9 |
| <a id="p16"></a>**P16 Revocation and lifecycle transitions** | Withdraw a permission or credential; explain effective time and residual effects. | T8, T9 |
| <a id="p17"></a>**P17 Dispute and accountable redress** | Challenge an outcome; submit relevant evidence; track review and remedy. | T9, T8 |
| <a id="p18"></a>**P18 Fraud and abuse resistance** | [Independently confirm an unexpected request]({{ '/docs/patterns/p18-01/' | relative_url }}); handle suspected compromise. | T1, T4–T7, T9, T13 |

The moment links are indicative and may overlap. IDs are stable catalogue labels; they are not protocol identifiers. Child pattern IDs use the family prefix, for example P18.01.

## Boundaries that prevent duplicate work

P08 explains the request; P10 supports choice; P11 establishes the commitment. P12 reports an action’s outcome; P15 explains subsequent changes; P16 manages withdrawal. A single screen may use several of these patterns.

P03, P13, P14 and P17 need separate flows for different actors or lifecycle stages. P15 needs a clear split between notification and current status. P18 also acts as a threat filter across every family.

## Develop the catalogue

[Development process and initial work queue]({{ '/docs/patterns/development/' | relative_url }}).
