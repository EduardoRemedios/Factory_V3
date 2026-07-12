# Factory V3 Decision Pack: V3-OP-003 Long-Running Remote-Interrupt Mission

## Version
v1.0

## Change Log
- v1.0 (2026-07-12): Added the commit-pinned Mission 026 claim-to-proof audit and FP/FN adjudication. Item 5 is satisfied for the current corpus; stale `commit_after`, same-actor verification, and mobile-clipping findings are explicit. Items 1, 3, and 4 remain insufficient/open, so the assessment remains `NO PROMOTION YET`.
- v0.9 (2026-07-12): Corrected the endurance criterion: roughly four hours is the upper capability envelope, not a minimum run duration. Mission outcome and endurance-evidence coverage are now separate; shorter correct missions pass and stop without proving the unobserved upper range. Updated stale transport and mission-control artifact status. Assessment remains `NO PROMOTION YET`.
- v0.8 (2026-07-02): Recorded POC Mission 026 post-run evidence review and mission-control contract extraction. Mission 026 transfers design patterns for evidence review, coherence, approval rehearsal, future-surface rehearsal, browser QA, and repeatable closeout verification, but assessment remains `NO PROMOTION YET`.
- v0.7 (2026-07-02): Recorded POC Mission 025 transfer classification and concrete non-executing Option A rung-3 envelope plus challenge review under `ladder/rung3/`. The envelope is `CONDITIONAL PASS` for sponsor-Go review only; assessment remains `NO PROMOTION YET`.
- v0.6 (2026-07-02): Added non-executing rung-3 formation pack status. Formation output, challenge review, and advisory loop contract exist under `ladder/rung3/`; formation quality is `CONDITIONAL PASS`, execution readiness remains `MORE DISCOVERY`, and the next gate is sponsor scope selection plus concrete execution-envelope authoring. Pre-written criteria unchanged; assessment remains `NO PROMOTION YET`.
- v0.5 (2026-06-11): Rung 2 PASSED at attempt 4 (`HDI-RUNG2-008`: all eight criteria, 95.25 active minutes, ~548 calls, restored browser QA). Item 1 gains its first duration-class rung pass; item 3 gains a complete health-signal series at genuine ~95-minute duration. Rung 3 unlocked (formation pending). Pre-written criteria unchanged; assessment remains `NO PROMOTION YET` (items 4-5 open; 2h/4h evidence outstanding).
- v0.4 (2026-06-11): Rung-2 attempt 3 recorded as FAILED on duration and budget floor (`HDI-RUNG2-006`; mechanics clean at 3.5x scope; honest 54m03s active, ~333 calls). Third consecutive duration failure routes the ladder to design review round 2. Item 3 now has checkpoint-series evidence from all three rung-2 attempts. Pre-written criteria unchanged; assessment remains `NO PROMOTION YET`.
- v0.3 (2026-06-11): Rung-2 attempt 2 recorded as FAILED on duration (`HDI-RUNG2-004`; mechanics 8/8; honest 40m06s active vs the 90-180 min band). Second consecutive duration failure routes the ladder to the mandatory design review. Item 3 now has checkpoint-series evidence from both rung-2 attempts. Pre-written criteria unchanged; assessment remains `NO PROMOTION YET`.
- v0.2 (2026-06-11): Evidence item 2 satisfied (phone-answered round-trip, POC Mission 021, plus the MR_020 timeout leg); rung-2 attempt 1 recorded as FAILED on duration (`HDI-RUNG2-002`). Pre-written criteria unchanged; assessment remains `NO PROMOTION YET`.
- v0.1 (2026-06-10): Initial decision pack with pre-written `PASS`, `CONDITIONAL PASS`, and `NO PROMOTION YET` criteria and a current assessment of `NO PROMOTION YET`.

## Status
Research-only and non-enforcing decision-preparation artifact. This pack promotes nothing; promotion requires the evidence below plus explicit human release approval per `PROMOTION_CRITERIA.md`. Writing the criteria before gathering the evidence is deliberate, so trial results are judged against fixed goalposts.

