# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for the Phase 2.5 decision.

## Checks

| ID | Tier | Command or Review | Expected |
|---|---|---|---|
| V1 | V1 | `bash scripts/knowledge_lint.sh` | PASS |
| V2 | V1 | `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json` | ADVISORY_PASS |
| V3 | V1 | `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json` | ADVISORY_PASS |
| V4 | V1 | `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json` | ADVISORY_PASS |
| V5 | V1 | `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json` | ADVISORY_PASS |
| V6 | V1 | `git diff --check` | PASS |
| V7 | V0 | Manual source-of-truth review | Records remain shadow-only |
