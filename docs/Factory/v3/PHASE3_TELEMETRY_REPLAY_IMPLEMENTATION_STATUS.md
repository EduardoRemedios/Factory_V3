# Factory v3 Phase 3 Telemetry Replay Implementation Status

## Version
v0.5

## Change Log
- v0.5 (2026-05-26): Recorded the third real advisory telemetry pilot and evidence-review prep.
- v0.4 (2026-05-26): Recorded the second real advisory telemetry pilot for fixture-maintenance work.
- v0.3 (2026-05-26): Recorded the first real advisory telemetry pilot for a docs-only Phase 3 status update.
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
- human clarification before execution,
- real-pilot-style fixture maintenance.

Invalid fixtures:
- non-monotonic sequence,
- command outside declared authority,
- file outside authorized scope,
- execution after failed verification without halt, fallback, or human decision,
- event after terminal closeout,
- excluded-data marker present.

## Current Limits
- Fixtures are synthetic.
- Three real advisory telemetry pilots exist:
  - `telemetry/pilots/PILOT_20260526_001_phase3_status_update/`
  - `telemetry/pilots/PILOT_20260526_002_replay_fixture_maintenance/`
  - `telemetry/pilots/PILOT_20260526_003_evidence_review_prep/`
- No natural halted, fallback, or clarification-heavy pilot has been captured yet; this is a gap, not negative-case evidence.
- Phase 3 now needs an evidence review before deciding whether telemetry remains experimental, continues to more pilots, or becomes recommended advisory evidence.
- `PHASE3_REAL_MISSION_TELEMETRY_CAPTURE_PLAN.md` defines the future pilot shape only.
- The validator is standalone and advisory only.
- The validator does not execute commands, read source contents, inspect git history, upload data, or block repository operations.

## Next Required Evidence
Run the Phase 3 telemetry evidence review using the three real pilot logs, overhead notes, redaction reviews, mission records, and replay reports.

Phase 3 cannot recommend telemetry until it has real mission telemetry logs, overhead notes, data-minimization review, and false-positive or false-negative classification.
