# Micro-sprints - V3 Mission Formation Skills Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial Stage G micro-sprint sequence.

## MS-01 - Skill Contract Design
- Objective: Define trigger descriptions, non-trigger boundaries, non-authority rules, and required outputs.
- Inputs: `MISSION_FORMATION_DIRECTION.md`, roadmap Phase 4.5, this pack.
- Outputs: future skill design note and implementation checklist.
- Entry criteria: human Go for future implementation.
- Exit criteria: contracts cover discovery, challenge, candidate mission envelope, fallback route, and human approval.
- Stop or go gate: stop if any wording grants execution authority.

## MS-02 - Skill Implementation
- Objective: Create instruction-only repo-scoped skills.
- Inputs: MS-01 design.
- Outputs: `.agents/skills/factory-mission-formation/SKILL.md` and `.agents/skills/factory-challenge-mission/SKILL.md`, unless a documented implementation decision keeps one skill.
- Entry criteria: MS-01 complete.
- Exit criteria: skill frontmatter exists, descriptions are precise, and instructions prohibit edits/execution authority.
- Stop or go gate: stop if scripts or dependencies are proposed without new approval.

## MS-03 - Trial Evidence
- Objective: Run at least three skill trials and record outcomes.
- Inputs: implemented skills.
- Outputs: trial records under an approved evidence path.
- Entry criteria: skills exist and can be invoked.
- Exit criteria: one more-discovery route, one V2/heavier-planning route, and one bounded candidate V3 route recorded.
- Stop or go gate: stop if skill output is treated as approval.

## MS-04 - Review And Recommendation
- Objective: Decide whether the skills should be kept, revised, split/merged, paused, or recommended as V3 intake aids.
- Inputs: trial records and before/after comparison.
- Outputs: skill evidence review.
- Entry criteria: MS-03 complete.
- Exit criteria: authority-boundary review, false-confidence review, V2 fallback review, and recommendation recorded.
- Stop or go gate: no recommendation if trial evidence is incomplete.

## Bounded Deferral Hook
Codex SDK/MCP orchestration is deferred until after MS-04 and requires a separate research pack.
