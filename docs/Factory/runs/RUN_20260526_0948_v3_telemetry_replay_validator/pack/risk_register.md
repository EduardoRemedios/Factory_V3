# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risk register for telemetry replay validator implementation.

| ID | Severity | Risk | Mitigation | Verification Hook |
|---|---|---|---|---|
| R1 | High | Required-gate drift. | Standalone script only. | V3 advisory lint. |
| R2 | High | Sensitive fixture data. | Synthetic fixture values. | Fixture review. |
| R3 | Medium | Overbuilt abstraction. | Single dependency-free script. | SIMPLE-CODE-GATE review. |
| R4 | Medium | Expected output nondeterminism. | `generated_at: not_recorded`. | `--expect` check. |
