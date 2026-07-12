# Sprint Envelope - Mission Re-entry Proof Pack

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Stage I hardening binds controlled scenario types, common-shape short-circuiting, mutation proofs, and execution-run reproduction rules.
- v0.1 (2026-07-12): Stage H candidate implementation envelope.

## Identity
- Sprint ID: `SPRINT_20260712_1249_V3_MISSION_REENTRY_PROOF_PACK`
- Run ID: `RUN_20260712_1249_v3_mission_reentry_proof_pack`
- Execution mode: `PLANNING_ONLY`
- Status: candidate implementation contract; cannot execute under this run

## Objective
Make clean, stale, changed-authority, and failed-verification re-entry decisions concrete in the existing advisory mission-control contract surface, with deterministic fixtures and no runtime authority.

## Authorized Product Files
1. `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
2. `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`
3. `docs/Factory/v3/templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`
4. `scripts/factory_v3_mission_control_contract_lint.py`
5. `tests/fixtures/factory_v3_mission_control_contract/README.md`
6. `tests/fixtures/factory_v3_mission_control_contract/valid_reentry_decisions.json`
7. `tests/fixtures/factory_v3_mission_control_contract/invalid/reentry_stale_state_continues.json`
8. `tests/fixtures/factory_v3_mission_control_contract/invalid/reentry_changed_authority_continues.json`
9. `tests/fixtures/factory_v3_mission_control_contract/invalid/reentry_failed_verification_without_recovery_continues.json`
10. `tests/fixtures/factory_v3_mission_control_contract/invalid/reentry_clean_missing_safe_action.json`
11. `tests/fixtures/factory_v3_mission_control_contract/expected/all.json`
12. `docs/Factory/v3/README.md`
13. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
14. `docs/Factory/v3/ANCHOR_REGISTRY.md`
15. `docs/PROJECT_STATE.md`
16. `docs/ROADMAP.md`
17. `docs/CHANGELOG.md`
18. `docs/Factory/v3/FRESH_WORKER_REENTRY_TRIAL_PLAN.md`

Run-root planning/execution closeout files and deterministic temporary reports under `/tmp` are excluded from the product cap.

## File-Touch Budget
| Micro-sprint | Maximum product files |
| --- | ---: |
| MS-00 | 0 |
| MS-01 | 4 |
| MS-02 | 6 |
| MS-03 | 2 |
| MS-04 | 6 |
| MS-05 | 0 additional |
| Total unique | 18 |

## Locked Behavior
- `reentry_protocol` remains reusable policy.
- Optional observed examples live only under `fixture_scenarios.reentry_cases`.
- Absence of `reentry_cases` is a no-op.
- Clean re-entry requires matching repository/authority state, passing current verification, one safe next action, and authority basis.
- Stale repository state requires `safe_hold` plus `stale_reentry`.
- Changed authority requires `safe_hold` plus `approval_required`.
- Failed verification without recovery authority requires safe-hold/halt plus `failed_verification`.
- Explicit recovery authority permits only one bounded `verify` action, not general continuation, closeout, or completion.
- `fresh_session` is scenario input, not proof of a real fresh or cross-harness session.
- Session memory is never sufficient.

## Advisory Finding Contract
- MC148 malformed optional container.
- MC149 malformed common case fields.
- MC150 invalid clean re-entry decision.
- MC151 stale repository decision does not safe-hold correctly.
- MC152 changed-authority decision does not safe-hold correctly.
- MC153 failed-verification/recovery-authority decision is unsafe or overbroad.

Controlled `scenario_type` values are:
- `clean_fresh_session_reentry`;
- `stale_repository_state`;
- `changed_authority_envelope`;
- `failed_verification_without_recovery_authority`;
- `failed_verification_with_bounded_recovery`.

Container and common-shape checks run before semantic checks. A malformed case emits MC148 or MC149 and skips scenario-specific evaluation so fixtures cannot accumulate misleading secondary findings.

## Allowed Implementation
- Direct template/docs edits at exact paths.
- One direct optional `_check_reentry_cases` helper called from `_check_fixture_scenarios` or equivalent existing fixture path.
- One rich valid and four isolated invalid repository fixtures.
- Invalid fixtures must be mechanically compared with the rich valid source and differ only in the intended case mutation plus record identity metadata if required.
- Deterministic temporary derivatives for MC148/MC149.
- Expected `all.json` regeneration only after old-subset equality.
- Run-root closeout mission record using existing optional evidence-integrity fields where relevant.

## Forbidden Implementation
- New schema, validator executable, dependency, recursive rule engine, registry, plugin, runtime state store, loop runner, dispatcher, scheduler, background worker, standing authorization, telemetry enforcement, routing, CI/factoryctl/required-gate wiring, historical record rewrite, live trial, real data, credential use, external effect, deployment, profile promotion, endurance field, V2 removal, commit, or push without separate authorization.

## SIMPLE-CODE-GATE
Use one direct helper and controlled constants only if they reduce branching. Do not generalize beyond the five named scenarios or create abstractions for future event types.

## Verification Commands
- `python3 -m py_compile scripts/factory_v3_mission_control_contract_lint.py`
- JSON parse for template and all mission-control fixtures.
- `python3 scripts/factory_v3_mission_control_contract_lint.py --target tests/fixtures/factory_v3_mission_control_contract --expect tests/fixtures/factory_v3_mission_control_contract/expected/all.json --json`
- Direct existing-valid and each new fixture checks with exact finding-set assertions.
- Filtered baseline compatibility comparison before expected-output installation.
- Temporary MC148/MC149 derivatives.
- Mission-record, telemetry, loop-contract, advisory docs, readiness, knowledge, context, stage, and pack checks named in `verification_plan.md`.
- `git diff --check` and exact changed-product-path comparison.

## Halt Conditions
- Existing valid contract or old-subset output changes.
- Optional case absence emits a finding.
- Stale or changed authority can continue.
- Failed verification can continue without recovery authority.
- Recovery authority permits `continue` or `close`.
- More than four invalid repository fixtures, more than 18 product paths, or any unrelated change is needed.
- Runtime, required-gate, routing, promotion, live-proof, endurance, dependency, or external-effect implication appears.

## Completion Conditions
- AC1-AC14 pass.
- MC148-MC153 branches are deterministic.
- Four invalid fixtures isolate MC150-MC153.
- Historical behavior is exact after filtering new paths.
- Full verification passes with `blocking_effect: none` retained.
- Closeout records one bounded shadow-use observation and does not claim live re-entry proof.

## Authorization Boundary
This planning-only envelope does not authorize implementation. After I2 and pack-lint PASS, the human may issue Go for a separate `EXECUTION_ENABLED` run using this exact envelope.

The execution-enabled run must copy this exact product path list, behavior contract, finding policy, verification checks, and file budgets. Any change requires a new planning decision; human Go does not authorize silent envelope expansion.
