# V3 Real-run Corpus Index

## Version
v0.1

## Change Log
- v0.2 (2026-05-27): Added third capture record for the negative-case opportunity register.
- v0.1 (2026-05-27): Initial Phase 4 real-run corpus index.

## Status
Research-only and non-enforcing.

This index is a navigation aid for Phase 4 evidence records. It does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this index. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`, and Factory V2 remains supported and available as fallback.

## Indexed Records
| Result ID | Path | Candidate | Harness Profile | Evidence Shape | Telemetry | Gap Status | Reviewer Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `RR_20260527_001` | `RR_20260527_001_phase4_candidate_status_update.md` | `P4-CAPTURE-CANDIDATE-001` | `../harness_profiles/HP_20260527_001_codex_phase4_candidate_status_update.md` | Happy-path docs-only status/evidence update | `NO_TELEMETRY` | Natural halted/fallback/clarification-heavy gap remains open | `accepted_advisory_evidence` |
| `RR_20260527_002` | `RR_20260527_002_phase4_corpus_index_update.md` | `P4-CAPTURE-CANDIDATE-002` | `../harness_profiles/HP_20260527_002_codex_phase4_corpus_index_update.md` | Happy-path docs-only corpus/profile index update | `NO_TELEMETRY` | Natural halted/fallback/clarification-heavy gap remains open | `accepted_advisory_evidence` |
| `RR_20260527_003` | `RR_20260527_003_phase4_negative_case_opportunity_register.md` | `P4-CAPTURE-CANDIDATE-003` | `../harness_profiles/HP_20260527_003_codex_phase4_negative_case_opportunity_register.md` | Happy-path docs-only negative-case opportunity register | `NO_TELEMETRY` | Natural halted/fallback/clarification-heavy gap remains open | `accepted_advisory_evidence` |

## Use Rules
- Use this index to locate advisory evidence records only.
- Do not use this index as a threshold table, router input, promotion ledger, gate checklist, or reduced-governance authority.
- Treat evidence bands inside records as review labels only.
- Keep the Phase 3 natural halted/fallback/clarification-heavy evidence gap open until a separately approved candidate naturally produces such evidence.

## Notes
This index does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 planning pipeline.
