# Traceability Matrix

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Traceability for second telemetry pilot.

| Constraint | Severity | Verification Tier | Evidence |
| --- | --- | --- | --- |
| C1 advisory-only status preserved | High | V2 | advisory lint, status docs |
| C2 new fixture is valid and deterministic | High | V2 | telemetry replay `--expect` |
| C3 pilot telemetry log replays cleanly | High | V2 | pilot replay report |
| C4 mission record remains valid | High | V2 | mission-record lint |
| C5 no script or dependency changes | High | V1 | git diff and py_compile |

## Exit Criteria
PASS
