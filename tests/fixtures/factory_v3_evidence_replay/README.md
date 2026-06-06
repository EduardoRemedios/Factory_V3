# Factory v3 Evidence Replay Fixtures

## Status
Research-only advisory fixtures. These examples do not approve runtime enforcement, required gates, telemetry, proof ledgers, or Factory v3 default operation.

## Purpose
Exercise the passive evidence replay mode in `scripts/factory_v3_mission_record_lint.py`.

The replay fixture has two record files:

- `MISSION_900_RECORD.json`: complete evidence chain with existing changed files, state file, checkpoint evidence, interrupt JSON, audit JSON, and external verification-command mention.
- `MISSION_901_RECORD.json`: intentionally incomplete evidence chain that should produce advisory replay warnings for a missing state file, missing changed file, missing checkpoint evidence, and missing external verification-command mention.

Use:

```bash
python3 scripts/factory_v3_mission_record_lint.py \
  --target tests/fixtures/factory_v3_evidence_replay/root/.factory-v3/evidence \
  --record-files-only \
  --replay-evidence \
  --evidence-root tests/fixtures/factory_v3_evidence_replay/root \
  --expect tests/fixtures/factory_v3_evidence_replay/expected/replay.json \
  --json
```

Replay is passive and non-executing. It resolves paths, parses referenced JSON, searches related evidence files, and reports advisory findings only.
