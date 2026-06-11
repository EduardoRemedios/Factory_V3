# Factory V3 Duration Ladder Plan

## Version
v0.4

## Change Log
- v0.4 (2026-06-11): Added friction-measurement counters for rung 2 onward (advisory observations, never targets) and named the rung-2 structured-waypoint-table trial, from the backlog research spike.
- v0.3 (2026-06-10): Added the naming-and-sizing rule per sponsor decision `HDI-TT-002`: hour-based rung names stay as the human-readable headline; measured pass criteria are budget-and-waypoint classes.
- v0.2 (2026-06-10): Recorded rung 1 as passed for mechanics (mission `LADDER_RUNG1_20260610`, sponsor adjudication `HDI-TT-001`); the duration-stress burden shifts explicitly to rung 2.
- v0.1 (2026-06-10): Initial three-rung duration ladder (roughly 1 hour, 2 hours, 4 hours) supplying the trial evidence named in `V3_OP_003_DECISION_PACK.md`.

## Status
Research-only and non-enforcing plan. No rung is approved by this document; each rung requires its own mission envelope and explicit sponsor Go before execution, and each runs under existing approved authority (`V3-OP-001` eligibility per waypoint) until `V3-OP-003` is itself promoted.

This document does not approve live transport use (see `INTERRUPT_TRANSPORT_TRIAL_PLAN.md` for that gate), unattended operation, scheduled wakes, credential use, real data, deployment scope, concurrency, required gates, governance routing, or runtime-control power.

## Purpose
No local mission has run at multi-hour scale. The ladder converts "can V3 govern a 4-hour mission" from a claim into three increasingly demanding, separately approved trials, each judged against the fixed criteria in `V3_OP_003_DECISION_PACK.md`. The expensive failure modes (confident drift, budget blowout, unanswered interrupts, context exhaustion) are cheaper to meet for the first time at one hour than at four.

## Naming And Sizing Rule (per `HDI-TT-002`, 2026-06-10)
Hour-based rung names remain the human-readable headline only. Each rung's mission envelope must state its measured pass criteria as budget-and-waypoint classes: tool-call budget, waypoint count, and command-sourced elapsed time. Wall-clock compression below the headline hours is judged against those measured criteria, not the headline (and for rung 2 onward, genuine duration is itself a named criterion per `HDI-TT-001`).

## Common Requirements (All Rungs)
- Attended start: sponsor Go per mission; sponsor reachable for Tier 3 decisions.
- Waypoint structure, checkpoints, authored mission state, and budget discipline per `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md` and `ADAPTIVE_MISSION_CONTROL.md`.
- All six mission-health signals recorded at every checkpoint per `MISSION_HEALTH_VOCABULARY.md`, with citations; per-checkpoint recording cost noted so the signal set can be validated or shrunk.
- Model identity recorded at every checkpoint per `MUTABLE_HARNESS_STATE.md`; any skill use follows `SKILL_PROVENANCE_POLICY.md`.
- Telemetry at checkpoint level, not per-event level: the Phase 3 review found per-event overhead disproportionate for routine work, and at duration that disproportion compounds. Checkpoint-level telemetry is itself trial evidence for the telemetry-mode question.
- Closeout mission record per `MISSION_RECORD_DESIGN_V0.md`, with budget actuals versus plan from command-sourced timestamps and tool-call counts.

## Friction Measurement (Rung 2 Onward)
Governance that measures missions must also measure itself. From rung 2 onward, each rung records three counters, all derivable from the budget discipline already required:

1. Governance-overhead ratio at closeout: tool calls spent on governance artifacts (envelope authoring, checkpoint writes, mission-record authoring, advisory-suite runs) versus tool calls spent on objective work.
2. Per-artifact authoring cost: the per-checkpoint recording-cost note already required above, extended to envelope authoring and closeout-record authoring.
3. Go-to-first-edit count: tool calls from sponsor Go to the first objective edit, measuring envelope ceremony directly.

