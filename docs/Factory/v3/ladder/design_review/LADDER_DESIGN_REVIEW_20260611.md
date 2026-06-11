# Ladder Design Review — Re-Basing Rung Classes on Measured Budget-And-Waypoint Evidence

## Status
Research-only and non-enforcing design review, mandated by the ladder failure-handling rule after two consecutive rung-2 duration failures (`HDI-RUNG2-002`, `HDI-RUNG2-004`) and executed under mission `LADDER_DESIGN_REVIEW_20260611` with explicit sponsor GO. This document proposes; it adopts nothing. Adoption of its output is the named open sponsor decision `HDI-RUNG2-005`. Until adoption is recorded, `DURATION_LADDER_PLAN.md` v0.6 remains the operative rung definition.

## Named Inputs (per `HDI-RUNG2-004`)
1. Finding F1: two-point calibration evidence that rung classes are mis-based on wall-clock and budget forecasts run 3.5-5x high.
2. Sponsor guidance (verbatim in `../rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md`): reaching genuine 90-minute/2-hour durations will likely require "a significantly larger scope. More ambitious and more long-ranging."
3. The adopted safe-hold-trigger principle, to be specified as an interrupt-record field set for future envelopes.
4. Standing constraints: `HDI-TT-001` (genuine duration is a named criterion from rung 2 onward; honesty rules — no padding, no throttling, honest early closeout), `HDI-TT-002` (hour names are headlines; measured criteria are budget-and-waypoint classes), and finding F3 (Codex harness observability gaps).

## Measured Evidence (Two Calibration Points)

| Quantity | Mission 021 (attempt 1) | Mission 022 (attempt 2) | Stability |
| --- | --- | --- | --- |
| Observed tool calls | 150 | 160 | stable despite ~2x deliverable scope |
| Forecast calls | 400-600 | 550-900 | both 3.5-5x high |
| Active duration | 24m11s | 40m06s (47m40s elapsed; 7m34s pause) | both far under the 90-180 min band |
| Working throughput | ~6.2 calls/min | ~5.7 calls/min (active time minus the 12m13s open-interrupt wait) | stable |
| Governance share of calls | ~56% | ~56% (90 of 160) | stable |
| Per-evidence-artifact authoring cost | — | ~10 calls | first measurement |
| Per-checkpoint recording cost | comparable | 5-13 calls | stable |
| Objective calls per build waypoint (module + tests) | — | ~14 (≈70 objective calls across 5 build waypoints) | first measurement |
| Mechanics criteria | 7/8 | 8/8 | improving |

## Diagnosis
The duration failures are envelope-design failures, not run failures or throughput failures.

- What replicated: working throughput (~6 calls/min), governance share (~56%), interrupt mechanics, pause/reentry, verification discipline. The execution engine is predictable.
- What failed: the conversion of *scope* into *calls*. Both envelopes sized budgets top-down (band minutes × throughput) and then assumed the named scope would fill that budget. It did not: Mission 022's entire operations epic — five build waypoints with tests, browser QA, and a real mid-run defect fix — consumed only ~70 objective calls. The `budget_slice` forecasts of 90-150 calls per waypoint were 6-10x the measured ~14.
- Consequence: the duration band can only be genuinely reached by sizing scope bottom-up from measured per-deliverable costs. At ~6 calls/min of honest work, the 90-minute band floor requires roughly **540 observed calls**; at ~56% governance share that is roughly **240 objective calls, i.e. ~17 Mission-022-scale build waypoints — about 3.5x Mission 022's entire deliverable scope**. The 180-minute ceiling corresponds to ~1080 calls, which also exposes that the current stop threshold (1100) leaves no margin at the band ceiling; a compliant maximum-duration run would brush its own stop rule (the attempt-1 latent contradiction, reappearing at the new threshold).

This converges exactly with the sponsor's guidance: the next attempt needs significantly larger, more ambitious, longer-ranging scope — and the sizing rule below makes "how much larger" a measured quantity instead of a guess.

## Proposed Redesign

### 1. Bottom-up scope-sizing rule (both options)
Every future rung envelope must derive its budget forecast bottom-up from measured per-deliverable costs (currently: ~14 objective calls per build waypoint with tests; ~10 calls per evidence artifact; 5-13 calls per checkpoint; ~56% governance share), citing the source missions for the coefficients. Time-derived forecasts (band minutes × throughput) are no longer acceptable as the sizing method; they are the documented cause of both failures. Each rung envelope updates the coefficients from the latest measured run, so calibration compounds.

