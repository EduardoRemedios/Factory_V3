# ROADMAP.md - Factory V3 Roadmap

> Last updated: 2026-06-03

## Current State

Factory V3 now has a dedicated repository. The migrated roadmap source of truth is `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`.

Factory V2 process tooling is available in this repository as temporary build-support scaffolding so V3 can be built using V2 planning, stage, pack, verification, and SIMPLE-CODE-GATE discipline while V3 matures.

The intended future state is V3 as a separate product with no V2 dependency in this repository. V2 deprecation/removal from this repository requires explicit V3 confidence evidence and release approval; the separate V2-only repository remains the preservation home for V2.

## Near-Term Work

- Keep `V3-OP-001` evidence and guidance in this repository.
- Use Factory V2 process artifacts and validators for V3 development work that needs Factory-controlled planning while V3 is still maturing.
- Continue Phase 4 eval expansion and capability profiling. The Phase 4 plan, harness capability profile template, and first synthetic operational-readiness fixture expansion now exist in advisory mode.
- Phase 4 real-run corpus capture planning, result-summary template, corpus index, harness-profile index, three separately approved happy-path docs-only capture records, two approved negative-case clean non-events with `NO_TELEMETRY`, one clarification-before-edit capture with `NO_TELEMETRY`, one read-only dynamic/parallel summary-export capture with `NO_TELEMETRY`, one telemetry-backed verification-halt clean non-event with `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`, and a research-only negative-case opportunity register now exist; clarification, summary-export, and selected telemetry replay evidence gaps are narrowed, while failed-verification halt, fallback, recovery, and routing-threshold gaps remain open.
- Dynamic/parallel workflow harnesses are tracked as a Phase 4 research-only path with `insufficient_evidence` external-source profiles plus one local read-only Codex multi-agent summary-export profile. The next step is a separately planned operational-readiness decision-prep pack using the user-defined operational scope: using V3 with Codex to design, build, test, and deploy an application in the same operational sense that V2 is used today, with standalone V3-only POC execution as a hard release criterion. The current POC candidate is an internal/private personal health and fitness tracker; Garmin Connect/API data paths and Hermes Agent surfaces should be researched before any POC dependency decision.
- Use `docs/Factory/v3/standalone_bootstrap/` as the seed package for the clean POC project when the sponsor approves the POC path. The package is V3-only by design and should not bring V2 scaffolding into the POC workspace.
- Use `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md` and the standalone checkpoint, mission-state, human-interrupt, and plan-delta templates as research-only guidance for larger V3 missions. The next evidence target is to prove that V3 can continue from explicit artifacts and ask for human decisions when needed, without using artificial time or size classes as mission-sizing authority.
- Keep the Codex Security scan follow-up narrow: advisory validator hardening is acceptable, but it does not create required gates, routing authority, default-mode promotion, or reduced-governance thresholds.
- Continue Phase 2 structured mission-record use in shadow/advisory mode; valid completed, pre-envelope fallback, halted, stale-reentry, and blocked examples now exist.
- Preserve current V2 fallback language and non-deprecation guarantees until explicit V3 confidence evidence approves the repository transition.
- Do not add required-gate integration, default-mode promotion, telemetry enforcement, runtime authority, or governance routing without explicit approval.
- Do not remove V2 build-support scaffolding from this repository until the final V3 product-independence decision explicitly approves exact removal scope.
