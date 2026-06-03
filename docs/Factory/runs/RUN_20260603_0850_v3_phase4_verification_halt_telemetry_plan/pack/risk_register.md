# Risk Register: Phase 4 Verification-halt Telemetry Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-03): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Suggested Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-001 | Critical | Verification-halt execution starts without explicit future approval. | Keep this run `PLANNING_ONLY`; envelope blocks execution until later Go names exact authority. | Stage/pack lint plus manual envelope review. |
| RISK-002 | Critical | Prohibited evidence is captured. | Evidence exclusions are explicit and repeated in envelope. | V3 advisory lint and manual data-minimization review. |
| RISK-003 | High | Optional telemetry is treated as required. | Telemetry recommendation is non-authorization and non-blocking. | V3 NL pilot and manual review. |
| RISK-004 | High | Local Codex capability is overstated from official docs. | Codex remains `insufficient_evidence` until a local candidate is executed. | Harness profile limitation review. |
| RISK-005 | High | Future evidence is generalized to routing thresholds. | Records must state no routing, governance reduction, default-mode, or promotion effect. | Operational-readiness eval and NL pilot. |
| RISK-006 | Medium | Future read-only probe has no useful signal. | Outcome classes include clean non-event and unavailable capability. | Future result summary classification. |

## Exit Criteria Status
- PASS
