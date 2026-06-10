# Factory V3 Mutable Harness State Principle

## Version
v0.1

## Change Log
- v0.1 (2026-06-10): Initial principle naming model identity, skill libraries, and credential state as mutable harness-resident state that replay evidence must pin or record.

## Status
Research-only and non-enforcing.

This document does not authorize required record fields, validator enforcement, governance routing, required gates, CI wiring, telemetry completeness checks, runtime-control power, proof, lease enforcement, default-mode behavior, V3 profile promotion, or Factory V2 build-support removal.

Factory V3 is not promoted by this document. Use it only as advisory design context for mission records, harness capability profiles, and future evidence work.

## Principle
Replay evidence is only as trustworthy as the stability of the state it references.

Coding harnesses now carry state that can change during a mission, or between a mission and its later replay, without that change appearing anywhere in the mission record. A mission record that silently depends on such state cannot support the replay question "would the same mission produce the same evidence."

The principle: any harness-resident state that can mutate independently of the mission record must be either pinned (held fixed for the mission) or recorded (its observed identity written into the record), before replay evidence that depends on it is trusted.

## Named Instances

| Instance | What can mutate | External signal | Local Factory evidence |
| --- | --- | --- | --- |
| Model identity | Vendor model routing can select a different model per task and can escalate a session to a different model mid-mission; silent vendor model upgrades change worker behavior without any local action. | factory.ai announced Factory Router on 2026-06-01, routing each task across a model pool with mid-session escalation. External announcement only; not locally observed. | All mission records through `MR_20260610_009` record `"model": "not_recorded"`. `MR_20260610_010` is the first record with model identity recorded. |
| Skill libraries | Skills are harness-resident files that can be added, edited, composed, or learned between missions; a skill-encoded verifier can change what verification means without the mission record changing. | Operator-relayed video evidence reviewed in `HP_20260530_001` v0.2; vendor skill systems also describe skills that create and improve other skills. External signals only; not locally observed. | Skill-encoded verifier and skill-chain authority watchpoints in `harness_profiles/HP_20260530_001_claude_code_dynamic_workflows_research.md`. |
| Credential state | Vendor credential vaults inject secrets at runtime and pick up rotated values on the next call, so the credentials a mission used can differ from the credentials present at replay review. | Vendor vault documentation describes runtime injection and mid-session rotation pickup. External documentation only; not locally observed, and no credential use is approved for V3 missions. | `none_yet`; credential use remains outside approved V3 mission scope. |

The external signals above are announcement-grade and documentation-grade sources in the same sense as `insufficient_evidence` harness-profile signals. They motivate recording discipline; they do not constitute local Factory evidence and must not be cited as such.

## Advisory Recording Rules

1. Model identity: a mission record should record the model identity when the harness exposes it. When vendor model routing or automatic model selection is enabled, the record should mark routing as enabled and list the observed model set when known. `not_recorded` remains a valid value only where the harness does not expose model identity, and the gap must stay explicit.
2. Skill state: any skill relied on for verification or evidence production should have its identity and version pinned in the mission record, per the `HP_20260530_001` watchpoints. A mission record that depends on an unpinned skill should name that as an explicit evidence gap.
3. Credential state: records should reference credential sources by label only and never store secret values. If a future approved mission ever uses vault-injected credentials, the record should note the vault reference and whether rotation occurred mid-mission, subject to a separate data-minimization review.

## Evidence Expiry Consequence
Evidence validated against a named model, skill set, or credential configuration speaks only for that configuration. When the underlying engine changes — a routed model swap, a vendor model upgrade, a skill edit — previously gathered capability evidence becomes stale for the new configuration until reconfirmed.

Harness capability profiles should therefore treat "model when known" as load-bearing rather than optional context, and treat a known engine change as a revalidation trigger for any profile claim that depends on it. This is an advisory review discipline, not a new gate.

## Relationship To Existing Canon
- `MISSION_RECORD_DESIGN_V0.md` carries the record-level recording guidance.
- `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md` v0.1 accepted missing model identity for early research evidence; that acceptability is retired for new records as of this principle, while existing records remain valid historical evidence with the gap explicit.
- `templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md` already includes "Model when known"; this principle raises its weight in review.
- `NON_GOALS_AND_BOUNDARIES.md` still governs: pinning and recording are evidence disciplines inside coding-mission scope, and enforcement of any kind remains outside this document.

## Named Follow-ups (Not Approved Here)
- Advisory validator support for model-identity and routing fields in mission records, with fixture coverage, as a separately approved change.
- A skill provenance policy covering authored versus learned skills.
- A revalidation note shape for harness profiles whose underlying engine changed.

Each follow-up requires its own scoped mission and human approval; listing them here approves nothing.

## Data Minimization
This document and the records it guides must not store secret values, raw credential material, chain-of-thought, vendor-private cognition state, or full command output. Model identity strings, skill identifiers with versions, and credential source labels are the maximum payload this principle asks for.
