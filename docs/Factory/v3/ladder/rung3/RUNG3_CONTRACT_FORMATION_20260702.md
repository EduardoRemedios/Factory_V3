# Rung 3 Contract Formation - 2026-07-02

## Status
Research-only, non-executing formation output.

This artifact does not approve rung-3 execution, `V3-OP-003` promotion, default V3 use, runtime authority, scheduled or unattended execution, real-data use, live integrations, deployment, required gates, governance routing, or Factory V2 removal.

## Source Evidence
- `docs/Factory/v3/ladder/LADDER_STATUS.md` v1.2
- `docs/Factory/v3/DURATION_LADDER_PLAN.md` v0.10
- `docs/Factory/v3/V3_OP_003_DECISION_PACK.md` v0.5
- `docs/Factory/v3/CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md` v0.1
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md` v0.2
- `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md` v0.1
- `.agents/skills/factory-mission-formation/SKILL.md`
- `.agents/skills/factory-challenge-mission/SKILL.md`

## Mission Formation Result

### Route
`CHALLENGE_NEEDED`

The rung-3 lane is ready for non-executing contract formation and challenge. It is not ready for execution because the concrete POC build objective, waypoint table, and sponsor-selected scope have not been named in this repository.

### Problem Statement
Factory V3 needs a rung-3-class mission contract that can test whether the candidate `V3-OP-003` long-running remote-interrupt profile can govern a roughly four-hour attended mission without drift, unsafe continuation, stale re-entry, or weak evidence.

### Desired Outcome
A future rung-3 execution envelope is prepared from a reviewed contract, with enough specificity that sponsor Go can be requested against explicit scope, authority, budget, verification, interrupt, safe-hold, and closeout rules.

### Non-Goals
- Do not execute rung 3 from this artifact.
- Do not promote `V3-OP-003`.
- Do not approve real data, live Garmin, live Telegram, public deployment, production infrastructure, credentials, scheduled work, or unattended work.
- Do not use V2 to govern the standalone POC execution if a later POC mission is approved.
- Do not seed a negative case and label it natural.
- Do not pad work only to satisfy time or call targets.

### Assumptions
- Rung 2 attempt 4 is the current calibration point: 95.25 active minutes, about 548 calls, 31 waypoints, restored browser QA, and one real UI defect plus QA-script defects found and fixed.
- Rung 3 should use the class from `DURATION_LADDER_PLAN.md`: floor 1100 observed calls, forecast band 1100-1700, stop threshold 2000, 200-300 minute wall-clock band, and bottom-up scope sufficiency.
- Browser availability must be a Go-blocking pre-flight check because rung-2 evidence showed missing browser workload materially shortened earlier attempts.
- Vendor session limits are mutable harness state and should be absorbed by pause/re-entry rather than treated as mission failure if the envelope allows it.
- Sponsor response latency is neutral telemetry. The safe-hold trigger controls agent posture; an answer is not "late" when it arrives after the trigger.

### Unknowns
- The concrete POC build objective and feature epics for rung 3.
- Whether the POC repository has enough valuable synthetic-first work remaining to support a 1100-1700 call class without artificial padding.
- Whether browser tooling, Codex mobile interrupt surface, and any required local server/browser surfaces are available at session start.
- Exact allowed git policy for the POC repo during a future rung-3 mission.
- Whether a natural halt, fallback, clarification, or failed-verification event will occur at duration.

### Options

| Option | Description | Value | Risk | Formation verdict |
| --- | --- | --- | --- | --- |
| A | Build a single large POC feature tranche with multiple epics, full browser QA, replay/evidence upgrades, and documentation closeout. | Best chance of genuine duration and realistic verification depth. | May over-broaden scope unless epics are tightly bounded. | Preferred if sponsor can name valuable synthetic-first scope. |
| B | Run a governance-suite hardening mission in the POC repo focused on tests, verifiers, replay, and negative-path evidence. | Strong evidence alignment and lower product risk. | Could become too synthetic and miss real feature-work pressure. | Good fallback if product feature scope is weak. |
| C | Defer rung 3 and first run Factory_V3-native negative-case captures. | Closes open Factory_V3 corpus gaps before another long run. | Does not progress `V3-OP-003` duration evidence. | Valid if no useful POC rung-3 scope exists. |

### Recommended Route
Choose Option A only if the sponsor can name a valuable synthetic-first POC scope with at least four epics and a bottom-up waypoint table that reaches the 1100-call floor without padding. Otherwise choose Option B or defer to Option C.

## Human Decisions Needed
1. Select the future rung-3 objective: Option A, B, C, or a sponsor-provided alternative.
2. Confirm the future mission repository and branch policy.
3. Confirm whether browser pre-flight is Go-blocking and what evidence proves browser availability.
4. Confirm the approved interrupt surface and safe-hold trigger window.
5. Confirm allowed git commands, checkpoint commit cadence, and push policy.
6. Confirm whether any real-data, live integration, credential, deployment, or public-exposure scope is excluded, as expected.

## Pre-Resolved Decisions
- `V3-OP-003` is candidate-only and cannot govern a mission until promoted.
- Rung-3 execution requires a separate envelope and explicit sponsor Go.
- Factory V2 fallback and non-deprecation language remain intact.
- The future rung must use authored artifacts for re-entry, not chat memory.
- A natural negative case may be recorded if it happens, but it must not be seeded and relabeled.
- Safe-hold is the correct posture for missing authority, stale state, failed verification without recovery authority, unsafe action, or unresolved Tier 3 decisions.

## Verification And Evidence Needs
- Bottom-up waypoint table with source coefficients and forecast.
- Browser pre-flight record.
- Interrupt field set v2 record for any Tier 3 interrupt.
- Mission state and checkpoint series with command-sourced timestamps.
- Mission-health signals at each checkpoint, with recording cost.
- Tool-call and command evidence, including omitted-tool rationale where relevant.
- Verification evidence per waypoint and final regression/no-touch checks.
- Claim-to-proof mapping at closeout.
- FP/FN review after rung 3 before any promotion decision.

## Candidate Mission Contract

### Objective
Prepare, and later only if separately approved execute, a rung-3-class synthetic-first POC mission that tests `V3-OP-003` long-running remote-interrupt governance at roughly four-hour scale.

### Success Criteria
- The execution envelope names a concrete POC objective, waypoint table, authorized files, forbidden scope, allowed commands, verification plan, interrupt rules, safe-hold rules, and re-entry protocol.
- Bottom-up forecast reaches the rung-3 floor without padding: at least 1100 observed-call class, forecast band 1100-1700, stop threshold 2000.
- Browser pre-flight, interrupt surface, git policy, and checkpoint cadence are explicit before Go.
- The challenge pass returns `PASS` or `CONDITIONAL PASS` for execution readiness after concrete scope is named.

### Authorized Scope For Formation
- Factory_V3 docs under `docs/Factory/v3/ladder/rung3/`.
- Advisory references to existing Factory_V3 ladder, loop-governance, mission-formation, and challenge artifacts.

### Forbidden Scope For Formation
- POC repo edits.
- Rung-3 execution.
- Real data, credentials, deployment, live integrations, scheduled work, unattended work, runtime authority, required gates, or V2 removal.

### Allowed Commands For Formation
- Read-only file inspection.
- Advisory lint/eval commands already approved for Factory_V3 docs.
- `python3 scripts/factory_v3_loop_contract_lint.py --target docs/Factory/v3/ladder/rung3/RUNG3_LOOP_CONTRACT_CANDIDATE_20260702.json --json`

### Dependency Policy
No new dependencies.

### Budget And Checkpoint Rules For Future Execution
- Budget forecast must be bottom-up from waypoint and evidence-artifact costs.
- Stop threshold: 2000 observed calls unless the future envelope explicitly revises with evidence and sponsor approval.
- Checkpoints at each waypoint boundary, before risky transitions, before/after Tier 3 interrupts, before/after pause/re-entry, and at budget risk thresholds.
- Command-sourced timestamps required where available; model-estimated minutes are not measurements.

### Human Interrupt Rules
- Tier 1 decisions must be pre-resolved in the future envelope.
- Tier 2 decisions may be resolved and logged only when they do not expand authority or weaken boundaries.
- Tier 3 interrupts are required for missing authority, privacy/safety boundary, dependency/credential choice, deployment, failed-verification recovery outside envelope, or contradictory scope.
- Safe-hold trigger records agent posture only. Sponsor answer latency is neutral telemetry.

### Halt And Fallback Rules
- Halt or safe-hold on failed verification unless recovery is explicitly authorized.
- Safe-hold on stale re-entry, missing state, contradictory evidence, unavailable browser pre-flight, failed interrupt delivery with a pending Tier 3 decision, or budget stop threshold.
- Fall back to V2/heavier planning for broad, ambiguous, unsafe, production, credential, infrastructure, or governance-kernel scope.

### Re-Entry Instructions
A future worker may re-enter only after reading the execution envelope, latest checkpoint, mission state, open decisions, verification evidence, and current repo state. If any authored state is stale, contradictory, missing, or invalidated, the worker must safe-hold rather than continue.

## Recommended Next Step
Ask the sponsor to select the future rung-3 objective and approve a concrete envelope-authoring step. Do not ask for rung-3 execution Go until the concrete scope, waypoint table, bottom-up budget derivation, browser pre-flight, interrupt surface, git policy, and verification plan are all written and challenged.

This is candidate mission-formation output only. It does not authorize execution until the human explicitly approves the mission contract.

