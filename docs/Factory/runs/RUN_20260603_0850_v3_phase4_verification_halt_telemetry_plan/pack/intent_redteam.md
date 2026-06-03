# Intent Red Team: Phase 4 Verification-halt Telemetry Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-03): Initial Stage B red-team review.

## Iteration
Iteration: 1 of max 2

## Findings
| ID | Severity | Finding | Why It Matters | Fix Recommendation | Status |
| --- | --- | --- | --- | --- | --- |
| RT-001 | High | Verification-halt wording could be mistaken as execution approval. | The research plan and opportunity register explicitly prohibit execution without separate approval. | State that this run is planning-only and future execution requires exact harness, files, commands, telemetry decision, and stop conditions. | Addressed in intent v0.2. |
| RT-002 | High | Optional telemetry could accidentally collect private cognition, raw transcripts, command dumps, or source dumps. | Phase 3 telemetry conditions allow only summary-only advisory evidence. | Forbid chain-of-thought, vendor-private cognition state, raw transcripts, secrets, source dumps, raw command-output dumps, and broad workflow internals. | Addressed in intent v0.2. |
| RT-003 | Medium | Prior clean non-event could be misread as evidence that the verification-halt gap is closed. | `P4-NEG-CAPTURE-CANDIDATE-002` passed verification and therefore did not exercise halt/fallback behavior. | State that the follow-up must record a clean non-event if verification passes again and must not seed failure. | Addressed in intent v0.2. |
| RT-004 | Medium | Optional telemetry could drift into required-gate semantics. | Phase 3 allows optional advisory telemetry only under explicit conditions. | Keep telemetry recommended but not approved; require summary-only, non-blocking, non-gate capture if later approved. | Addressed in intent v0.2. |

## Agent Failure Modes
- Treating external source signals as local Factory evidence.
- Running fixture or expected-output maintenance from the planning pack alone.
- Capturing raw workflow internals instead of reviewable summaries.
- Updating routing or threshold canons from one future verification probe.

## Verification Holes
- This planning run cannot verify verification-halt harness behavior because no candidate is executed.
- Future verification must classify missing evidence as an observation, not as a successful capability signal.

## Exit Criteria Status
- PASS
