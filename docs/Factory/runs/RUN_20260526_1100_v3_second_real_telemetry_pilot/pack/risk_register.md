# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risks for second telemetry pilot.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R1 | High | Expected fixture output masks behavior drift. | No script changes; inspect expected-output diff. | telemetry replay `--expect` |
| R2 | High | Pilot implies telemetry recommendation. | Status says 2 of 3 logs and advisory only. | advisory lint |
| R3 | Medium | Telemetry overhead remains disproportionate. | Record friction and event count. | overhead review |
| R4 | Medium | Fixture path or command authority is inconsistent. | Use replay validator and mission-record lint. | V3 validators |

## Exit Criteria
PASS
