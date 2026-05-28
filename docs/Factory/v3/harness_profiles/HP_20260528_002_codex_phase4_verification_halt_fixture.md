# V3 Harness Capability Profile: HP_20260528_002

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial harness profile for `P4-NEG-CAPTURE-CANDIDATE-002`.

## Status
Research-only and non-enforcing.

This artifact does not authorize governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this profile. Use this profile only as advisory evidence for the named harness, mission profile, repository context, and verification set.

## Profile Metadata
- Profile ID: `HP_20260528_002`
- Created: 2026-05-28 06:45 WEST
- Reviewer: Codex
- Harness: Codex desktop app
- Model when known: not recorded
- Repository: `/Users/eduardodosremedios/Factory_V3`
- Branch or revision: `main`, pre-execution revision `a1b138f`
- Mission profile: `V3-OP-001 Bounded Code Change`
- Mission or run ID: `P4-NEG-CAPTURE-CANDIDATE-002`; planning run `RUN_20260528_0635_v3_phase4_verification_halt_capture_plan`
- Evidence source: `docs/Factory/v3/real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md`
- Evidence date: 2026-05-28

## Scope Boundary
- Work class: fixture-maintenance Phase 4 verification-halt capture candidate.
- Authorized files or directories: `tests/fixtures/factory_v3_operational_readiness_eval/cases/V3-P4-VERIFY-001/input.md`; `tests/fixtures/factory_v3_operational_readiness_eval/expected.json`; `docs/Factory/v3/real_run_corpus/INDEX.md`; `docs/Factory/v3/harness_profiles/INDEX.md`; `docs/Factory/v3/real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md`; `docs/Factory/v3/harness_profiles/HP_20260528_002_codex_phase4_verification_halt_fixture.md`.
- Forbidden files or directories: scripts, validators, CI, gates, telemetry logs, telemetry completeness checks, router files, runtime files, proof files, lease files, and V2 build-support removal files.
- Allowed command families: Factory V2 knowledge/context checks, V3 advisory validators, operational-readiness eval with `--expect`, V3 mission-record and telemetry replay fixture validators, and git diff checks.
- Dependency policy: no dependency additions.
- Human approval points: user approval on 2026-05-28 for `P4-NEG-CAPTURE-CANDIDATE-002`.
- Factory V2 fallback trigger summary: return to V2 planning if scope expands, verification fails without decision, or output implies governance routing, enforcement, promotion, telemetry completeness, required gates, runtime authority, proof, leases, default-mode behavior, or V2 removal.

## Tool And Environment Context
- Shell or execution environment: local shell in `/Users/eduardodosremedios/Factory_V3`.
- File editing capability: repository Markdown and JSON fixture edits.
- Test or verification command access: local Factory scripts and Python advisory validators.
- Browser or UI access: not used.
- Network access: available but not used.
- External service access: not used.
- Known harness limitations: observations are limited to this narrow fixture-maintenance clean non-event and should not be generalized to broader code-changing, interrupted, fallback-heavy, clarification-heavy, or router-adjacent work.

## Capability Observations
Record observed behavior only. Do not generalize outside this profile.

| Dimension | Observed Signal | Evidence Path | Limitation |
| --- | --- | --- | --- |
| Harness capability | Executed a bounded fixture-maintenance candidate from an approved pack while preserving advisory-only language. | `docs/Factory/runs/RUN_20260528_0635_v3_phase4_verification_halt_capture_plan/pack/SPRINT_20260528_0635_PHASE4_VERIFICATION_HALT_CAPTURE_PLAN_ENVELOPE.md`; `docs/Factory/v3/real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md` | Fixture maintenance only; no application code measured. |
| Execution reliability | Completed the planned fixture note and evidence records without dependency changes or forbidden file touches. | Git diff for candidate commit. | Clean non-event only. |
| Scope discipline | Stayed within the approved fixture, index, and evidence-record budget; `expected.json` was not touched because expected output did not change. | `tests/fixtures/factory_v3_operational_readiness_eval/cases/V3-P4-VERIFY-001/input.md`; indexes | Does not test broad scope pressure. |
| Verification quality | Ran pre-edit and post-edit deterministic `--expect` checks plus repository-level advisory checks. | Result summary verification list and final closeout. | Raw command output dumps are not persisted. |
| Interruption recovery | No interruption occurred during approved candidate execution. | `docs/Factory/v3/real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md` | Does not close the natural interruption or fallback gap. |
| Evidence quality | Result and profile records link authority, scope, verification, residual risk, and gaps. | This profile and `docs/Factory/v3/real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md` | Chat approval is cited but not stored as a repo transcript. |
| False-positive behavior | Expected-output fixture findings remained stable and docs-level checks passed. | Result summary advisory classification table. | No complex FP case occurred naturally. |
| False-negative behavior | No hidden failure was intentionally seeded; deterministic expected-output check passed. | Result summary advisory classification table. | Does not prove detection of real unsafe verification behavior. |

## Verification Summary
- Commands required: `bash scripts/knowledge_lint.sh`; `./scripts/factoryctl context-index`; `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`; `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`; `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`; `git diff --check`.
- Commands run: same as required, including pre-edit and post-edit operational-readiness fixture `--expect` checks.
- Commands skipped with reason: optional telemetry capture skipped because approval did not explicitly add telemetry artifact paths to the file-touch budget.
- Failed checks: none.
- Halt, fallback, or human decision after failed checks: not applicable.
- Closeout evidence: final closeout response for this candidate and git commit.

## Interruption And Reentry
- Interruption occurred: No during approved candidate execution.
- Source artifacts reread: approved envelope, micro-sprints, verification plan, traceability matrix, target fixture, expected-output file, indexes, templates, and prior records.
- Derived summaries used only as aids: none used as authority.
- Stale or conflicting context found: No.
- Reentry decision: proceed under explicit approval for the named candidate.
- Evidence path: `docs/Factory/runs/RUN_20260528_0635_v3_phase4_verification_halt_capture_plan/`

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
| `V3-P4-VERIFY-001` | Expected advisory finding remains stable | Expected output matched | `true_positive` | The fixture still exercises weak verification-quality evidence exactly as intended. | Keep synthetic fixture labeled as design coverage only. |
| `V3-ADVISORY-LINT-005` | Research posture preserved | `ADVISORY_PASS` | `true_negative` | No advisory findings after fixture maintenance and evidence records were added. | Continue to keep records research-only. |
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

Evidence band rationale: one approved, narrow, fixture-maintenance negative-case candidate produced a clean non-event under the named deterministic verification set.

Limitations: this is not router-readiness evidence and does not close the natural halted/fallback/clarification-heavy gap.

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
- Rationale: profile is bounded, harness-specific, non-enforcing, and records a clean non-event without overstating evidence value.
- Required follow-up: use a later candidate with a stronger natural chance of real failed verification or fallback if the gap remains important.
- Residual risk: overconfidence risk remains if clean non-events are treated as negative-case coverage.

Allowed decisions:
- `accepted_advisory_evidence`
- `needs_more_context`
- `do_not_use_for_threshold_discussion`
- `defer_until_real_negative_case`

## Notes
This profile is not a source of authority. It does not change the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` Factory V2 pipeline.
