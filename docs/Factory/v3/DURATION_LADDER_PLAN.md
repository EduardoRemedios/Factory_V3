# Factory V3 Endurance Evidence Ladder Plan

## Version
v0.11

## Change Log
- v0.11 (2026-07-12): Corrected the ladder model: the roughly four-hour headline is an endurance ceiling to support, not a minimum mission duration or workload target. Mission PASS is now separate from observed endurance coverage; no time, call, waypoint, test, file, or scope padding is allowed. Historical adjudications remain unchanged as evidence under their then-current criteria.
- v0.10 (2026-06-11): RUNG 2 PASSED — attempt 4 recorded per sponsor adjudication `HDI-RUNG2-008` (POC Mission 024: all eight criteria, 95.25 active minutes, ~548 calls, restored browser QA with real defect-fix loops). The validated findings: the browser workload was the missing duration component (`HDI-RUNG2-006` F2 hypothesis confirmed); vendor session limits are duration-relevant external state that the pause/reentry mechanism absorbs (new rung-3 planning input); governance overhead amortizes with scale (0.83:1). Rung 3 unlocked as the `HDI-RUNG2-007` hybrid: contract formation with the mission-formation and challenge skills (`V3-ANCHOR-005` trial), class parameters to be recalibrated from the four-point dataset at formation.
- v0.9 (2026-06-11): Applied sponsor decision `HDI-RUNG2-007` (design review round 2, `ladder/design_review/LADDER_DESIGN_REVIEW_ROUND2_HDI_RUNG2_007.md`): Option A-final adopted — rung-2 attempt 4 at ~27 build waypoints (~2x Mission 023) with browser tooling enabled and verified at pre-flight (Go-blocking check); coefficients recalibrated from Mission 023 actuals (~21 total calls per build waypoint, ~50% governance share, ~6.2 calls/min); forecast band ~700-1050 calls; floor 540, band 90-180 min, stop 1300 unchanged. The rung-2/rung-3 hybrid (mission-formation contract, `V3-ANCHOR-005` trial) is the named contingent follow-on either way. Falling-coefficient risk stated honestly.
- v0.8 (2026-06-11): Recorded rung-2 attempt 3 as FAILED on duration and budget floor per sponsor adjudication `HDI-RUNG2-006` (POC Mission 023; mechanics clean at 3.5x scope; honest 54m03s active, ~333 calls vs the 90-min/540-call floors). First calibration verdict on the v0.7 sizing rule: throughput calibrated (~6.2 calls/min across three runs); per-waypoint cost coefficient too high and falling as the codebase matures. Sponsor findings recorded: browser tooling unexposed in the session shortened the run (enablement directed for future runs; availability to be recorded at pre-flight as harness state); a further ~2x scope jump is the only remaining Option A variant. Third failure routes the lane to design review round 2 per the unchanged failure-handling rule.
- v0.7 (2026-06-11): Applied sponsor decision `HDI-RUNG2-005` adopting the ladder design review (`ladder/design_review/LADDER_DESIGN_REVIEW_20260611.md`), Option A: the duration band stays a pass criterion, guarded by a bottom-up measured sizing rule and a scope-sufficiency precondition; rung classes restated from the two measured calibration points (rung 2: floor 540 calls, ~12-20 waypoints, stop 1300; rung 3: floor 1100, ~20-30 waypoints, stop 2000); interrupt-record field set v2 (safe-hold trigger) specified for all future rung envelopes. Failure handling unchanged.
- v0.6 (2026-06-11): Recorded rung-2 attempt 2 as FAILED on duration per sponsor adjudication `HDI-RUNG2-004` (POC Mission 022; mechanics 8/8; honest 40m06s active vs the 90-180 min band; 160 calls vs 550-900 forecast). Two consecutive failures invoke the failure-handling route: the lane goes to the design review before any further attempt. The same record adopts the sponsor's safe-hold-trigger principle for interrupt timeouts: an answer is never "late"; the named timeout governs only the agent's wait posture; latency is neutral telemetry.
- v0.5 (2026-06-11): Recorded rung-2 attempt 1 as FAILED on duration per sponsor adjudication `HDI-RUNG2-002` (mechanics 7/8; honest compression to 24m11s); rerun path is an open sponsor decision (larger scope vs design review re-basing rung classes).
- v0.4 (2026-06-11): Added friction-measurement counters for rung 2 onward (advisory observations, never targets) and named the rung-2 structured-waypoint-table trial, from the backlog research spike.
- v0.3 (2026-06-10): Added the naming-and-sizing rule per sponsor decision `HDI-TT-002`: hour-based rung names stay as the human-readable headline; measured pass criteria are budget-and-waypoint classes.
- v0.2 (2026-06-10): Recorded rung 1 as passed for mechanics (mission `LADDER_RUNG1_20260610`, sponsor adjudication `HDI-TT-001`); the duration-stress burden shifts explicitly to rung 2.
- v0.1 (2026-06-10): Initial three-rung duration ladder (roughly 1 hour, 2 hours, 4 hours) supplying the trial evidence named in `V3_OP_003_DECISION_PACK.md`.

