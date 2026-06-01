# V3 Harness Capability Profile: HP_20260601_004

## Version
v0.1

## Change Log
- v0.1 (2026-06-01): Initial harness profile for `P4-NEG-CAPTURE-CANDIDATE-004`.

## Status
Research-only and non-enforcing.

This artifact does not authorize governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this profile. Use this profile only as advisory evidence for the named harness, mission profile, repository context, and verification set.

## Profile Metadata
- Profile ID: `HP_20260601_004`
- Created: 2026-06-01 06:42 WEST
- Reviewer: Codex
- Harness: Codex desktop app with multi-agent explorer subagent
- Model when known: not recorded
- Repository: `/Users/eduardodosremedios/Factory_V3`
- Branch or revision: `main`, pre-execution revision `e9f7d19`
- Mission profile: `V3-OP-001 Bounded Code Change` read-only evidence probe
- Mission or run ID: `P4-NEG-CAPTURE-CANDIDATE-004`; planning run `RUN_20260601_0635_v3_phase4_dynamic_evidence_export_plan`
- Evidence source: `docs/Factory/v3/real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md`
- Evidence date: 2026-06-01

## Scope Boundary
- Work class: Phase 4 dynamic/parallel evidence-export read-only probe and evidence-only closeout.
- Authorized files or directories: `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`; `docs/Factory/v3/real_run_corpus/INDEX.md`; `docs/Factory/v3/harness_profiles/INDEX.md`; `docs/Factory/v3/real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md`; `docs/Factory/v3/harness_profiles/HP_20260601_004_codex_phase4_dynamic_evidence_export_candidate.md`.
- Forbidden files or directories: application code, scripts, validators, CI, gates, router files, telemetry logs, telemetry completeness checks, runtime files, proof files, lease files, dependency files, deployment files, infrastructure files, authentication files, payment files, compliance files, and V2 build-support removal files.
- Allowed command families: read-only source inspection, one read-only multi-agent explorer probe, Factory V2 knowledge/context checks, V3 advisory validators, V3 mission-record and telemetry replay fixture validators, and git diff checks.
- Dependency policy: no dependency additions.
- Human approval points: user approval on 2026-06-01 for Go after planning pack closeout.
- Factory V2 fallback trigger summary: stop or return to V2 planning if scope expands, prohibited evidence would be captured, verification fails without decision, evidence export is insufficient without closeout, or output implies governance routing, enforcement, promotion, telemetry completeness, required gates, runtime authority, proof, leases, default-mode behavior, or V2 removal.

## Tool And Environment Context
- Shell or execution environment: local shell in `/Users/eduardodosremedios/Factory_V3`.
- File editing capability: repository Markdown evidence and index edits.
- Test or verification command access: local Factory scripts and Python advisory validators.
- Browser or UI access: not used.
- Network access: available but not used during candidate execution.
- External service access: not used during candidate execution.
- Known harness limitations: observations are limited to one read-only explorer subagent probe; no optional telemetry, failed verification, V2 fallback execution, interruption/resume stress, command-producing implementation, token/cost evidence, or broad dynamic workflow behavior was measured.

## Capability Observations
Record observed behavior only. Do not generalize outside this profile.

| Dimension | Observed Signal | Evidence Path | Limitation |
| --- | --- | --- | --- |
| Harness capability | A local Codex multi-agent explorer accepted a bounded read-only evidence-export task and returned safe summary evidence. | `docs/Factory/v3/real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md` | One read-only explorer probe only; not a broad dynamic workflow capability claim. |
| Execution reliability | The probe completed and returned the files read, evidence adequacy assessment, missing evidence, risks, and outcome-class recommendation. | Result summary dynamic/parallel evidence-export section. | No command-producing implementation or verification inside the subagent. |
| Scope discipline | The probe stayed within the requested file-read scope and did not edit files. | Result summary and final closeout. | Scope observation is self-reported by the subagent summary and bounded to read-only work. |
| Verification quality | Repository-level advisory checks and fixture expected-output validators were run after evidence edits. | Result summary verification list and final closeout. | Raw command output dumps are not persisted. |
| Interruption recovery | No interruption occurred during approved candidate execution. | `docs/Factory/v3/real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md` | Does not test dynamic pause/resume behavior. |
| Evidence quality | The subagent final summary was enough to replay the read-only evidence-export question without storing prohibited internals. | This profile and `docs/Factory/v3/real_run_corpus/RR_20260601_004_phase4_dynamic_evidence_export_candidate.md` | Raw subagent transcript and private reasoning were not stored. |
| False-positive behavior | Advisory docs checks passed after records were added. | Result summary advisory classification table. | No complex FP case occurred naturally. |
| False-negative behavior | Missing dynamic evidence was explicitly reported; the result does not claim promotion or routing readiness. | Result summary evidence gaps and reviewer decision. | Does not prove detection of unsafe dynamic implementation behavior. |

