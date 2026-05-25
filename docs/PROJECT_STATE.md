# PROJECT_STATE.md - Factory V3 State

> Last updated: 2026-05-25

## What Exists

- Factory V3 content has moved from `factory-starter-kit` into this repository.
- Factory V2 process docs, templates, scripts, and helper fixtures are present in this repository as temporary build-support scaffolding for V3 development work.
- Optional operational use is approved only for `V3-OP-001 Bounded Code Change`.
- V3 docs, templates, trials, evidence, advisory scripts, and deterministic fixtures are present under this repository.
- The migrated content preserves its original paths where practical so historical evidence remains readable.

## Current Boundary

- This repository does not make Factory V3 the default for all work.
- This repository does not currently deprecate Factory V2.
- Factory V2 remains available as the planning/governance process for building V3 when Factory-controlled planning is needed while V3 is still maturing.
- The intended future state is V3 as a separate product with no V2 dependency in this repository, after explicit confidence evidence and release approval. V2 remains preserved in the separate V2-only repository.
- Advisory validators remain advisory unless future evidence and approval promote them.
- Runtime authority, proof, lease enforcement, telemetry, governance routing, and external governance-kernel adapters remain out of scope unless explicitly approved.

## Verification

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json
```