## Status
Research-only and non-enforcing plan. No rung is approved by this document; each rung requires its own mission envelope and explicit sponsor Go before execution, and each runs under existing approved authority (`V3-OP-001` eligibility per waypoint) until `V3-OP-003` is itself promoted.

This document does not approve live transport use (see `INTERRUPT_TRANSPORT_TRIAL_PLAN.md` for that gate), unattended operation, scheduled wakes, credential use, real data, deployment scope, concurrency, required gates, governance routing, or runtime-control power.

## Purpose
The ladder converts "can V3 govern a mission that naturally needs up to roughly four hours without drift or quality loss" from a claim into graduated evidence. It measures whether objective, authority, checkpoints, re-entry, verification, evidence, and output quality remain stable as actual exposure increases. It does not require any mission to consume a target duration.

## Mission Result Versus Endurance Coverage
Every run records two separate outcomes:

1. Mission result: `PASS`, `HALT`, `BLOCKED`, or another terminal state based on objective completion, authority, and verification evidence.
2. Endurance coverage: the observed elapsed exposure and whether continuity quality was demonstrated at that exposure.

A mission that completes correctly in two or three hours passes and stops. It must not add work, calls, waypoints, tests, files, scope, or waiting to approach four hours. The unobserved remainder of the endurance envelope remains `INSUFFICIENT_EVIDENCE`, not a mission failure.

## Naming And Sizing Rule
Hour-based rung names are orientation labels for observed exposure, not pass floors. Envelopes must size work from real deliverables and set budget stop thresholds as ceilings. Command-sourced elapsed time and tool-call counts remain useful measurements, but they cannot authorize continuation after completion or turn a shorter successful mission into failure.

## Bottom-Up Sizing And Exposure Classification
The 2026-06-11 design-review history remains valuable calibration evidence, but its workload floors are no longer active mission-pass criteria:

1. Size each mission from its objective and measurable deliverables, citing prior costs only as forecasts.
2. Treat time, call, and waypoint budgets as planning ranges and stop ceilings, never minimum consumption targets.
3. Classify endurance coverage from observed evidence after the mission: short exposure, sustained exposure, or upper-envelope exposure. Do not reverse-engineer scope to hit a class.
4. Promotion of an up-to-four-hour capability still requires credible quality-continuity evidence near the upper envelope. Until useful work naturally supplies it, the claim remains insufficiently evidenced.

## Interrupt-Record Field Set v2 (per `HDI-RUNG2-004` and `HDI-RUNG2-005`)
For all future rung envelopes and interrupt records in this lane, applying the adopted safe-hold-trigger principle (a sponsor answer is never "late"):

- `safe_hold_trigger_seconds` replaces the named-timeout concept: when it fires, the agent parks safely (checkpoint, commit, halt with reentry instruction) and the question remains open; an answer is valid whenever it arrives and is applied on reentry if the mission parked. Inferring an answer remains forbidden.
- `answer_latency_seconds`: neutral telemetry, never a criterion.
- `safe_hold_entered`: boolean; records what the agent actually did.
- Timestamps command-sourced where the harness exposes them; honest `unexposed` entries otherwise.
- Transport pass criteria measure delivery and integrity only: ask reached the sponsor's device, no inferred answer, clean park if the trigger fired, answer applied in-session or on reentry. Sponsor response speed is never a criterion.

## Common Requirements (All Rungs)
- Attended start: sponsor Go per mission; sponsor reachable for Tier 3 decisions.
- Waypoint structure, checkpoints, authored mission state, and budget discipline per `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md` and `ADAPTIVE_MISSION_CONTROL.md`.
- All six mission-health signals recorded at every checkpoint per `MISSION_HEALTH_VOCABULARY.md`, with citations; per-checkpoint recording cost noted so the signal set can be validated or shrunk.
- Model identity recorded at every checkpoint per `MUTABLE_HARNESS_STATE.md`; any skill use follows `SKILL_PROVENANCE_POLICY.md`.
- Telemetry at checkpoint level, not per-event level: the Phase 3 review found per-event overhead disproportionate for routine work, and at duration that disproportion compounds. Checkpoint-level telemetry is itself trial evidence for the telemetry-mode question.
- Closeout mission record per `MISSION_RECORD_DESIGN_V0.md`, with budget actuals versus plan from command-sourced timestamps and tool-call counts.
- Closeout separates mission result from endurance coverage and compares early-run with late-run requirement, verification, drift, checkpoint, re-entry, and evidence quality.
- Stop immediately when the objective and required verification are complete; padding invalidates the run as endurance evidence.

