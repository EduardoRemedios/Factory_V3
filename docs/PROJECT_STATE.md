# PROJECT_STATE.md - Factory V3 State

> Last updated: 2026-05-27

## What Exists

- Factory V3 content has moved from `factory-starter-kit` into this repository.
- Factory V2 process docs, templates, scripts, and helper fixtures are present in this repository as temporary build-support scaffolding for V3 development work.
- Optional operational use is approved only for `V3-OP-001 Bounded Code Change`.
- V3 docs, templates, trials, evidence, advisory scripts, and deterministic fixtures are present under this repository.
- Phase 3 telemetry/replay now has a fixture-first advisory replay validator, deterministic fixtures, three real advisory telemetry pilot logs under `docs/Factory/v3/telemetry/pilots/`, and an evidence review at `docs/Factory/v3/PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`.
- Phase 4 eval expansion has started. `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`, `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`, and synthetic `V3-P4-*` operational-readiness fixtures now exist.
- Phase 4 real-run corpus capture planning artifacts now exist at `docs/Factory/v3/PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md` and `docs/Factory/v3/templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md`.
- Phase 4 real-run corpus and harness-profile indexes now exist at `docs/Factory/v3/real_run_corpus/INDEX.md` and `docs/Factory/v3/harness_profiles/INDEX.md`.
- Three separately approved Phase 4 real-run capture records now exist under `docs/Factory/v3/real_run_corpus/`, with matching harness profiles under `docs/Factory/v3/harness_profiles/`.
- The Phase 4 negative-case opportunity register now exists at `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md` as research-only planning aid for future natural halt, fallback, clarification-heavy, stale-reentry, or advisory FP/FN opportunities.
- The migrated content preserves its original paths where practical so historical evidence remains readable.

## Current Boundary

- This repository does not make Factory V3 the default for all work.
- This repository does not currently deprecate Factory V2.
- Factory V2 remains available as the planning/governance process for building V3 when Factory-controlled planning is needed while V3 is still maturing.
- The intended future state is V3 as a separate product with no V2 dependency in this repository, after explicit confidence evidence and release approval. V2 remains preserved in the separate V2-only repository.
- Advisory validators and telemetry replay checks remain advisory unless future evidence and approval promote them.
- Runtime authority, proof, lease enforcement, telemetry enforcement, governance routing, and external governance-kernel adapters remain out of scope unless explicitly approved.
- Phase 3 telemetry is conditionally recommended only as optional advisory shadow evidence for selected narrow `V3-OP-001` evidence missions. It is not required or gate-enforced.
- Phase 4 remains research-only and non-enforcing. Three happy-path docs-only `V3-OP-001` real-run corpus records exist with `NO_TELEMETRY`, and the opportunity register lists unapproved future opportunities only; they do not close the Phase 3 natural halted/fallback/clarification-heavy gap and do not support routing, reduced governance, required gates, default-mode behavior, V3 promotion, or V2 build-support removal.

## Verification

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json
python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json
python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json
```
