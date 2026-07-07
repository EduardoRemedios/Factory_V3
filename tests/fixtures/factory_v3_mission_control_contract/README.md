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
