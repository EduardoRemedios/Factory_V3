# Human Decision Interrupt — HDI-RUNG2-003 (Rung-2 Rerun Path)

## Status
Research-only and non-enforcing mission evidence: structured sponsor-decision record for the rung-2 rerun path after the `HDI-RUNG2-002` FAIL adjudication. It approves the path selection only; the rerun itself requires its own envelope in the POC repo and explicit sponsor Go.

## Record
- Decision ID: `HDI-RUNG2-003`
- Recording mission: `RUNG2_RERUN_PREP_20260611`
- Decision tier: 3 (rerun path after a failed rung is a sponsor roadmap decision; named as the open gate in `HDI-RUNG2-002`)
- Raised at: 2026-06-11, in the `HDI-RUNG2-002` adjudication record and the same session thread
- Answered at: 2026-06-11, in-thread
- Transport: in-session thread (sponsor attending); no notification surface used

## Question
After rung-2 attempt 1 failed on duration with mechanics 7/8, should the rerun keep the wall-clock band and use genuinely larger scope (Option A), or should the ladder first run a design review re-basing rung classes on budget-and-waypoint classes (Option B)?

## Options (as named in `HDI-RUNG2-002`)
- Option A: Rerun rung 2 with genuinely larger scope (~550-750 objective tool calls per measured throughput) and a raised stop threshold, keeping the wall-clock band as pass criterion.
- Option B: Ladder design review first; wall clock becomes a recorded observation; rerun against redesigned criteria. (Recommended in the adjudication prep.)

## Answer
- Answer source: sponsor, Claude Code session thread, 2026-06-11 ("lets go with option A")
- Answer: Option A — rerun rung 2 with genuinely larger scope under the unchanged wall-clock band (90-180 minutes, genuine duration per `HDI-TT-001`).

## Named Consequences
- The rerun mission (POC Mission 022) must carry genuinely larger scope sized from measured throughput: roughly 550-900 total tool calls of honest work, with the stop threshold raised to 1100 so the duration band and the budget class no longer contradict (the attempt-1 latent-contradiction finding).
- The honesty rules stand unchanged: no padding, no harness-speed throttling to stretch wall clock, close out early honestly if the objective completes — and if the rerun fails the duration band again, the lane routes to the Option B design review as mandated by `DURATION_LADDER_PLAN.md` failure handling (two consecutive failures of the same rung).
- Pre-rerun fix (from `HDI-RUNG2-002` finding 2): the rerun envelope must not reference Factory_V3-only files as operative authority — referenced canon (mission-health vocabulary) is vendored into the POC repo or inlined.
- The rerun envelope must require the harness speed/effort setting to be recorded at mission start and on change (`HDI-RUNG2-002` finding 5).
- All rung-2 criteria apply afresh to the rerun, including a new live phone-answered Tier 3 interrupt with the sponsor away, and a new deliberate pause/fresh-session reentry.
- Option B is not rejected permanently: it is the named mandatory route on a second duration failure, and remains available to the sponsor at any time as a separately approved design review.