## Decision Scope
Whether `V3-OP-003` (see `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`) may become an approved optional profile for attended long-running missions, in the same sense that `V3-OP-001` is approved: optional, not default, V2 fallback retained.

Out of scope for this decision: unattended or scheduled operation, live messaging beyond the approved transport trial, credential use, real data, deployment, concurrency.

## Evidence Held Today

| Evidence | Source | What it shows | Limit |
| --- | --- | --- | --- |
| Checkpoint, interrupt, plan-delta, mission-state artifacts from POC Missions 012/013 | POC repo mission records | The adaptive-control artifact set works in real missions; tool-call counts beat estimated minutes (6-9x inflation observed) | Sub-hour scale; simulated interrupt surface |
| Halt, recovery, stale-reentry, fallback/no-go evidence from POC Missions 015-018 | POC repo mission records | Halt and reentry discipline works when seeded | Seeded, not natural; not at duration |
| Interrupt transport | repo-root `RESEARCH_SPIKE_20260604_interrupt_transport_surfaces.md`; POC Mission 021; MR_020 | Vendor-native transport exists; a real phone round-trip and timeout-to-safe-hold are evidenced | Satisfied for this candidate decision only; no live messaging automation approval |
| Adaptive mission control protocol | `ADAPTIVE_MISSION_CONTROL.md` v0.2 | Loop, tiers, budget discipline, checkpoint shape are defined | Research-only; quality continuity near the upper endurance envelope remains untested |
| Mutable-state and provenance canon | `MUTABLE_HARNESS_STATE.md`; `SKILL_PROVENANCE_POLICY.md` | Long-duration evidence can stay attributable across model swaps and skill use | New; untested in a long mission |
| Rung-3 formation and Option A envelope pack | `ladder/rung3/` | Mission-formation and challenge skills can produce a contract, classify POC transfer evidence, and author a concrete Option A envelope; POC Mission 026 completed that envelope and produced post-run evidence | Does not prove upper-envelope quality continuity or close natural negative-case and FP/FN requirements |
| Mission-control contract extraction | `MISSION_CONTROL_CONTRACT.md`; `templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`; `scripts/factory_v3_mission_control_contract_lint.py`; `tests/fixtures/factory_v3_mission_control_contract/`; `ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md` | Mission 026 evidence supports the Factory/worker split and now has advisory template, lint, and deterministic fixture coverage | Research-only; no routing, required gate, runtime behavior, or profile is promoted |
| Mission 026 claim-to-proof and FP/FN adjudication | `ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`; `ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md` | Exact-commit replay reproduces 322 tests and mission QA; identifies stale final-commit state, same-actor verification limits, and one clipped final mobile artifact; completes item 5 for the current corpus | Mission 026 is about 10-12 minutes of exposure and does not prove upper-envelope continuity; no historical POC repair or promotion |

## Evidence Required Before Decision

1. Endurance evidence per `DURATION_LADDER_PLAN.md`: successful missions retain full checkpoint series, mission state, budget actuals, verification, and closeout quality as natural elapsed exposure increases toward the roughly four-hour ceiling. No mission has a minimum duration, call, waypoint, test, file, or scope floor. A shorter correct mission passes but does not prove the unobserved upper range; promotion still requires sufficient evidence that quality and governance remain stable near the upper envelope, as explicitly accepted by the sponsor.
2. Live interrupt-transport trial completed per `INTERRUPT_TRANSPORT_TRIAL_PLAN.md`, including at least one real Tier 3 round-trip and one exercised timeout reaching safe-hold.
3. Mission-health signals (per `MISSION_HEALTH_VOCABULARY.md`) recorded at checkpoints across sustained-duration evidence, including evidence close enough to the upper envelope to judge late-run drift and quality continuity.
4. At least one natural (non-seeded) halt, fallback, or clarification event captured at duration — this also closes the long-open Phase 3 negative-case gap.
5. False-positive and false-negative review over the ladder evidence, per `PROMOTION_CRITERIA.md` minimum inputs.

