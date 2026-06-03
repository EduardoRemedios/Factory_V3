# Factory v3 Promotion Criteria

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added long-running mission promotion inputs and no-go conditions for adaptive mission control, replay stability, git authority, and verification side effects.
- v0.2 (2026-05-25): Clarified that V2 governance is build-support during V3 maturation, not a V3 product dependency, and that V2 deprecation/removal from this repo requires explicit confidence and release evidence.
- v0.1 (2026-05-18): Initial promotion criteria for Factory v3 research.

## Status
Research only. This document defines candidate promotion criteria but does not promote Factory v3.

## Promotion Principle
Factory v3 may only be promoted after it has been planned, evaluated, and hardened using the currently available Factory v2 governance scaffolding or a later explicitly approved V3-equivalent governance path.

Promotion requires evidence and explicit human release approval.

V2 governance in this repository is build-support during V3 maturation. It is not a V3 product dependency. V2 deprecation/removal from this repository is a future promotion decision that requires explicit V3 confidence evidence, migration guidance, and human release approval; the separate V2-only repository remains the preservation home for V2.

## Minimum Promotion Inputs
Before any v3 artifact becomes authoritative, there must be:
- a Factory v2 planning pack approving the promotion scope
- clear list of artifacts being promoted
- pilot evidence from advisory or shadow use
- false-positive and false-negative review for advisory checks
- external-kernel boundary review
- public README language explaining the release posture
- migration guidance for existing v2 users
- standalone V3 operation evidence for the named scope, with no dependency on Factory V2 stage, pack, or lint behavior for normal operation
- for any long-running or overnight-capable mission claim, checkpoint, authored mission-state, human decision interrupt, plan-delta, verification side-effect, and git-authority evidence showing the mission can continue from artifacts instead of hidden chat memory or elapsed-time assumptions
- explicit human release approval

## Required Evidence
Promotion evidence should include:
- paths to evaluated v3 docs
- advisory validator reports, if any
- pilot profile outcomes
- examples of drift caught
- examples of warnings rejected as false positives
- unresolved risks
- human decision record

## Promotion Levels

### Level 0 - Research
- Meaning: Docs and candidates only.
- Authority: none.
- Current status: active.

### Level 1 - Advisory
- Meaning: Optional validators or schemas may produce non-blocking reports.
- Authority: advisory only.
- Promotion requirement: pilot plan and non-blocking output format approved.

### Level 2 - Recommended
- Meaning: v3 artifacts are recommended for certain run types, but v2 remains valid without them.
- Authority: guidance only.
- Promotion requirement: repeated pilot evidence and README guidance.

### Level 3 - Required For Specific Profiles
- Meaning: selected v3 checks become required only for named profiles.
- Authority: bounded enforcement.
- Promotion requirement: separate Factory v2 pack, compatibility review, and release approval.

### Level 4 - Factory v3 Release
- Meaning: a coherent v3 operating profile is released.
- Authority: release-level process contract.
- Promotion requirement: migration guidance, validator coverage, pilot evidence, and explicit human release decision.

## Hard No-go Conditions
Do not promote if:
- Factory v2 behavior would change without explicit approval
- the named operational scope still depends on Factory V2 stage, pack, or lint behavior for normal operation
- external governance kernel would become required
- Factory would duplicate runtime-kernel authority
- shadow schemas would become required without advisory evidence
- promotion language lacks exact artifact paths
- public README language is ambiguous
- human release approval is absent
- historical replay depends on a mutable global fixture set instead of mission-scoped evidence
- verification mutates tracked evidence without explicit authority and review rules
- git init, commit, push, remote changes, or branch deletion are performed or recommended without mission-level authority and before/after evidence
- live Telegram, bot token, polling, webhook, or other human-interrupt automation is implied without separate bridge approval, identity allowlisting, timeout behavior, and replay-log rules

## Release Decision Template
Use this shape for a future release decision:

```text
Decision: GO | NO-GO
Promotion level:
Artifacts promoted:
Evidence paths:
Known residual risks:
separate governance kernel dependency introduced: yes | no
Runtime-kernel behavior introduced: yes | no
Human approver:
Date:
```

## Current Decision
Decision: NO-GO for Factory v3 release.

Reason: v3 is still in research. Strategy, concepts, advisory validation, pilot profiles, and promotion criteria exist as research artifacts only.
