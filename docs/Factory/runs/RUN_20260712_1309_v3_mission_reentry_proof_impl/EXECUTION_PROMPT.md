# Execution Prompt - Mission Re-entry Proof Implementation

## Authorization
- Execution mode: `EXECUTION_ENABLED`
- Human authorization: explicit `Go` on 2026-07-12 against the passed planning envelope.
- Execute only the exact v0.2 envelope in this run.

## Read Order
1. `raw_brief.md`
2. `pack/intent.md`
3. `pack/intent_lock_report.md`
4. `pack/risk_register.md`
5. `pack/verification_plan.md`
6. `pack/micro_sprints.md`
7. `pack/SPRINT_20260712_1309_V3_MISSION_REENTRY_PROOF_IMPL_ENVELOPE.md`
8. `pack/SPRINT_20260712_1309_V3_MISSION_REENTRY_PROOF_IMPL_ENVELOPE_REDTEAM.md`
9. `pack/PACK_AUDIT_REPORT.md`

## Execution Rules
- Follow MS-00 through MS-05 in order.
- Touch only the 18 authorized product paths plus run-root closeout evidence and `/tmp` reports.
- Apply SIMPLE-CODE-GATE: one direct optional helper, no dependency or generic framework.
- Preserve absent-case compatibility and historical deterministic output.
- Treat fixture `fresh_session` values as scenario inputs, not live proof.
- Recovery authority permits only one `verify` action.
- Halt on any envelope condition.

## Verification
Run the full `verification_manifest.yaml` and `verification_plan.md`, including baseline filtering, isolated finding sets, temporary MC148/MC149 derivatives, cross-validator regressions, knowledge lint, context index, stage/pack lint, exact path comparison, and diff check.

## Exit Checklist
- AC1-AC14 pass.
- Product paths changed: 18 or fewer, all authorized.
- `blocking_effect: none` retained.
- No runtime/gate/routing/promotion/endurance/dependency implication.
- Implementation closeout and retrospective complete.
- One bounded evidence-integrity shadow-use observation recorded without visual evidence.
- No commit or push unless separately authorized.
