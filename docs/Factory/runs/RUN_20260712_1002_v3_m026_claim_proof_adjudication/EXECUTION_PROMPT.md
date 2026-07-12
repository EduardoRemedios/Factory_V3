# Execution Prompt - Mission 026 Claim-To-Proof Adjudication

## Authorization
- Human Go received: 2026-07-12.
- Execution mode: `EXECUTION_ENABLED`.
- Approved pack: `docs/Factory/runs/RUN_20260712_1002_v3_m026_claim_proof_adjudication/pack/`.
- Closeout workflow: `factory-execution-closeout`.

## Objective
Audit Mission 026 at POC commit `404a32a` against baseline `8f25437`, replay its deterministic evidence in an isolated detached clone, inspect the pinned browser artifacts, and publish a claim-to-proof ledger plus false-positive/false-negative adjudication.

## Required Outcome
- Grade material claims as `PROVED`, `WEAK`, `MISSING`, or `CONTRADICTED` with explicit evidence and limits.
- Keep original-run summaries distinct from the 2026-07-12 replay.
- Classify the final record's stale `commit_after` value.
- Distinguish deterministic same-worker checks from independent verification.
- Separate Mission 026 completion from upper-envelope endurance coverage.
- Map all five `V3-OP-003` decision-pack evidence items.
- Retain the explicit decision `NO PROMOTION YET`.

## Execution Boundaries
- Treat `/Users/eduardodosremedios/V3_POC_App_Creation` as read-only.
- Run all POC Python, QA, verifier, JSON, and screenshot-hash commands in `/tmp/factory_v3_m026_audit_20260712` after detached checkout at `404a32a`.
- Do not install dependencies, repair the POC, alter schemas or validators, add runtime authority, promote a V3 profile, commit, or push.
- Touch no more than the 11 authorized Factory product files in the approved envelope. Run-root closeout evidence is excluded from that count.
- Halt on source mutation, commit mismatch, unavailable visual evidence, unauthorized path, failed required gate, or promotion implication.

## Sequence
1. Record source POC status and verify both pinned commits.
2. Create the isolated clone and confirm detached `HEAD`.
3. Inventory `8f25437..404a32a`, inspect material source/evidence, and replay focused/full tests plus Mission 024/026 checks.
4. Parse records, verify screenshot hashes, and visually inspect all four final screenshots.
5. Produce the claim-to-proof audit and FP/FN adjudication.
6. Reconcile only stale active pointers, retaining same-context non-promotion language.
7. Run all Factory verification, confirm source-status equality, and create the implementation closeout.

## Completion Decision
Use the `factory-execution-closeout` decision vocabulary. Mark `READY` only if the implementation stays within the approved pack, every required gate passes, the source POC is unchanged, and residual evidence limits remain explicit.
