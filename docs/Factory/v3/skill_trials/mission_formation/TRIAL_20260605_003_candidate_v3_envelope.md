# Trial 003 - Candidate V3 Envelope Route

## Status
Research-only dry run. No execution authority.

## Input Brief
Create a short docs note under `docs/Factory/v3/` explaining that mission-formation skills are research-only, and run the V3 advisory lint.

## Skill Used
`factory-mission-formation`

## Route
`CANDIDATE_V3_ENVELOPE`

## Problem Statement
The repository needs a small documentation note that reinforces the research-only status of mission-formation skills.

## Desired Outcome
A concise docs note exists and V3 advisory lint passes.

## Candidate Mission Contract
- Objective: Add a short research-only note for mission-formation skills.
- Success criteria: note is present, concise, and does not imply profile promotion or execution authority.
- Authorized scope: one new markdown file under `docs/Factory/v3/`.
- Forbidden scope: no skill implementation, no SDK/MCP work, no required gates, no runtime authority, no V2 removal.
- Allowed commands: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`.
- Dependency policy: no dependencies.
- Verification: V3 advisory lint passes.
- Halt rules: halt on advisory finding that suggests promotion, default mode, authority, or V2 deprecation drift.
- Fallback rules: route to V2/heavier planning if scope expands beyond a single docs note.

## Challenge Summary
`factory-challenge-mission` would likely return `CONDITIONAL PASS`: the task is bounded enough for a candidate V3 envelope, but execution still requires explicit human approval.

This is candidate mission-formation output only. It does not authorize execution until the human explicitly approves the mission contract.