## Pre-Written Outcome Criteria

### PASS
All five evidence items complete; upper-envelope endurance evidence shows no unresolved objective, authority, scope, checkpoint, re-entry, verification, evidence, or late-run quality findings; safe-hold worked as specified when exercised; budget actuals remained within the envelope stop threshold; sponsor grants explicit release approval naming exact artifact paths.

### CONDITIONAL PASS
Evidence items 1-3 complete with credible sustained-duration quality evidence, but the uppermost range remains partially observed or item 4 (natural negative case) or item 5 (FP/FN review) is outstanding; any promotion is limited to named mission types and an evidenced maximum envelope, with written conditions, follow-up missions, and an expiry. Conditions unmet after two further long-running missions revert the profile to candidate.

### NO PROMOTION YET
Upper-envelope continuity remains insufficiently evidenced, any safe-hold or transport failure is unresolved, any objective, authority, scope, checkpoint, re-entry, verification, evidence, or late-run quality finding remains unresolved, or sponsor approval is absent. A shorter successful mission is not itself a failure; it records partial endurance coverage.

## Evidence Progress (2026-07-12)
- Item 1 (endurance evidence): rung 1 passed for mechanics (`HDI-TT-001`); RUNG 2 PASSED at attempt 4 under its historical pre-written criteria (`HDI-RUNG2-008`: 95.25 active minutes, ~548 calls, all eight criteria) after three honest historical duration-class failures (`HDI-RUNG2-002`, `-004`, `-006`) and two design reviews (`-005`, `-007`); rung 3 formation pack exists under `ladder/rung3/`; POC Mission 025 (`8f25437`) is narrow transfer evidence; POC Mission 026 (`404a32a`) transferred mission-control design patterns. Current interpretation preserves those adjudications but no longer treats elapsed time or workload consumption as mission-pass floors. Quality continuity near the upper endurance envelope remains insufficiently evidenced.
- Item 2 (live transport trial): SATISFIED — one real Tier 3 round-trip answered from the sponsor's phone with the sponsor away from the terminal (POC Mission 021, Codex mobile, deliver-to-answer 96s, full interrupt record at `.factory-v3/evidence/MISSION_021_INTERRUPT_HDI001.json` in the POC repo), and one exercised timeout reaching safe-hold (MR_020).
- Item 3 (health signals): recorded with citations and per-checkpoint cost at rung 1 and all four rung-2 attempts; Mission 024 supplies the first complete series at genuine ~95-minute duration. Evidence at greater natural exposure remains open; no mission should be prolonged to create it.
- Item 4 (natural negative case at sustained duration): open.
- Item 5 (FP/FN review): SATISFIED FOR CURRENT CORPUS by `ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`. The review does not compensate for missing endurance or natural-negative-case evidence.

## Current Assessment
`NO PROMOTION YET` — evidence items 2 and 5 are satisfied for the current corpus, Mission 024 provides sustained checkpoint evidence at roughly 95 active minutes, and POC Mission 026 provides useful mission-control design evidence from the approved Option A envelope. However, continuity of objective, authority, checkpoint, re-entry, verification, evidence, and output quality near the upper roughly four-hour envelope is not yet sufficiently evidenced; no natural negative case at sustained duration is recorded; Mission 026 has record-finalization, verifier-provenance, and mobile-evidence limitations; and no human release approval promotes the candidate profile. Shorter correct missions remain successful and must stop when complete.

## Decision Record (to be completed at decision time)
```text
Decision: PASS | CONDITIONAL PASS | NO PROMOTION YET
Promotion level: (per PROMOTION_CRITERIA.md levels)
Artifacts promoted:
Evidence paths:
Conditions (if CONDITIONAL PASS), each with follow-up mission and expiry:
Known residual risks:
Separate governance kernel dependency introduced: yes | no
Runtime-kernel behavior introduced: yes | no
Human approver:
Date:
```
