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
- Phase 4 real-run corpus capture planning, result-summary template, corpus index, harness-profile index, three separately approved happy-path docs-only capture records, two approved negative-case clean non-events, one clarification-before-edit capture, one read-only dynamic/parallel summary-export capture, and a research-only negative-case opportunity register now exist, with `NO_TELEMETRY`; clarification and summary-export evidence gaps are narrowed, while telemetry, failed-verification halt, fallback, recovery, and routing-threshold gaps remain open.
- Dynamic/parallel workflow harnesses are tracked as a Phase 4 research-only path with `insufficient_evidence` external-source profiles plus one local read-only Codex multi-agent summary-export profile; next, prefer a separately planned failed-verification halt or fallback candidate with optional advisory telemetry approved, but no such execution is authorized without separate candidate planning and approval.
- Keep the Codex Security scan follow-up narrow: advisory validator hardening is acceptable, but it does not create required gates, routing authority, default-mode promotion, or reduced-governance thresholds.
- Continue Phase 2 structured mission-record use in shadow/advisory mode; valid completed, pre-envelope fallback, halted, stale-reentry, and blocked examples now exist.
- Preserve current V2 fallback language and non-deprecation guarantees until explicit V3 confidence evidence approves the repository transition.
- Do not add required-gate integration, default-mode promotion, telemetry enforcement, runtime authority, or governance routing without explicit approval.
- Do not remove V2 build-support scaffolding from this repository until the final V3 product-independence decision explicitly approves exact removal scope.
