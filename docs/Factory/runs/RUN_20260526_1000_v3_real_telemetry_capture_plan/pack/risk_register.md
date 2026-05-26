# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risk register for real telemetry capture planning.

| ID | Severity | Risk | Mitigation | Verification Hook |
|---|---|---|---|---|
| R1 | High | Real telemetry starts without execution approval. | Separate execution run required. | Plan review. |
| R2 | High | Sensitive data stored in logs. | Redaction review and excluded-data rules. | Redaction review template. |
| R3 | Medium | Overhead is disproportionate. | Capture event count and time spent. | `OVERHEAD.md`. |
| R4 | Medium | Telemetry conflicts with mission records. | Link each pilot to a mission record. | Mission-record lint and replay report. |
