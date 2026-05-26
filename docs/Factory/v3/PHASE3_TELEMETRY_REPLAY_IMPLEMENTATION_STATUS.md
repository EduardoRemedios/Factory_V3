# Factory v3 Phase 3 Telemetry Replay Implementation Status

## Version
v0.2

## Change Log
- v0.2 (2026-05-26): Linked the planning-only real mission telemetry capture plan as the next Phase 3 evidence shape.
- v0.1 (2026-05-26): Recorded initial fixture-first advisory replay validator implementation.

## Status
Initial fixture-first advisory implementation complete.

This status is research-only and non-enforcing. It does not approve real mission telemetry collection, required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal.

## Implemented Artifacts
- `scripts/factory_v3_telemetry_replay_lint.py`
- `tests/fixtures/factory_v3_telemetry_replay/`
- `tests/fixtures/factory_v3_telemetry_replay/expected/all.json`

## Implemented Advisory Checks
- JSONL event parsing.
- Common event-field validation.
- Mission and record identifier consistency.
- Gap-free monotonic sequence checks.
- Authority declaration before command and file-change events.
- Command labels checked against declared authority.
- File paths checked against declared authority.
- Failed verification followed by halt, fallback, or human decision before further execution.
- Terminal closeout ordering.
- Excluded-data marker detection.

## Fixture Coverage

Valid fixtures:
- happy-path bounded code change,
- verification halt,
- pre-envelope fallback,
- stale reentry check,
- human clarification before execution.

Invalid fixtures:
- non-monotonic sequence,
- command outside declared authority,
- file outside authorized scope,
- execution after failed verification without halt, fallback, or human decision,
- event after terminal closeout,
- excluded-data marker present.

## Current Limits
- Fixtures are synthetic.
- No real mission telemetry logs exist yet.
- `PHASE3_REAL_MISSION_TELEMETRY_CAPTURE_PLAN.md` defines the future pilot shape only.
- The validator is standalone and advisory only.
- The validator does not execute commands, read source contents, inspect git history, upload data, or block repository operations.

## Next Required Evidence
Use the validator on future real `V3-OP-001` mission telemetry only after a separate execution-enabled V2 run approves the exact pilot mission, telemetry storage path, redaction workflow, allowed event subset, and verification commands.

Phase 3 cannot recommend telemetry until it has real mission telemetry logs, overhead notes, data-minimization review, and false-positive or false-negative classification.
