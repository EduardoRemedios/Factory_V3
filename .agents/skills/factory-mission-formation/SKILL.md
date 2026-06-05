---
name: factory-mission-formation
description: Use when turning a vague idea, product direction, long-running build request, overnight Codex goal, or "what am I missing" prompt into a non-executing Factory V3 discovery output, option set, execution-readiness assessment, and candidate mission contract. Do not use for already-bounded code changes that can proceed directly under an approved execution envelope.
---

# Factory Mission Formation

## Status
Non-executing Factory V3 intake skill. This skill does not grant execution authority, approve a V3 profile, approve non-coding execution, or replace human approval.

## Core Rule
Discovery is autonomy preparation.

Use this skill to improve mission quality before implementation. Do not edit files, run implementation commands, create production effects, or treat conversation as approval authority.

## Source Context
When working in this repository, align with:
- `docs/Factory/v3/MISSION_FORMATION_DIRECTION.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` Phase 4.5
- `docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md` for SDK/MCP boundaries

Load these only when the task needs repository-grounded V3 direction.

## Trigger
Use this skill when the user asks to:
- turn an idea into a mission,
- prepare a long-running or overnight Codex build,
- ask what they are missing,
- explore whether something should be built,
- create a mission envelope from vague intent,
- run discovery before execution,
- compare solution paths before implementation.

Do not use this skill when:
- the request is already a narrow code change with named files, allowed commands, and verification,
- the user explicitly asks only for implementation,
- a Factory pack or mission envelope already grants execution authority for the current work.

## Workflow
1. Restate the candidate mission in one sentence.
2. Classify the request as `DISCOVERY_NEEDED`, `CHALLENGE_NEEDED`, `V2_OR_HEAVY_PLANNING`, or `CANDIDATE_V3_ENVELOPE`.
3. Ask only high-value Socratic questions that would change the mission contract, route, budget, risk, or verification plan.
4. Identify assumptions, unknowns, constraints, stakeholders, non-goals, and decision points.
5. Generate 2-3 viable paths when more than one path is plausible.
6. Compare paths by value, risk, complexity, reversibility, verification, and authority needs.
7. Recommend a route and state why.
8. Produce a candidate mission contract only when enough information exists.
9. Mark any candidate contract as non-authoritative until human approval.

## Decision Tiers
- Tier 1: Pre-resolved by the user's prompt or existing mission envelope.
- Tier 2: Resolve-and-log using stated principles when the choice does not expand authority or weaken boundaries.
- Tier 3: Human decision required for scope, safety, privacy, credentials, deployment, irreversible action, dependency choice, failed-verification recovery, or authority gaps.

## Output Shape
Use concise headings:

```text
Mission Formation Result
Route
Problem Statement
Desired Outcome
Non-Goals
Assumptions
Unknowns
Options
Risks
Human Decisions Needed
Pre-Resolved Decisions
Verification And Evidence Needs
Recommended Next Step
Candidate Mission Contract
```

If no candidate contract is ready, say so clearly and explain the missing decisions.

## Candidate Mission Contract
When ready, include:
- objective,
- success criteria,
- authorized scope,
- forbidden scope,
- allowed tools and commands,
- dependency policy,
- verification requirements,
- budget and checkpoint rules,
- human interrupt rules,
- halt and fallback rules,
- reentry instructions.

End with:

```text
This is candidate mission-formation output only. It does not authorize execution until the human explicitly approves the mission contract.
```

## Guardrails
- Prefer fewer, better questions over exhaustive interviews.
- Do not ask questions that ordinary implementation judgment can resolve inside existing authority.
- Do not overfit to coding; mission formation can route strategy, product, or discovery work to heavier planning.
- Preserve V2 fallback for broad, ambiguous, high-risk, or unsuitable work.
- Treat Codex SDK/MCP orchestration as follow-on research unless separately approved.
