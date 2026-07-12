# Intent - Mission 026 Claim-To-Proof And FP/FN Adjudication

## Version
v0.3

## Change Log
- v0.3 (2026-07-12): Intent unlock restored up to nine active pointer/status files from the user-approved raw-brief candidate set after direct next-gate inventory showed seven would leave stale canon.
- v0.2 (2026-07-12): Bound Red Team replay-provenance, verifier-independence, absence-claim, screenshot, scope, record-integrity, endurance, and FP/FN controls.
- v0.1 (2026-07-12): Initial Stage A intent.

## Purpose
Replace narrative confidence about POC Mission 026 with a source-backed claim ledger and an explicit non-promotion adjudication.

## Goal
Produce two durable audit artifacts that distinguish proved behavior, weak/self-attested claims, missing evidence, and contradictions; replay key verification at commit `404a32a`; assess false positives and false negatives under the corrected endurance model; and update only the minimum active Factory V3 pointers needed to record `NO PROMOTION YET`.

## Source Requirements
- R1 [SOURCE: user approval, 2026-07-12] Proceed with the passive Mission 026 claim-to-proof audit and explicit FP/FN adjudication.
- R2 [SOURCE: `docs/Factory/v3/V3_OP_003_DECISION_PACK.md` v0.9] Promotion requires evidence of stable governance and quality near the claimed endurance envelope, natural negative-case review, FP/FN review, and explicit human release approval.
- R3 [SOURCE: POC commit `404a32a`] Mission 026 closeout, record, audit summary, checkpoints, browser notes, state, tests, QA, verifier, source diff, and screenshots are the evidence under audit.
- R4 [SOURCE: `docs/Factory/v3/DURATION_LADDER_PLAN.md` v0.11] Mission result and endurance coverage are separate; early correct completion is PASS, not duration failure.
- R5 [SOURCE: `AGENTS.md`] Preserve V3 advisory-only semantics and do not introduce runtime authority, required gates, routing, telemetry enforcement, profile promotion, or V2 removal.

## Principles
- Commit-pinned source outranks mutable working-tree state and narrative summaries.
- Replayed evidence outranks self-attestation.
- Absence claims require stronger proof than presence claims.
- Builder-generated QA and verifier scripts are useful but not automatically independent.
- Preserve historical records; record gaps in Factory V3 rather than repairing the POC.
- Keep `NO PROMOTION YET` in the same paragraph as every positive operational finding.

## Roles
- Root Planner: prepare and validate this execution pack.
- Evidence Auditor: construct the claim-to-proof ledger.
- Replay Verifier: rerun commit-pinned tests, QA, verifier, JSON, hashes, and screenshot checks independently.
- FP/FN Reviewer: assess over-blocking, under-detection, self-attestation, and endurance misclassification.
- Purple Reviewer: lock scope and adjudicate pack quality.
- Human Sponsor: give post-pack Go and retain all promotion authority.

## Acceptance Criteria
- AC1: Every material Mission 026 outcome, verification, browser, boundary, and design-transfer claim has a stable ID and status `PROVED`, `WEAK`, `MISSING`, or `CONTRADICTED`.
- AC2: Every `PROVED` claim cites direct commit path plus replay command, source function/test, screenshot/hash, or independent artifact evidence.
- AC3: Builder assertions, generated audit summary, QA script, verifier script, and independent replay are identified separately.
- AC4: Exact-commit focused tests, full suite, Mission 026 QA, Mission 026 verifier, JSON parse, changed-path review, and screenshot hashes are rerun where practical without changing the source POC.
- AC5: Desktop and mobile governance screenshots are independently inspected for the claimed surfaces and obvious overflow/blank-output failures.
- AC6: Stale or contradictory evidence is explicit, including `commit_after: pending_final_closeout_commit` in the final mission record.
- AC7: Negative boundary claims are narrowed to what the commit diff, tests, config, and replay can prove; unsupported global absence or harness-use claims remain `WEAK`.
- AC8: Mission 026 is classified as mission PASS and design-transfer evidence without being treated as upper-envelope endurance proof.
- AC9: FP/FN review names at least false-confidence risks, over-strict historical duration classification, evidence independence gaps, and any missed record-integrity issue.
- AC10: Adjudication remains explicitly `NO PROMOTION YET` and maps all five decision-pack evidence items.
- AC11: No POC file or historical Factory evidence is changed.
- AC12: Active canon points to the new audit/adjudication and names the next evidence-driven step without authorizing schema/runtime work.
- AC13: Original Mission 026 summaries and 2026-07-12 replay results are never conflated; replay proves reproducibility only.
- AC14: FP means an existing governance/eval signal was stronger than its evidence warranted; FN means an existing artifact missed or underweighted a material gap.

## Authorized Scope
The two new audit artifacts, at most nine directly affected active pointer/status files from `raw_brief.md`, this run root, and temporary `/tmp` replay artifacts. The POC repository is read-only source evidence.

## Non-Goals
- No POC repair or record backfill.
- No profile promotion, schema change, validator change, runtime orchestration, required gate, telemetry enforcement, routing, scheduler, deployment, real-data work, external write, commit, push, or V2 removal.
- No claim that replay at `404a32a` proves later POC state or four-hour endurance.

## Open Questions
### BLOCKING
- None for planning. Any exact-commit replay failure that cannot be explained without source mutation becomes blocking during execution.

### NON-BLOCKING
- Whether the stale `commit_after` should be repaired in the POC is a later separately authorized decision.
- Optional mission-record fields remain deferred until this audit is complete.

## Go Or No-Go Rule
Go only if the envelope keeps the POC read-only, requires conservative claim grading, makes replay and screenshot inspection explicit, preserves `NO PROMOTION YET`, and passes I2 plus post-pack human Go. Otherwise no-go.
