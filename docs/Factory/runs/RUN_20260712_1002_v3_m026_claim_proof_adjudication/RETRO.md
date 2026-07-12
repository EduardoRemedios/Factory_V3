# Retrospective

## Result
The source-isolated replay and claim ledger exposed evidence defects that the original same-worker verifier missed without requiring POC mutation. The run completed at the exact 11-product-file envelope maximum and retained `NO PROMOTION YET`.

## What Worked
- Commit-pinned source plus a detached clone kept mutable POC state out of the audit.
- Hash checks and visual checks were treated as separate evidence, which exposed clipping hidden by a broad browser PASS.
- Separating mission outcome, record integrity, observed exposure, and endurance coverage prevented both overclaiming and retroactive mission failure.
- Fixed FP/FN definitions made same-actor verification and bounded absence claims reviewable.

## What To Improve
- Verification-plan V1-015 should have said “at most 9 active pointers and 11 total product files” to match the intent and envelope directly.
- Future packs should request explicit research-only wording in new V3 artifacts before advisory lint.
- Original-run command output should be preserved separately from replay output where practical.

## Follow-Up
The next separately approved gate should evaluate backward-compatible advisory fields for final-commit consistency, original/replay provenance, verifier independence, per-artifact visual evidence, bounded absence claims, and separate mission/endurance outcomes. Do not combine that proposal with runtime implementation or POC repair.