## Verification Summary
- Commands required: `bash scripts/knowledge_lint.sh`; `./scripts/factoryctl context-index`; `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`; `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`; `git diff --check`.
- Commands run: same as required, plus one read-only multi-agent explorer probe.
- Commands skipped with reason: optional telemetry capture skipped because approval did not explicitly add telemetry artifact paths to the file-touch budget.
- Failed checks: none.
- Halt, fallback, or human decision after failed checks: not applicable.
- Closeout evidence: final closeout response for this candidate and git commit.

## Interruption And Reentry
- Interruption occurred: No during approved candidate execution.
- Source artifacts reread: approved envelope, micro-sprints, verification plan, evidence templates, prior records, indexes, and opportunity register.
- Derived summaries used only as aids: subagent summary is recorded as evidence of the read-only probe output, not as authority beyond the observed candidate.
- Stale or conflicting context found: No.
- Reentry decision: proceed with evidence-only closeout for the approved read-only candidate.
- Evidence path: `docs/Factory/runs/RUN_20260601_0635_v3_phase4_dynamic_evidence_export_plan/`

## Evidence Quality Review
- Objective traceable: Yes, to the approved candidate envelope and `P4-NEG-OPP-006`.
- Authority traceable: Yes, to user Go and the planning pack.
- Commands traceable: Yes, command list is recorded in result summary and this profile.
- File touches traceable: Yes, through the candidate commit.
- Human decisions traceable: Partially; chat approval is cited but not persisted as a repository transcript.
- Verification traceable: Yes, through final closeout and reproducible commands.
- Residual risks traceable: Yes.
- Evidence gaps: no optional telemetry, no failed-verification halt, no V2 fallback execution, no dynamic interruption/resume stress, no command-producing implementation, and no promotion/routing value.

## False-positive And False-negative Review
| Finding ID | Expected | Observed | Human Adjudication | Rationale | Follow-up |
| --- | --- | --- | --- | --- | --- |
| `P4-NEG-CAPTURE-CANDIDATE-004` | Dynamic/parallel harness should expose safe summary evidence or record insufficiency | Safe summary evidence was sufficient for this read-only probe | `true_positive` | The subagent summary was replayable without storing prohibited evidence. | Use a later candidate if command-producing or interruption/resume dynamic evidence is desired. |
| `V3-ADVISORY-LINT-005` | Research posture preserved | `ADVISORY_PASS` | `true_negative` | No advisory findings after evidence records were added. | Continue to keep records research-only. |
| `V3-OP-READINESS-005` | V3 docs remain stable | `ADVISORY_PASS` | `true_negative` | No docs-level operational-readiness findings were introduced. | Continue advisory-only posture. |
| `V3-NL-PILOT-005` | Promotion-adjacent wording remains non-operational | `ADVISORY_PASS` | `true_negative` | No routing, promotion, or reduced-governance language was introduced. | Preserve explicit non-promotion and open-gap language. |

Allowed adjudication values:
- `true_positive`
- `false_positive`
- `true_negative`
- `false_negative`
- `needs_more_context`
- `deferred`

## Advisory Evidence Band
Chosen evidence band: `harness_profile_observed`

Evidence band rationale: one approved read-only Codex multi-agent explorer probe produced enough safe summary evidence for replay of the evidence-export adequacy question.

Limitations: no optional telemetry, no failed verification, no V2 fallback execution, no interruption/resume stress, no command-producing implementation, and no routing or promotion value.

This band does not route work, reduce governance, promote V3, or change Factory V2 fallback.

## Data Minimization Review
This profile does not include:
- chain-of-thought,
- raw command output dumps,
- source file contents,
- secrets,
- raw environment dumps,
- unrelated personal data,
- vendor-private cognition state,
- external proof artifacts outside the repository boundary.

## Reviewer Decision
- Decision: `accepted_advisory_evidence`
- Rationale: profile is bounded, harness-specific, non-enforcing, and records a narrow read-only dynamic/parallel evidence-export signal without overstating evidence value.
- Required follow-up: use a later explicitly approved candidate if optional telemetry, command-producing dynamic/parallel execution, failed verification, or interruption/resume behavior needs direct observation.
- Residual risk: overconfidence risk remains if this one read-only probe is treated as telemetry, fallback, router, promotion, or broad dynamic/parallel capability evidence.

Allowed decisions:
- `accepted_advisory_evidence`
- `needs_more_context`
- `do_not_use_for_threshold_discussion`
- `defer_until_real_negative_case`

## Notes
This profile is not a source of authority. It does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 pipeline.
