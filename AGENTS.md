# AGENTS.md - Factory V3 Repository Context Map

Purpose:
- Give agents a short, authoritative map for V3 work after the split from `factory-starter-kit`.
- Factory V3 is the subject under development. Factory V2 is temporary build-support scaffolding to use when work needs Factory-controlled planning; it is not a V3 product dependency.
- Intended direction: once V3 is built, confidence-backed, and explicitly approved, this repository may become V3-only and deprecate/remove the V2 scaffolding here. The separate V2-only repository remains the place where V2 is preserved.

## 1) Read Order
1. `README.md`
2. `docs/PROJECT_STATE.md`
3. `docs/ROADMAP.md`
4. `docs/Factory/ARCHITECTURE.md`
5. `docs/Factory/ORCHESTRATION.md`
6. `docs/Factory/Spec/STAGE_CONTRACTS.md`
7. `docs/Factory/v3/README.md`
8. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
9. `docs/Factory/v3/USER_GUIDE.md`
10. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
11. `docs/Factory/EXTERNAL_GOVERNANCE_KERNEL_BOUNDARY.md`
12. Current V3 evidence under `docs/Factory/runs/` when a task references a run, decision, or profile.

## 2) Canonical V2 Commands
- Knowledge lint preflight: `bash scripts/knowledge_lint.sh`
- Context index refresh: `./scripts/factoryctl context-index`
- Stage validation: `./scripts/factoryctl stage-lint --run <RUN_ID> --stage <STAGE>`
- Pack validation: `./scripts/factoryctl pack-lint --run <RUN_ID>`
- Run metrics initialization: `./scripts/factoryctl metrics-init --run <RUN_ID>`
- Task memory initialization: `./scripts/factoryctl memory-init`
- Repo cartographer scan: `./scripts/cartographer`
- Mission lint: `bash scripts/mission_lint.sh <MISSION_ID>` when advancing an already-authorized mission unit.
- Mission cursor lint: `bash scripts/mission_cursor_lint.sh <MISSION_ID>` when using the optional derived cursor.

## 3) Canonical V3 Advisory Commands
- V3 docs advisory lint: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- V3 operational-readiness eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- V3 natural-language pilot eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- V3 mission-record lint: `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json`

## 4) Hard Guardrails
- Use Factory V2 planning, lint, pack, and SIMPLE-CODE-GATE semantics to govern V3 repository changes when Factory-controlled planning is needed while V3 is still maturing.
- Preserve V3 advisory-only semantics unless explicit release evidence approves promotion.
- Do not imply current Factory V2 deprecation in this repository until explicit V3 confidence and release evidence approves that transition.
- Do not wire advisory validators into required gates without explicit approval.
- Do not introduce runtime authority, proof, lease enforcement, telemetry, governance routing, or external governance-kernel adapters without separate approval.
- Keep deterministic fixture outputs stable when changing validator behavior.
- Apply SIMPLE-CODE-GATE: prefer the smallest direct change, avoid dependency creep, and fail clearly for invalid records or config.
