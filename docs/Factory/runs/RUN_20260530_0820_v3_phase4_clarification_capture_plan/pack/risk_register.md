# Risk Register: Phase 4 Clarification-heavy Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-30): Initial Stage E risk register.

| Risk ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-01 | Critical | Manufactured ambiguity corrupts negative-case evidence. | Bind future candidate to current canons and stop if ambiguity is artificial. | Envelope stop conditions; future result summary gap review. |
| RISK-02 | High | Future agent edits without explicit target authority. | Require source-derived target selection or human clarification before editing. | Future closeout must record clarification path. |
| RISK-03 | High | Scope expands into router, enforcement, telemetry completeness, or V2 removal. | Forbidden-scope list and advisory lint checks. | V3 advisory lint; NL pilot; manual review. |
| RISK-04 | Medium | Candidate produces another clean non-event. | Record honestly; do not claim gap closure. | Result summary and opportunity register update. |
| RISK-05 | Medium | Optional telemetry overhead outweighs value. | Keep `NO_TELEMETRY` valid and require explicit telemetry decision. | Telemetry decision point in MS-01. |

## Exit Criteria Status
- PASS
