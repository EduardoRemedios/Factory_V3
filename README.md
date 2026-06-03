# Factory V3

Factory V3 is the experimental and operational-evidence track for governed autonomous execution.

The long-term product framing is simple: Factory V3 is an operating system for supervised AI workers. Humans define missions, constraints, budgets, verification requirements, and approval rules; autonomous AI workers execute over longer horizons under bounded authority, continuous verification, replayable evidence, escalation rules, and human supervision at key checkpoints.

That is the product vision, not the current operational approval. Today this repository approves only optional `V3-OP-001 Bounded Code Change` use.

Coding is the first concrete proving ground for this model because software work produces reviewable evidence: diffs, commands, tests, failures, and closeout records. The broader target is knowledge work and engineering missions where autonomous actors need to operate safely under controlled supervision, but non-coding profiles require separate evidence, governance review, and explicit approval before use.

This repository was split out of `factory-starter-kit` so V3 can evolve independently from Factory V2 and earlier content.

Factory V3 development in this repository can use Factory V2 process semantics while V3 is still maturing. The V2 docs, templates, and scripts are included as temporary build-support scaffolding so V3 can be built with the same planning, lint, pack, verification, and SIMPLE-CODE-GATE discipline that governed the earlier V3 evidence.

This does not make V3 dependent on V2 as a product. The intended direction is for this repository to become V3-only once V3 is built, confidence-backed, and explicitly approved. V2 remains preserved in the separate V2-only repository.

## Current Scope

- Optional `V3-OP-001 Bounded Code Change` guidance and evidence.
- V3 mission-envelope, closeout, fallback, SIMPLE-CODE-GATE, and mission-record templates.
- V3 advisory validators and deterministic fixtures.
- V3 advisory telemetry replay evidence, including three real Phase 3 pilot logs and an evidence review that conditionally recommends optional advisory telemetry for selected narrow evidence missions.
- V3 Phase 4 eval expansion plan, harness capability profile template, synthetic operational-readiness fixture expansion, real-run corpus and harness-profile indexes, three happy-path docs-only real-run corpus records, four negative-case capture records, and a research-only negative-case opportunity register.
- V3 research-only dynamic/parallel workflow harness planning with `insufficient_evidence` status, including Claude Code as an external-announcement signal and Codex as an official-docs source signal.
- V3 operational-readiness, trial, and decision evidence.
- External governance-kernel boundary guidance for V3 work.
- Factory V2 build-support layer, including orchestration docs, stage contracts, templates, lint scripts, Mission Mode, and helper tooling for building V3 while V3 matures.

## Important Boundaries

- The only currently approved optional V3 operational profile is `V3-OP-001 Bounded Code Change`.
- Broader supervised-worker or non-coding mission language is roadmap vision, not current operating authority.
- Current Factory V3 state does not make Factory V2 obsolete.
- V3 required-gate integration is not implied by this repository split.
- V2 process tooling in this repo is build-support scaffolding for V3 development; it does not make V3 validators required gates or create a V3 product dependency on V2.
- Future V2 deprecation/removal from this repository requires explicit V3 confidence evidence and release approval.
- Runtime authority, production action mediation, proof, leases, telemetry enforcement, and governance routing remain separately governed by explicit V3 evidence and approval.
- Existing V3 advisory tools remain advisory unless a future release explicitly promotes them.
- Phase 3 telemetry is not a required gate; Phase 4 eval expansion has started with advisory planning artifacts, synthetic fixtures, three separately approved happy-path docs-only real-run captures using `NO_TELEMETRY`, two approved negative-case clean non-events using `NO_TELEMETRY`, one clarification-before-edit capture using `NO_TELEMETRY`, one read-only dynamic/parallel summary-export capture using `NO_TELEMETRY`, and a research-only opportunity register.
- The Phase 3 natural halted/fallback/clarification-heavy telemetry gap remains open; clarification and summary-export evidence gaps are narrowed by non-telemetry evidence only.
- Phase 4 does not approve governance routing, reduced governance, default-mode behavior, telemetry completeness checks, required gates, runtime authority, proof, lease enforcement, dynamic-workflow execution by default, or V2 build-support removal.

## Key Paths

- `docs/Factory/v3/` - primary V3 docs, templates, trials, and roadmap.
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
```
