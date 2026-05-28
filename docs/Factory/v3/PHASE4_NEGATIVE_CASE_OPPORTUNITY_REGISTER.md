# Factory V3 Phase 4 Negative-case Opportunity Register

## Version
v0.2

## Change Log
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

That evidence gap remains open. The first three Phase 4 real-run captures are happy-path docs-only records with `NO_TELEMETRY`, and the first approved negative-case capture candidate produced a clean advisory FP/FN non-event with `NO_TELEMETRY`; these records do not close the gap, prove recovery behavior, or support routing thresholds.

## Opportunity Register
| Opportunity ID | Natural Signal To Watch | Possible Future Candidate Shape | Why It Might Produce Signal | Current Status | Guardrail |
| --- | --- | --- | --- | --- | --- |
| `P4-NEG-OPP-001` | Clarification-heavy start | A narrow doc update where the requested target file or canonical source is ambiguous. | A real agent should ask for or derive clarification from source artifacts before editing. | Unapproved opportunity only | Do not manufacture ambiguity; stop if objective is not bounded. |
| `P4-NEG-OPP-002` | Verification halt | A deterministic fixture or expected-output maintenance task where verification may legitimately fail after an edit. | A real failure would test halt and human-decision behavior. | Unapproved opportunity only | Do not seed a failure just to satisfy the register. |
| `P4-NEG-OPP-003` | V2 fallback before execution | A candidate that appears `V3-OP-001` eligible but reveals broader scope during planning. | A natural scope expansion should trigger fallback to V2 planning instead of execution. | Unapproved opportunity only | Do not approve broad scope inside V3 advisory evidence. |
| `P4-NEG-OPP-004` | Stale reentry or source-conflict recovery | A future continuation after canon files changed since the candidate was planned. | A real reentry should reread source artifacts and reject stale derived context. | Unapproved opportunity only | Source artifacts remain authority; derived summaries are aids only. |
| `P4-NEG-OPP-005` | Advisory false positive or false negative | A docs-only change whose wording is close to promotion, routing, or threshold language. | The natural-language pilot may flag risk that needs human adjudication. | Executed as `P4-NEG-CAPTURE-CANDIDATE-001`; clean non-event; no advisory FP/FN finding observed | Use same-paragraph non-promotion language and classify findings honestly. |

## Executed Candidate Records
| Candidate ID | Source Opportunity | Result Summary | Harness Profile | Observed Signal | Gap Status |
| --- | --- | --- | --- | --- | --- |
| `P4-NEG-CAPTURE-CANDIDATE-001` | `P4-NEG-OPP-005` | `real_run_corpus/RR_20260528_001_phase4_advisory_threshold_wording.md` | `harness_profiles/HP_20260528_001_codex_phase4_advisory_threshold_wording.md` | Clean non-event: no natural advisory FP/FN finding, halt, fallback, clarification-heavy behavior, stale reentry, evidence-quality weakness, verification-quality weakness, or scope-discipline pressure occurred. | Phase 3 natural halted/fallback/clarification-heavy gap remains open. |

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
