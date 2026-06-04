# V3 POC Mission Template

## Status
Research-only and non-enforcing template until a separate POC mission is approved.

## Mission Status
DRAFT | APPROVED | HALTED | COMPLETE

## Profile
- Profile ID: `V3-POC-STANDALONE`
- Profile status: POC proof profile, not general production approval.
- V3-only: YES
- V2 allowed: NO

## Objective
-

## Success Criteria
-

## Eligible-Work Rationale
Why this mission is bounded enough for V3:
-

## Non-Goals
-

## Pre-Resolved Decisions
Optional Tier 1 decisions answered before execution:
-

## Decision Principles (Tier 2)
Optional principles for resolving implementation choices within mission authority:
-

## Deferred Decisions Log
Tier 2 choices to review at closeout:
-

## Authorized Files And Directories
-

## Forbidden Scope
-

## Allowed Commands
-

## Dependency Policy
- New dependencies allowed: YES/NO
- If YES, approval reference:
- Install command:
- Rollback plan:

## Verification
Commands and expected evidence:
-

## Adaptive Mission Control
- Checkpoints required: YES/NO
- Checkpoint cadence: phase boundary | verification gate | before pause | other
- Mission state file:
- Human decision interrupts allowed: YES/NO
- Human decision interrupt tier: Tier 3 only after Tier 1 pre-resolved decisions and Tier 2 decision principles cannot answer the decision.
- Interrupt surfaces allowed: thread | file | telegram-research-only | other
- Timeout behavior for unresolved interrupts: pause | continue_without_expansion | halt
- Plan delta required before scope change: YES
- Verification side effects allowed: YES/NO
- If YES, authorized output paths:
- Budget timestamp command: `date -u +%Y-%m-%dT%H:%M:%SZ`
- Duration measurement source: checkpoint timestamps or git commit times; never model-estimated minutes.
- Rate-limit window note:

## Halt Rules
Stop if:
-

## Standalone Gap Rule
If this mission cannot proceed without Factory V2, stop and record a V3 standalone gap. Do not use V2 as a fallback while claiming POC readiness.

## Reentry Rules
- Resume only from authored mission artifacts and current repository state.
- For larger missions, resume from `.factory-v3/templates/V3_MISSION_STATE_TEMPLATE.md`-compatible state and latest checkpoint.
- Halt if derived state conflicts with authored artifacts.

## Closeout
Use `.factory-v3/templates/V3_POC_CLOSEOUT_TEMPLATE.md`.
