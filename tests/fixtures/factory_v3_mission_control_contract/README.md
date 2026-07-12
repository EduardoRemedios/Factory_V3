# Factory V3 Mission-Control Contract Fixtures

These fixtures exercise the research-only advisory mission-control contract validator:

```bash
python3 scripts/factory_v3_mission_control_contract_lint.py --target tests/fixtures/factory_v3_mission_control_contract --json
```

Expected-output checks:

```bash
python3 scripts/factory_v3_mission_control_contract_lint.py --target tests/fixtures/factory_v3_mission_control_contract --expect tests/fixtures/factory_v3_mission_control_contract/expected/all.json --json
```

The validator emits `blocking_effect: none`. These fixtures are advisory and do not approve runtime orchestration, required gates, governance routing, scheduled execution, new profiles, or Factory V2 removal.

## Coverage

- `valid_mission_control_contract.json` covers the minimum rich advisory contract with next-action authorization, requirement-to-evidence status, independent verification, restartable handoff, safe-hold, and worker-interface fields.
- `invalid/next_action_continue_without_authority.json` proves continuation cannot be claimed without explicit authorization.
- `invalid/evidence_and_verifier_gaps.json` proves weak requirement evidence must name the unresolved gap and builder/verifier separation is represented.
- `invalid/reentry_and_approval_scope_unsafe.json` proves session memory alone is not sufficient for re-entry and advisory contracts cannot approve runtime, routing, required-gate, scheduled, default-mode, or new-profile behavior.
- `valid_reentry_decisions.json` covers five optional advisory re-entry cases: clean continuation, stale repository safe-hold, changed-authority safe-hold, failed verification without recovery authority, and one bounded recovery verification action.
- `invalid/reentry_clean_missing_safe_action.json` isolates an invalid clean continuation with no safe next action (`V3-MC150`).
- `invalid/reentry_stale_state_continues.json` isolates stale repository state that incorrectly continues (`V3-MC151`).
- `invalid/reentry_changed_authority_continues.json` isolates changed authority that incorrectly continues (`V3-MC152`).
- `invalid/reentry_failed_verification_without_recovery_continues.json` isolates failed verification that incorrectly continues without recovery authority (`V3-MC153`).

The `fresh_session` values in these fixtures are scenario inputs, not evidence that a live fresh-session or cross-harness handoff occurred.
