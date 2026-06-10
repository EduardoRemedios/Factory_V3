# Factory V3 Regulatory Crosswalk (EU AI Act / ISO 42001) — Advisory Orientation

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial advisory crosswalk from V3 artifacts to EU AI Act human-oversight and logging themes and ISO/IEC 42001 themes, marked for human review.

## Status
Research-only, advisory, and non-enforcing.

This document is not a compliance claim, not a conformity assessment, not a certification artifact, and not legal advice. Per the Product Owner role definition, every correspondence asserted below is marked for human review before any external use. Factory V3 remains a research and operational-evidence track with one approved optional bounded profile; nothing here changes that.

This document does not authorize regulated-action paths, production deployment, required gates, governance routing, runtime-control power, or any new V3 scope.

## Purpose
Regulatory context: the EU AI Act's obligations for high-risk AI systems, including Article 14 (human oversight) and Article 26 (deployer obligations), apply from 2026-08-02, and ISO/IEC 42001 is emerging as the enterprise AI-management checkbox.

V3's supervision and evidence discipline was not designed from these texts, but it maps closely onto their themes. This crosswalk records the correspondence in one place so that (a) future design work can keep the mapping tight, and (b) a human reviewer can later turn selected rows into externally usable material. The crosswalk maps artifact to theme; it deliberately does not assert that any V3-governed system is or is not a high-risk AI system — that classification is fact-specific and belongs to human and legal review.

## Crosswalk

| V3 artifact | Regulatory theme | Correspondence (marked for human review) | Known gap |
| --- | --- | --- | --- |
| Tiered decisions and human decision interrupts (`ADAPTIVE_MISSION_CONTROL.md`) | AI Act Art. 14: effective oversight by natural persons; ability to intervene during operation | Tier 3 interrupts route runtime decisions to a human and record the answer and plan delta as replayable evidence. | Research-only; no live interrupt transport is approved. |
| Mission envelope, halt rules, V2 fallback (`OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`) | AI Act Art. 14: ability to decide not to use, to override, or to halt the system | Bounded authority, named halt conditions, and a required fallback path exist per mission and are sponsor-approved before execution. | Applies to one bounded coding profile only. |
| Mission records and telemetry replay (`MISSION_RECORD_DESIGN_V0.md`, `telemetry/pilots/`) | AI Act Art. 12 record-keeping and Art. 26 deployer logging duties | Per-mission machine-readable records with ordered advisory telemetry support after-the-fact reconstruction of authority, commands, verification, and human decisions. | No retention policy exists; Art. 26's minimum six-month log retention is a named design consideration below. |
| Model identity and mutable-state recording (`MUTABLE_HARNESS_STATE.md`) | AI Act Art. 12 traceability; ISO 42001 lifecycle documentation and change management | Recording model identity, skill versions, and credential references keeps evidence attributable to the engine configuration that produced it. | New as of 2026-06-10; records before `MR_20260610_010` carry `not_recorded` model values. |
| Escalation rules and halt evidence (`SHADOW_SCHEMA_CANDIDATES.md` escalation shapes, halted mission records) | AI Act Art. 14: detect and address anomalies, dysfunctions, unexpected performance | Halt-on-failed-verification and escalation-to-human are first-class decision states with fixture and POC evidence. | Natural (non-seeded) negative-case evidence in this repository remains an open gap. |
| Harness capability profiles and evidence bands (`templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`) | ISO 42001 performance evaluation and risk treatment | Capability claims carry explicit evidence bands from `insufficient_evidence` upward, preventing vendor-claim inflation. | Profiles are advisory and most sit at `insufficient_evidence`. |
| Sponsor approval gates and promotion criteria (`PROMOTION_CRITERIA.md`, release approvals) | ISO 42001 management review; AI Act Art. 14 oversight assignment | Capability expansion requires named human release approval backed by evidence, giving a documented oversight chain. | Single-sponsor model; no multi-role oversight assignment exists. |
| Skill provenance policy (`SKILL_PROVENANCE_POLICY.md`) | ISO 42001 change management; AI Act robustness themes | Learned or unknown-provenance capability is quarantined from execution and verification until human promotion. | Review discipline only; untested against real skill behavior. |

## Design Considerations Raised By This Crosswalk
- Log retention: Art. 26 requires deployers of high-risk systems to retain automatically generated logs for at least six months. Mission records and telemetry are git-resident and effectively retained indefinitely, but no named retention statement exists; adding one to the mission-record design is a cheap named follow-up.
- Oversight competence: Art. 14 expects overseers to understand the system's capacities and limitations. The anchor registry and evidence bands are the V3 artifacts that serve this; keeping them current is part of the oversight story.

## What This Crosswalk Does Not Establish
- No opinion on whether any V3-governed system is a high-risk AI system under the AI Act.
- No conformity assessment, certification readiness, or audit result.
- No claim that research-only artifacts satisfy any legal obligation.
- No approval for external publication; human review is required before any row is used outside this repository.

## Named Follow-ups (Not Approved Here)
- Human/legal review of each crosswalk row before external use.
- A retention statement in `MISSION_RECORD_DESIGN_V0.md`.
- Periodic re-check of the mapping as AI Act guidance and ISO 42001 practice mature.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.
