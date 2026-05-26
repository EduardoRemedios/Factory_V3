# Factory v3 Telemetry Replay Fixtures

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial fixture corpus for the standalone advisory telemetry replay validator.

## Status
Research-only advisory fixtures. These logs do not represent real mission telemetry and do not approve telemetry collection, required gates, runtime authority, proof, lease enforcement, or governance routing.

## Fixture Groups
- `valid/`: expected `ADVISORY_PASS` logs.
- `invalid/`: expected advisory findings for replay-sequence, authority, terminal-state, and data-minimization checks.
- `expected/`: deterministic expected output for `--expect` checks.