## Friction Measurement (Rung 2 Onward)
Governance that measures missions must also measure itself. From rung 2 onward, each rung records three counters, all derivable from the budget discipline already required:

1. Governance-overhead ratio at closeout: tool calls spent on governance artifacts (envelope authoring, checkpoint writes, mission-record authoring, advisory-suite runs) versus tool calls spent on objective work.
2. Per-artifact authoring cost: the per-checkpoint recording-cost note already required above, extended to envelope authoring and closeout-record authoring.
3. Go-to-first-edit count: tool calls from sponsor Go to the first objective edit, measuring envelope ceremony directly.

These counters are advisory observations, never targets or gates: setting a target ratio would invite under-recording, which is the failure the counters exist to detect. The counters also supply the affordability evidence for the `MISSION_ECONOMICS_VOCABULARY.md` lane decision.

Rung 2 additionally trials the structured waypoint table per the `mission_waypoint` candidate shape in `SHADOW_SCHEMA_CANDIDATES.md`: the rung-2 envelope states its waypoints as a table with the candidate's essential fields and provisional type labels, so the ladder produces evidence on whether structured waypoints earn their cost. This trials a documentation shape only; it adds no required fields, validators, or gates.

## Rung 1 — Roughly One Hour, This Repository

Status: PASSED for mechanics (2026-06-10). Mission `LADDER_RUNG1_20260610` (evidence under `ladder/rung1/`, closeout `mission_records/MR_20260610_019_ladder_rung1_state_doc_consistency.json`) exercised all rung-1 mechanics cleanly and completed in about seven minutes. Current interpretation: mission PASS and mechanics evidence are valid; longer endurance exposure was simply not exercised.
- Mission type: docs-and-fixtures work in `Factory_V3` decomposed into 3-5 waypoints (for example, a multi-document consistency pass with verification per document group).
- New thing being tested: waypoint mechanics, checkpoint cadence, mission-state upkeep, and health-signal recording at a scale where failure is cheap.
- Interrupts: simulated (file/thread-based) per the existing phased path; no live transport needed.
- Rung passes when: all waypoints closed with per-waypoint verification, checkpoint series complete with grounded health signals, budget actuals within plan, no scope drift findings.

## Rung 2 — Roughly Two Hours, POC Repository

Status: **PASSED at attempt 4 (2026-06-11)** under the then-current pre-written criteria. POC Mission 024 (`LADDER_RUNG2A4_20260611`, envelope `3b0ed95`, closeout `1ae7542`, adjudication `HDI-RUNG2-008`) supplied 95.25 active minutes of sustained evidence, about 548 calls, four feature epics at 31 waypoints with 315 tests, browser QA with real defect-fix loops, a clean interrupt, and pause/re-entry through a vendor session-limit wait. Current interpretation preserves that PASS and treats the run as strong sustained-exposure evidence, without retaining its call or elapsed floors for future mission outcomes. History of the four attempts follows unchanged as evidence under the prior criteria.

Attempts 1 and 2 FAILED on duration (2026-06-11); the lane was routed to the mandatory design review per the failure-handling rule below. Attempt 2 (POC Mission 022, `LADDER_RUNG2R_20260611`, envelope commit `e043b37`, closeout `9d0c463`, adjudication `HDI-RUNG2-004`) carried genuinely larger scope per `HDI-RUNG2-003` Option A and passed all 8 mechanics criteria — including a clean live phone interrupt whose 734s answer latency is recorded as neutral telemetry under the adopted safe-hold-trigger principle — but closed honestly at 47m40s elapsed (40m06s active) with 160 observed calls against the 550-900 forecast. Two calibration points now show budget forecasts 3.5-5x high and scope size, not throughput, as the duration gap; the sponsor's design-review guidance is that genuine 90-min/2-hour durations likely require significantly larger, more ambitious, longer-ranging scope. Attempt 1: POC Mission 021 (`LADDER_RUNG2_20260611`, envelope commit `a5c2c9a`, closeout `63a0a99`) passed 7 of 8 measured criteria — including the live phone-answered Tier 3 interrupt (96s), pause/fresh-session reentry, full health-signal series with recording costs, friction counters, and the waypoint-table trial — but closed honestly at 24m11s against the 90-180 minute band with no padding. Sponsor adjudication `HDI-RUNG2-002` (Factory_V3 `ladder/rung2/`): FAIL per the pre-written criteria. Findings include a latent envelope contradiction (measured throughput ~6.2 calls/min puts the 120-minute headline at ~745 calls, above the 700-call stop threshold) and a standalone-canon reference defect. The failed rung does not unlock rung 3; the rerun path (genuinely larger scope versus a design review re-basing rung classes on budget-and-waypoint classes) is an open sponsor decision recorded in the adjudication.

