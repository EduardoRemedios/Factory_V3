# Premortem: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface failure modes.
- v0.2 (2026-06-03): Added V3-only and Garmin failure modes.
- v0.1 (2026-06-03): Initial Stage E premortem.

## Failure Modes
| ID | Failure Mode | Consequence | Prevention |
| --- | --- | --- | --- |
| PM-001 | The future POC quietly uses V2 to compensate for missing V3 capability. | Readiness evidence is invalid. | Make V3-only execution a hard stop and acceptance criterion. |
| PM-002 | Current V2-governed planning is misread as permission to use V2 during the POC build. | Scope confusion. | State the distinction in intent, envelope, verification, and micro-sprints. |
| PM-003 | Garmin integration is started before access and terms are understood. | Rework, blocked auth, credential risk, or brittle dependency. | Run research spike first and require a decision record. |
| PM-004 | Synthetic data produces a polished app but no credible ingestion path. | POC proves only UI/build flow. | Label synthetic-only evidence and plan a separate Garmin/manual import milestone if needed. |
| PM-005 | Internal/private use leads to implicit public deployment or production infrastructure. | Unapproved operational surface. | Keep deployment local/private until a later explicit approval. |
| PM-006 | The pack implies default V3 production readiness. | Overclaim. | Limit outcome to named POC decision readiness. |
| PM-007 | V2 removal is inferred from standalone POC planning. | Premature deprecation. | Preserve V2 until explicit release evidence approves removal. |
| PM-008 | Hermes is adopted as an execution helper before boundary review. | V3-only proof becomes ambiguous. | Keep Hermes research-only until explicit approval and label any Hermes-assisted evidence separately. |

## Conclusion
The highest-risk failure is accepting V2-assisted POC execution as V3 evidence. The pack must block that path explicitly.
