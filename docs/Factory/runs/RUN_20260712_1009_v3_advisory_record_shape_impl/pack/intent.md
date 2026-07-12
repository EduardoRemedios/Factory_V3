# Intent - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Initial Stage A intent.

## Goal
Implement the accepted narrow advisory record shape through docs/template, fixture-first coverage, minimal validator checks, and current canon reconciliation within an exact 18-file product cap.

## Source Requirements
- R1 [SOURCE: user decision, 2026-07-12] `ADOPT_NARROW_SET` accepted; prepare implementation pack.
- R2 [SOURCE: planning run PASS] Four optional structures adopted, commit semantics revised, endurance fields deferred.
- R3 [SOURCE: Mission 026 audit] Stale commit, same-worker verification, visual clipping, replay provenance, and bounded absence claims are observed gaps.
- R4 [SOURCE: current mission-record design] Record remains optional, advisory, non-enforcing, and subordinate to authored evidence.
- R5 [SOURCE: `AGENTS.md`] No runtime/gate/promotion authority; deterministic outputs stable.

## Acceptance Criteria
- AC1: template adds only the four optional structures and no endurance field.
- AC2: design documents allowed values, source-of-truth limits, privacy, and omission behavior.
- AC3: absent optional structures produce no new finding.
- AC4: original and replay observations coexist; `supersedes_original` must be false.
- AC5: same actor cannot report `independent`; deterministic separation is explicit.
- AC6: visual hash and visual verdict are separately represented; hash-match/visual-fail is valid evidence.
- AC7: `PROVED` boundary claims require bounded proof scope, non-empty evidence refs, and a non-empty limit.
- AC8: completed records with explicit placeholder `commit_after` receive an advisory finding; `same_commit`, literal hash, and `not_recorded` remain handled as documented.
- AC9: five new fixtures cover one rich valid record and four invalid contradictions.
- AC10: deterministic `all.json` and `invalid.json` match; old fixture semantics are unchanged.
- AC11: validator remains standalone with `blocking_effect: none` and no required-gate wiring.
- AC12: exactly the 18 authorized product files or fewer are touched.
- AC13: no historical record/POC repair, migration, generic schema framework, dependency, or runtime work.
- AC14: active canon records completion while retaining `NO PROMOTION YET` and endurance deferral.

## Validator Policy
Proposed advisory IDs:
- `V3-MR081`: invalid verification observation/supersession.
- `V3-MR082`: verifier provenance contradiction.
- `V3-MR083`: malformed visual evidence.
- `V3-MR084`: boundary claim lacks proof scope/evidence/limit or has invalid status.
- `V3-MR085`: completed record carries explicit pending/placeholder commit.

Checks apply only to Factory V3 shadow records. POC schema routes are unchanged.

## Authorized Scope
Exactly the 18 product paths listed in `raw_brief.md`, plus this run root and generated temporary verification output.

## Non-Goals
No implementation before post-I2 Go. No other product path, historical evidence edit, runtime behavior, telemetry, enforcement, routing, CI, profile promotion, or V2 removal.

## Open Issues
### BLOCKING
- None for planning.

### NON-BLOCKING
- Exact finding messages may be mechanically refined while IDs and semantics remain fixed.

## Go Rule
Go only after I2 PASS and explicit human Go. Halt on any old-record regression, scope expansion, required-field behavior, or authority implication.
