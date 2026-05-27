# Risk Register: Phase 4 First Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-01 | Critical | Candidate planning implies execution approval. | Require separate Go. | TRACE-01 |
| RISK-02 | High | Docs-only capture gives weak signal. | Require command and verification evidence. | TRACE-02 |
| RISK-03 | High | Telemetry gap is misstated. | Record `NO_TELEMETRY` and gap remains open. | TRACE-03 |
| RISK-04 | High | Candidate exits `V3-OP-001`. | Stop on excluded domains or broad scope. | TRACE-04 |
| RISK-05 | Medium | FP/FN adjudication is skipped. | Require classification fields. | TRACE-05 |
