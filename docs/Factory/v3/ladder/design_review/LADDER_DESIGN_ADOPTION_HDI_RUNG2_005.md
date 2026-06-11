# Human Decision Interrupt — HDI-RUNG2-005 (Design-Review Adoption)

## Status
Research-only and non-enforcing mission evidence: structured sponsor-decision record adopting the ladder design review's output. It amends the ladder plan only; it approves no rung execution — the rung-2 re-attempt requires its own envelope, scope-sufficiency demonstration, and explicit sponsor Go.

## Record
- Decision ID: `HDI-RUNG2-005`
- Recording mission: `LADDER_ADOPTION_20260611`
- Decision tier: 3 (rung-class redesign adoption is a sponsor roadmap decision; named open in `LADDER_DESIGN_REVIEW_20260611.md` and `MR_20260611_026`)
- Raised at: 2026-06-11, at the design-review mission closeout in the Claude Code session thread
- Answered at: 2026-06-11, in-thread
- Transport: in-session thread (sponsor attending); no notification surface used

## Question
Should the design review's output be adopted as Option A (the 90-180 minute duration band remains a rung-2 pass criterion, guarded by the bottom-up measured sizing rule and the scope-sufficiency precondition) or Option B (wall-clock demoted to a recorded observation; passes judged purely on budget-and-waypoint classes)?

## Verbatim Sponsor Answer
"i agree with option A"

## Decision
**Option A adopted.** The duration band stays a named pass criterion per `HDI-TT-001`; the failure mode is fixed at envelope-design time instead: no rung envelope is eligible for sponsor Go unless its bottom-up forecast, built from measured per-deliverable coefficients, reaches the rung's budget-class floor.

## Operative Consequences (applied in `DURATION_LADDER_PLAN.md` v0.7 by this mission)
1. Bottom-up sizing rule: rung envelopes derive budget forecasts from measured per-deliverable costs (initial coefficients from Missions 021/022: ~14 objective calls per build waypoint with tests; ~10 calls per evidence artifact; 5-13 calls per checkpoint; ~56% governance share; ~6 calls/min working throughput), citing source missions; each rung updates the coefficients. Time-derived sizing is no longer acceptable.
2. Scope-sufficiency precondition: an envelope whose bottom-up forecast falls short of the rung's budget-class floor is rejected at design time, before Go is asked.
3. Restated rung classes: rung 2 re-attempt — budget floor 540 observed calls (forecast band 540-1080), ~12-20 waypoints, stop threshold 1300, wall-clock band 90-180 min as criterion; rung 3 — budget floor 1100 (forecast band 1100-1700), ~20-30 waypoints, stop threshold 2000, wall-clock band 200-300 min as criterion. Stop thresholds sit ~20% above the budget-class ceiling so a compliant maximum-duration run never brushes its own stop rule.
4. Interrupt-record field set v2 (specifying the `HDI-RUNG2-004` safe-hold-trigger adoption) applies to all future lane envelopes: `safe_hold_trigger_seconds` (agent wait posture only; on firing, park safely and the question remains open), `answer_latency_seconds` (neutral telemetry, never a criterion), `safe_hold_entered` (boolean); command-sourced timestamps where exposed, honest `unexposed` entries otherwise; transport criteria measure delivery and integrity only.
5. Failure handling unchanged: a third rung-2 duration failure routes back to design review.
6. Next named gate: the rung-2 re-attempt envelope (POC repo), scoped at roughly 3.5x Mission 022's deliverables (multi-epic), drafted with its scope-sufficiency derivation shown, then sponsor Go.

## Evidence Pointers
- `LADDER_DESIGN_REVIEW_20260611.md` (the adopted review, including the measured-evidence table and the derivations behind every number above).
- `../rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md` (the triggering adjudication and the safe-hold-trigger adoption).
- `DURATION_LADDER_PLAN.md` v0.7 (the amended operative plan).
