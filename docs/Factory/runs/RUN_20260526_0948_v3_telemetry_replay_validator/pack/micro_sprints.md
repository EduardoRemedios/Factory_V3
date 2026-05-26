# Micro-Sprints

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Micro-sprints for telemetry replay validator implementation.

## MS-01: Validator
- Entry: Intent locked.
- Work: Add standalone advisory replay validator.
- Exit: Script parses JSONL and emits deterministic reports.
- Stop/Go: Stop if required-gate wiring is needed.

## MS-02: Fixtures
- Entry: Validator exists.
- Work: Add valid, invalid, and expected fixtures.
- Exit: `--expect` check passes.
- Stop/Go: Stop if fixtures require real telemetry.

## MS-03: Docs And Verification
- Entry: Fixture check passes.
- Work: Update status/docs and run verification.
- Exit: Required checks pass.
- Stop/Go: Stop on required lint failure.
