# Intent - Mission Re-entry Proof Pack

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Adopted Stage B recovery-boundary, policy/event separation, isolated-fixture, claim-bounding, compatibility, and canon-scope fixes.
- v0.1 (2026-07-12): Initial Stage A intent.

## Purpose
Make Factory V3's re-entry decision semantics concrete and deterministically reviewable without implementing runtime orchestration.

## Goal
Extend the existing advisory mission-control contract fixture surface with five re-entry decision cases: clean continuation, stale-repository safe-hold, changed-authority safe-hold, failed-verification safe-hold without recovery authority, and one bounded recovery/verification action with explicit authority.

## Source Requirements
- R1 [SOURCE: sponsor approval, 2026-07-12] Proceed with the Mission Re-entry Proof Pack as the next bounded Factory slice.
- R2 [SOURCE: `docs/ROADMAP.md`] Use optional evidence-integrity fields in suitable records and harden concrete mission-state/re-entry proof before orchestration discovery.
- R3 [SOURCE: `MISSION_CONTROL_CONTRACT.md`] Re-entry requires authored state, current repo checks, a last safe checkpoint, and one safe next action; session memory is insufficient.
- R4 [SOURCE: `LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`] Stale state, changed authority, and failed verification without recovery authority require safe-hold.
- R5 [SOURCE: `MISSION_RECORD_DESIGN_V0.md`] Optional evidence-integrity observations and bounded claims remain advisory and reference evidence rather than replacing it.
- R6 [SOURCE: `AGENTS.md`] No runtime authority, gate promotion, routing, telemetry enforcement, or profile promotion without separate approval.

## Design Choice
Use the existing `fixture_scenarios` extension point in the mission-control contract. Add optional `reentry_cases`; do not create a new top-level schema, standalone validator, runtime state model, or generic scenario framework.

Each re-entry case should record:
- `scenario_type`;
- `fresh_session`;
- `repo_state_matches_checkpoint`;
- `authority_matches_checkpoint`;
- `verification_status`;
- `recovery_authority_present`;
- `expected_gate_result`;
- `expected_terminal_state`;
- `one_safe_next_action`;
- `authority_basis`;
- `required_evidence`;
- `safe_hold_or_interrupt_required`.

## Acceptance Criteria
- AC1: one rich valid fixture contains all five named re-entry cases.
- AC2: clean re-entry may continue only when repository state and authority match, verification is passing/current, and one safe next action has an authority basis.
- AC3: stale repository state cannot claim `continue`; it requires safe-hold and terminal state `stale_reentry`.
- AC4: changed authority cannot claim `continue`; it requires safe-hold and terminal state `approval_required`.
- AC5: failed verification without explicit recovery authority cannot claim `continue`; it requires safe-hold or halt and terminal state `failed_verification`.
- AC6: failed verification with explicit recovery authority may authorize only one bounded recovery or verification action, not general continuation or completion.
- AC7: session memory is never accepted as evidence or authority.
- AC8: four invalid fixtures isolate the semantic contradictions in AC2-AC5.
- AC9: optional mission-record evidence-integrity fields are used in the implementation closeout record where relevant, producing the first real authoring-friction/FP-FN note; planning artifacts alone do not count as operational evidence.
- AC10: existing mission-control contracts remain valid when `reentry_cases` is absent.
- AC11: existing expected behavior is unchanged after filtering the five new fixtures.
- AC12: validator remains standalone, advisory, and `blocking_effect: none`.
- AC13: no new dependency, runtime behavior, required gate, routing, telemetry enforcement, profile promotion, historical rewrite, or endurance field.
- AC14: no more than the 18 authorized product paths are changed.

## Authorized Product Scope
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

Run-root planning/closeout files and temporary deterministic reports under `/tmp` are excluded from the product cap.

## Non-Goals
- No execution before a separate post-I2 human Go.
- No live cross-session or cross-harness trial; `FRESH_WORKER_REENTRY_TRIAL_PLAN.md` remains unexecuted.
- No worker dispatcher, loop runner, scheduler, background process, standing authorization, persistent runtime state, or external effects.
- No mission-record schema expansion; use its already optional evidence-integrity structures only in closeout where relevant.
- No `V3-OP-003` promotion or endurance claim.

## Principles
- Policy remains in `reentry_protocol`; examples remain in optional `fixture_scenarios.reentry_cases`.
- Validate only high-value semantic contradictions, not prose quality or exhaustive workflow state.
- Preserve evidence of failure; do not turn safe-hold scenarios into malformed records merely because the mission cannot continue.
- Prefer explicit checks over a generic rule engine.

## Advisory Finding Policy
- `V3-MC148`: optional `reentry_cases` container is malformed.
- `V3-MC149`: a supplied re-entry case lacks common shape/evidence fields.
- `V3-MC150`: clean re-entry lacks current matching state, passing verification, authority basis, or one safe next action.
- `V3-MC151`: stale repository state does not safe-hold as `stale_reentry`.
- `V3-MC152`: changed authority does not safe-hold as `approval_required`.
- `V3-MC153`: failed verification without recovery authority permits continuation, or recovery authority permits an action broader than `verify`.

The four repository invalid fixtures isolate `V3-MC150` through `V3-MC153`. `V3-MC148` and `V3-MC149` may be checked with deterministic temporary derivatives rather than expanding the repository fixture count.

## Roles
- Factory root planner: coordinate A-I2 only.
- Implementer after Go: make bounded docs/fixture/validator changes.
- Verifier: compare historical outputs, run deterministic scenarios, and audit authority claims.
- Human sponsor: decide Go/No-go after I2.

## Open Issues
### BLOCKING
- None for planning.

### NON-BLOCKING
- Exact advisory finding IDs/messages may be assigned during planning, but semantics and isolated fixture coverage must remain fixed.

## Go Or No-Go Rule
Go only after Stage I2 PASS, pack-lint PASS, and explicit human Go. No-go on duplicate schema, historical regression, optional-field completeness enforcement, scope expansion, or any runtime/authority implication.
