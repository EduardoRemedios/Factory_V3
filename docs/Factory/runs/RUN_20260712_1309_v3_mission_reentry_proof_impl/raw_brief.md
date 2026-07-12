# Raw Brief

## Request
Execute the exact passed Mission Re-entry Proof Pack envelope in a separate execution-enabled Factory run.

## Source Authorization
Conversation approval on 2026-07-12: explicit human `Go` against `RUN_20260712_1249_v3_mission_reentry_proof_pack` after Stage I2 and pack-lint PASS.

## Execution Posture
- Execution Mode: `EXECUTION_ENABLED`
- Execution Authorization: sponsor `Go` in the conversation on 2026-07-12 for exact reproduction of the planning envelope.
- Downstream Fan-Out: not approved.

## Goal
Define the smallest practical docs, deterministic fixtures, and advisory validation changes needed to prove that a fresh worker can decide whether it may resume from repository artifacts alone.

The proposed evidence set should cover:
1. clean fresh-session re-entry from the last safe checkpoint;
2. stale repository state causing safe-hold;
3. changed authority envelope preventing continuation;
4. failed verification requiring explicit recovery authority;
5. one clearly authorized safe next action after re-entry.

## Evidence-Integrity Shadow Use
Use the newly implemented optional mission-record fields where relevant to record:
- original versus replay/audit observations;
- verifier actor/session provenance;
- bounded claims about what re-entry proves;
- final commit consistency;
- visual evidence only when genuinely relevant.

Record expected authoring friction and false-positive/false-negative review points. This pack may count as the first planned shadow-use candidate, but planning artifacts are not operational evidence.

## Hard Boundaries
- Advisory and non-blocking only.
- Existing mission records remain valid.
- No session memory as authority or proof.
- No runtime loop runner, worker dispatcher, scheduler, background service, standing authorization, governance router, telemetry enforcement, required gate, default-mode behavior, or profile promotion.
- No `V3-OP-003` promotion claim.
- No real data, live integrations, deployment, credentials, or external side effects.
- No endurance/exposure schema and no manufactured duration, failure, workload, calls, waypoints, tests, files, or scope.
- No new dependencies.
- No Factory V2 removal or weakening of V2 fallback/build-support language.
- Implementation paths must be exact and bounded before human Go.

## Verification Expectations
- Deterministic valid and invalid fixtures.
- Historical expected outputs remain unchanged unless an exact fixture addition requires aggregate expectation refresh.
- Each invalid fixture isolates one intended finding.
- JSON parse, Python compile, focused deterministic expectations, cross-validator regression, advisory docs lint, operational-readiness eval, knowledge lint, context index, Stage A lint, and pack lint.
- Explicit no-touch checks for POC routing, runtime authority, required gates, endurance fields, dependencies, and historical records.

## Human Decision Required
Implementation may begin after this transferred A→I2 pack and pack lint pass unchanged; the sponsor's explicit Go applies only to the exact v0.2 planning envelope.
