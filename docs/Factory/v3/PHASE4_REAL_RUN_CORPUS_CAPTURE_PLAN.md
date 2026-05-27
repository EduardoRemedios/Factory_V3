# Factory V3 Phase 4 Real-run Corpus Capture Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial real-run corpus and harness capability profile capture plan.

## Status
Research-only and non-enforcing.

This plan does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Research only: this plan does not promote Factory V3. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`. Factory V2 remains supported and available as fallback.

## Purpose
Define how Phase 4 should capture real-run evidence for selected narrow `V3-OP-001` work after separate mission-level approval.

This plan prepares the evidence shape only. It does not select, authorize, start, or close any real mission.

## Inputs
- `PHASE4_EVAL_EXPANSION_PLAN.md`
- `templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`
- `templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md`
- `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`
- `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`
- `ROADMAP_TO_FULL_VISION.md`
- Factory V2 planning pack `docs/Factory/runs/RUN_20260527_0712_v3_phase4_real_run_corpus_plan/`

## Evidence Gap Carried Forward
Phase 3 did not capture a natural halted, fallback, or clarification-heavy telemetry pilot.

This remains an evidence gap. Real-run corpus capture may record such a case if it naturally occurs during a separately approved narrow evidence mission, but this plan must not manufacture one or claim the gap is closed before evidence exists.

## Corpus Capture Goal
Capture one or two real `V3-OP-001` evidence mission summaries that show how a named harness behaves under bounded authority and known verification.

Each captured run should produce:
- one result summary using `templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md`,
- one harness capability profile using `templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`,
- links to existing mission evidence, commands, verification results, closeout notes, and any advisory eval output,
- human FP/FN adjudication notes for relevant findings,
- explicit residual risks and evidence gaps.

## Candidate Selection Rules
Candidate missions are not approved by this plan. A future capture attempt needs explicit human approval naming the candidate.

Eligible candidate traits:
- profile is `V3-OP-001`,
- objective is clear before execution,
- authorized files or modules can be named,
- allowed commands and verification commands are known,
- no dependency addition is needed unless explicitly authorized,
- the small-change gate can be applied,
- V2 fallback triggers are explicit,
- no payment, authentication, compliance, deployment, infrastructure, runtime-kernel, regulated-action, or production-action concern is implicated.

Useful candidate shapes:
- a small doc or template update tied to an approved V3 decision,
- a focused fixture or expected-output maintenance task,
- a narrow local validator message or trigger adjustment with deterministic fixture coverage.

No-go candidate traits:
- ambiguous objective,
- broad refactor or architecture work,
- new framework, plugin layer, registry, or strategy system,
- missing verification path,
- hidden dependency or tool authority,
- security, auth, payment, compliance, deployment, infrastructure, runtime, or data migration involvement,
- likely need for Phase 5 routing or governance reduction discussion.

## Capture Workflow
1. Choose one candidate and record why it appears eligible for `V3-OP-001`.
2. Obtain explicit human approval for that candidate and whether optional advisory telemetry is permitted.
3. Before execution, record objective, authority, allowed commands, verification, halt rules, reentry rules, and V2 fallback triggers.
4. Execute the mission under the approved profile and preserve normal evidence.
5. If verification fails, halt until a human decision, fallback, or closeout is recorded.
6. Fill one real-run result summary.
7. Fill one harness capability profile.
8. Run advisory V3 eval commands and classify any findings with human adjudication.
9. Record whether the run was happy-path, halted, fallback, clarification-heavy, or incomplete.
10. Keep any optional telemetry summary-only and non-blocking.

## Optional Telemetry Decision Point
Telemetry remains optional shadow evidence only.

For each future candidate, the decision must say one of:
- `NO_TELEMETRY`: use ordinary command and closeout evidence only.
- `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`: collect summary-only advisory telemetry for this evidence mission.

Telemetry must not include chain-of-thought, raw command output dumps, source file contents, diffs, secrets, raw environment dumps, unrelated personal data, vendor-private cognition state, external proof, private policy state, or runtime-kernel evidence.

Telemetry must not be wired into CI, `factoryctl`, required gates, default workflows, or completeness checks.

## Result Summary Requirements
Each result summary must record:
- mission identifier,
- harness and model when known,
- repository and branch or revision,
- mission profile,
- objective and authority summary,
- candidate eligibility rationale,
- commands attempted and verification results,
- skipped checks with reason,
- interruption or reentry events,
- halt, fallback, or clarification events,
- evidence gaps,
- advisory eval output and finding classification,
- false-positive and false-negative human adjudication,
- residual risks,
- reviewer decision.

## Harness Capability Profile Requirements
Each capability profile must:
- bind observations to this harness, model when known, repository, mission profile, tool access, date, and evidence,
- avoid universal capability scoring,
- identify limitations and missing evidence,
- preserve V2 fallback and non-deprecation language,
- use advisory evidence bands only for review organization.

## FP/FN Adjudication
Every advisory finding relevant to the run should be classified as one of:
- `true_positive`
- `false_positive`
- `true_negative`
- `false_negative`
- `needs_more_context`
- `deferred`

Each classification needs a short rationale and follow-up. Missing adjudication is itself an evidence gap.

## Evidence Bands
Use evidence bands only for organizing review:
- `insufficient_evidence`
- `harness_profile_observed`
- `repeatable_low_risk_signal`
- `candidate_for_later_router_study`

These bands do not route work, reduce governance, promote V3, or change Factory V2 fallback.

## Verification For A Future Capture Attempt
Before and after each capture attempt, run the commands named by the mission.

For repository-level V3 checks, run:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
git diff --check
```

## Exit Criteria For This Capture Step
The real-run corpus step is ready for review only when:
- at least one result summary exists from a separately approved candidate,
- at least one harness capability profile exists,
- human FP/FN adjudication is recorded for relevant findings,
- V2 fallback review is explicit,
- the Phase 3 natural halted, fallback, or clarification-heavy gap is either captured naturally or still stated as open.

## Stop Conditions
Stop and return to Factory V2 planning if:
- the candidate no longer fits `V3-OP-001`,
- verification cannot be run,
- verification fails without a halt/fallback/human decision,
- scope expands beyond approved files or commands,
- the run begins to imply routing, enforcement, reduced governance, default-mode behavior, runtime authority, proof, lease enforcement, required gates, telemetry completeness, V3 promotion, or V2 removal.
