# Sprint Envelope - Mission 026 Claim-To-Proof And FP/FN Adjudication

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Stage I hardening requires all replay commands to run in the detached `/tmp` clone, adds before/after source status comparison, and separates generated cache/output from source evidence.
- v0.1 (2026-07-12): Stage H execution envelope.

## Sprint Identity
- Sprint ID: `SPRINT_20260712_1002_V3_M026_CLAIM_PROOF_ADJUDICATION`
- Run ID: `RUN_20260712_1002_v3_m026_claim_proof_adjudication`
- Execution mode: `EXECUTION_ENABLED`
- Status: awaiting I2 PASS and post-pack human Go

## Objective
Create a commit-pinned Mission 026 claim-to-proof ledger, replay key evidence without modifying the source POC, independently inspect browser artifacts, perform FP/FN review, and record explicit `NO PROMOTION YET` adjudication under the corrected endurance model.

## Authorized Product Files
New audit artifacts:
- `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`

Active pointer/status updates:
- `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ladder/rung3/README.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`

Planning/closeout files under this run root and replay artifacts under `/tmp/factory_v3_m026_audit_20260712` are authorized. POC source files are read-only and forbidden from modification.

## File-Touch Budget
| Micro-sprint | Product files |
| --- | ---: |
| MS-00 | 0 |
| MS-01 | 0 |
| MS-02 | 1 |
| MS-03 | 2 |
| MS-04 | up to 8 additional |
| MS-05 | 0 additional |
| Total unique maximum | 11 |

## Source Authority
- POC source commit: `404a32a`.
- Baseline: `8f25437`.
- Commit-pinned `git show`, `git diff`, and detached temporary clone outrank mutable source working-tree content.
- Screenshots from source paths require hash agreement with commit-pinned browser notes before visual use.

## Allowed Commands And Tools
- Read-only `git`, `rg`, `sed`, `find`, `shasum`, `diff`, JSON parsing, and file inspection.
- Local `git clone --no-hardlinks` into the named `/tmp` path and detached checkout there.
- POC focused/full unittest commands and existing Mission 024/026 QA/verifier scripts in the temporary clone.
- Factory V3 knowledge lint, advisory lint, operational-readiness evals, mission-record lint, stage/pack lint, context index, and `git diff --check`.
- Local image inspection for the four final Mission 026 screenshots.

No dependency installation, source POC write, network write, external message, deployment, credential use, destructive source command, commit, or push is authorized.

All POC Python, QA, verifier, JSON, and screenshot-hash commands must run with working directory `/tmp/factory_v3_m026_audit_20260712` after detached checkout. The source POC may receive read-only Git commands only. Record source `git status --short --branch` before clone and after all replay; any changed tracked or untracked state attributable to this run is a hard failure.

## Claim Grading Rules
- `PROVED`: direct source plus reproducible command, source/test path, hash-and-visual evidence, or equivalent independent artifact proof.
- `WEAK`: plausible and partially corroborated, but dependent on self-attestation, same-actor verification, missing raw logs, or incomplete absence proof.
- `MISSING`: required evidence is absent and no reliable inference closes it.
- `CONTRADICTED`: direct evidence conflicts with the claim or field value.
- Every positive status must name its limit.

## Required Findings
- Classify the stale final `commit_after` value.
- Separate original summaries from 2026-07-12 replay.
- Do not treat replay-generated caches, temporary databases, or rewritten audit output in the clone as original Mission 026 evidence.
- Separate deterministic verifier scripts from actor independence.
- Narrow “no Factory V2” and other absence claims to what evidence can support.
- Separate Mission 026 PASS, observed duration exposure, and insufficient upper-envelope endurance evidence.
- Map decision-pack items 1-5 and retain `NO PROMOTION YET`.

## Verification Contract
Run every manifest check and every additional check in `verification_plan.md`. Verify source status before and after. Visually inspect desktop/mobile governance screenshots. Run Factory advisory and deterministic gates after pointer updates. Any source mutation, promotion implication, or unauthorized path is a hard halt.

## Halt And Fallback
Halt if source commit identity fails, the source POC changes, replay requires dependencies or source repair, visual evidence is unavailable, material claims cannot be graded honestly, file budget expands, or canon implies promotion. Factory V2 remains the governing fallback; this run grants no V3 execution profile.

## Completion Conditions
- AC1-AC14 have evidence statuses.
- Claim inventory is complete.
- Replay provenance and limitations are explicit.
- Screenshot identity and visual findings are recorded.
- FP/FN definitions and findings are applied.
- Decision remains `NO PROMOTION YET`.
- At most 11 product files changed; no POC/historical evidence changed.
- Required Factory checks pass and closeout is ready.
