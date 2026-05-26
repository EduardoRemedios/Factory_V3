# Micro-sprints: Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage G micro-sprint plan.

## MS-01 Phase 4 Plan Document
- Objective: Draft `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md` after human execution approval.
- Inputs: roadmap Phase 4 section, Phase 3 telemetry evidence review, operational-readiness eval plan, current fixtures.
- Outputs: advisory-only Phase 4 plan covering eval families, harness capability profiling, real-run corpus needs, FP/FN rollup, and threshold discussion.
- Entry criteria: this planning pack passes and user approves execution.
- Exit criteria: plan explicitly avoids router, enforcement, required gates, telemetry completeness checks, default-mode promotion, runtime authority, proof, leases, and V2 removal.
- Stop or go gate: stop if threshold language reads as operational routing.

## MS-02 Harness Capability Profile Template
- Objective: Draft `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`.
- Inputs: Phase 4 plan, Phase 3 data-minimization conditions, eval plan E9.
- Outputs: template fields for harness, model when known, tool access, mission profile, repo context, verification behavior, interruption recovery, evidence quality, FP/FN notes, limitations, and date.
- Entry criteria: MS-01 complete.
- Exit criteria: scores are evidence-bound and cannot be read as universal capability.
- Stop or go gate: stop if template requests chain-of-thought, raw command output, source contents, secrets, or vendor-private cognition state.

## MS-03 Fixture And Rollup Design
- Objective: Plan fixture expansion for `tests/fixtures/factory_v3_operational_readiness_eval/` plus FP/FN rollup shape.
- Inputs: current fixture corpus, Phase 3 negative-case gap, Phase 4 objective.
- Outputs: fixture backlog for capability, reliability, scope discipline, verification quality, reentry, evidence quality, V2 fallback, and advisory threshold cases; FP/FN rollup fields.
- Entry criteria: MS-01 complete.
- Exit criteria: synthetic-only cases are labeled and real-run-derived negative cases are preferred when available.
- Stop or go gate: stop if the design creates a Phase 5 router.

## MS-04 Verification And Closeout
- Objective: Verify future Phase 4 implementation remains advisory and scoped.
- Inputs: outputs from MS-01 through MS-03.
- Outputs: advisory lint/eval command results, no-touch review for prohibited systems, and closeout evidence.
- Entry criteria: artifacts drafted.
- Exit criteria: all approved verification commands pass or failures are explicitly halted.
- Stop or go gate: stop on required-gate, CI, enforcement, router, telemetry completeness, default-mode, runtime authority, proof, lease, or V2-removal drift.
