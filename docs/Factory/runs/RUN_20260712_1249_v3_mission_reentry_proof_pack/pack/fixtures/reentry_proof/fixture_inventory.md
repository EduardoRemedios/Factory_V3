# Re-entry Proof Fixture Inventory

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F fixture inventory.

## Valid Rich Fixture
- `valid_reentry_decisions.json`: five re-entry cases covering clean continuation, stale repository state, changed authority, failed verification without recovery authority, and explicitly authorized bounded recovery verification.

## Invalid Fixtures
- `reentry_clean_missing_safe_action.json` -> `V3-MC150` only.
- `reentry_stale_state_continues.json` -> `V3-MC151` only.
- `reentry_changed_authority_continues.json` -> `V3-MC152` only.
- `reentry_failed_verification_without_recovery_continues.json` -> `V3-MC153` only.

## Temporary Derivatives
- malformed `reentry_cases` container -> `V3-MC148`.
- malformed common case fields -> `V3-MC149`.

## Compatibility Fixture
- Existing `valid_mission_control_contract.json` remains unchanged and passes with absent `reentry_cases`.
