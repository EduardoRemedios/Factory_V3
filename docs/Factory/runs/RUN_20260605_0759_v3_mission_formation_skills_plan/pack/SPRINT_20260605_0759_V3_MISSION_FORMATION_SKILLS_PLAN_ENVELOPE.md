# Sprint Envelope - V3 Mission Formation Skills Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial Stage H envelope.

## Sprint ID
`SPRINT_20260605_0759_V3_MISSION_FORMATION_SKILLS_PLAN`

## Execution Mode
PLANNING_ONLY

## Objective
Prepare a human-reviewable pack for a future bounded implementation run that designs, creates, trials, and reviews non-executing Factory V3 mission-formation skills.

## Authorized Future Implementation Files
For the future implementation run only, candidate target paths are:
- `.agents/skills/factory-mission-formation/SKILL.md`
- `.agents/skills/factory-challenge-mission/SKILL.md`
- optional `.agents/skills/*/agents/openai.yaml` only if kept non-authoritative
- future trial/evidence docs under a path explicitly approved by that run

This planning run does not authorize editing those files.

## Forbidden Scope
- No code edits or skill implementation in this run.
- No Codex SDK, Codex MCP, Agents SDK, or automation implementation.
- No new V3 operational profile.
- No non-coding execution approval.
- No runtime authority, production action, deployment, credential handling, proof, lease enforcement, telemetry enforcement, required gates, governance routing, default-mode promotion, or V2 scaffolding removal.

## File-Touch Budget
- This planning run: one run root under `docs/Factory/runs/RUN_20260605_0759_v3_mission_formation_skills_plan/`.
- Future implementation run: expected maximum 2 skill directories plus bounded trial evidence and review docs, to be named by that future envelope.

## Verification
Required before human review:
- `./scripts/factoryctl stage-lint --run RUN_20260605_0759_v3_mission_formation_skills_plan --stage <A|B|C|D|E|F|G|H|I|J|I2>`
- `./scripts/factoryctl pack-lint --run RUN_20260605_0759_v3_mission_formation_skills_plan`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`

## SIMPLE-CODE-GATE
Future skill implementation must apply SIMPLE-CODE-GATE by keeping skills instruction-only first, avoiding dependency creep, and avoiding speculative helper scripts unless trial evidence proves a deterministic need.

## Halt Rules
Halt if:
- any future skill text grants execution authority,
- SDK/MCP implementation appears,
- V2 fallback is weakened,
- V3 promotion or default-mode language appears,
- verification fails and cannot be repaired inside scope.

## Human Go Rule
This pack authorizes no implementation. A future skill implementation requires separate human Go naming the target files and verification commands.
