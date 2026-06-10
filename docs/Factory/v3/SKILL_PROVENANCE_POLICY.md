# Factory V3 Skill Provenance Policy

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial research-only policy promoting the HP_20260530_001 skill watchpoints into named provenance, pinning, quarantine, and non-laundering rules.

## Status
Research-only and non-enforcing.

This document does not authorize skill execution, required record fields, validator enforcement, governance routing, required gates, CI wiring, runtime-control power, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this document. It is advisory review discipline for any future mission that relies on harness skills.

## Problem
Harness skills are an instance of mutable harness state (`MUTABLE_HARNESS_STATE.md`): files resident in the harness that can be added, edited, composed, or generated between and during missions, outside the mission record.

Two observed watchpoints motivate this policy (`harness_profiles/HP_20260530_001_claude_code_dynamic_workflows_research.md` v0.2, operator-relayed external evidence):

1. A skill-encoded verifier changes what verification means without the mission record changing.
2. Skill chains can invoke other skills, including outward actions, so composition can expand effective scope beyond what a sponsor approved.

Vendor skill systems additionally describe skills that create and improve other skills. A skill the harness learned or refined on its own is a capability the sponsor never reviewed; relying on it silently expands worker capability outside the approval chain.

## Provenance Classes

| Provenance | Meaning |
| --- | --- |
| `authored` | Written or explicitly adopted by a human and versioned inside a repository the mission record can reference (for example `.agents/skills/`). |
| `vendor_supplied` | Shipped by the harness or platform vendor; identity and version come from vendor metadata. |
| `learned` | Generated or refined by the harness from its own execution, including skills produced by skill-creation skills. |
| `unknown` | Provenance cannot be established. Treated as `learned` for every rule below. |

## Advisory Rules

1. Provenance is recorded. Any skill relied on during a mission should be named in the mission record with its identity, version, and provenance class.
2. Verification skills are pinned. A skill relied on for verification or evidence production must have identity and version pinned in the mission record before replay evidence that depends on it is trusted (existing HP_20260530_001 watchpoint, restated as policy).
3. Learned skills are quarantined. A `learned` or `unknown` skill must not be relied on for mission execution or verification until a human reviews its content and explicitly promotes it, after which it is recorded as `authored` with a reference to the promotion review. Quarantine is a review discipline, not a technical control; this document builds no enforcement.
4. Composition must not launder authority. A skill invoking another skill does not extend mission scope; each composed link needs the same scope and approval treatment as a direct action, and any outward fan-out needs separate approval (existing watchpoint, restated as policy).
5. Repo-resident skills follow repo discipline. The existing `.agents/skills/` mission-formation and challenge skills are `authored`, non-executing, and grant no authority; nothing in this policy upgrades them.

## Relationship To Existing Canon
- `MUTABLE_HARNESS_STATE.md` names skill state as a mutable-state instance; this policy is the skill-specific elaboration it listed as a follow-up.
- `MISSION_RECORD_DESIGN_V0.md` v0.8 already advises naming verification skills in records; provenance classes refine that guidance.
- `MISSION_FORMATION_DIRECTION.md` and the `.agents/skills/` skill files keep their own non-authority language; this policy adds review vocabulary, not authority.
- `NON_GOALS_AND_BOUNDARIES.md` still governs; skill review stays inside coding-mission scope.

## Named Follow-ups (Not Approved Here)
- An optional `skills_relied_on` template field in the mission record, with advisory validator and fixture support, as a separately approved change.
- A promotion-review note shape for moving a `learned` skill to `authored`.
- Local trial evidence of skill-encoded verification under a bounded envelope before any reliance on it.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.

## Data Minimization
Records guided by this policy store skill identifiers, versions, provenance classes, and promotion-review references only — not skill file contents, chain-of-thought, or vendor-private cognition state.
