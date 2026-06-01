# V3 Harness Capability Profile Index

## Version
v0.8

## Change Log
- v0.8 (2026-06-01): Added fourth approved negative-case capture candidate harness profile for read-only Codex multi-agent evidence-export probing.
- v0.7 (2026-05-30): Added third approved negative-case capture candidate harness profile for clarification-heavy stop-before-edit intake.
- v0.6 (2026-05-30): Added Codex subagent-workflows research profile and generalized the dynamic-workflow class path.
- v0.5 (2026-05-30): Added Claude Code dynamic workflows research profile with `insufficient_evidence` band.
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
| `HP_20260530_001` | `HP_20260530_001_claude_code_dynamic_workflows_research.md` | `../PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md` | Claude Code dynamic workflows | no local mission; future candidate must be separately scoped | `insufficient_evidence` | External announcement and local research plan only; no local command, diff, verification, interruption, resume, token, or cost evidence. |
| `HP_20260530_002` | `HP_20260530_002_codex_subagent_workflows_research.md` | `../PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md` | Codex subagent workflows and experimental CSV fanout | no local mission | `insufficient_evidence` | Official-docs source signal only; no local command, diff, verification, interruption, resume, token, or cost evidence. |
| `HP_20260530_003` | `HP_20260530_003_codex_phase4_clarification_heavy_candidate.md` | `../real_run_corpus/RR_20260530_003_phase4_clarification_heavy_candidate.md` | Codex desktop app | `V3-OP-001 Bounded Code Change` candidate intake only | `harness_profile_observed` | Third negative-case capture candidate produced a natural stop-before-edit clarification signal; no optional telemetry, failed-verification halt, or V2 fallback execution occurred. |
| `HP_20260601_004` | `HP_20260601_004_codex_phase4_dynamic_evidence_export_candidate.md` | `../real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md` | Codex desktop app with multi-agent explorer subagent | `V3-OP-001 Bounded Code Change` read-only evidence probe | `harness_profile_observed` | Fourth negative-case capture candidate produced a safe summary-export signal for one read-only probe; no optional telemetry, command-producing implementation, failed-verification halt, V2 fallback execution, or interruption/resume stress occurred. |

## Use Rules
- Use this index to locate advisory harness profiles only.
- Do not generalize profile observations across harnesses, models, repositories, mission profiles, or risk classes.
- Do not use this index as a threshold table, router input, promotion ledger, gate checklist, or reduced-governance authority.
- Keep profile limitations visible when citing any record.

## Notes
This index does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 planning pipeline.
