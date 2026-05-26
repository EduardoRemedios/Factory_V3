# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risks for first telemetry pilot.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R1 | High | Advisory evidence is interpreted as enforcement. | State non-enforcing status in docs and telemetry reports. | advisory lint |
| R2 | High | Excluded data enters telemetry. | Use summary-only payloads and redaction review. | replay lint and manual review |
| R3 | Medium | Pilot overhead is disproportionate. | Record event count and friction in `OVERHEAD.md`. | overhead review |
| R4 | Medium | Mission record and telemetry disagree. | Use one mission id and matching closeout state. | mission-record lint and replay lint |

## Exit Criteria
PASS
