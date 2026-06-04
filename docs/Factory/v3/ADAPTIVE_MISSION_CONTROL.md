# V3 Adaptive Mission Control

## Version
v0.2

## Change Log
- v0.2 (2026-06-04): Added command-sourced timestamp budget discipline and three decision tiers so human interrupts remain exceptional.
- v0.1 (2026-06-03): Initial adaptive mission control protocol with checkpoints, human decision interrupts, plan deltas, and reentry state.

## Status
Research-only and non-enforcing. This document does not make V3 the default, approve required gates, approve live Telegram automation, approve unattended production work, deprecate V2, or authorize runtime authority.

## Purpose
Define how a V3 mission can run longer without relying on artificial time or size targets.

V3 should not force a mission to be large because of a size class. Mission size should emerge from the objective, implementation facts, verification requirements, and human-approved constraints.

Long-running V3 work should be governed by:
- mission clarity,
- budget and checkpoint discipline,
- replayable evidence,
- human decision interrupts,
- plan deltas,
- halt and reentry rules.

## Core Principle
Use time as an operational guardrail, not as the mission sizing primitive.

Codex can track explicit artifacts better than elapsed time. V3 missions should therefore make continuation decisions from authored evidence:
- current objective,
- current phase,
- files changed,
- commands run,
- verification status,
- unresolved risks,
- budget state,
- pending human decisions.

## Adaptive Mission Control Loop
For larger missions, V3 should operate in this loop:

1. Read mission envelope and current mission state.
2. Execute the next bounded phase.
3. Record a checkpoint.
4. Run the phase verification or evidence check.
5. Continue if scope, budget, and verification remain valid.
6. Ask for human input if ambiguity, authority, product decision, or risk boundary appears.
7. Record the human answer as an interrupt and, if needed, a plan delta.
8. Halt if the answer is missing, ambiguous, unsafe, or outside mission authority.

## Budget And Timing Discipline
Budget state should be measured from command-sourced evidence where possible.

At each checkpoint, record:
- `checkpoint_recorded_at` from `date -u +%Y-%m-%dT%H:%M:%SZ`,
- elapsed time since the previous checkpoint, derived from checkpoint timestamps or git commit times,
- tool-call count since the previous checkpoint or mission start,
- qualitative context and buffer concerns,
- whether a stop threshold has been reached,
- rate-limit window notes when relevant.

Do not record model-estimated minutes as measurements. Forecasts may be recorded only when clearly labeled as forecasts. Mission 012 and Mission 013 POC evidence showed checkpoint-estimated minutes inflated real elapsed time by roughly 6-9x, while tool-call counts were the more useful self-reported size metric.

Duration bands may remain observational guardrails, but they must not become mission size classes. Mission size still emerges from objective, scope, implementation facts, verification requirements, budget, and evidence.

Rate-limit window awareness is operational context, not a required gate. The current sponsor target is an interim, tunable parameter: aim to fit a roughly 4-hour run inside a roughly 5-hour plan window when designing long-running work. If throttling, exhaustion, or context risk prevents clean continuation, record a checkpoint, commit if authorized, halt cleanly, and include a reentry instruction.

## Decision Tiers
Human interrupts should be the exception, not the default. Missions should use the lowest decision tier that preserves authority and safety.

Tier 1 Pre-Resolved Decisions are questions answered by the sponsor in the mission envelope before execution. The envelope should enumerate the decision, answer, source, and date so the mission can proceed without re-asking.

Tier 2 Resolve-and-Log decisions use envelope-stated decision principles to decide within mission authority. The mission records the choice in a deferred-decisions log for closeout review. Tier 2 is appropriate for wording, ordering, synchronization, or implementation-detail choices that do not expand scope or weaken boundaries.

Tier 3 Human Decision Interrupts are reserved for decisions involving missing authority, safety or privacy boundaries, irreversible actions, dependency or credential choices, deployment authority, failed-verification recovery outside the envelope, or contradictions inside the envelope. If possible, continue parallel authorized work while the answer is pending. If the mission becomes blocked, checkpoint, commit if authorized, and halt cleanly with reentry instructions.

## Human Decision Interrupts
A human decision interrupt is a structured request for human input during a mission.

Use it when the mission encounters:
- product ambiguity,
- scope expansion,
- missing authority,
- dependency decision,
- safety or privacy boundary,
- failed verification recovery choice,
- user-experience choice,
- budget/context risk,
- deployment or credential decision.

Before asking, check whether Tier 1 or Tier 2 already answers the decision. Do not use a human decision interrupt for ordinary implementation judgment that remains within mission authority.

## Interrupt Record
Each interrupt should record:
- interrupt ID,
- mission ID,
- decision tier,
- pre-resolution check,
- question,
- reason,
- decision type,
- options,
- recommended option,
- risk of each major option,
- timeout behavior,
- answer source,
- answer,
- answer interpretation,
- plan delta,
- continuation decision.

## Telegram Bridge Boundary
Telegram is a candidate human interrupt surface, not a required V3 dependency.

Phased path:
1. File/thread-based simulated interrupts.
2. Telegram bridge research.
3. Approved Telegram bridge implementation with allowlisted user identity, token handling, timeout behavior, and replay logs.
4. Long-running mission trial using the bridge.

Until separately approved:
- do not create a Telegram bot,
- do not use a Telegram token,
- do not poll or webhook Telegram,
- do not send live Telegram messages from V3.

## Checkpoints
Longer missions should record checkpoints at natural phase boundaries and before risky transitions.

A checkpoint should include:
- current phase,
- objective progress,
- files changed,
- commands run,
- verification status,
- budget state,
- open risks,
- pending decisions,
- next planned action,
- reentry instruction.

Checkpoint cadence should be chosen by the mission. It may be based on phases, test gates, file groups, or budget thresholds. Do not require checkpoints only by elapsed time.

## Mission State
Larger missions should keep an authored mission-state file.

The mission state is not hidden agent memory. It is replayable evidence and should include:
- current phase,
- last checkpoint,
- active plan,
- completed phases,
- pending phases,
- open interrupts,
- accepted plan deltas,
- next action,
- halt status.

## Plan Deltas
When a human answer changes the mission, record a plan delta before continuing.

A plan delta should state:
- what changed,
- why it changed,
- which human answer authorized it,
- newly authorized files/commands if any,
- newly forbidden scope if any,
- verification impact,
- whether the mission can continue or must halt for a new mission.

## Read-Only Verification Rule
Verification commands should be read-only by default.

If verification generates or updates evidence, the mission must declare:
- output path,
- whether overwriting tracked evidence is allowed,
- how the result is reviewed,
- how to avoid hiding drift.

## Git Authority
Git operations are mission authority.

If a mission may initialize git, commit, push, or change remotes, the mission envelope must explicitly authorize:
- allowed git commands,
- remote policy,
- commit cadence,
- commit message policy,
- push policy,
- checkpoint relationship,
- `commit_before` and `commit_after` evidence.

## Completion Rule
Complete the mission when the objective is satisfied and verification evidence passes. Do not pad files, fixtures, tests, or phases to satisfy a size target.

If the mission becomes too broad, halt and create a plan delta or successor mission.
