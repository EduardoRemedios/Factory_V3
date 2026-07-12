# Intent - Advisory Mission-Record Shape Decision

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Initial Stage A intent.

## Purpose
Decide the smallest backward-compatible advisory mission-record additions justified by the Mission 026 audit, without implementing or promoting them.

## Goal
Produce a planning pack that recommends `ADOPT`, `REVISE`, or `DEFER` for each of six candidate field families and defines a later fixture-first implementation envelope only if evidence supports it.

## Source Requirements
- R1 [SOURCE: user approval, 2026-07-12] Prepare the recommended planning-only record-shape slice.
- R2 [SOURCE: `MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`] Record-finalization, replay provenance, verifier independence, per-artifact visual review, bounded absence claims, and endurance coverage are material evidence gaps.
- R3 [SOURCE: `MISSION_026_FP_FN_ADJUDICATION_20260712.md`] `V3-OP-003` remains `NO PROMOTION YET`; historical POC evidence must not be repaired in this slice.
- R4 [SOURCE: `MISSION_RECORD_DESIGN_V0.md`] The mission record is an optional replay aid, not a second mission-state source, proof ledger, telemetry system, or runtime kernel.
- R5 [SOURCE: representative mission-record fixtures] Existing completed, halted, stale-reentry, blocked, and pre-envelope records use v0.1 and must remain valid.
- R6 [SOURCE: `AGENTS.md`] No schema/validator/fixture or runtime change without separate approval; advisory-only semantics remain.

## Design Tests
Each candidate must pass all of these:
1. Evidence need: closes an observed audit gap, not speculative future variation.
2. Non-duplication: does not replace authored envelopes, checkpoints, state, verification logs, or closeouts.
3. Backward compatibility: absence is valid and existing records need no rewrite.
4. Bounded semantics: values cannot imply stronger proof or authority than evidence supports.
5. Replay value: improves later review enough to justify authoring cost.
6. Ownership: belongs to Factory governance evidence, not worker tactical state.

## Candidate Decisions To Reach
- Commit finalization: decide whether better semantics/checks on existing `mission.commit_after` are enough or a new field is justified.
- Original/replay provenance: decide the smallest representation that prevents later replay from overwriting original-run claims.
- Verifier provenance: distinguish actor/session provenance from deterministic verifier separation.
- Visual evidence: separate file/hash identity from human or tool visual verdict per artifact.
- Boundary/absence claims: scope each negative claim to change range, static repository, runtime trace, self-attestation, or unknown proof.
- Mission/endurance: keep mission result separate from exposure and coverage without contaminating the base V3-OP-001 record with premature profile-specific fields.

## Acceptance Criteria
- AC1: all six families receive `ADOPT`, `REVISE`, or `DEFER` with source evidence.
- AC2: recommended additions are optional and preserve all existing schema routes and fixtures.
- AC3: no recommendation creates a second authored mission ledger or runtime/proof authority.
- AC4: commit handling covers literal hash, `same_commit`, `not_recorded`, placeholder, and unavailable commit cases.
- AC5: original and replay results are separately attributable.
- AC6: verifier independence is an explicit status, not inferred from a script name.
- AC7: each visual artifact can carry separate hash and visual findings.
- AC8: absence claims name proof scope and evidence limits.
- AC9: mission outcome and endurance evidence remain conceptually separate; profile-specific fields are not added without sufficient evidence.
- AC10: later implementation scope, likely files, deterministic checks, compatibility fixtures, and stop conditions are explicit but not authorized.
- AC11: recommendation is one of `ADOPT_NARROW_SET`, `REVISE_AND_REVIEW`, or `DEFER_ALL`.
- AC12: pack retains `NO PROMOTION YET`, V2 fallback, advisory-only behavior, and no runtime/required-gate language.

## Authorized Scope
- This run root and its planning pack only.
- Read-only inspection of current V3 docs, templates, validator, deterministic fixtures, and Mission 026 audit artifacts.

## Non-Goals
- No product/canon/template/validator/fixture/historical-record edit.
- No JSON Schema, migration, POC repair, telemetry, proof ledger, runtime authority, routing, CI, required gate, scheduler, profile promotion, or V2 removal.

## Initial Recommendation Hypothesis
`ADOPT_NARROW_SET`: preserve `mission.commit_after` and improve its later advisory consistency semantics; add only optional provenance structures with demonstrated replay value; defer profile-specific endurance fields until natural sustained evidence justifies a stable shape.

## Open Questions
### BLOCKING
- None for planning.

### NON-BLOCKING
- Exact field names and nesting are subject to Red/Blue challenge.
- Whether a later implementation updates mission-record lint or only docs/template must be decided in the later envelope.

## Go / No-Go
Proceed through I2 only if the pack remains planning-only, additive, backward-compatible, evidence-derived, and explicit about deferrals. Otherwise no-go.
