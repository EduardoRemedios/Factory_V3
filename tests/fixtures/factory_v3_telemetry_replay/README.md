# Factory v3 Telemetry Replay Fixtures

## Version
v0.2

## Change Log
- v0.2 (2026-05-26): Added a valid real-pilot-style fixture covering summary-only fixture maintenance telemetry.
- v0.1 (2026-05-26): Initial fixture corpus for the standalone advisory telemetry replay validator.

## Status
Research-only advisory fixtures. These logs do not represent real mission telemetry and do not approve telemetry collection, required gates, runtime authority, proof, lease enforcement, or governance routing.

## Fixture Groups
- `valid/`: expected `ADVISORY_PASS` logs.
- `invalid/`: expected advisory findings for replay-sequence, authority, terminal-state, and data-minimization checks.
- `expected/`: deterministic expected output for `--expect` checks.

## Valid Fixture Notes
- `real_pilot_style.jsonl` is synthetic. It mirrors the event shape used by real telemetry pilots without storing raw command output, source contents, diffs, secrets, full transcripts, or chain-of-thought.
