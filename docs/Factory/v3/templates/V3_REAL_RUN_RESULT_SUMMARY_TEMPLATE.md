# V3 Real-run Result Summary Template

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Phase 4 real-run result summary template.

## Status
Research template only and non-enforcing.

This template does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Use only after a specific `V3-OP-001` evidence mission has separate human approval.

## Summary Metadata
- Result ID:
- Created:
- Reviewer:
- Repository:
- Branch or revision:
- Mission or run ID:
- Mission profile:
- Harness:
- Model when known:
- Evidence date:
- Optional telemetry decision: `NO_TELEMETRY` or `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`

## Candidate Eligibility
- Objective:
- Authorized files or modules:
- Allowed command families:
- Verification commands:
- Dependency policy:
- SIMPLE-CODE-GATE applicability:
- V2 fallback triggers:
- Human approval reference:

## Execution Summary
- Start state:
- Work performed:
- Files touched:
- Commands attempted:
- Checks skipped with reason:
- Verification results:
- Closeout status:

## Halt, Fallback, Clarification, And Reentry
- Halt occurred:
- Fallback occurred:
- Clarification required:
- Interruption occurred:
- Reentry source artifacts reread:
- Stale or conflicting context found:
- Human decision after halt, fallback, clarification, or failed verification:

## Evidence Links
- Mission envelope or authority evidence:
- Command evidence:
- Verification evidence:
- Diff or file-change evidence:
- Closeout evidence:
- Advisory eval output:
- Harness capability profile:
- Optional advisory telemetry evidence:

## Evidence Gaps
- Missing command evidence:
- Missing verification evidence:
- Missing human decision evidence:
- Missing halt, fallback, or clarification-heavy natural case evidence:
- Other gaps:

## Advisory Finding Classification
| Finding ID | Finding Source | Expected | Observed | Human Adjudication | Rationale | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Allowed adjudication values:
- `true_positive`
- `false_positive`
- `true_negative`
- `false_negative`
- `needs_more_context`
- `deferred`

## Harness Capability Snapshot
- Capability profile path:
- Evidence band:
- Band rationale:
- Limitations:

Allowed evidence bands:
- `insufficient_evidence`
- `harness_profile_observed`
- `repeatable_low_risk_signal`
- `candidate_for_later_router_study`

These bands are advisory review labels only. They do not route work, reduce governance, promote V3, or change Factory V2 fallback.

## Data Minimization Review
Confirm this result summary does not include:
- chain-of-thought,
- raw command output dumps,
- source file contents,
- secrets,
- raw environment dumps,
- unrelated personal data,
- vendor-private cognition state,
- external proof artifacts outside the repository boundary.

## Reviewer Decision
- Decision:
- Rationale:
- Residual risk:
- Required follow-up:

Allowed decisions:
- `accepted_advisory_evidence`
- `needs_more_context`
- `defer_until_negative_case`
- `do_not_use_for_threshold_discussion`

## Notes
Keep notes evidence-linked and concise. This template is not authority for future missions.
