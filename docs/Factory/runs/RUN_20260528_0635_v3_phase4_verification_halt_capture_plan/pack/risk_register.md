# Risk Register: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage E risk register.

| ID | Risk | Severity | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-01 | Candidate execution starts without later approval. | Critical | Envelope states execution is blocked until explicit Go. | TRACE-01 |
| RISK-02 | Verification failure is manufactured. | Critical | Require ordinary fixture-maintenance rationale and no seeded mismatch. | TRACE-02 |
| RISK-03 | Failed verification does not halt work. | Critical | Require halt until human decision, fallback, or closeout. | TRACE-03 |
| RISK-04 | Optional telemetry becomes required or enforced. | High | Later approval must confirm telemetry mode; no completeness checks. | TRACE-04 |
| RISK-05 | Phase 3 gap is closed by assertion instead of evidence. | High | Require natural halt evidence or clean non-event note. | TRACE-05 |
| RISK-06 | Scope expands into tooling or routing. | Critical | File-touch budget excludes scripts, validators, runtime, routing, gates, proof, leases, and V2 removal. | TRACE-06 |
| RISK-07 | Expected-output maintenance obscures FP/FN adjudication. | Medium | Result summary must classify advisory findings or explicitly record none. | TRACE-07 |
