# Raw Brief - Mission 026 Claim-To-Proof And FP/FN Adjudication

Execution Mode: EXECUTION_ENABLED

Execution Authorization: User approval in the active Codex thread on 2026-07-12: "Agree proceed" after the verified recall/endurance-canon run recommended a passive Mission 026 claim-to-proof audit followed by explicit `NO PROMOTION YET` FP/FN adjudication.

Downstream Fan-Out: NOT_APPROVED

## Objective
Audit the material claims made by POC Mission 026 against direct, commit-pinned evidence; classify each claim as `PROVED`, `WEAK`, `MISSING`, or `CONTRADICTED`; perform a false-positive/false-negative review under the corrected endurance model; and record an explicit `NO PROMOTION YET` adjudication against `V3_OP_003_DECISION_PACK.md`.

## Authoritative Source Baselines
- Factory V3 repository: current working tree after `RUN_20260712_0927_v3_recall_sync_endurance_canon`; those verified but uncommitted changes are baseline, not scope for reversal.
- POC repository: commit `404a32a`, with Mission 026 baseline `8f25437`.
- POC evidence must be read through commit-pinned Git content or a temporary clone checked out at `404a32a`; the mutable POC working tree and its unrelated untracked files are not authority.
- Screenshot files may be inspected from the unchanged POC paths only after hash comparison with Mission 026 browser notes.

## Required Outputs
- `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- Minimal active-canon updates required to point at the audit and preserve `NO PROMOTION YET`.
- Factory planning and execution evidence under this run root.

## Audit Requirements
- Enumerate material closeout, mission-record, browser, boundary, verification, and design-transfer claims.
- Cite exact POC commit paths, Factory source paths, commands, screenshots, hashes, or explicit gaps.
- Rerun Mission 026 focused/full verification and verifier scripts from a temporary clone pinned to `404a32a` where practical.
- Inspect desktop and mobile governance screenshots independently.
- Distinguish evidence produced by the builder from independent/replayed verification.
- Treat self-attested absence claims conservatively.
- Record stale or malformed evidence, including the unresolved final `commit_after` value, without modifying the POC.
- Separate mission PASS from endurance coverage: Mission 026 may be successful without proving quality continuity near four hours.

## Candidate Factory V3 Scope
- `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ladder/rung3/README.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`

The implementation envelope may reduce this set. Changes to POC files are forbidden.

## Non-Goals
- No POC repair, record backfill, commit, push, deployment, or source edit.
- No `V3-OP-003` promotion or conditional promotion.
- No mission-record schema or validator change.
- No runtime orchestration, required gate, telemetry enforcement, routing, scheduler, background worker, external write, real-data work, or V2 removal.
- No manufactured duration, failure, negative case, or evidence.
- No rewrite of historical Factory or POC adjudication records.

## Verification
- Parse Mission 026 JSON evidence.
- Verify commit range and changed paths.
- Verify screenshot hashes and visually inspect final desktop/mobile governance screenshots.
- Rerun commit-pinned Mission 026 tests, QA, and verifier in `/tmp` without modifying the source POC.
- Run Factory knowledge lint, V3 advisory lint, operational-readiness evals, mission-record lint, pack/stage lint, and `git diff --check`.
- Manual same-paragraph non-promotion review.

## Go / No-Go Rule
Proceed only after I2 PASS and explicit post-pack human Go. Halt if commit-pinned POC evidence is unavailable, replay requires modifying the source POC or adding dependencies, claims cannot be separated from unsupported inference, or any output would imply promotion from partial evidence.
