# Intent Red Team - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage B challenge using `factory-challenge-mission`.

## Verdict
`CONDITIONAL PASS`

## High Findings
1. Old-output stability is ambiguous if `all.json` changes because new fixtures are added.
   - Repair: compare baseline records/findings as a filtered subset; expected aggregate may grow only for named new files.
2. Placeholder commit detection could flag historical `not_recorded` values.
   - Repair: MR085 applies only to explicit pending/placeholder strings in `completed_with_v3`; `not_recorded` remains valid and limited.
3. Visual fail should not make a record structurally invalid.
   - Repair: visual `fail`/`limited` are valid evidence; MR083 checks only shape/vocabulary.
4. Boundary claim validation could turn evidence quality into required completeness.
   - Repair: validate only supplied claims; stronger requirements apply only when supplied status is `PROVED`.
5. Pointer updates could exceed core implementation value.
   - Repair: seven exact active surfaces only; no unrelated editorial churn.

## Critical Findings
- None.

## Authority Gaps
- Implementation authority remains pending post-pack Go.

## Verification Gaps
- Baseline subset comparison must be explicit before expected-output regeneration.

## Recommended Repair
Bind aggregate-output growth to new fixture paths while preserving old per-path findings and statuses.

## Execution Readiness
Continue planning after synthesis binds all five High findings.
