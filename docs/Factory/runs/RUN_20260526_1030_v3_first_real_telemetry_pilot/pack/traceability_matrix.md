# Traceability Matrix

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Traceability for first telemetry pilot.

| Constraint | Severity | Verification Tier | Evidence |
| --- | --- | --- | --- |
| C1 advisory-only status preserved | High | V2 | advisory lint, status docs |
| C2 telemetry replay passes for pilot log | High | V2 | pilot replay report |
| C3 mission record remains valid | High | V2 | mission-record lint |
| C4 fixture corpus remains deterministic | High | V2 | telemetry replay `--expect` |
| C5 no broad code or dependency changes | High | V1 | git diff and py_compile |

## Exit Criteria
PASS
