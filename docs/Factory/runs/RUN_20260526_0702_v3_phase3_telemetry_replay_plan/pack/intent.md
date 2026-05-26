# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Locked intent for Phase 3 telemetry/replay planning.

## Purpose
Define the minimal Phase 3 telemetry/replay plan before any telemetry implementation begins.

## Goal
Produce `docs/Factory/v3/PHASE3_TELEMETRY_REPLAY_PLAN.md` and update V3 roadmap/status docs so the next implementation step is bounded by data minimization, fixture shape, replay checks, and non-enforcement constraints.

## Non-goals
- No telemetry implementation.
- No telemetry log fixtures added yet.
- No replay validator implementation.
- No `factoryctl`, CI, `knowledge_lint`, `stage-lint`, or `pack-lint` integration.
- No runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.

## Principles
- Keep Phase 3 planning smaller than Phase 3 implementation.
- Preserve optional shadow evidence semantics.
- Store only replay-useful operational facts.
- Exclude chain-of-thought, full chat transcripts, secrets, private vendor cognition state, and external governance-kernel proof.
- Keep future implementation portable across harnesses.

## Roles
- Root Planner: maintain V2 run evidence.
- Intent Contractor: lock planning scope.
- Red Team: challenge telemetry overreach and privacy risk.
- Blue Team: harden the plan.
- Purple Gate: adjudicate whether the plan stays within approved scope.
- Verification Specialist: define checks that can validate the planning artifacts without implementing telemetry.

## Acceptance Criteria
- The plan defines event fields.
- The plan defines excluded data.
- The plan defines fixture shape.
- The plan defines replay checks.
- The plan defines data-minimization rules.
- The plan does not approve implementation.
- V3 advisory and operational-readiness checks pass.
- V2 stage-lint and pack-lint pass for this planning run.

## Go or No-go Rule
Go if the plan constrains future Phase 3 work without adding runtime behavior or enforcement. No-go if it introduces telemetry implementation, required gates, governance routing, or promotion language.

## Open Questions
- NON-BLOCKING: Exact JSON field names may be revised during a future implementation pack.
- NON-BLOCKING: Real telemetry overhead targets need measurement after fixture and pilot implementation exist.
