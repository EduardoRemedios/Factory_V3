# Sprint Envelope: SPRINT_20260527_0712_PHASE4_REAL_RUN_CORPUS

## Version
v0.2

## Change Log
- v0.2 (2026-05-27): Hardened after envelope red-team review.
- v0.1 (2026-05-27): Initial Stage H envelope.

## Sprint ID
- `SPRINT_20260527_0712_PHASE4_REAL_RUN_CORPUS`

## Execution Mode
- PLANNING_ONLY for this run.
- Future artifact writing requires explicit user approval after this pack.

## Objective
Prepare the implementation envelope for real-run corpus capture planning artifacts only.

## File-touch Budget For Future Execution
- `docs/Factory/v3/PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`: new file.
- `docs/Factory/v3/templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md`: new file.
- Optional canonical status touch if artifacts are created: up to 3 docs among `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, and `docs/Factory/v3/README.md`.
- Total budget: 2 new V3 files plus up to 3 canonical status updates.
- No scripts, validators, fixtures, CI, required gates, telemetry logs, mission records, router files, runtime files, proof files, lease files, or V2 removal files.

## Constraints
- Do not execute real missions.
- Do not collect telemetry.
- Do not approve candidate missions.
- Preserve V3 advisory-only status and V2 fallback.
- Preserve the Phase 3 missing natural halted, fallback, or clarification-heavy evidence gap.
- Optional telemetry may be planned only as separately approved shadow evidence.
- Apply SIMPLE-CODE-GATE.

## Verification Before Merge
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `git diff --check`

## Stop Conditions
- Any artifact authorizes live mission execution.
- Any artifact claims routing, reduced governance, required gates, telemetry completeness, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 removal.
- Any artifact treats current synthetic fixtures as real negative-case evidence.
