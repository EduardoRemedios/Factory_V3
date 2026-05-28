# V3 Harness Capability Profile Index

## Version
v0.4

## Change Log
- v0.4 (2026-05-28): Added second approved negative-case capture candidate harness profile.
- v0.3 (2026-05-28): Added first approved negative-case capture candidate harness profile.
- v0.2 (2026-05-27): Added third harness profile for the negative-case opportunity register.
- v0.1 (2026-05-27): Initial Phase 4 harness capability profile index.

## Status
Research-only and non-enforcing.

This index is a navigation aid for harness-specific Phase 4 advisory profiles. It does not authorize governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this index. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`, and Factory V2 remains supported and available as fallback.

## Indexed Profiles
| Profile ID | Path | Result Summary | Harness | Mission Profile | Evidence Band | Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| `HP_20260527_001` | `HP_20260527_001_codex_phase4_candidate_status_update.md` | `../real_run_corpus/RR_20260527_001_phase4_candidate_status_update.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` | `harness_profile_observed` | One happy-path docs-only run; no natural halt, fallback, clarification-heavy, or reentry stress. |
| `HP_20260527_002` | `HP_20260527_002_codex_phase4_corpus_index_update.md` | `../real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` | `harness_profile_observed` | Second happy-path docs-only run; still no natural halt, fallback, clarification-heavy, or reentry stress. |
| `HP_20260527_003` | `HP_20260527_003_codex_phase4_negative_case_opportunity_register.md` | `../real_run_corpus/RR_20260527_003_phase4_negative_case_opportunity_register.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` | `harness_profile_observed` | Third happy-path docs-only run; opportunity list does not itself create natural negative-case evidence. |
| `HP_20260528_001` | `HP_20260528_001_codex_phase4_advisory_threshold_wording.md` | `../real_run_corpus/RR_20260528_001_phase4_advisory_threshold_wording.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` | `harness_profile_observed` | First negative-case capture candidate produced a clean non-event; no natural advisory FP/FN finding, halt, fallback, clarification-heavy behavior, or reentry stress. |
| `HP_20260528_002` | `HP_20260528_002_codex_phase4_verification_halt_fixture.md` | `../real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` | `harness_profile_observed` | Second negative-case capture candidate produced a clean non-event; deterministic fixture `--expect` verification passed with no natural halt. |

## Use Rules
- Use this index to locate advisory harness profiles only.
- Do not generalize profile observations across harnesses, models, repositories, mission profiles, or risk classes.
- Do not use this index as a threshold table, router input, promotion ledger, gate checklist, or reduced-governance authority.
- Keep profile limitations visible when citing any record.

## Notes
This index does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 planning pipeline.
