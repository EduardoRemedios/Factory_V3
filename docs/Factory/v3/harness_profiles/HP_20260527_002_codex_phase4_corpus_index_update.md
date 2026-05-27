# V3 Harness Capability Profile: HP_20260527_002

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial harness profile for `P4-CAPTURE-CANDIDATE-002`.

## Status
Research-only and non-enforcing.

This artifact does not authorize governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this profile. Use this profile only as advisory evidence for the named harness, mission profile, repository context, and verification set.

## Profile Metadata
- Profile ID: `HP_20260527_002`
- Created: 2026-05-27 07:49 WEST
- Reviewer: Codex
- Harness: Codex desktop app
- Model when known: not recorded
- Repository: `/Users/eduardodosremedios/Factory_V3`
- Branch or revision: `main`, pre-execution revision `a7fa7b2`
- Mission profile: `V3-OP-001 Bounded Code Change`
- Mission or run ID: `P4-CAPTURE-CANDIDATE-002`; planning run `RUN_20260527_0744_v3_phase4_second_capture_candidate_plan`
- Evidence source: `docs/Factory/v3/real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md`
- Evidence date: 2026-05-27

## Scope Boundary
- Work class: docs-only Phase 4 corpus/profile index update.
- Authorized files or directories: `docs/Factory/v3/real_run_corpus/INDEX.md`; `docs/Factory/v3/harness_profiles/INDEX.md`; `docs/Factory/v3/real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md`; `docs/Factory/v3/harness_profiles/HP_20260527_002_codex_phase4_corpus_index_update.md`.
- Forbidden files or directories: scripts, fixtures, validators, CI, gates, telemetry logs, router files, runtime files, proof files, lease files, and V2 build-support removal files.
- Allowed command families: Factory V2 knowledge/context checks, V3 advisory validators, and git diff checks.
- Dependency policy: no dependency additions.
- Human approval points: user approval on 2026-05-27 for `P4-CAPTURE-CANDIDATE-002`.
- Factory V2 fallback trigger summary: return to V2 planning if scope expands, verification fails without decision, or output implies governance routing, enforcement, promotion, telemetry completeness, required gates, runtime authority, proof, leases, default-mode behavior, or V2 removal.

## Tool And Environment Context
- Shell or execution environment: local shell in `/Users/eduardodosremedios/Factory_V3`.
- File editing capability: repository Markdown edits.
- Test or verification command access: local Factory scripts and Python advisory validators.
- Browser or UI access: not used.
- Network access: available but not used.
- External service access: not used.
- Known harness limitations: observations are limited to this docs-only index candidate and should not be generalized to code-changing, interrupted, fallback-heavy, clarification-heavy, or router-adjacent work.

## Capability Observations
Record observed behavior only. Do not generalize outside this profile.

| Dimension | Observed Signal | Evidence Path | Limitation |
| --- | --- | --- | --- |
| Harness capability | Able to execute a bounded docs-only index update from an approved pack while preserving advisory-only language. | `docs/Factory/runs/RUN_20260527_0744_v3_phase4_second_capture_candidate_plan/pack/SPRINT_20260527_0744_PHASE4_SECOND_CAPTURE_CANDIDATE_ENVELOPE.md`; `docs/Factory/v3/real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md` | Docs-only run; no code-path complexity measured. |
| Execution reliability | Completed the planned four-file set without dependency changes or forbidden file touches. | Git diff for candidate commit. | Second happy-path run only. |
| Scope discipline | Stayed within corpus/profile indexes and matching evidence records. | `docs/Factory/v3/real_run_corpus/INDEX.md`; `docs/Factory/v3/harness_profiles/INDEX.md` | Does not test ambiguous or expanding scope. |
| Verification quality | Ran the approved repository-level checks before closeout. | Final closeout response and reproducible commands in the result summary. | Raw command output dumps are not persisted. |
| Interruption recovery | No interruption occurred during approved candidate execution. | `docs/Factory/v3/real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md` | Does not close the natural interruption or fallback gap. |
| Evidence quality | Index docs and evidence records link authority, scope, verification, residual risk, and gaps. | This profile and `docs/Factory/v3/real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md` | Evidence remains review-oriented, not gate authority. |
| False-positive behavior | Advisory findings are classified only after validator results are observed. | Result summary advisory classification table. | No complex FP case occurred naturally. |
| False-negative behavior | No negative hidden failure mode was intentionally seeded. | Result summary evidence gaps. | Does not measure false negatives against real execution failure. |

