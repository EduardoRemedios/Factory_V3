# Risk Register: Phase 4 Real-run Corpus Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-01 | Critical | Planning authorizes live missions implicitly. | Require later explicit approval per mission. | TRACE-01 |
| RISK-02 | Critical | Profiles imply routing readiness. | Mark outputs advisory and non-operational. | TRACE-02 |
| RISK-03 | High | Optional telemetry becomes routine. | Require separate mission-level approval. | TRACE-03 |
| RISK-04 | High | Corpus is happy-path only. | Track missing natural negative case. | TRACE-04 |
| RISK-05 | High | FP/FN lacks adjudication. | Require human adjudication fields. | TRACE-05 |
| RISK-06 | Medium | Sensitive data enters profile artifacts. | Enforce data minimization exclusions. | TRACE-06 |
| RISK-07 | Medium | V2 fallback language weakens. | Include fallback trigger capture. | TRACE-07 |
