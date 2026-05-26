# Sprint Envelope: SPRINT_20260526_1304_PHASE4_EVAL_PLAN

## Version
v0.2

## Change Log
- v0.2 (2026-05-26): Hardened after envelope red-team review.
- v0.1 (2026-05-26): Initial Stage H envelope.

## Sprint ID
- `SPRINT_20260526_1304_PHASE4_EVAL_PLAN`

## Execution Mode
- PLANNING_ONLY for this run.
- Future implementation requires separate explicit human approval after this pack.

## Objective
Prepare the execution envelope for future Phase 4 planning artifacts without implementing them now.

## File-touch Budget For Future Execution
- MS-01: up to 1 new doc, `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`.
- MS-02: up to 1 new template, `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`.
- MS-03: up to 1 planning section or appendix inside the Phase 4 plan for fixture expansion and FP/FN rollup; no fixture files unless a later approval names them.
- MS-04: no product files expected beyond approved closeout evidence if execution is later authorized.
- Total future budget: 2 new V3 files plus planning text inside the Phase 4 plan. Any script, validator, CI, `factoryctl`, required-gate, telemetry-completeness, router, runtime-authority, proof, lease, or V2-removal edit is out of scope.

## Implementation Constraints For Future Execution
- Preserve V3 advisory/optional status.
- Preserve V2 fallback and non-deprecation language.
- Keep thresholds advisory and non-operational.
- Bind capability observations to harness, model when known, mission profile, repo, tools, date, and evidence.
- Carry the Phase 3 missing natural halted, fallback, or clarification-heavy telemetry case as an evidence gap.
- Apply SIMPLE-CODE-GATE: smallest clear change, no dependency creep, no broad abstractions, no silent failures.

## Verification Before Future Merge
- Run `bash scripts/knowledge_lint.sh`.
- Run `./scripts/factoryctl context-index`.
- Run V3 advisory lint: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`.
- Run operational readiness eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`.
- Run natural-language pilot eval: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`.
- Run `git diff --check`.
- Perform no-touch review for prohibited systems and Phase 5 router drift.

## Stop Conditions
- Any implementation authority appears in this planning run.
- Threshold language reads as routing, default promotion, or reduced governance.
- V2 is described as deprecated or replaced.
- Telemetry becomes required, complete-by-default, CI-wired, or gate-enforced.
- Runtime authority, proof, lease enforcement, external governance-kernel adapter work, or V2 scaffolding removal appears.

## References
- `pack/verification_plan.md`
- `pack/traceability_matrix.md`
- `pack/micro_sprints.md`