Attempt 3 (POC Mission 023, `LADDER_RUNG2R2_20260611`, envelope `a301cb3`, closeout `28e06b6`, adjudication `HDI-RUNG2-006`): FAILED on duration and budget floor by honest compression — 16 build waypoints across three epics (lifecycle governance, operator console, quality/observability), 247 tests, mechanics clean including the first live interrupt under the field set v2 (86s, neutral telemetry) — but 54m03s active and ~333 calls against the 90-min/540-call floors. Calibration verdict: throughput calibrated; the per-waypoint cost coefficient was still too high and falls as the codebase matures, so duration-by-scope chases a receding target (~27+ build waypoints would now be needed). Browser tooling was unexposed in the session, shortening the run and weakening verification depth (sponsor enablement direction recorded). Lane routed to design review round 2.

Attempt-4 class (adopted via `HDI-RUNG2-007`, superseding the attempt-3 class): ~27 build waypoints (~2x Mission 023, including ~3 dedicated browser-QA waypoints restoring the missing workload), ~31-34 waypoints total, bottom-up forecast ~700-1050 calls from Mission 023-recalibrated coefficients (~21 total calls per build waypoint, ~50% governance share, ~6.2 calls/min) — budget floor 540, stop threshold 1300, wall-clock band 90-180 min as criterion, scope-sufficiency derivation shown in the envelope before Go is asked. Pre-flight additions (Go-blocking): browser-tool availability verified and recorded as harness state; interrupt field set v2. Named contingent follow-on per `HDI-RUNG2-007`: after attempt 4, a rung-3-class hybrid contract (mission-formation + challenge skills, the `V3-ANCHOR-005` trial) may absorb the duration burden; if attempt 4 compresses again, the hybrid is the named next move and the wall-clock criterion is re-presented with four calibration points — not a fifth scope inflation.

- Future sustained-exposure candidates must be useful multi-waypoint work sized from their objective, with independent verification and authored-artifact re-entry where applicable.
- A shorter correct finish passes the mission; record the actual exposure and do not classify unconsumed budget as failure.
- Sustained endurance evidence is useful only when late-run quality remains comparable to early-run quality and no objective, authority, scope, checkpoint, re-entry, verification, or evidence drift is unresolved.

## Rung 3 — Upper Envelope, Up To Roughly Four Hours

This rung is an endurance-capability observation, not a four-hour task prescription. Candidate work must be genuinely useful and may finish earlier. Its envelope sets maximum time/cost and checkpoint thresholds but no minimum consumption floor.

- Mission type: a real multi-waypoint build mission whose contract is drafted with the mission-formation skill and red-teamed with the challenge skill (both non-executing) before sponsor Go — this is the `V3-ANCHOR-005` live non-executing trial, folded in.
- New things being tested: quality continuity as natural work approaches the upper envelope; natural Tier 3 interrupts (not seeded); budget discipline; context and re-entry management across a long session.
- Hoped-for side evidence: at least one natural (non-seeded) halt, fallback, or clarification event at duration — decision-pack evidence item 4 and the long-open Phase 3 negative-case gap. If none occurs naturally, the gap stays honestly open; do not seed and relabel.
- Evidence is sufficient only when the closeout shows continuation decisions traceable to checkpoints and health signals rather than chat memory, verification quality does not degrade late in the run, and the sponsor accepts the observed exposure as adequate support for the claimed envelope. Earlier completion remains a mission PASS with partial endurance coverage.

## Failure Handling
A mission fails only for objective, authority, scope, checkpoint, re-entry, verification, evidence, safety, or quality reasons defined by its envelope. Finishing before an exposure headline is not failure. Record actual coverage as observed, partial, or not exercised. Any real failure is evidence: classify it, file friction notes, and return to design review before retrying the affected behavior.

## Ladder Output
Assemble observed endurance evidence into `V3_OP_003_DECISION_PACK.md`, run the claim-to-proof and false-positive/false-negative reviews, and present only the evidenced envelope to the sponsor. Do not round partial exposure up to four-hour capability.

## Named Follow-ups (Not Approved Here)
- Passive Mission 026 claim-to-proof audit and FP/FN review.
- Per-run harness capability observations on future useful long-running missions.
- Upper-envelope evidence only when a real mission naturally supplies sufficient exposure; no padding or synthetic workload inflation.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
