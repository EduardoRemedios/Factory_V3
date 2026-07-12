# Handoff Stage F

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Initial Stage F handoff.

## Stage
- Stage ID: STAGE_F
- Stage Name: Verification Assets
- Timestamp: 2026-07-12 09:27 Atlantic/Canary
- Execution profile used: Codex high-reasoning
- Contradiction status: Verification covers every Critical and High constraint.
- Applicable hard rules: Verification tiers and executable manifest provided.

## Inputs (LOAD)
- `pack/intent.md`
- `pack/risk_register.md`

## Inputs (DISK)
- `pack/intent_lock_report.md`

## Skill Routing Contract
- Skill used (or `NONE`): NONE
- Use when: normal Stage F verification design is sufficient.
- Do not use when: a dedicated approved verification skill is required.
- Expected output artifact(s): fixtures, verification plan, traceability matrix, verification manifest.

## Outputs Produced (paths)
- `pack/fixtures/recall_repair_endurance/verification_cases.md`
- `pack/verification_plan.md`
- `pack/traceability_matrix.md`
- `pack/verification_manifest.yaml`

## Changes Made
- Added focused, regression, advisory, manual, no-touch, and source-comparison coverage.

## Assumptions
- Existing V3 fixture validators remain stable and advisory.

## Open Issues
### BLOCKING
- None.

### NON-BLOCKING
- Manual source-diff and canon review cannot be reduced to one trustworthy command.

## Verification Steps Recommended
- Run stage-lint for Stage F.

## Exit Criteria Status
- PASS
