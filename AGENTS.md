# AGENTS.md - Factory V3 Repository Context Map

Purpose:
- Give agents a short, authoritative map for V3 work after the split from `factory-starter-kit`.

## 1) Read Order
1. `README.md`
2. `docs/Factory/v3/README.md`
3. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
4. `docs/Factory/v3/USER_GUIDE.md`
5. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
6. `docs/Factory/EXTERNAL_GOVERNANCE_KERNEL_BOUNDARY.md`
7. Current V3 evidence under `docs/Factory/runs/` when a task references a run, decision, or profile.

## 2) Canonical Advisory Commands
- V3 docs advisory lint: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- V3 operational-readiness eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- V3 natural-language pilot eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- V3 mission-record lint: `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json`

## 3) Hard Guardrails
- Preserve V3 advisory-only semantics unless explicit release evidence approves promotion.
- Do not imply Factory V2 deprecation.
- Do not wire advisory validators into required gates without explicit approval.
- Do not introduce runtime authority, proof, lease enforcement, telemetry, governance routing, or external governance-kernel adapters without separate approval.
- Keep deterministic fixture outputs stable when changing validator behavior.
- Apply SIMPLE-CODE-GATE: prefer the smallest direct change, avoid dependency creep, and fail clearly for invalid records or config.
