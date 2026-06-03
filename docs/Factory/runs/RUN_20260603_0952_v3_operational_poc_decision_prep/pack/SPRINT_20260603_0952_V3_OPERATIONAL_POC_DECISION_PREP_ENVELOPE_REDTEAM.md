# Envelope Red Team: V3 Operational POC Decision Prep

## Version
v0.4

## Change Log
- v0.4 (2026-06-03): Expanded Hermes risk review beyond desktop.
- v0.3 (2026-06-03): Added initial Hermes risks.
- v0.2 (2026-06-03): Added V3-only and Garmin risks.
- v0.1 (2026-06-03): Initial Stage I red team.

## Findings
| ID | Severity | Concern | Impact | Required Mitigation | Status |
| --- | --- | --- | --- | --- | --- |
| ERT-001 | Critical | POC execution may use V2 because this planning pack used V2. | Readiness evidence invalid. | Envelope distinguishes current planning support from future V3-only POC execution. | Addressed in envelope v0.2. |
| ERT-002 | Critical | V3 standalone gaps may be accepted as operational readiness. | False readiness claim. | V2 dependency is a stop condition and no-go decision. | Addressed in envelope v0.2. |
| ERT-003 | High | Garmin integration may be selected without research. | Blocked or brittle POC. | Research spike required before POC implementation planning. | Addressed in envelope v0.2. |
| ERT-004 | High | Hermes could add agent authority outside V3 and obscure whether V3 is actually operational. | Invalid V3-only proof. | Hermes surfaces may be researched, but not used as POC dependency or V3 substitute without explicit approval. | Addressed in envelope v0.4. |
| ERT-005 | High | Hermes memory, skills, MCP, scheduling, subagents, gateway, or sandbox backends could introduce credentials or unattended action risk. | Boundary and safety ambiguity. | Research must evaluate authority, memory, credentials, model routing, and unattended automation before use. | Addressed in envelope v0.4. |
| ERT-006 | Medium | Internal/private deployment could still trigger production-like infrastructure. | Unapproved infrastructure scope. | Envelope blocks public deployment and infrastructure changes. | Addressed in envelope v0.2. |

## Residual Risk
- Hermes may be useful as an optional comparison harness, but using it during the first POC could make the V3-only readiness signal harder to interpret.
- Garmin access may force the first POC to use synthetic or manual-import data while preserving Garmin integration as a later milestone.

## Conclusion
Envelope is acceptable for planning. Future execution must remain V3-only unless the sponsor explicitly changes the readiness question.
