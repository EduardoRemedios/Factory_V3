# Traceability Matrix: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface traceability.
- v0.2 (2026-06-03): Added V3-only POC and Garmin research traceability.
- v0.1 (2026-06-03): Initial Stage G traceability matrix.

| Requirement | Source | Evidence |
| --- | --- | --- |
| R1 | User operational definition | Intent defines V3 operations as using V3 with Codex for app design/build/test/deploy. |
| R2 | User standalone clarification | Intent, envelope, risk register, and verification plan make V3-only POC execution mandatory. |
| R3 | User POC concept | Intent and envelope identify a private personal health and fitness tracker as the candidate POC. |
| R4 | User deployment boundary | Intent and envelope keep deployment internal/private and block public deployment. |
| R5 | User synthetic-data allowance | Intent, micro-sprints, and verification plan allow synthetic data while preventing overclaiming. |
| R6 | User Garmin direction | Intent, risk register, envelope, and micro-sprints require a Garmin research spike. |
| R7 | User Hermes direction and Hermes public docs | Intent, envelope, risk register, and micro-sprints require a Hermes Agent surface research spike. |
| R8 | `PROMOTION_CRITERIA.md` | The pack treats V2 dependency as a hard no-go for readiness. |
| R9 | `ROADMAP_TO_FULL_VISION.md` | The pack prepares a decision path, not default production promotion. |
| R10 | Official Garmin docs and current public repository landscape | Research spike must compare official access with open-source approaches before implementation. |

## Verification Coverage
| Requirement | Verification |
| --- | --- |
| R1 | Manual review plus V3 operational-readiness eval. |
| R2 | Manual review plus stop-condition check. |
| R3 | Manual review of intent and envelope. |
| R4 | Manual review of boundaries. |
| R5 | Manual review of synthetic-data evidence labels. |
| R6 | MS-01 research spike exit criteria. |
| R7 | MS-02 research spike exit criteria. |
| R8 | Promotion criteria review and operational-readiness eval. |
| R9 | Roadmap review. |
| R10 | Research spike source review before POC planning. |
