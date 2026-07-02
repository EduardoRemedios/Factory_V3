# Factory V3 Governance Boundaries

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Moved the Important Boundaries section out of the repository README into this dedicated document. The boundary content is unchanged in substance; this document approves nothing new.

## Status
Authoritative statement of current Factory V3 approval boundaries. Relocating this content out of the README changes where it lives, not its force. Every boundary below remains binding until a future release explicitly changes it.

## Scope Of This Document
This document states what is and is not currently approved for Factory V3 use. It is the single place the repository README points to for boundary detail.

For the separate architectural boundary between Factory and external runtime governance kernels, see `NON_GOALS_AND_BOUNDARIES.md`. For pointer-first orientation across anchors, evidence paths, and next named gates, see `ANCHOR_REGISTRY.md`.

## Boundaries

- The only currently approved optional V3 operational profile is `V3-OP-001 Bounded Code Change`.
- The next operational-readiness decision scope is user-defined as using V3 with Codex to design, build, test, and deploy an application in the same operational sense that V2 is used today. The future POC application build itself must use V3 only; V2 may support current V3 repository planning, but V2 must not help design, build, test, deploy, govern, lint, stage, pack, recover, or validate the POC application. For that scope to be approved as operational, V3 must be usable standalone and must not depend on Factory V2 behavior for normal operation; this does not by itself approve production-action, infrastructure, CI, required-gate, runtime-authority, or V2-removal scope.
- The current POC track is an internal/private personal health and fitness tracker with standalone V3-only execution evidence, a sponsor-approved interim `PASS_WITH_LIMITATIONS` eval, and a sponsor-approved final `PASS_NAMED_POC` eval at 20/22 for the named synthetic-first private POC scope. Missions 015-018 now narrow failed-verification halt, bounded recovery, seeded stale-reentry, and seeded fallback/no-go evidence; Missions 019-020 now narrow private deployment smoke, with Mission 020 passing through Tailscale Serve over the private MagicDNS tailnet route after user-installed/authenticated Tailscale; Mission 026 now provides synthetic mission-control design-transfer evidence for evidence review, report coherence, approval rehearsal, future-surface rehearsal, browser QA, and closeout verification. Real-data boundary, live Telegram/ambient runtime, public deployment, production infrastructure, runtime authority, and Factory V2 fallback remain unapproved. Synthetic data may be used to accelerate design and build. Garmin-backed paths and Hermes Agent surfaces remain separately scoped research; they do not imply dependency or execution approval.
- Broader supervised-worker or non-coding mission language is roadmap vision, not current operating authority.
- Current Factory V3 state does not make Factory V2 obsolete.
- V3 required-gate integration is not implied by the repository split from `factory-starter-kit`.
- V2 process tooling in this repo is build-support scaffolding for V3 development; it does not make V3 validators required gates or create a V3 product dependency on V2.
- Future V2 deprecation/removal from this repository requires explicit V3 confidence evidence and release approval.
- Runtime authority, production action mediation, proof, leases, telemetry enforcement, and governance routing remain outside current approval and separately governed by explicit V3 evidence and approval.
- Existing V3 advisory tools remain advisory unless a future release explicitly promotes them.
- Adaptive mission control is research-only and non-enforcing. It does not approve live Telegram automation, unattended production work, new required gates, runtime authority, or V3 default-mode execution.
- Mission-formation skills are research-only and non-enforcing. They may help discovery, challenge, and candidate mission-contract creation, but they do not approve execution, new V3 profiles, recommended V3 intake, or non-coding autonomous work.
- Codex SDK/MCP orchestration is research-only and non-enforcing. Codex may become a governed worker runtime in future evidence, but Factory/Harmony remains the authority layer; no unattended execution, production action, credential use, or runtime authority is approved.
- Mission health, mission-control contract work, and continuation judgment are research-only and non-enforcing. They do not approve schema changes, validators, gates, routing authority, runtime-control power, required checkpoint fields, or default-mode behavior.
- Phase 3 telemetry is not a required gate; Phase 4 eval expansion has started with advisory planning artifacts, synthetic fixtures, three separately approved happy-path docs-only real-run captures using `NO_TELEMETRY`, two approved negative-case clean non-events using `NO_TELEMETRY`, one clarification-before-edit capture using `NO_TELEMETRY`, one read-only dynamic/parallel summary-export capture using `NO_TELEMETRY`, one telemetry-backed verification-halt clean non-event using `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`, and a research-only opportunity register.
- The Phase 3 natural halted/fallback/clarification-heavy telemetry gap remains open; clarification, summary-export, and selected telemetry replay evidence gaps are narrowed, but failed-verification halt, fallback, recovery, stale reentry, and routing-threshold gaps remain open for the Factory_V3 real-run corpus. The separate standalone POC has narrowed failed-verification halt, recovery, seeded stale reentry, seeded fallback/no-go, and private deployment smoke through Missions 015-020.
- Phase 4 does not approve governance routing, reduced governance, default-mode behavior, telemetry completeness checks, required gates, runtime authority, proof, lease enforcement, dynamic-workflow execution by default, or V2 build-support removal.
