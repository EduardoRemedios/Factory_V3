# Handoff Stage F

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F handoff.

## Stage
- Stage ID: STAGE_F
- Stage Name: Verification Design
- Timestamp: 2026-07-12 10:09 Atlantic/Canary
- Execution profile used: Codex
- Contradiction status: None.
- Applicable hard rules: tiered coverage and executable manifest.

## Inputs (LOAD)
- lock and risk artifacts

## Inputs (DISK)
- current commands and expected outputs

## Skill Routing Contract
- Skill used: NONE
- Use when: designing runnable checks.
- Do not use when: executing before Go.
- Expected output artifact(s): verification plan, traceability, manifest.

## Outputs Produced (paths)
- `verification_plan.md`; `traceability_matrix.md`; `verification_manifest.yaml`

## Changes Made
- Defined 15 checks and five manifest commands.

## Assumptions
- Dedicated old-fixture expected files remain stable.

## Open Issues
### BLOCKING
- None.
### NON-BLOCKING
- Additional existing fixture commands may be added at execution closeout.

## Verification Steps Recommended
- Stage F lint.

## Exit Criteria Status
- PASS
