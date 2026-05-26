# Factory V3 Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Phase 4 eval expansion and harness capability profiling plan.

## Status
Research-only and non-enforcing.

This document does not authorize governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Research only: this document does not promote Factory V3. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`. Factory V2 remains supported and available as fallback.

## Purpose
Define the Phase 4 evaluation expansion needed to judge harness capability and execution reliability for future evidence decisions.

Phase 4 measures whether a harness can preserve V2 safety properties for bounded `V3-OP-001` work with less decomposition. It prepares evidence for later decisions, but it does not make those decisions.

## Inputs
- `ROADMAP_TO_FULL_VISION.md` Phase 4.
- `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`.
- `PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_STATUS.md`.
- `OPERATIONAL_READINESS_EVAL_PLAN.md`.
- `tests/fixtures/factory_v3_operational_readiness_eval/`.
- The Factory V2 planning pack at `docs/Factory/runs/RUN_20260526_1304_v3_phase4_eval_expansion_plan/`.

## Phase 3 Carry-forward Gap
Phase 3 did not capture a natural halted, fallback, or clarification-heavy telemetry pilot.

Phase 4 must treat that as an evidence gap. It may plan fixture and profile coverage for the gap, but it must not claim real negative-case telemetry evidence until a real case exists.

## Evaluation Dimensions

### Harness Capability
Record what the harness actually did under a named mission profile, repository context, tool-access pattern, and verification set.

Required signals:
- harness and model when known,
- mission profile and risk class,
- available tools and command permissions,
- context and interruption behavior,
- verification command reliability,
- human intervention points,
- known limitations.

Capability observations must not be generalized across harnesses, models, repositories, mission profiles, or tool policies without matching evidence.

### Execution Reliability
Measure whether the harness can complete real bounded work without losing the guarantees V2 normally provides.

Required signals:
- planned commands were run or explicitly skipped with reason,
- failed checks halted work until a human decision or fallback record existed,
- closeout matched actual command and file-change evidence,
- stale reentry was detected before further work,
- interruptions resumed from source artifacts rather than chat memory.

### Scope Discipline
Measure whether the harness keeps work inside the mission envelope.

Required signals:
- no unapproved file-scope growth,
- no new dependency or framework work unless authorized,
- no conversion of advisory evidence into authority,
- no V2 fallback weakening.

### Verification Quality
Measure whether verification evidence is meaningful, not merely present.

Required signals:
- each critical or high constraint has an appropriate verification tier,
- command evidence includes exit status and summary,
- known skipped checks are called out,
- failed checks lead to halt, fallback, or explicit human decision.

### Interruption Recovery
Measure whether the harness can recover after a pause without inventing state.

Required signals:
- source artifacts are reread,
- derived cursors or summaries are treated as aids only,
- stale or conflicting evidence triggers halt,
- resumed work preserves the original authority and verification boundaries.

### Evidence Quality
Measure whether a later reviewer can replay the mission.

Required signals:
- objective, authority, commands, file touches, decisions, verification, and residual risks are traceable,
- evidence gaps are explicit,
- telemetry, if used, remains summary-only and optional,
- no chain-of-thought, raw command output dumps, source file contents, secrets, or vendor-private cognition state are captured in profile artifacts.

## Fixture Expansion Plan
Do not add fixture files until a later approved execution run names exact files and expected outputs.

Planned fixture families for `tests/fixtures/factory_v3_operational_readiness_eval/`:

| Proposed ID Range | Family | Expected Signal |
| --- | --- | --- |
| `V3-P4-CAP-*` | Capability profile completeness | Flags missing harness, model-when-known, repo, mission profile, tool access, verification, limitation, or evidence-date fields. |
| `V3-P4-REL-*` | Execution reliability | Distinguishes real check execution, skipped checks with reason, failed-check halt behavior, and closeout consistency. |
| `V3-P4-SCOPE-*` | Scope discipline | Flags unauthorized file growth, dependency drift, speculative abstractions, and advisory evidence used as authority. |
| `V3-P4-VERIFY-*` | Verification quality | Flags shallow evidence, missing exit status, missing skipped-check rationale, or weak constraint-to-check mapping. |
| `V3-P4-RECOVER-*` | Interruption recovery | Flags stale reentry, source-artifact conflict, and derived-summary authority claims. |
| `V3-P4-EVID-*` | Evidence quality | Flags missing human decisions, residual risks, command evidence summaries, and explicit evidence gaps. |
| `V3-P4-FPN-*` | False-positive and false-negative classification | Tests human adjudication fields and accepted/deferred classification flow. |
| `V3-P4-THRESH-*` | Advisory threshold wording | Flags wording that turns evidence bands into routing, reduced governance, or default-mode decisions. |

Each fixture should declare whether it is synthetic, real-run-derived, or backfilled from historical evidence. Synthetic-only negative fixtures must be labeled so later reports do not overstate real failure coverage.

## Real-run Result Corpus Plan
Phase 4 should collect result summaries only from selected low-risk `V3-OP-001` evidence missions after separate approval.

Each result should record:
- harness and model when known,
- repository and mission profile,
- objective and authority summary,
- commands attempted,
- verification results,
- interruption or reentry events,
- evidence gaps,
- human decisions,
- false-positive and false-negative classifications,
- reviewer notes,
- residual risk.

Optional telemetry may be attached only when it follows Phase 3 conditions: selected narrow evidence missions, summary-only payloads, non-blocking replay output, and no gate wiring.

## False-positive And False-negative Rollup Shape
Use a rollup table or JSON-compatible structure with these fields:

| Field | Meaning |
| --- | --- |
| `case_id` | Fixture, real-run, or pilot identifier. |
| `source_type` | `fixture_synthetic`, `fixture_real_derived`, `real_run`, or `historical_backfill`. |
| `harness` | Harness under review. |
| `model_when_known` | Model identifier when available and appropriate to record. |
| `mission_profile` | Example: `V3-OP-001`. |
| `finding_id` | Eval or reviewer finding identifier. |
| `expected_classification` | Expected result when known. |
| `observed_classification` | Actual eval or reviewer result. |
| `human_adjudication` | `true_positive`, `false_positive`, `true_negative`, `false_negative`, `needs_more_context`, or `deferred`. |
| `rationale` | Short reviewer rationale. |
| `follow_up` | Fixture, doc, template, or evaluator change proposed. |
| `blocking_effect` | Always `none` for Phase 4 advisory evidence. |

The rollup is decision-prep evidence only. It does not approve any profile, route, required gate, or governance reduction.

## Advisory Threshold Discussion
Phase 4 may discuss evidence bands only as a way to organize future review.

Non-operational bands:
- `insufficient_evidence`: too few cases or unresolved critical gaps.
- `harness_profile_observed`: useful signal for one harness/profile/repo shape.
- `repeatable_low_risk_signal`: repeated signal across comparable bounded work.
- `candidate_for_later_router_study`: enough evidence to justify a separate Phase 5 planning run.

These bands do not route work. They do not reduce V2 governance. They do not make V3 the default. They cannot be used outside the harness, model-when-known, mission profile, repository context, and verification conditions that produced the evidence.

## Harness Capability Report Template
Use `templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md` for individual profile reports.

Profile reports should be reviewed as evidence snapshots, not scorecards with universal meaning.

## Verification For A Later Phase 4 Implementation
Run:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
git diff --check
```

Manual review:
- confirm no router, enforcement, required gate, telemetry completeness, runtime authority, proof, lease, default-mode, or V2-removal language was introduced,
- confirm Phase 3 negative-case telemetry gap remains explicit,
- confirm fixture work remains planned unless separately approved,
- confirm V2 fallback remains supported.

## Exit Criteria For Phase 4
Phase 4 is ready for evidence review only when:
- the capability profile template exists,
- planned fixture families are implemented under separate approval,
- at least one real-run result corpus format is trialed,
- false-positive and false-negative rollups include human adjudication,
- the missing natural halted, fallback, or clarification-heavy case is either captured or still carried as an explicit gap,
- threshold discussion remains advisory and non-operational.

## No-go Conditions
Stop Phase 4 work if:
- evidence bands are used as routing decisions,
- capability scores are presented as universal across harnesses or profiles,
- document compliance is treated as execution reliability,
- telemetry becomes required or gate-enforced,
- V2 fallback is weakened,
- external runtime authority, proof, lease enforcement, or production action mediation is claimed.
