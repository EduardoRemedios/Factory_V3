# Verification Plan: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage F verification plan.

## Planning Pack Verification
| ID | Tier | Constraint | Check |
| --- | --- | --- | --- |
| VP-01 | V1 | Required Factory preflight and recall pass. | `KNOWLEDGE_LINT.txt` records PASS and `CONTEXT_RECALL_REPORT.md` is not WEAK. |
| VP-02 | V1 | Stage artifacts meet V2 contracts. | Run `stage-lint` for A, B, C, D, E, F, G, H, I, J, and I2. |
| VP-03 | V1 | Full pack is complete and internally consistent. | Run `./scripts/factoryctl pack-lint --run RUN_20260528_0635_v3_phase4_verification_halt_capture_plan`. |
| VP-04 | V1 | Operational-readiness fixture expected output is stable before execution. | Run `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`. |
| VP-05 | V1 | V3 advisory docs remain advisory. | Run V3 advisory lint and operational-readiness evals, including NL pilot. |
| VP-06 | V1 | Evidence-integrity fixture checks remain stable. | Run mission-record and telemetry replay validators with expected outputs. |
| VP-07 | V1 | No whitespace or patch hygiene defects. | Run `git diff --check`. |

## Future Capture Verification Shape
- Before future execution, rerun source docs and confirm the candidate still fits `V3-OP-001`.
- Record planned fixture and expected-output edits before changing files.
- Run the operational-readiness eval with `--expect` before and after the edit.
- If post-edit verification fails, stop immediately and record a halt plus human decision, V2 fallback, or closeout.
- If post-edit verification passes, record a clean non-event and keep the Phase 3 gap open.
- If optional advisory telemetry is approved later, store only summary events and keep replay output non-blocking.

## Stop Conditions
- Later approval is absent or ambiguous.
- Candidate no longer has named files and known verification.
- Verification fails and no halt, fallback, human decision, or closeout is recorded.
- Work drifts into tooling, enforcement, routing, default-mode behavior, runtime authority, proof, leases, telemetry completeness, V3 promotion, or V2 removal.
