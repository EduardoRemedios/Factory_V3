# Intent Red Team

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Red-team review for Phase 3 telemetry/replay planning intent.

## Iteration
Iteration: 1 of max 2

## Findings

| Severity | Finding | Why It Matters | Fix Recommendation |
|---|---|---|---|
| High | Telemetry language can sound like implementation approval. | Phase 2.5 only approved Phase 3 planning. | State repeatedly that this plan does not implement telemetry or approve required gates. |
| High | Event fields can over-collect sensitive data. | Replay needs operational facts, not private cognition or secrets. | Add explicit excluded-data and redaction rules. |
| Medium | Fixture shape can become too broad. | Broad schema work would violate SIMPLE-CODE-GATE. | Define only the first minimal fixture corpus for a later implementation pack. |
| Medium | Replay checks can imply enforcement. | Replay should remain advisory until a later gate approves enforcement. | Name replay checks as future advisory checks. |

## Agent Failure Modes
- Treating planned event names as current runtime artifacts.
- Adding validators while writing the plan.
- Expanding Phase 3 into governance routing or capability profiling.
- Recording full command output or chat transcript as telemetry.

## Verification Holes
- Planning docs cannot prove overhead; they can only define how overhead will be measured later.
- No real telemetry logs exist yet, by design.

## Exit Criteria
PASS
