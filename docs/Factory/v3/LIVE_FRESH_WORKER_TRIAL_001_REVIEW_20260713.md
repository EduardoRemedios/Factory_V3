# Live Fresh-Worker Trial 001 Evidence Review

## Status

Research-only evidence review. `V3-FW-TRIAL-001` ended `FAIL_CLOSED_SAFE_HOLD` on 2026-07-13. This review closes that failed trial; it does not authorize recovery, a new worker, an attended serial epic, profile promotion, or runtime orchestration.

## Evidence Scope

- Product repository: `/Users/eduardodosremedios/same_second`
- Trial branch: `codex/v3-fw-trial-001`
- Pause checkpoint: `c995bd79f0c5afee84e8f4dc5ea6f39547076325`
- Fresh-worker brief: `55a87e498905a031970dd0aa89281a1a040c7e9b`
- Comparison and safe hold: `084cb002745b74082e1b0a6f79fad4e24173b8ab`
- Authored state: revision 7, event 8, parent and active child at `safe_hold`
- Fresh-worker result: 19 of 23 scored fields matched

The originating task and the fresh Codex task used the same harness family. The fresh task reported no access to the originating transcript, memory, or summary. That isolation statement is actor-reported; git proves the brief-before-comparison commit order, not when a file was read or what private context the worker possessed.

## Observed Protocol

The pause leg committed ordinary graph, state, checkpoint, envelope, and sealed-key artifacts before the fresh task began. The fresh task committed `REENTRY_BRIEF.json`, reported opening the sealed key only afterward, then committed `REENTRY_COMPARISON.json` and the kernel safe-hold transition after comparison failed. Git proves the commit order, while key-read timing remains actor-reported. The comparison commit changed no product scripts, tests, contracts, or fixtures. Child C02 therefore never received start authorization.

## Findings

| Missing or mismatched field | Classification | Observation |
| --- | --- | --- |
| `open_interrupts` | Normal-artifact shape gap | The pause checkpoint did not state an explicit empty collection outside the sealed key. Absence was ambiguous to the fresh worker. |
| `repository_state.commit_before_pause_leg` | Re-entry brief extraction/shape omission | The committed checkpoint contained the value, but the brief did not reproduce it under the scored path. |
| `repository_state.factory_v3_source_commit` | Re-entry brief extraction/shape omission | The committed checkpoint contained the value, but the brief did not reproduce it under the scored path. |
| Explicit `mandatory_first_action` | Re-entry brief shape omission | The worker performed the required first action but did not emit the exact scored field. |

The strict all-fields comparison failed honestly. The omitted fields were not all equally safety-critical, so a later trial should separate continuation-critical scoring from provenance/completeness scoring without allowing either derived values or session memory to grant authority.

## What The Trial Demonstrated

- Authored state and events rejected continuation and preserved one active child at safe hold.
- Brief-before-key ordering is visible in git history.
- A fresh task reconstructed most of the mission from repository artifacts and performed the mandatory first action.
- Failure produced durable comparison evidence instead of product implementation.
- The kernel's safe-hold behavior was useful under an operationally imperfect handoff.

## What The Trial Did Not Demonstrate

- It did not prove artifact-sufficient continuation, because the scored brief failed.
- It did not prove cross-harness isolation, private-context absence, attended serial-epic behavior, worker dispatch, endurance, concurrency, or runtime authority.
- It did not validate product code; C02 did not start and no product tests were required after the authored halt rule fired.
- It did not prove filesystem atomicity across the state and event files.

## State And Closeout Distinction

The state-kernel v0.1 CLI has no terminal `halt` transition. The authored machine state therefore remains honestly at `safe_hold` revision 7/event 8. The human decision recorded in the product-repository closeout is to halt and close this failed trial rather than resume it. That administrative closeout does not rewrite the authored state, append a synthetic kernel event, or claim a terminal state the kernel cannot represent.

## Validator Observations

The mission-record validator accepted the halted record and produced no observed false positive or false negative. The 19/23 result exposed trial-design and artifact-authoring friction, not a demonstrated mission-record-validator defect. Exact path scoring caught real omissions, while treating all 23 fields as one undifferentiated continuation gate would overstate the safety significance of provenance-only omissions.

## Decision And Next Gate

Close `V3-FW-TRIAL-001` as a failed, fail-closed trial. Do not resume C02. The next possible mission is a separately formed and approved `V3-FW-TRIAL-002` that:

1. uses a new parent mission and branch rather than reopening Trial 001;
2. makes empty interrupts and decisions explicit in ordinary checkpoint artifacts;
3. supplies a value-free brief template with exact required paths;
4. separates continuation-critical results from provenance/completeness findings while preserving an honest overall verdict;
5. requires a new non-forked fresh task and retains brief-before-key ordering; and
6. starts product work only after the pre-authorized comparison gate passes.

Only after separately approved live fresh-worker evidence should Factory decide whether to run an attended serial-epic pilot. Read-only Codex SDK/MCP discovery remains later still.
