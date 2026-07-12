# Factory V3 Fresh-Worker Reentry Trial Plan

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Distinguished deterministic mission-control re-entry decision fixtures from this unexecuted live artifact-sufficiency trial. Fixture `fresh_session` inputs are not operational proof.
- v0.1 (2026-06-11): Initial trial plan from the backlog research spike: make artifact sufficiency falsifiable via a sealed answer key and a cross-harness fresh worker.

## Status
Research-only and non-enforcing plan. Executing this trial is not approved by this document.

The deterministic re-entry cases under `tests/fixtures/factory_v3_mission_control_contract/` validate decision semantics only. They do not prove that a real worker lacked prior-session memory, reconstructed the mission from authored artifacts, or completed a safe continuation. This trial remains necessary for those operational claims.

The trial runs only after the duration-ladder rung 2 completes, under its own mission envelope and explicit sponsor Go naming the mission, both harnesses, and the date window. This document does not approve unattended operation, scheduled wakes, concurrent multi-worker execution, credential use, live transport use, required gates, governance routing, or runtime-control power.

## Purpose
The candidate `V3-OP-003` profile requires that continuation decisions come from authored artifacts, never from chat memory. POC Missions 012 and 013 produced fresh-session resumes from authored artifacts only, but those resumes were judged informally and ran on the same harness that paused the mission. This trial makes artifact sufficiency falsifiable: a worker with no access to the prior session's memory must reconstruct the mission from authored artifacts alone, and its reconstruction is scored against a record written before the pause.

The strongest form is cross-harness — the mission pauses under one harness and resumes under another (for example Codex pauses, Claude Code resumes) — because it removes every channel except the authored artifacts and directly exercises `MUTABLE_HARNESS_STATE.md` at the harness level. The ladder itself became cross-harness via sponsor decision `HDI-RUNG2-001`, so this evidence also serves rung-to-rung comparability.

## What Is New Versus Normal Checkpoint/Reentry
Normal reentry (per `ADAPTIVE_MISSION_CONTROL.md` and the stale-reentry discipline) assumes the same worker resumes with the sponsor in-thread; sufficiency of the artifacts is asserted, not tested. This trial differs in three ways:

1. The resuming worker has no session continuity with the pausing worker, and in the cross-harness form, not even the same harness.
2. Sufficiency is scored against a sealed answer key authored at pause time, not judged after the fact.
3. The handoff must travel entirely through the normal authored artifact set — if the pausing worker needs to write a special handoff letter beyond its ordinary envelope, mission state, and checkpoints, the checkpoint discipline has failed, and that failure is the finding.

The profile's serial-one-worker constraint is preserved: this is a sequential handoff, never concurrent execution.

## Trial Protocol
1. Pause leg: a mission (synthetic or a designated waypoint mission) pauses at a planned checkpoint. As part of that ordinary checkpoint, the pausing worker authors the answer key (see below) and commits per the mission's git authority.
2. Handoff: the fresh worker starts in a new session with the standing reentry instruction only: resume mission X per its reentry rule.
3. Reentry brief: before any edit, the fresh worker authors a reentry brief from allowed inputs alone, stating its reconstruction of the answer-key fields.
4. Comparison: brief versus answer key, field by field, recorded verbatim.
5. Continuation: the fresh worker completes at least one waypoint under the original envelope, with normal checkpoint and verification discipline.
6. Closeout: mission record naming both workers' harness and model identities per `MUTABLE_HARNESS_STATE.md`.

## Answer Key
Authored at pause time inside the normal checkpoint discipline, containing: current waypoint, next planned action, open interrupts and pending decisions, active authorized scope, and budget state. Sealing is procedural, not cryptographic: the key lives in a named file the reentry instruction directs the fresh worker not to open until its brief is committed, and the brief-before-key ordering is verified from git history. This designed limitation is acceptable for a research trial and is recorded as such.

## Allowed Inputs (Fresh Worker)
- The mission envelope, mission-state file, checkpoint series, and interrupt records.
- Git history, diffs, and repository content.
- Factory V3 canon documents.
- The standing reentry instruction naming the mission.

## Forbidden Inputs (Fresh Worker)
- The prior session's transcript, chat memory, or summaries of either.
- Any sponsor briefing beyond the standing reentry instruction.
- Any handoff artifact authored specially for the trial outside the normal artifact set.
- The answer key, until the reentry brief is committed.

## Pass Criteria
- The reentry brief matches the answer key on current waypoint, next action, open interrupts, and active scope; budget-state mismatches are findings but not automatic failures if the brief's value is derivable from the artifacts.
- The fresh worker completes at least one waypoint with verification passing and no scope violation.
- No question is raised to the sponsor that the authored artifacts already answer.

## Fail Criteria
- Wrong next action or wrong current waypoint in the brief.
- Re-asking a decision an interrupt record already answers.
- Scope drift at resume, or use of a forbidden input.
- The pause leg requiring a special handoff artifact to make the resume possible.

## Evidence Requirements
- The committed answer key and its pause checkpoint.
- The committed reentry brief, with git evidence of brief-before-key ordering.
- The field-by-field comparison.
- Both workers' harness and model identities.
- Closeout mission record per `MISSION_RECORD_DESIGN_V0.md`; a failed trial is evidence, not embarrassment, and is recorded with findings classified.

## Sequencing
After rung 2, before or alongside rung 3, at sponsor discretion. Rung 2's own pause/reentry leg proceeds unchanged — folding this trial into rung 2 would confound the rung's already-stacked new variables (new harness, doubled duration, live phone interrupt). Rung 2's reentry evidence informs what the answer key must contain.

## Named Follow-ups (Not Approved Here)
- The trial's own mission envelope and sponsor Go.
- A harness capability profile observation for the resuming harness.
- If the trial passes, a `reentry_request` shadow-candidate refinement using the answer-key fields.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
