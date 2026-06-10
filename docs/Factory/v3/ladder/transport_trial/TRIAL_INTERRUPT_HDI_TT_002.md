# Human Decision Interrupt — HDI-TT-002 (Deliberate-Timeout Leg)

## Status
Research-only and non-enforcing mission evidence: structured interrupt record for the active transport trial. Approves nothing.

## Record
- Interrupt ID: `HDI-TT-002`
- Mission ID: `TRANSPORT_TRIAL_20260610`
- Decision tier: 3 (ladder naming convention is a sponsor roadmap-vocabulary decision flagged in MR_019 design signals)
- Pre-resolution check: Tier 1/2 reviewed — naming convention changes how all future rung evidence is labeled; not an in-mission wording detail
- Raised at: 2026-06-10T13:40:40Z
- Transport attempt (verbatim harness result): "Not sent — terminal has focus. Terminal + mobile suppressed."
- Transport observation: second confirmation of focus-based suppression while the sponsor is attending the session; consistent with HDI-TT-001.
- Timeout behavior (named at raise time, per trial design): the end of the session turn in which this interrupt is raised. The sponsor is instructed NOT to answer within that window; this leg exists to exercise the no-response safe-hold path under controlled conditions.

## Question
Should duration-ladder rungs keep their hour-based names (roughly 1h/2h/4h), or move to budget-and-waypoint classes (tool-call budget + waypoint count), given the MR_019 finding that harness speed compresses wall clock far below human-paced estimates?

## Reason
MR_019 design signal flagged the naming question; it affects how rung 2-3 envelopes state their pass criteria.

## Decision Type
Ladder naming / sizing vocabulary

## Options (for the reentry answer)
- Option A: Keep hour-based rung names as the headline, with budget-and-waypoint classes added as the measured pass criteria (hours stay human-readable; budgets stay honest).
- Option B: Rename rungs to budget-and-waypoint classes only; drop hour names.
- Option C: Keep hour names unchanged and handle compression case-by-case in each envelope.

## Recommended Option
Option A

## Timeout Outcome
- Answer within timeout: none — the named timeout expired at end of turn with no answer, as designed.
- Outcome recorded per the no-response safe-hold rule (`CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`): timeout logged as the answer-source outcome; no answer inferred or assumed; checkpoint recorded; mission entered safe-hold (no further file changes beyond this record, the checkpoint, and the halt note); clean halt with reentry instruction.

## Answer (completed at reentry)
- Answer source: sponsor, reentry session reply, 2026-06-10T13:42Z window ("ok I answer it as A")
- Answer: Option A — hour-based rung names remain the human-readable headline; budget-and-waypoint classes become the measured pass criteria
- Answer interpretation: `DURATION_LADDER_PLAN.md` adds a naming-and-sizing rule requiring each rung envelope to state measured pass criteria as budget-and-waypoint classes (tool-call budget, waypoint count, command-sourced elapsed time) alongside the hour-based headline.
- Plan delta: none — matches the envelope's planned Decision 2 shape.
- Continuation decision: continue to closeout (`MR_20260610_020`), then scoped commit per envelope git authority.
