# Premortem

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Premortem for real telemetry capture planning.

## Failure Scenarios

| Scenario | Mitigation |
|---|---|
| Planning doc is treated as live telemetry approval. | Require a separate execution-enabled run per pilot. |
| Logs store sensitive data. | Require redaction review and excluded-data rules. |
| Pilot scope is too large. | Limit first pilots to small `V3-OP-001` missions. |
| Telemetry overhead exceeds value. | Require overhead capture and replay usefulness notes. |
