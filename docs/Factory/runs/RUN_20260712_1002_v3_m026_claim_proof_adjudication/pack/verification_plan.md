# Verification Plan - Mission 026 Claim Audit

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F verification plan.

## Strategy
Verify source identity, replay commit-pinned behavior in a temporary clone, inspect screenshots, reconcile every source claim, then validate Factory V3 boundary wording and pack integrity.

## Required Checks
| ID | Tier | Constraint | Check | Expected |
| --- | --- | --- | --- | --- |
| V4-001 | V4 | C-002, H-001 | Confirm POC commit `404a32a`, baseline `8f25437`, source status, and changed-path range | Exact commits readable; source POC unchanged |
| V4-002 | V4 | H-001, M-001 | Clone POC locally to `/tmp`, detach at `404a32a`, and record HEAD | Isolated exact-commit replay root |
| V2-003 | V2 | H-005 | Run Mission 026 focused recommendation/report tests | PASS with count recorded |
| V3-004 | V3 | H-005 | Run full POC test discovery at `404a32a` | PASS with count recorded |
| V2-005 | V2 | H-005 | Run Mission 024 verifier, Mission 026 QA, and Mission 026 verifier | PASS or explicit replay limitation |
| V1-006 | V1 | H-006 | Parse final mission record and audit summary; inspect `commit_after` | JSON valid; stale value classified `CONTRADICTED` |
| V4-007 | V4 | H-004 | Verify screenshot SHA-256 against browser notes | All audited hashes match |
| V4-008 | V4 | H-004 | Independently inspect final desktop/mobile governance screenshots | Claimed surfaces visible; blank/overflow findings recorded |
| V1-009 | V1 | H-002 | Inspect commit diff, dependency files, relevant code/tests, and boundary assertions | Presence/absence claims graded conservatively |
| V0-010 | V0 | H-003 | Review actor provenance for builder, QA, verifier, and audit replay | Independence limits explicit |
| V1-011 | V1 | H-005 | Reconcile claim inventory against closeout, record, audit summary, checkpoints, browser notes, state, QA, verifier, tests, and diff | No material claim family omitted |
| V0-012 | V0 | H-007 | Separate mission result, observed exposure, and upper-envelope coverage | Mission PASS; upper envelope insufficient |
| V1-013 | V1 | C-001 | Run V3 advisory lint and operational-readiness evals | No new authority/promotion regression |
| V3-014 | V3 | H-008 | Run knowledge lint, unit tests, stage/pack lint, and `git diff --check` in Factory V3 | All PASS |
| V1-015 | V1 | M-002 | Count changed Factory product paths | At most 9; no POC or historical evidence path changed |

## Evidence Interpretation
- Original command summaries: evidence that Mission 026 recorded a result, not raw output proof.
- Exact-commit replay: proof that the recorded behavior is reproducible in the current environment.
- Builder-authored QA/verifier: deterministic corroboration, not independent actor separation.
- Screenshot hash: artifact identity only.
- Visual inspection: surface meaning and obvious layout state.
- Diff/code/test inspection: bounded proof of what Mission 026 added or preserved within its change range.

## Failure Policy
Do not install dependencies, modify the source POC, repair evidence, weaken claim grades, or broaden Factory scope. A replay limitation may yield `WEAK` rather than aborting the audit; commit unavailability, source mutation, or promotion drift is a hard stop.
