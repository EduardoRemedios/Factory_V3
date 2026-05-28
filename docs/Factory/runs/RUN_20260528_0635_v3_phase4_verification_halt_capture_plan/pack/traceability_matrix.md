# Traceability Matrix: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage F traceability matrix.

| Constraint | Severity | Source | Coverage | Tier |
| --- | --- | --- | --- | --- |
| TRACE-01 Future capture requires separate explicit approval. | Critical | intent R1; RISK-01 | envelope execution gate; checklist C8 | V1 |
| TRACE-02 Verification failure must not be manufactured. | Critical | intent principles; RISK-02 | envelope constraints; future rationale field | V1 |
| TRACE-03 Failed verification must halt work until decision, fallback, or closeout. | Critical | intent R4; RISK-03 | verification plan; envelope stop conditions | V1 |
| TRACE-04 Optional telemetry remains summary-only, advisory, and non-blocking. | High | intent R3; RISK-04 | envelope telemetry decision point | V1 |
| TRACE-05 Phase 3 natural halted, fallback, or clarification gap remains open until real evidence exists. | High | Phase 3 review; RISK-05 | future result-summary requirement | V1 |
| TRACE-06 Scope excludes tooling, telemetry enforcement, routing, runtime, proof, leases, gates, and V2 removal. | Critical | intent non-goals; RISK-06 | envelope file-touch budget | V1 |
| TRACE-07 Advisory FP/FN findings must be adjudicated or explicitly absent. | Medium | capture plan; RISK-07 | future result-summary shape | V0 |

## Coverage Summary
- Critical and High constraints have verification coverage and tiers.
- V0 coverage is limited to a future evidence-record field because this run is planning-only.
