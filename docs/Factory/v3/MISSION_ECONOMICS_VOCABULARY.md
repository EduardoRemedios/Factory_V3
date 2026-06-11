# Factory V3 Mission Economics Vocabulary

## Version
v0.1

## Change Log
- v0.1 (2026-06-11): Initial advisory vocabulary for waypoint-boundary mission-economics terms, from the backlog research spike; vocabulary-before-schema per the V3-ANCHOR-007 pattern.

## Status
Research-only and non-enforcing.

This document defines vocabulary only. It does not authorize schema files, validators, required checkpoint or waypoint fields, routing decisions, gates, thresholds, runtime-control power, default-mode behavior, V3 profile promotion, a new research-lane anchor, or Factory V2 build-support removal.

Factory V3 is not promoted by this document.

## Purpose
`MISSION_HEALTH_VOCABULARY.md` answers a state question: is this mission still functioning correctly? Economics answers a value question that health does not: is finishing this mission still the best use of its remaining budget? A long mission can be perfectly healthy — on objective, within plan, verified — and still no longer worth completing because the remaining criteria are cheap to abandon and expensive to finish.

Economics consumes health signals as inputs (notably `budget_burn` and `objective_value`); it does not duplicate them. The two vocabularies stay separate documents because they answer different questions, but a mission records them in the same checkpoint discipline.

## Terms

Each term is recorded at waypoint boundaries only — not at every checkpoint — with a one-line evidence citation.

| Term | Question it answers | Grounding |
| --- | --- | --- |
| `remaining_objective_map` | Which envelope success criteria remain, and which remaining waypoints serve them? | Cited mapping from criteria to waypoints; a criterion with no serving waypoint is a finding |
| `marginal_burn` | What did the last completed waypoint actually cost? | Tool-call count and command-sourced elapsed time for that waypoint, versus its forecast slice if one was named |
| `cost_to_complete` | What will the remaining waypoints cost? | Forecast labeled as a forecast, derived only from measured same-mission per-waypoint actuals |
| `halt_cost` | What does stopping now cost? | Reentry overhead from prior measured resumes, staleness risk, and any work that cannot be recovered from authored artifacts |
| `economic_judgment` | Is continuation still the best use of the remaining budget? | `worth_continuing` \| `diminishing_returns` \| `stop_loss`, consistent with the checkpoint's `continuation_judgment` |

## Grounding Rules (Anti-Theater)

1. Every term cites artifact evidence; a term without a citation is `not_recorded`, not a guess.
2. `marginal_burn` grounds only in tool-call counts and command-sourced timestamps. Model-estimated minutes are not measurements (POC Missions 012/013 observed 6-9x inflation) and must not ground any economics term.
3. `cost_to_complete` is always labeled as a forecast per `ADAPTIVE_MISSION_CONTROL.md` forecast discipline, and may be derived only from measured per-waypoint actuals of the same mission. A mission with no completed waypoints has no `cost_to_complete`; it records `not_yet_derivable`.
4. Value claims cite envelope success criteria. No term may claim value the envelope did not name.
5. Sunk cost is never a reason to continue. An `economic_judgment` grounded in spend already incurred ("we have already invested N hours") is malformed. Only remaining cost versus remaining criteria may ground the judgment.
6. `economic_judgment` must be consistent with the same checkpoint's `continuation_judgment` from `MISSION_HEALTH_VOCABULARY.md`; when the two conflict and the contradiction cannot be explained in one line, the correct judgment is `checkpoint_and_ask` or stronger.
7. These terms are advisory observations, never targets or gates. No threshold discussion before ladder evidence exists.

## Recording Cadence
Waypoint boundaries only. The first recording trial is the rung-3 ladder mission per `DURATION_LADDER_PLAN.md`; rung 2 is not required to record economics terms — rung 2 instead records the friction counters that determine whether this vocabulary is affordable at all. Adding economics recording to rung 2 requires a sponsor-approved envelope change, not this document.

## Relationship To Existing Canon
- `MISSION_HEALTH_VOCABULARY.md`: health signals are inputs to economics; `objective_value: diminishing` plus `budget_burn` approximate the economics question but lack cost-to-complete and halt-cost, which is exactly what this vocabulary adds.
- `ADAPTIVE_MISSION_CONTROL.md`: budget measurement and forecast-labeling discipline ground every term here.
- `DURATION_LADDER_PLAN.md`: the ladder supplies the recording-cost evidence that decides whether economics becomes a research lane.

## Named Follow-ups (Not Approved Here)
- A research-lane anchor for mission economics, decided only after rung-2 friction-counter evidence shows the recording cost is affordable.
- Shadow schema candidate fields for these terms.
- Threshold discussion only after ladder evidence exists.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
