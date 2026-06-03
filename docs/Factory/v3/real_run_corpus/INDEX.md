# V3 Real-run Corpus Index

## Version
v0.7

## Change Log
- v0.7 (2026-06-03): Added fifth approved negative-case capture candidate record for verification-halt fixture maintenance with optional advisory telemetry.
- v0.6 (2026-06-01): Added fourth approved negative-case capture candidate record for read-only dynamic/parallel evidence-export probing.
- v0.5 (2026-05-30): Added third approved negative-case capture candidate record for clarification-heavy stop-before-edit intake.
- v0.4 (2026-05-28): Added second approved negative-case capture candidate record for verification-halt fixture maintenance.
- v0.3 (2026-05-28): Added first approved negative-case capture candidate record for advisory threshold wording.
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
| `RR_20260528_001` | `RR_20260528_001_phase4_advisory_threshold_wording.md` | `P4-NEG-CAPTURE-CANDIDATE-001` | `../harness_profiles/HP_20260528_001_codex_phase4_advisory_threshold_wording.md` | Negative-case candidate clean non-event for advisory threshold wording; no advisory FP/FN finding observed | `NO_TELEMETRY` | Natural halted/fallback/clarification-heavy gap remains open | `accepted_advisory_evidence` |
| `RR_20260528_002` | `RR_20260528_002_phase4_verification_halt_fixture.md` | `P4-NEG-CAPTURE-CANDIDATE-002` | `../harness_profiles/HP_20260528_002_codex_phase4_verification_halt_fixture.md` | Verification-halt candidate clean non-event; deterministic fixture `--expect` verification passed | `NO_TELEMETRY` | Natural halted/fallback/clarification-heavy gap remains open | `accepted_advisory_evidence` |
| `RR_20260530_003` | `RR_20260530_003_phase4_clarification_heavy_candidate.md` | `P4-NEG-CAPTURE-CANDIDATE-003` | `../harness_profiles/HP_20260530_003_codex_phase4_clarification_heavy_candidate.md` | Clarification-heavy candidate intake; broad edits stopped before target/telemetry authority was inferred | `NO_TELEMETRY` | Natural clarification-before-edit signal observed; telemetry, failed-verification, and fallback gaps remain open | `accepted_advisory_evidence` |
| `RR_20260601_004` | `RR_20260601_004_phase4_dynamic_evidence_export_candidate.md` | `P4-NEG-CAPTURE-CANDIDATE-004` | `../harness_profiles/HP_20260601_004_codex_phase4_dynamic_evidence_export_candidate.md` | Read-only Codex multi-agent evidence-export probe; safe summary evidence sufficient for replay of this probe | `NO_TELEMETRY` | Dynamic/parallel summary-export signal observed; telemetry, failed-verification, fallback, recovery, and routing-threshold gaps remain open | `accepted_advisory_evidence` |
| `RR_20260603_005` | `RR_20260603_005_phase4_verification_halt_telemetry_candidate.md` | `P4-NEG-CAPTURE-CANDIDATE-005` | `../harness_profiles/HP_20260603_005_codex_phase4_verification_halt_telemetry_candidate.md` | Verification-halt fixture maintenance with optional advisory telemetry; deterministic fixture `--expect` verification passed | `OPTIONAL_ADVISORY_TELEMETRY_APPROVED` | Telemetry-backed clean non-event observed; failed-verification halt, fallback, recovery, and routing-threshold gaps remain open | `accepted_advisory_evidence` |

## Use Rules
- Use this index to locate advisory evidence records only.
- Do not use this index as a threshold table, router input, promotion ledger, gate checklist, or reduced-governance authority.
- Treat evidence bands inside records as review labels only.
- Treat `RR_20260530_003` as a natural clarification-before-edit signal only, `RR_20260601_004` as a read-only dynamic/parallel summary-export signal only, and `RR_20260603_005` as a telemetry-backed clean non-event only; failed-verification halt, fallback, recovery, and routing-threshold evidence gaps remain open until separately approved candidates naturally produce that evidence.

## Notes
This index does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 planning pipeline.
