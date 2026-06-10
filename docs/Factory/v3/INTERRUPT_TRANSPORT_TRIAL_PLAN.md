# Factory V3 Interrupt-Transport Live Trial Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial plan for a narrow live trial of a vendor-native human-interrupt transport, building on the 2026-06-04 interrupt-transport spike.

## Status
Research-only and non-enforcing plan. Executing this trial is not approved by this document.

A separate, explicit sponsor approval is required before any live transport use, naming the transport, the mission, the date window, and the participating human. Until that approval exists, all spike-era prohibitions stand: no Telegram bot, token, polling, webhook, or live messaging from V3, and no unattended runs.

This document does not approve scheduled operation, credential use, production scope, required gates, governance routing, or runtime-control power.

## Purpose
Close `V3_OP_003_DECISION_PACK.md` evidence item 2: at least one real Tier 3 interrupt round-trip over a live transport, and one exercised timeout reaching safe-hold, each fully recorded.

The 2026-06-04 spike concluded that interrupt transport is vendor-solved and V3's job is the governance record regardless of which transport carried the message. This trial tests exactly that division: the vendor moves the message; V3 produces the structured interrupt record, captures the answer, and records the plan delta.

## Transport Selection
Per the spike's recommendation order:

1. Primary candidate: Claude Code Remote Control with push notifications (local session synced to phone or browser).
2. Secondary candidate: Codex mobile (ChatGPT app surface), if the trial mission runs under a Codex harness.
3. Telegram bridge remains fallback-only with no build, per the spike decision.

The trial uses one transport. Comparing transports is out of scope; a second transport would be a second trial.

## Trial Mission Shape
- One synthetic, docs-only mission in this repository under `V3-OP-001` (the trial mission itself is bounded and short; long duration is the ladder's job, not this trial's).
- The mission envelope pre-plants two genuine Tier 3 decision points that cannot be Tier 1/Tier 2 resolved (for example, a wording choice the sponsor genuinely has not pre-decided, and a scope question with real alternatives).
- Pre-mission delivery test: before Go, a test notification round-trip confirms the transport reaches the sponsor's device and an answer reaches the session.

## Trial Protocol
1. Interrupt 1 (answered): the mission raises the first Tier 3 interrupt over the transport, with the full interrupt-record fields from `ADAPTIVE_MISSION_CONTROL.md` including a named timeout. The sponsor answers from the remote device. The mission records answer, interpretation, plan delta if any, and continues.
2. Interrupt 2 (timed out, deliberately): the sponsor deliberately does not answer within the named timeout. The mission executes the no-response safe-hold rule from `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`: record the timeout outcome, checkpoint, enter safe-hold, and halt cleanly with a reentry instruction after the safe-hold window.
3. Reentry: a follow-up session reenters per stale-reentry discipline, obtains the pending answer (now given), records it, and completes the mission.

## Required Evidence
- The pre-mission delivery test result.
- Two complete interrupt records (one answered, one timed out), each naming the transport that carried the message.
- The safe-hold checkpoint and halt record, then the reentry record.
- Latency observations: command-sourced timestamps for ask-to-deliver and deliver-to-answer (measured, not estimated).
- A transport-failure note if delivery fails at any point — a failed delivery is valid trial evidence, not a trial failure; it routes to the V2 fallback trigger and gets recorded.
- Closeout mission record per `MISSION_RECORD_DESIGN_V0.md`, including model identity and any skill use per `SKILL_PROVENANCE_POLICY.md`.

## Pass/Learn Criteria
The trial passes when both interrupt paths (answered; timed-out-to-safe-hold) produced complete replayable records and the governance record was transport-independent (no record field required vendor-private data beyond a transport name and timestamps).

The trial still succeeds as evidence if the transport itself misbehaves, provided the mission halted cleanly and recorded honestly; what it must not do is continue past an unanswered Tier 3 decision.

## Data Minimization
Interrupt records store the question, options, answer, timestamps, and transport name. They do not store device identifiers, phone numbers, vendor account identifiers, message-platform metadata beyond the transport name, or any credential material.

## Named Follow-ups (Not Approved Here)
- The sponsor approval record for the trial itself (transport, mission, window, human).
- A harness capability profile observation for the chosen transport after the trial.
- Repeat trial under the 2-hour ladder rung once `DURATION_LADDER_PLAN.md` reaches that rung.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