## Verification Summary
- Commands required: `bash scripts/knowledge_lint.sh`; `./scripts/factoryctl context-index`; `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; `git diff --check`.
- Commands run: `bash scripts/knowledge_lint.sh`; `./scripts/factoryctl context-index`; `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; `git diff --check`.
- Commands skipped with reason: mission-record lint skipped because no mission-record JSON changed; telemetry replay lint skipped because candidate decision is `NO_TELEMETRY`.
- Failed checks: none.
- Halt, fallback, or human decision after failed checks: not applicable unless a check fails.
- Closeout evidence: final closeout response for this candidate and git commit.

## Interruption And Reentry
- Interruption occurred: No during approved candidate execution.
- Source artifacts reread: approved envelope, micro-sprints, verification plan, traceability matrix, scratchpad pitfalls, first capture record, first harness profile, capture plan, and templates.
- Derived summaries used only as aids: none used as authority.
- Stale or conflicting context found: No.
- Reentry decision: proceed under explicit approval for the named candidate.
- Evidence path: `docs/Factory/runs/RUN_20260527_0744_v3_phase4_second_capture_candidate_plan/`

## Evidence Quality Review
- Objective traceable: Yes, to the approved candidate envelope.
- Authority traceable: Yes, to user approval and the planning pack.
- Commands traceable: Yes, command list is recorded in result summary and this profile.
- File touches traceable: Yes, through the candidate commit.
- Human decisions traceable: Partially; chat approval is cited but not persisted as a repository transcript.
- Verification traceable: Yes, through final closeout and reproducible commands.
- Residual risks traceable: Yes.
- Evidence gaps: natural halted, fallback, or clarification-heavy case remains missing.

## False-positive And False-negative Review
| Finding ID | Expected | Observed | Human Adjudication | Rationale | Follow-up |
| --- | --- | --- | --- | --- | --- |
| `V3-ADVISORY-LINT-002` | Research posture preserved | `ADVISORY_PASS` | `true_negative` | No advisory findings after the index and evidence docs were added. | Continue to keep records research-only. |
| `V3-OP-READINESS-002` | Synthetic readiness fixtures remain stable | `ADVISORY_PASS` | `true_negative` | No operational-readiness findings after the index and evidence docs were added. | Continue to keep fixtures synthetic and advisory. |
| `V3-NL-PILOT-002` | Natural-language pilot eval remains stable | `ADVISORY_PASS` | `true_negative` | Same-paragraph non-promotion wording avoided the prior promotion-evidence ambiguity. | Preserve explicit non-promotion language in future records. |

Allowed adjudication values:
- `true_positive`
- `false_positive`
- `true_negative`
- `false_negative`
- `needs_more_context`
- `deferred`

## Advisory Evidence Band
Chosen evidence band: `harness_profile_observed`

Evidence band rationale: one approved, narrow, docs-only index candidate produced navigation indexes and harness-specific evidence under the named verification set.

Limitations: this is not router-readiness evidence or negative-case evidence.

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
- Rationale: profile is bounded, harness-specific, and non-enforcing.
- Required follow-up: collect more separately approved real-run records before any threshold discussion, especially a natural halted, fallback, or clarification-heavy case if one occurs.
- Residual risk: overconfidence risk remains high if happy-path docs-only profiles are treated as universal capability evidence.

Allowed decisions:
- `accepted_advisory_evidence`
- `needs_more_context`
- `do_not_use_for_threshold_discussion`
- `defer_until_real_negative_case`

## Notes
This profile is not a source of authority. It does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 pipeline.
