# Traceability Matrix: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage F traceability matrix.

| Constraint | Severity | Source | Coverage | Tier |
| --- | --- | --- | --- | --- |
| TRACE-01 Threshold checks must not route work. | Critical | intent R1; RISK-01 | Future `V3-P4-THRESH-001`; manual review | V2 |
| TRACE-02 Eval output must remain advisory and non-blocking. | Critical | intent R3; RISK-02 | Expected JSON review | V2 |
| TRACE-03 Fixture cases must be synthetic-labeled. | High | premortem PM3 | Future fixture text review | V1 |
| TRACE-04 Evaluator change must be direct trigger checks only. | High | RISK-04 | Future diff review | V1 |
| TRACE-05 Expected output must be deterministic. | High | AGENTS.md; RISK-05 | `--expect` fixture command | V2 |
| TRACE-06 V2 fallback must remain explicit. | High | README; ROADMAP | Future `V3-P4-SCOPE-001` | V1 |
| TRACE-07 FP/FN rollup shape must require human adjudication. | Medium | Phase 4 plan | Future `V3-P4-FPN-001` | V1 |

## Coverage Summary
- Critical and High constraints have verification tiers.
- Future executable coverage is V2 because fixture eval can run deterministically after approval.
