# Factory V3

**Factory V3 is an operating system for supervised AI workers.**

Humans define missions, constraints, budgets, verification requirements, and approval rules. Autonomous AI workers execute over longer horizons under bounded authority, continuous verification, replayable evidence, escalation rules, and human supervision at key checkpoints. This repository is the experimental and operational-evidence track for that model of governed autonomous execution.

## Why Coding First

Coding is the first concrete proving ground for this model because software work produces reviewable evidence: diffs, commands, tests, failures, and closeout records. The broader target is knowledge work and engineering missions where autonomous actors need to operate safely under controlled supervision, but non-coding profiles require separate evidence, governance review, and explicit approval before use.

## Direction

The current strategic direction is broader than coding automation alone. V3 is moving toward AI-assisted mission formation plus governed autonomous mission execution: discovery and challenge reduce uncertainty before a mission becomes executable, and Codex can later be treated as a bounded worker runtime under Factory/Harmony authority rather than as the governance brain.

## Approval Status

That is the product vision, not the current operational approval. Today this repository approves only optional `V3-OP-001 Bounded Code Change` use; everything else is research-only and non-enforcing, and Factory V2 remains the governing default and required fallback. The full, binding statement of what is and is not approved lives in [docs/Factory/v3/GOVERNANCE_BOUNDARIES.md](docs/Factory/v3/GOVERNANCE_BOUNDARIES.md).

## Relationship To Factory V2

This repository was split out of `factory-starter-kit` so V3 can evolve independently from Factory V2 and earlier content.

Factory V3 development in this repository can use Factory V2 process semantics while V3 is still maturing. The V2 docs, templates, and scripts are included as temporary build-support scaffolding so V3 can be built with the same planning, lint, pack, verification, and SIMPLE-CODE-GATE discipline that governed the earlier V3 evidence.

This does not make V3 dependent on V2 as a product. The intended direction is for this repository to become V3-only once V3 is built, confidence-backed, and explicitly approved. V2 remains preserved in the separate V2-only repository.

## Current Scope

- Optional `V3-OP-001 Bounded Code Change` guidance and evidence.
- V3 mission-envelope, closeout, fallback, SIMPLE-CODE-GATE, and mission-record templates.
- V3 advisory validators and deterministic fixtures.
- V3 advisory telemetry replay evidence, including three real Phase 3 pilot logs and an evidence review that conditionally recommends optional advisory telemetry for selected narrow evidence missions.
- V3 Phase 4 eval expansion plan, harness capability profile template, synthetic operational-readiness fixture expansion, real-run corpus and harness-profile indexes, three happy-path docs-only real-run corpus records, five negative-case capture records, and a research-only negative-case opportunity register.
- V3 research-only dynamic/parallel workflow harness planning with `insufficient_evidence` status, including Claude Code as an external-announcement signal and Codex as an official-docs source signal.
- V3 operational-readiness, trial, and decision evidence.
- V3 standalone bootstrap package for seeding a clean V3-only POC project.
- V3 research-only adaptive mission control guidance and templates for checkpoints, human decision interrupts, plan deltas, mission state, and replayable long-running mission evidence.
- V3 research-only mission-formation and challenge direction, initial repo-scoped non-executing skills, and dry-run trial evidence for improving mission quality before long-running execution.
- V3 research-only Codex SDK/MCP orchestration direction for treating Codex as a governed worker runtime in possible future Factory/Harmony workflows.
- V3 research-only mission-health and continuation-judgment roadmap lane for future advisory value, cost, confidence, drift, risk, and continuation signals.
- V3 research-only loop-governance artifacts: loop contract template, terminal-state and safe-hold vocabulary, advisory loop-contract lint, and deterministic fixtures for memory/re-entry, tool-use, blind-action, and feature-verification gaps.
- V3 research-only anchor registry for pointer-first cold-start orientation across approved profiles, candidate gates, evidence paths, and guardrails.
- V3 research-only mutable-harness-state principle for pinning or recording model identity, skill versions, and credential references in replay evidence.
- V3 research-only standing-authorization schema candidates for future scheduled or ambient missions, with per-mission human Go remaining the only approved authorization shape.
- V3 research-only skill provenance policy classifying authored, vendor-supplied, and learned skills, with pinning, quarantine-until-promoted, and non-laundering review rules.
- V3 advisory regulatory crosswalk mapping V3 artifacts to EU AI Act human-oversight and logging themes and ISO/IEC 42001 themes, marked for human review and making no compliance claims.
- V3 research-only long-running mission lane: candidate `V3-OP-003` profile, a decision pack with pre-written promotion criteria currently at `NO PROMOTION YET`, an advisory mission-health vocabulary for checkpoint-time continuation judgment, an interrupt-transport live trial plan whose execution requires separate sponsor approval, a three-rung duration-ladder plan toward roughly 4-hour attended missions, and a concrete non-executing Option A rung-3 envelope that still requires explicit sponsor Go before any rung-3 run.
- External governance-kernel boundary guidance for V3 work.
- Factory V2 build-support layer, including orchestration docs, stage contracts, templates, lint scripts, Mission Mode, and helper tooling for building V3 while V3 matures.

## Key Paths

- `docs/Factory/v3/` - primary V3 docs, templates, trials, and roadmap.
- `docs/Factory/v3/ANCHOR_REGISTRY.md` - pointer-first map of current V3 anchor points, evidence paths, current status labels, and next named gates.
- `.agents/skills/factory-mission-formation/` and `.agents/skills/factory-challenge-mission/` - research-stage repo skills for non-executing mission discovery and challenge.
- `docs/Factory/ARCHITECTURE.md`, `docs/Factory/ORCHESTRATION.md`, `docs/Factory/Spec/`, and `docs/Factory/templates/` - Factory V2 build-support layer for governing V3 work while V3 matures.
- `docs/Factory/runs/` - V3-related Factory run evidence migrated from `factory-starter-kit`.
- `scripts/factory_v3_*.py` - standalone advisory V3 validators.
- `scripts/factoryctl`, `scripts/factory_stage_lint.py`, `scripts/factory_pack_lint.py`, and related helpers - Factory V2 build-support tooling.
- `tests/fixtures/factory_v3_*/` - deterministic fixture corpora for the advisory validators.

## Basic Verification

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json
python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json
python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json
python3 scripts/factory_v3_loop_contract_lint.py --target tests/fixtures/factory_v3_loop_contract --expect tests/fixtures/factory_v3_loop_contract/expected/all.json --json
```
