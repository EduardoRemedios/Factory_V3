# Intent Red Team - Mission Re-entry Proof Pack

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage B challenge.

Iteration: 1 of max 2

## Findings

### RT-001 - High - Recovery authority could become general continuation authority
Why it matters: a case that changes failed verification directly to `continue` would teach the wrong governance rule and weaken the next-action boundary.

Fix: the authorized recovery case must use `gate_result: verify`, identify exactly one bounded action, and retain `failed_verification` as the prior observed status rather than claiming mission success.

### RT-002 - High - Policy and event evidence could be conflated
Why it matters: adding observed state directly to `reentry_protocol` would mix reusable policy with one event and create competing sources of truth.

Fix: keep policy unchanged and place observed examples only under optional `fixture_scenarios.reentry_cases`.

### RT-003 - High - Invalid fixtures could generate multiple unrelated findings
Why it matters: copying the current unsafe approval fixture would obscure whether re-entry semantics are actually tested.

Fix: derive invalid fixtures from the new rich valid fixture and mutate exactly one semantic condition per file; compare finding IDs per file.

### RT-004 - Medium - Planning could be mislabeled as first shadow-use evidence
Why it matters: planning examples do not measure actual authoring friction during a mission closeout.

Fix: state that only a post-Go implementation closeout using the optional mission-record fields counts as the first shadow-use observation.

### RT-005 - Medium - `fresh_session` may be asserted without evidence
Why it matters: a fixture cannot prove a real fresh session or cross-harness handoff.

Fix: treat `fresh_session` as scenario input, not operational proof; bound claims explicitly and preserve the unexecuted fresh-worker trial.

### RT-006 - Medium - Existing contracts may become invalid
Why it matters: requiring `reentry_cases` would break backward compatibility and convert an advisory example into a required schema addition.

Fix: absence remains a no-op; validate only when the optional list is supplied.

### RT-007 - Medium - Canon churn may exceed implementation value
Why it matters: eight canon files can duplicate implementation details and create staleness.

Fix: each canon update should be pointer/status-only; detailed semantics live in the mission-control and safe-hold documents.

## Agent Failure Modes
- Generalizing from five scenarios into a workflow engine.
- Treating `authority_matches_checkpoint` as proof rather than a declared scenario fact.
- Allowing stale-state `verify` actions that mutate the repository before safe-hold.
- Rejecting honest safe-hold outcomes as malformed contracts.
- Updating the live trial plan to imply execution or cross-harness evidence.

## Verification Holes
- Need old-subset report comparison before expected-output refresh.
- Need explicit absence/no-op test for `reentry_cases`.
- Need static assertion that no runtime modules, dependencies, or required-gate scripts change.
- Need proof that the authorized recovery case cannot use `continue` or `close`.

## Recommendation
Proceed after synthesis adopts RT-001 through RT-007 and binds four isolated finding IDs plus an absence/no-op regression check.
