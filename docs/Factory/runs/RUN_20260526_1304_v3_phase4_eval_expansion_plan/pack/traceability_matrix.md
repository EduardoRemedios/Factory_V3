# Traceability Matrix: Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage F traceability matrix.

| Constraint | Severity | Source | Coverage | Tier |
| --- | --- | --- | --- | --- |
| TRACE-01 Capability profiles must be harness/profile-specific, not universal. | Critical | intent R2, R6; RISK-01 | Premortem PM1; future template requirement; artifact review | V0 |
| TRACE-02 Threshold language must be advisory and non-operational. | Critical | intent R2, R5; RISK-02 | Premortem PM4, PM5; verification V0-A5 | V0 |
| TRACE-03 This run must not implement Phase 4 tooling or files. | Critical | raw brief; RISK-03 | Verification V0-A1 through V0-A3; git diff review | V1 |
| TRACE-04 Phase 4 must measure execution reliability, not only documents. | High | roadmap Phase 4; RISK-04 | Premortem PM2; planned output acceptance | V0 |
| TRACE-05 Negative fixture plan must avoid synthetic-only overconfidence. | High | raw brief; RISK-05 | Premortem PM3; fixture notes | V0 |
| TRACE-06 Missing natural halted, fallback, or clarification-heavy telemetry pilot must remain a named gap. | High | Phase 3 review; RISK-06 | Intent R3; premortem PM6; verification V0-A4 | V0 |
| TRACE-07 V2 fallback and non-deprecation must remain explicit. | High | README; roadmap; RISK-07 | Intent non-goals; premortem PM7; verification V0-A6 | V1 |
| TRACE-08 FP/FN rollup must support human adjudication. | Medium | raw brief; RISK-08 | Micro-sprint MS-03 planned output | V0 |
| TRACE-09 Data minimization boundaries must remain summary-only. | Medium | Phase 3 review; RISK-09 | Premortem PM9; future template notes | V0 |

## Coverage Summary
- Every Critical and High constraint has a verification tier.
- V0 coverage is acceptable because this is a `PLANNING_ONLY` run with no implementation authority.
