# Intent - V3 Mission Formation Skills Plan

## Version
v0.2

## Change Log
- v0.2 (2026-06-05): Incorporated Red/Blue hardening for skill split, trial evidence, and SDK boundary.
- v0.1 (2026-06-05): Initial Stage A intent.

## Purpose
Create a planning-only Factory pack for the future design and implementation of non-executing Factory V3 mission-formation skills.

## Goal
Define the future work needed to create and trial one or more skills that help Codex perform Socratic discovery, challenge assumptions, and produce candidate mission contracts before long-running V3 execution.

## Source Requirements
- R1 [SOURCE: `docs/Factory/v3/MISSION_FORMATION_DIRECTION.md`] Mission quality determines autonomy quality; discovery and challenge must not create execution authority.
- R2 [SOURCE: `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`] Phase 4.5 is planned for non-executing mission-formation and challenge skills with trial evidence before recommendation.
- R3 [SOURCE: `docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md`] Codex SDK/MCP orchestration is follow-on research after skill trials; Codex remains a worker under Factory/Harmony authority.
- R4 [SOURCE: `AGENTS.md`] Preserve V3 advisory-only semantics and do not add runtime authority, required gates, governance routing, telemetry enforcement, or V2 deprecation.

## Principles
- Design skills before automation.
- Keep discovery and challenge non-executing.
- Treat skill output as evidence, not approval.
- Preserve V2 fallback for ambiguous, risky, or broad work.
- Prefer instruction-only skills first; add scripts only if evidence shows deterministic support is needed.
- Keep implementation targets small and repo-scoped.

## Roles
- Root Planner: create and validate this planning pack.
- Skill Designer: future implementer of the skill instructions.
- Trial Operator: runs three representative skill trials.
- Purple Reviewer: adjudicates whether skill output improves mission quality without authority drift.

## Acceptance Criteria
- The pack names exact future skill-design outputs and trial evidence.
- The pack decides whether to start with one skill or two, or defines a decision gate for that choice.
- The pack defines future target paths, verification commands, and no-go boundaries.
- The pack explicitly blocks execution authority, SDK/MCP orchestration implementation, new V3 profiles, required gates, runtime authority, production actions, and V2 scaffolding removal.
- The pack passes stage-lint and pack-lint.

## Recommended Future Scope
Create two repo-scoped instruction-only skills:
- `.agents/skills/factory-mission-formation/SKILL.md`
- `.agents/skills/factory-challenge-mission/SKILL.md`

The future implementation run may adjust names only if it records the reason and keeps the same non-authority contract.

## Non-Goals
- No skill implementation in this planning run.
- No Codex SDK, Codex MCP, or Agents SDK implementation.
- No runtime authority, proof, lease enforcement, telemetry enforcement, governance routing, required gates, default-mode promotion, production actions, deployment, credential handling, or V2 removal.
- No claim that mission-formation skills are operationally recommended before trial evidence exists.

## Open Questions
### BLOCKING
- None for this planning pack.

### NON-BLOCKING
- Whether the future skill implementation should include optional `agents/openai.yaml` metadata can be decided during implementation if kept non-authoritative.

## Go Or No-Go Rule
Go for future implementation only after this pack passes I2 and the human explicitly approves a separate skill-implementation run. No implementation is authorized by this planning pack alone.
