# Verification Plan - Mission Re-entry Proof Pack

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F verification plan.

| ID | Tier | Constraint | Check | Expected |
| --- | --- | --- | --- | --- |
| V3-001 | V3 | R-003/R-005 | Save current aggregate mission-control report and existing valid fixture output before edits | Baseline captured and current expected PASS |
| V3-002 | V3 | R-003/R-005 | After edits, filter five new fixture paths from aggregate report and compare with baseline | Exact equality |
| V2-003 | V2 | R-001 | Rich clean case | `continue`, current matching state, pass, action and basis; no finding |
| V2-004 | V2 | R-001 | Stale-state contradiction fixture | `V3-MC151` only |
| V2-005 | V2 | R-001 | Changed-authority contradiction fixture | `V3-MC152` only |
| V2-006 | V2 | R-002 | Failed-verification/no-recovery contradiction fixture | `V3-MC153` only |
| V2-007 | V2 | AC2 | Clean case missing action fixture | `V3-MC150` only |
| V2-008 | V2 | R-002 | Rich valid recovery case | `verify` only, explicit basis/action; no finding |
| V2-009 | V2 | shape | Temporary malformed container/common case | `V3-MC148` / `V3-MC149` deterministically |
| V3-010 | V3 | R-003 | Existing valid fixture direct lint | Exact baseline PASS before/after; absence no-op |
| V1-011 | V1 | R-004 | Static review of `fresh_session` and boundary claims | Scenario input only; no live-proof claim |
| V1-012 | V1 | R-006 | Per-invalid finding-set assertion | Exactly one intended ID per file |
| V1-013 | V1 | R-007 | Exact changed-product-path comparison | At most 18, no unauthorized path |
| V1-014 | V1 | R-007/R-008 | Diff/dependency/runtime/gate/routing search and Python compile | No forbidden implementation; compile PASS |
| V3-015 | V3 | regression | Mission-record, telemetry, loop-contract, advisory docs, readiness, knowledge, context, stage, pack checks | PASS/no new blocking effect |
| V0-016 | V0 | R-009/R-010 | Closeout review | One-sample friction bounded; visual evidence omitted as irrelevant |

## Baseline And Expected-Output Policy
Do not refresh `expected/all.json` until the unchanged existing valid fixture passes and the old-subset comparison succeeds. Aggregate differences may contain only the five new paths and MC150-MC153 findings.

## Failure Policy
Halt on historical mismatch, optional-list completeness finding, invalid fixture with multiple IDs, recovery result broader than `verify`, unauthorized path, dependency, runtime/gate/promotion implication, or claim that fixture inputs prove a real fresh session.
