# Execution Prompt - Recall Sync And Endurance Canon

## Version
v1.1

## Change Log
- v1.1 (2026-07-12): Instantiated after I2 PASS and explicit human Go.

## Run Metadata
- RUN_ID: `RUN_20260712_0927_v3_recall_sync_endurance_canon`
- Sprint ID: `SPRINT_20260712_0927_V3_RECALL_SYNC_ENDURANCE_CANON`
- Created: 2026-07-12 09:27 Atlantic/Canary
- Source Pack: `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/`

## Purpose
Synchronize the commit-pinned Factory V2 direct-source recall repair, prove it before continuing, then reconcile active V3 canon so roughly four hours is an endurance capability ceiling rather than a workload floor. Runtime authority, profile promotion, orchestration, scheduled execution, required gates, telemetry enforcement, schema expansion, historical evidence rewriting, commit, and push are out of scope.

## Required Read Order
1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md` `## Active Pitfalls (Mandatory)` only
5. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/intent.md`
6. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/intent_lock_report.md`
7. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/risk_register.md`
8. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/verification_plan.md`
9. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/traceability_matrix.md`
10. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/verification_manifest.yaml`
11. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/micro_sprints.md`
12. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/SPRINT_20260712_0927_V3_RECALL_SYNC_ENDURANCE_CANON_ENVELOPE.md`
13. `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract
- Use the factory-execution-closeout skill for scope comparison, verification review, and closeout decision.
- No dedicated implementation skill applies; execute the implementation via the approved envelope and micro-sprint contract.

## Hard Guardrails
- Do not expand the authorized file list.
- Read upstream source from commit `06646d7`; do not mutate the separate upstream worktree.
- Preserve V3 advisory-only, no-promotion, and V2-fallback boundaries.
- Do not edit prior run evidence or human adjudication records.
- A mission stops when objective and verification are complete; never pad time, calls, waypoints, tests, files, or scope.
- Do not claim that this repair proves four-hour endurance.

## SIMPLE-CODE-GATE (v2)
- Implement the smallest direct change.
- No dependency creep, speculative abstraction, broad validator refactor, hidden side effects, or silent failure.
- Fail clearly for invalid repair evidence.

## Micro-sprint Execution Sequence
0. MS-00 Baseline And Source Pin: verify source commit, target state, and baseline. Stop on ambiguous overlap or unclassified failure.
1. MS-01 V2 Contract And Template Sync: edit three contract/template files. Stop if raw `WEAK` semantics weaken.
2. MS-02 Validator And Test Sync: edit four validator/test files. Stop on unrelated refactor or deterministic regression.
3. MS-03 V2 Slice Verification Gate: run focused/full tests, compile, knowledge lint, and source comparison. No V3 canon edit before PASS.
4. MS-04 Endurance And Active-Canon Reconciliation: make minimal active status and semantics edits within the authorized candidate set.
5. MS-05 Independent Verification And Closeout: run every planned check and report AC1-AC13 evidence status.

## Verification Contract
- Run every check in `pack/verification_manifest.yaml` in order.
- Run every additional required check in `pack/verification_plan.md`.
- Any `halt_on_failure: true` failure stops execution.
- Preserve command evidence under `artifacts/verification/` or in the execution closeout record.
- Run `git diff --check` and changed-path/no-touch review before closeout.

## Troubleshooting And Failure Policy
- Stop at a failed gate and report the exact command and likely cause.
- Do not weaken tests, validators, evidence classifications, or approval boundaries to pass.
- If source or canon state becomes stale or contradictory, safe-hold and request human direction.

## Final Exit Checklist
- [ ] Scope delivered per envelope and micro-sprints.
- [ ] SIMPLE-CODE-GATE v2 satisfied.
- [ ] V2 slice passed before V3 canon edits.
- [ ] All verification commands passed.
- [ ] AC1-AC13 classified with evidence.
- [ ] Project state, roadmaps, changelog, and active V3 status agree.
- [ ] Upper-envelope evidence gap remains explicit.
- [ ] No unauthorized path, external effect, commit, or push occurred.
