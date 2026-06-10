# Factory V3 Mission Health Vocabulary

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial advisory vocabulary for checkpoint-time mission-health signals, fulfilling the V3-ANCHOR-007 named gate of defining vocabulary before schema, validator, or gate proposals.

## Status
Research-only and non-enforcing.

This document defines vocabulary only. It does not authorize schema files, validators, required checkpoint fields, routing decisions, gates, thresholds, runtime-control power, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this document.

## Purpose
Over a multi-hour mission the expensive failure is not a bad edit — it is hours of confident drift. Checkpoints need a small, fixed vocabulary for answering "is this mission still healthy and worth continuing," so that continuation decisions come from authored evidence instead of momentum.

This vocabulary is designed to be recorded at checkpoints under `ADAPTIVE_MISSION_CONTROL.md` and is required input evidence for the `V3_OP_003_DECISION_PACK.md` ladder (evidence item 3).

## Signals

Each signal is recorded at checkpoint time with one allowed value and a one-line evidence citation.

| Signal | Question it answers | Allowed values |
| --- | --- | --- |
| `budget_burn` | How does measured spend compare to the envelope plan? | `within_plan` \| `approaching_threshold` \| `threshold_exceeded` |
| `objective_value` | Does the remaining planned work still serve the mission objective? | `on_objective` \| `diminishing` \| `off_objective` |
| `confidence` | What grade of evidence supports the current approach? | `verified` \| `provisional` \| `speculative` |
| `drift` | How does actual touched scope compare to the envelope? | `none` \| `within_expansion_room` \| `scope_drift_detected` |
| `risk` | What is the trend of open risks since the last checkpoint? | `stable` \| `accumulating` \| `boundary_risk` |
| `continuation_judgment` | What should the mission do next? | `continue` \| `continue_with_adjustment` \| `checkpoint_and_ask` \| `safe_hold` \| `halt` |

## Grounding Rules (Anti-Theater)

1. Every signal value cites artifact evidence: verification results, tool-call counts, command-sourced timestamps, diff scope versus authorized files, or the open-risk list. A signal without a citation is `not_recorded`, not a guess.
2. `budget_burn` is measured from tool-call counts and command-sourced timestamps per `ADAPTIVE_MISSION_CONTROL.md`. Model-estimated minutes are not measurements (POC Missions 012/013 observed 6-9x inflation) and must not ground this signal.
3. `confidence` is graded by evidence class: `verified` means passing verification output exists for the current approach; `provisional` means the approach rests on read evidence not yet verified; `speculative` means neither. It is not a self-reported feeling.
4. `drift` compares the actual touched-file and command set against the envelope. `within_expansion_room` is valid only when the envelope named expansion room in advance.
5. `continuation_judgment` must be consistent with the other five signals; a checkpoint recording `threshold_exceeded` or `off_objective` together with plain `continue` must explain the contradiction or is malformed.
6. Two consecutive checkpoints at `diminishing`, or any checkpoint at `off_objective`, should produce `checkpoint_and_ask` or stronger. This is advisory review discipline, not a gate.

## Worked Example (Synthetic)
```text
checkpoint: CP-04
budget_burn: approaching_threshold  (tool calls 212 of ~260 planned; elapsed 2h41m per git timestamps)
objective_value: on_objective       (waypoints 1-3 closed; waypoint 4 maps to success criterion 2)
confidence: provisional             (waypoint 4 approach based on read evidence; tests not yet run)
drift: within_expansion_room        (touched docs/x.md, named as expansion room in envelope)
risk: stable                        (open risks unchanged since CP-03)
continuation_judgment: continue
```

## Relationship To Existing Canon
- `ADAPTIVE_MISSION_CONTROL.md` defines where these signals live (checkpoints) and the budget measurement discipline they rely on.
- `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md` lists envelope-named mission-health halt thresholds among its V2 fallback triggers, pending this vocabulary maturing.
- `MUTABLE_HARNESS_STATE.md`: a mid-mission model change is checkpoint-worthy context when interpreting a `confidence` or `risk` shift.

## Named Follow-ups (Not Approved Here)
- Shadow schema candidate fields for these signals in checkpoint records.
- Advisory validator checks for signal/judgment consistency (rule 5) with fixture coverage.
- Threshold discussion (what values trigger what) only after ladder evidence exists.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