### 2. Scope-sufficiency precondition (both options)
A rung envelope is not eligible for sponsor Go unless its bottom-up forecast reaches the rung's budget-class floor. An under-scoped envelope is rejected at design time — converting duration failure from a run outcome into a reviewable envelope defect.

### 3. Restated rung classes
Headline hour names remain human-readable labels per `HDI-TT-002`. Measured classes, derived from the calibration points:

| Rung | Headline | Budget class (observed calls of honest work) | Waypoint class | Stop threshold | Wall-clock band |
| --- | --- | --- | --- | --- | --- |
| 2 (re-attempt) | ~2 hours | floor 540, forecast band 540-1080 | ~12-20 waypoints (multiple epics) | 1300 | 90-180 min — status per Option A/B below |
| 3 | ~4 hours | floor 1100, forecast band 1100-1700 | ~20-30 waypoints | 2000 | 200-300 min — status per Option A/B below |

Stop thresholds are set ~20% above the budget-class ceiling so a compliant maximum-duration run never brushes its own stop rule.

### 4. Interrupt-record field set v2 (safe-hold-trigger, adopted in `HDI-RUNG2-004`)
For all future envelopes and interrupt records in this lane:
- `safe_hold_trigger_seconds` replaces the named-timeout concept: when it fires, the agent parks safely (checkpoint, commit, halt with reentry instruction) and the question **remains open**.
- `answer_latency_seconds`: neutral telemetry, never a criterion; a sponsor answer is never "late".
- `safe_hold_entered`: boolean; records what the agent actually did, not what the sponsor did.
- Timestamps command-sourced where the harness exposes them; honest `unexposed` entries otherwise (finding F3).
- Transport pass criteria measure delivery and integrity only: ask reached the sponsor's device, no inferred answer, clean park if the trigger fired, answer applied (in-session or on reentry).

## Adoption Options (`HDI-RUNG2-005`, open sponsor decision)

### Option A — Duration band stays a pass criterion, guarded by the sizing rule (RECOMMENDED)
The 90-180 min band remains a named rung-2 pass criterion per `HDI-TT-001`, and items 1-4 above are adopted with it. The scope-sufficiency precondition makes the band reachable honestly: the envelope must prove, from measured coefficients, that the named scope fills the band floor before Go is asked. Recommended because it matches the sponsor's stated intent (reach the durations via larger scope), preserves the decision-pack requirement for health-signal evidence at genuine duration, and fixes the failure where it occurred (envelope design) rather than moving the goalposts.

### Option B — Wall-clock demoted to recorded observation
Rung passes are judged purely on budget-and-waypoint classes; wall-clock is recorded but not a criterion. Simpler and immune to compression surprises, but it weakens the link to the decision pack's purpose (evidence that governance holds at genuine multi-hour duration) and would judge a third 40-minute run a pass — which the sponsor's guidance argues against.

Under either option, a third rung-2 duration failure (Option A) or budget-class miss (Option B) routes back to design review; the failure-handling rule is unchanged.

## Consequences If Adopted
- `DURATION_LADDER_PLAN.md` is amended (v0.7) with the restated rung classes, the sizing rule, the scope-sufficiency precondition, and the interrupt field set v2 — in the `HDI-RUNG2-005` recording mission, not here.
- The rung-2 re-attempt envelope (POC repo) must name scope ~3.5x Mission 022's deliverables, sized bottom-up: a candidate shape is a multi-epic PPOS build (e.g. three Mission-022-scale epics) with ~12-20 waypoints, forecast 540-1080 calls, stop threshold 1300, and one live phone interrupt plus one deliberate pause/reentry as before.
- Pre-written decision-pack criteria remain unamended; rung 3 stays locked; assessment stays `NO PROMOTION YET`.

## Evidence Pointers
- `../rung2/RUNG2_ADJUDICATION_HDI_RUNG2_002.md`; `../rung2/RUNG2_RERUN_PATH_HDI_RUNG2_003.md`; `../rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md`.
- POC repo: Mission 021 and Mission 022 closeouts, records, interrupt JSONs, checkpoint logs (commits `a5c2c9a`..`63a0a99`, `e043b37`..`9d0c463`).
- `DURATION_LADDER_PLAN.md` v0.6 (operative until adoption); `MISSION_ECONOMICS_VOCABULARY.md` (the coefficients above are its first usable dataset).
