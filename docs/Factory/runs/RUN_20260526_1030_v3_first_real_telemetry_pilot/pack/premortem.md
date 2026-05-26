# Premortem

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Premortem for first telemetry pilot.

## Failure Scenarios
- Telemetry stores too much data. Mitigation: summary-only payloads and redaction review.
- Pilot implies enforcement. Mitigation: repeat advisory-only status in docs and reports.
- Mission record and telemetry diverge. Mitigation: use one mission id and cross-link artifacts.
- Verification misses replay failure. Mitigation: run pilot replay plus fixture expected check.

## Exit Criteria
PASS
