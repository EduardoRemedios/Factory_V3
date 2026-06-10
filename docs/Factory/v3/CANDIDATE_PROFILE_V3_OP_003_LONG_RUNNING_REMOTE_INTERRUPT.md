# Factory V3 Candidate Profile: V3-OP-003 Long-Running Remote-Interrupt Mission

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial candidate profile drafted from POC Mission 012/013 checkpoint and interrupt evidence, `ADAPTIVE_MISSION_CONTROL.md` v0.2, and the 2026-06-04 interrupt-transport spike.

## Status
Candidate only. Not approved for any use.

This profile has no release approval and may not govern any mission. Promotion requires the evidence named in `V3_OP_003_DECISION_PACK.md` and explicit human release approval per `PROMOTION_CRITERIA.md`. Factory V2 remains the governing default, and `V3-OP-001` remains the only approved optional V3 profile.

This document does not approve live messaging automation, unattended execution, scheduled wakes, credential use, deployment scope, required gates, governance routing, or runtime-control power.

## Purpose
Define the profile shape for a single attended long-running mission — on the order of four hours — so that duration-ladder trials can be judged against a concrete profile instead of abstract ambition, mirroring how `V3-OP-001` anchored bounded-change readiness.

"Attended" means a human sponsor launches the mission with per-mission Go and remains asynchronously reachable through an approved interrupt transport. This profile is not for unattended or scheduled operation; that is the separate standing-authorization research lane (`V3-ANCHOR-009`).

## Profile Identity
- Profile ID: `V3-OP-003`
- Profile name: Long-Running Remote-Interrupt Mission
- Profile type: candidate optional V3 operational profile (not approved)
- Governing default outside this profile: Factory v2
- Required fallback: Factory v2

## Eligible Work
Work may be eligible for this profile only when all conditions are true:

- The objective decomposes into named waypoints: bounded phases, each with its own verification or evidence check.
- Each waypoint would individually satisfy `V3-OP-001` eligibility, or names exactly why not plus the compensating verification.
- The affected scope can be named per waypoint before execution.
- The sponsor has pre-resolved foreseeable decisions (Tier 1) and stated decision principles for Tier 2 in the envelope.
- An approved interrupt transport is available and named in the envelope, with tested delivery before mission start.
- Explicit halt, safe-hold, reentry, and V2 fallback rules exist before execution.
- The mission fits the interim budget target: roughly a 4-hour run inside a roughly 5-hour plan window, measured per `ADAPTIVE_MISSION_CONTROL.md` budget discipline.

## Excluded Work
- Anything `V3-OP-001` excludes (production deployment, regulated action paths, payment, authentication policy, data migration, security boundaries, infrastructure authority) unless a future heavier profile exists.
- Missions whose waypoints cannot be verified independently.
- Missions requiring credential use, live integrations, or real-data scope not separately approved.
- Unattended or scheduled operation of any kind.
- Concurrent multi-worker execution; this profile is serial, one worker.

## Mission Structure
1. Mission contract: objective, waypoints, success criteria per waypoint, non-goals. The contract should be drafted or red-teamed with the mission-formation and challenge skills (non-executing) before sponsor Go.
2. Execution loop: per `ADAPTIVE_MISSION_CONTROL.md` — execute waypoint, checkpoint, verify, continue/ask/halt.
3. Checkpoints at every waypoint boundary, before risky transitions, and at budget thresholds. Each checkpoint records the `ADAPTIVE_MISSION_CONTROL.md` checkpoint fields plus the model identity observed at that checkpoint (`MUTABLE_HARNESS_STATE.md`); a model change mid-mission is a checkpoint-worthy event and a Tier 2 log entry at minimum.
4. Authored mission state file maintained throughout; continuation decisions come from authored artifacts, never from chat memory or elapsed-time estimates.
5. Closeout: full mission record per `MISSION_RECORD_DESIGN_V0.md`, including all checkpoints, interrupts, plan deltas, deferred-decision log, and budget actuals versus the envelope target.

## Remote Interrupt Rules
- Tier 3 interrupts travel over the approved transport named in the envelope and are recorded with the full interrupt-record fields from `ADAPTIVE_MISSION_CONTROL.md`, regardless of which transport carried the message.
- Every Tier 3 interrupt names its timeout when asked.
- While an answer is pending, the mission may continue only parallel work that is already authorized and unaffected by the pending decision.

## No-Response Safe-Hold Rule
If a Tier 3 interrupt's timeout expires without a human answer:

1. Record the timeout as the interrupt's answer-source outcome; do not infer or assume an answer.
2. Record a checkpoint and update the mission state file.
3. Commit if and only if the envelope's git authority allows a checkpoint commit.
4. Enter safe-hold: no further file changes, no new waypoints; only read-only commands and halt actions are permitted.
5. If a second configurable window passes in safe-hold, halt cleanly with a reentry instruction.

Reentry from safe-hold follows the same stale-reentry discipline as halted missions: reread authored artifacts, verify scope is unchanged, and obtain the pending human answer before any further change. Skills relied on during the mission follow `SKILL_PROVENANCE_POLICY.md`; a learned or unknown-provenance skill is never an acceptable substitute for a missing human answer.

## Authority Limits
This candidate profile, if ever approved, would not authorize:

- runtime-kernel behavior or production action mediation
- unattended continuation past safe-hold
- scope expansion by plan delta beyond envelope-named expansion room; larger changes end the mission and start a successor
- dependency additions without explicit Tier 3 approval
- continuation after failed halt-on-failure verification
- CI or required-gate wiring, V2 deprecation, or default-mode behavior

## V2 Fallback Triggers
All `V3-OP-001` triggers apply, plus:

- the interrupt transport fails its pre-mission delivery test or fails during the mission with a Tier 3 decision pending
- checkpoint or mission-state writing fails twice
- budget actuals exceed the envelope stop threshold
- safe-hold is entered twice in one mission
- mission-health signals (once defined) cross an envelope-named halt threshold

## Evidence Requirements
Closeout must name everything `V3-OP-001` requires, plus: the checkpoint series with per-checkpoint model identity, the interrupt log with timeout outcomes, plan deltas, the deferred-decision (Tier 2) log, budget actuals from command-sourced timestamps and tool-call counts, and the safe-hold record if entered.

## Promotion Dependencies
See `V3_OP_003_DECISION_PACK.md`. This profile cannot be used before that pack reaches `PASS` or `CONDITIONAL PASS` with explicit human release approval.
