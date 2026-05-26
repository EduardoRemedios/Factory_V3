# Intent Red Team

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Red-team review for Phase 3 implementation approval intent.

## Iteration
Iteration: 1 of max 2

## Findings

| Severity | Finding | Why It Matters | Fix Recommendation |
|---|---|---|---|
| High | Approval language may be mistaken for V3 promotion. | The approved scope is only the first advisory implementation step. | State that V3 remains optional and non-enforcing. |
| High | Validator implementation could drift into required-gate behavior. | Required gates need later approval. | Name the script standalone and advisory-only. |
| High | Fixture payloads could include sensitive data. | Phase 3 data minimization forbids secrets and private cognition state. | Require excluded-data marker fixtures without storing actual secrets. |
| Medium | Implementation could overbuild a generic schema framework. | SIMPLE-CODE-GATE calls for the smallest useful replay check. | Limit implementation to local JSONL parsing and deterministic checks. |

## Agent Failure Modes
- Adding telemetry collection for real missions before fixture evidence exists.
- Wiring the validator into CI or `factoryctl`.
- Treating invalid fixture findings as blocking repository gates.
- Adding broad abstractions for future harnesses before real need.

## Verification Holes
- This pack cannot validate code behavior because implementation is deferred.
- The future implementation must run deterministic `--expect` checks before pilot use.

## Exit Criteria
PASS
