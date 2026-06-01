# Intent Red Team: Phase 4 Dynamic/Parallel Evidence-export Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-01): Initial Stage B red-team review.

## Iteration
Iteration: 1 of max 2

## Findings
| ID | Severity | Finding | Why It Matters | Fix Recommendation | Status |
| --- | --- | --- | --- | --- | --- |
| RT-001 | High | Dynamic/parallel wording could be mistaken as execution approval. | The research plan and opportunity register explicitly prohibit execution without separate approval. | State that this run is planning-only and future execution requires exact harness, files, commands, telemetry decision, and stop conditions. | Addressed in intent v0.2. |
| RT-002 | High | Evidence-export capture could accidentally collect private cognition or raw transcripts. | Dynamic workflows may expose planner/subagent internals that are not Factory evidence and should not be stored. | Forbid chain-of-thought, vendor-private cognition state, raw transcripts, secrets, source dumps, and broad workflow internals. | Addressed in intent v0.2. |
| RT-003 | Medium | Codex preference could overstate local capability. | Existing Codex profile is official-docs-based `insufficient_evidence`, not local execution evidence. | Prefer Codex only if locally available and explicitly approved; otherwise record unavailable capability or choose a separately approved harness. | Addressed in intent v0.2. |
| RT-004 | Medium | Optional telemetry could drift into required-gate semantics. | Phase 3 allows optional advisory telemetry only under explicit conditions. | Keep telemetry recommended but not approved; require summary-only, non-blocking, non-gate capture if later approved. | Addressed in intent v0.2. |

## Agent Failure Modes
- Treating external source signals as local Factory evidence.
- Running a dynamic/parallel workflow from the research plan alone.
- Capturing raw workflow internals instead of reviewable summaries.
- Updating routing or threshold canons from one future evidence-export probe.

## Verification Holes
- This planning run cannot verify dynamic/parallel harness behavior because no candidate is executed.
- Future verification must classify missing evidence as an observation, not as a successful capability signal.

## Exit Criteria Status
- PASS
