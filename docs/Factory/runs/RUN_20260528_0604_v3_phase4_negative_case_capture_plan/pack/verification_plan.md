# Verification Plan: Phase 4 Negative-case Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage F verification plan.

## Planning Pack Verification
| ID | Tier | Constraint | Check |
| --- | --- | --- | --- |
| VP-01 | V1 | Required Factory preflight and recall pass. | `KNOWLEDGE_LINT.txt` records PASS and `CONTEXT_RECALL_REPORT.md` is not WEAK. |
| VP-02 | V1 | Stage artifacts meet V2 contracts. | Run `stage-lint` for A, B, C, D, E, F, G, H, I, J, and I2. |
| VP-03 | V1 | Full pack is complete and internally consistent. | Run `./scripts/factoryctl pack-lint --run RUN_20260528_0604_v3_phase4_negative_case_capture_plan`. |
| VP-04 | V1 | V3 advisory docs remain advisory. | Run V3 advisory lint and operational-readiness evals, including NL pilot. |
| VP-05 | V1 | Recent evidence-integrity validator fixtures remain stable. | Run mission-record and telemetry replay validators with expected outputs. |
| VP-06 | V1 | No whitespace or patch hygiene defects. | Run `git diff --check`. |

## Future Capture Verification Shape
- Before future execution, rerun source docs and confirm the candidate still fits `V3-OP-001`.
- Record planned commands and verification commands before editing.
- If any check fails, halt until human decision, V2 fallback, or closeout.
- Record advisory eval findings as `true_positive`, `false_positive`, `true_negative`, `false_negative`, `needs_more_context`, or `deferred`.
- If no halt, fallback, clarification, stale reentry, FP/FN, evidence weakness, verification weakness, or scope pressure occurs, record a clean non-event and keep the Phase 3 gap open.

## Stop Conditions
- Later approval is absent or ambiguous.
- Candidate no longer has named files and known verification.
- Work drifts into tooling, enforcement, routing, default-mode behavior, runtime authority, proof, leases, telemetry completeness, V3 promotion, or V2 removal.
