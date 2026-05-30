# Factory V3 Phase 4 Negative-case Opportunity Register

## Version
v0.6

## Change Log
- v0.6 (2026-05-30): Recorded `P4-NEG-OPP-001` as the source for the third approved negative-case capture candidate, with a clarification-heavy stop-before-edit signal.
- v0.5 (2026-05-30): Generalized the dynamic-workflow opportunity to include future dynamic/parallel workflow harnesses such as possible Codex equivalents.
- v0.4 (2026-05-30): Added an unapproved dynamic-workflow evidence-export opportunity for future harness research.
- v0.3 (2026-05-28): Recorded `P4-NEG-OPP-002` as the source for the second approved negative-case capture candidate, with a clean verification-halt non-event.
- v0.2 (2026-05-28): Recorded `P4-NEG-OPP-005` as the source for the first approved negative-case capture candidate, with a clean advisory FP/FN non-event.
- v0.1 (2026-05-27): Initial research-only opportunity register for future natural negative-case capture candidates.

## Status
Research-only and non-enforcing.

This register does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

This register does not promote Factory V3. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`, and Factory V2 remains supported and available as fallback.

## Purpose
List future opportunity shapes that may naturally exercise halt, fallback, clarification-heavy, stale-reentry, or failed-verification behavior during separately approved `V3-OP-001` evidence work.

This register does not create, approve, execute, or preselect any future candidate. It is a planning aid for later Factory V2-governed candidate selection.

## Evidence Gap
Phase 3 did not capture a natural halted, fallback, or clarification-heavy telemetry pilot.

That evidence gap remains open. The first three Phase 4 real-run captures are happy-path docs-only records with `NO_TELEMETRY`, the first two approved negative-case capture candidates produced clean non-events with `NO_TELEMETRY`, and the third approved negative-case capture candidate produced a natural clarification-before-edit signal with `NO_TELEMETRY`. These records narrow the clarification evidence gap but do not close telemetry, failed-verification halt, fallback, recovery, or routing-threshold gaps.

## Opportunity Register
| Opportunity ID | Natural Signal To Watch | Possible Future Candidate Shape | Why It Might Produce Signal | Current Status | Guardrail |
| --- | --- | --- | --- | --- | --- |
| `P4-NEG-OPP-001` | Clarification-heavy start | A narrow doc update where the requested target file or canonical source is ambiguous. | A real agent should ask for or derive clarification from source artifacts before editing. | Executed as `P4-NEG-CAPTURE-CANDIDATE-003`; natural stop-before-edit clarification signal observed; no optional telemetry, failed-verification halt, or V2 fallback execution occurred | Do not manufacture ambiguity; stop if objective is not bounded. |
| `P4-NEG-OPP-002` | Verification halt | A deterministic fixture or expected-output maintenance task where verification may legitimately fail after an edit. | A real failure would test halt and human-decision behavior. | Executed as `P4-NEG-CAPTURE-CANDIDATE-002`; clean non-event; deterministic `--expect` verification passed | Do not seed a failure just to satisfy the register. |
| `P4-NEG-OPP-003` | V2 fallback before execution | A candidate that appears `V3-OP-001` eligible but reveals broader scope during planning. | A natural scope expansion should trigger fallback to V2 planning instead of execution. | Unapproved opportunity only | Do not approve broad scope inside V3 advisory evidence. |
| `P4-NEG-OPP-004` | Stale reentry or source-conflict recovery | A future continuation after canon files changed since the candidate was planned. | A real reentry should reread source artifacts and reject stale derived context. | Unapproved opportunity only | Source artifacts remain authority; derived summaries are aids only. |
| `P4-NEG-OPP-005` | Advisory false positive or false negative | A docs-only change whose wording is close to promotion, routing, or threshold language. | The natural-language pilot may flag risk that needs human adjudication. | Executed as `P4-NEG-CAPTURE-CANDIDATE-001`; clean non-event; no advisory FP/FN finding observed | Use same-paragraph non-promotion language and classify findings honestly. |
| `P4-NEG-OPP-006` | Dynamic-workflow evidence export or replay gap | A future dynamic/parallel workflow candidate, including Claude Code dynamic workflows or Codex subagent workflows, whose subtask, verification, or resume evidence may be incomplete for Factory replay. | A parallel harness may finish work while exposing too little reviewable evidence for Factory closeout. | Unapproved opportunity only; linked research plan at `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md` | Do not execute without separate approval; do not capture chain-of-thought, vendor-private cognition state, raw transcripts, secrets, or broad workflow internals. |

## Executed Candidate Records
| Candidate ID | Source Opportunity | Result Summary | Harness Profile | Observed Signal | Gap Status |
| --- | --- | --- | --- | --- | --- |
| `P4-NEG-CAPTURE-CANDIDATE-001` | `P4-NEG-OPP-005` | `real_run_corpus/RR_20260528_001_phase4_advisory_threshold_wording.md` | `harness_profiles/HP_20260528_001_codex_phase4_advisory_threshold_wording.md` | Clean non-event: no natural advisory FP/FN finding, halt, fallback, clarification-heavy behavior, stale reentry, evidence-quality weakness, verification-quality weakness, or scope-discipline pressure occurred. | Phase 3 natural halted/fallback/clarification-heavy gap remains open. |
| `P4-NEG-CAPTURE-CANDIDATE-002` | `P4-NEG-OPP-002` | `real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md` | `harness_profiles/HP_20260528_002_codex_phase4_verification_halt_fixture.md` | Clean non-event: deterministic fixture `--expect` verification passed, so no natural verification halt, fallback, clarification-heavy behavior, stale reentry, evidence-quality weakness, verification-quality weakness, or scope-discipline pressure occurred. | Phase 3 natural halted/fallback/clarification-heavy gap remains open. |
| `P4-NEG-CAPTURE-CANDIDATE-003` | `P4-NEG-OPP-001` | `real_run_corpus/RR_20260530_003_phase4_clarification_heavy_candidate.md` | `harness_profiles/HP_20260530_003_codex_phase4_clarification_heavy_candidate.md` | Natural clarification-before-edit signal: broad roadmap/status edits and optional telemetry were not performed because exact target files and telemetry authority were not explicit after Go. | Clarification evidence gap is narrowed; telemetry, failed-verification halt, fallback, and recovery gaps remain open. |

## Selection Rules For Later Candidates
- A later candidate must be separately planned and approved before execution.
- A listed opportunity is not a candidate until a future Factory V2 pack names it.
- A natural negative-case signal must be observed during real work; it must not be scripted, seeded, or manufactured.
- `NO_TELEMETRY` remains the default unless optional advisory telemetry is separately approved for a specific candidate.
- Any future result summary must state whether the Phase 3 natural negative-case gap remains open or was naturally observed.

## Excluded Uses
- Do not use this register as a router input.
- Do not use this register as a threshold table.
- Do not use this register as promotion evidence.
- Do not use this register as approval for any future candidate.
- Do not use this register to weaken Factory V2 fallback or non-deprecation language.

## Notes
This register is a planning aid only. It does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 planning pipeline.
