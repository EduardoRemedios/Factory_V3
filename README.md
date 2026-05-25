# Factory V3

Factory V3 is the experimental and operational-evidence track for mission-governed AI coding workflows.

This repository was split out of `factory-starter-kit` so V3 can evolve independently from Factory V2 and earlier content.

## Current Scope

- Optional `V3-OP-001 Bounded Code Change` guidance and evidence.
- V3 mission-envelope, closeout, fallback, SIMPLE-CODE-GATE, and mission-record templates.
- V3 advisory validators and deterministic fixtures.
- V3 operational-readiness, trial, and decision evidence.
- External governance-kernel boundary guidance for V3 work.

## Important Boundaries

- Factory V3 does not make Factory V2 obsolete.
- V3 required-gate integration is not implied by this repository split.
- Runtime authority, production action mediation, proof, leases, telemetry, and governance routing remain separately governed by explicit V3 evidence and approval.
- Existing V3 advisory tools remain advisory unless a future release explicitly promotes them.

## Key Paths

- `docs/Factory/v3/` - primary V3 docs, templates, trials, and roadmap.
- `docs/Factory/runs/` - V3-related Factory run evidence migrated from `factory-starter-kit`.
- `scripts/factory_v3_*.py` - standalone advisory V3 validators.
- `tests/fixtures/factory_v3_*/` - deterministic fixture corpora for the advisory validators.

## Basic Verification

```bash
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json
```
