# Premortem

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Premortem for second telemetry pilot.

## Failure Scenarios
- Expected output changes beyond the new valid fixture. Mitigation: inspect diff and run deterministic `--expect`.
- Fixture accidentally models enforcement. Mitigation: keep `blocking_effect: none` and advisory language unchanged.
- Telemetry records excluded data. Mitigation: use summary-only payloads and redaction review.
- Mission expands into validator code. Mitigation: scripts are forbidden scope.

## Exit Criteria
PASS
