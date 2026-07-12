# Handoff Stage I

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Initial Stage I handoff.

## Stage
- Stage ID: STAGE_I
- Stage Name: Envelope Red/Blue
- Timestamp: 2026-07-12 10:02 Atlantic/Canary
- Execution profile used: Codex high-reasoning
- Contradiction status: No unresolved Critical or High findings.
- Applicable hard rules: Iteration and challenge skill rules satisfied.

## Iteration
Iteration: 1 of max 2

## Inputs (LOAD)
- sprint envelope
- `pack/verification_plan.md`
- `pack/traceability_matrix.md`
- `pack/micro_sprints.md`

## Inputs (DISK)
- fixtures, manifest, risk register, intent lock

## Skill Routing Contract
- Skill used (or `NONE`): factory-challenge-mission
- Use when: challenging the execution envelope.
- Do not use when: implementing or granting Go.
- Expected output artifact(s): challenge report and hardened envelope.

## Outputs Produced (paths)
- `pack/SPRINT_20260712_1002_V3_M026_CLAIM_PROOF_ADJUDICATION_ENVELOPE_REDTEAM.md`
- `pack/SPRINT_20260712_1002_V3_M026_CLAIM_PROOF_ADJUDICATION_ENVELOPE.md`

## Changes Made
- Pinned replay working directory, source status comparison, and replay-output provenance.

## Assumptions
- The named `/tmp` clone path is absent at execution start.

## Open Issues
### BLOCKING
- None.

### NON-BLOCKING
- Actor independence remains an audit limitation.

## Verification Steps Recommended
- Run stage-lint for Stage I.

## Exit Criteria Status
- PASS