These counters are advisory observations, never targets or gates: setting a target ratio would invite under-recording, which is the failure the counters exist to detect. The counters also supply the affordability evidence for the `MISSION_ECONOMICS_VOCABULARY.md` lane decision.

Rung 2 additionally trials the structured waypoint table per the `mission_waypoint` candidate shape in `SHADOW_SCHEMA_CANDIDATES.md`: the rung-2 envelope states its waypoints as a table with the candidate's essential fields and provisional type labels, so the ladder produces evidence on whether structured waypoints earn their cost. This trials a documentation shape only; it adds no required fields, validators, or gates.

## Rung 1 — Roughly One Hour, This Repository

Status: PASSED for mechanics (2026-06-10). Mission `LADDER_RUNG1_20260610` (evidence under `ladder/rung1/`, closeout `mission_records/MR_20260610_019_ladder_rung1_state_doc_consistency.json`) exercised all rung-1 mechanics cleanly but compressed to ~7 minutes wall clock; sponsor adjudication `HDI-TT-001` passed the rung as mechanics evidence and assigned the duration-stress burden to rung 2, whose pass criteria must include genuine duration.
- Mission type: docs-and-fixtures work in `Factory_V3` decomposed into 3-5 waypoints (for example, a multi-document consistency pass with verification per document group).
- New thing being tested: waypoint mechanics, checkpoint cadence, mission-state upkeep, and health-signal recording at a scale where failure is cheap.
- Interrupts: simulated (file/thread-based) per the existing phased path; no live transport needed.
- Rung passes when: all waypoints closed with per-waypoint verification, checkpoint series complete with grounded health signals, budget actuals within plan, no scope drift findings.

## Rung 2 — Roughly Two Hours, POC Repository
- Mission type: bounded POC feature or test-expansion work with 5-8 waypoints, in the standalone POC repo where halt/recovery/reentry evidence already lives.
- New things being tested: duration doubling; one seeded Tier 3 interrupt over the live transport (requires the `INTERRUPT_TRANSPORT_TRIAL_PLAN.md` trial approved and passed first); reentry after a deliberate mid-mission pause.
- Rung passes when: rung 1 criteria hold at duration, the live interrupt round-trip produced a complete record, and pause/reentry worked from authored artifacts alone. Per `HDI-TT-001`, this rung now carries the duration-stress burden explicitly: a run that compresses far below the duration band does not pass this rung regardless of mechanics.

## Rung 3 — Roughly Four Hours, POC Repository
- Mission type: a real multi-waypoint build mission whose contract is drafted with the mission-formation skill and red-teamed with the challenge skill (both non-executing) before sponsor Go — this is the `V3-ANCHOR-005` live non-executing trial, folded in.
- New things being tested: full target duration inside the roughly 5-hour plan window; natural Tier 3 interrupts (not seeded); budget discipline near the stop threshold; context management across a long session.
- Hoped-for side evidence: at least one natural (non-seeded) halt, fallback, or clarification event at duration — decision-pack evidence item 4 and the long-open Phase 3 negative-case gap. If none occurs naturally, the gap stays honestly open; do not seed and relabel.
- Rung passes when: rung 2 criteria hold at full duration and the closeout shows continuation decisions traceable to checkpoints and health signals rather than chat memory.

## Failure Handling
A failed rung is evidence, not embarrassment: record it, classify findings, file friction notes, and rerun the rung after fixes. Two consecutive failures of the same rung route the lane back to design review before another attempt. Failed rungs do not unlock the next rung.

## Ladder Output
When all three rungs are complete, assemble the evidence into `V3_OP_003_DECISION_PACK.md` (items 1-4), run the false-positive/false-negative review (item 5), and present the pack to the sponsor for the promotion decision against the pre-written criteria.

## Named Follow-ups (Not Approved Here)
- Rung 1 mission envelope and sponsor Go.
- Interrupt-transport trial approval (prerequisite for rung 2).
- Per-rung harness capability profile observations.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
