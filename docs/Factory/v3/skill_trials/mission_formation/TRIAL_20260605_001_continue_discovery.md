# Trial 001 - Continue Discovery Route

## Status
Research-only dry run. No execution authority.

## Input Brief
I want Harmony to manage overnight AI builds end to end. What am I missing?

## Skill Used
`factory-mission-formation`

## Route
`DISCOVERY_NEEDED`

## Mission Formation Result
The idea is directionally aligned with Factory V3, but it is not ready for an execution envelope because the authority model, worker boundaries, interruption path, and verification model are still unresolved.

## Key Questions
- Which mission classes should Harmony supervise first: coding, integration adapters, discovery, QA, or deployment?
- What can Harmony decide itself, and what always requires human approval?
- What is the first acceptable overnight failure mode?
- What evidence must exist before a human trusts a completed run?
- Which actions are explicitly forbidden during unattended work?

## Assumptions
- Harmony remains the authority layer.
- Codex is a worker runtime, not the governance brain.
- Long-running work must preserve checkpoint, halt, and reentry evidence.

## Unknowns
- Worker orchestration substrate.
- Human interrupt surface.
- Budget and rate-limit policy.
- First non-production trial scope.

## Recommended Next Step
Continue discovery and challenge before creating an execution mission.

## Candidate Mission Contract
Not ready. Missing authority, first profile, evidence, and halt-policy decisions.

This is candidate mission-formation output only. It does not authorize execution until the human explicitly approves the mission contract.
