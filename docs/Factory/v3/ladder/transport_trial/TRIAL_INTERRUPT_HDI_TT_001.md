# Human Decision Interrupt — HDI-TT-001

## Status
Research-only and non-enforcing mission evidence: structured interrupt record for the active transport trial. Approves nothing.

## Record
- Interrupt ID: `HDI-TT-001`
- Mission ID: `TRANSPORT_TRIAL_20260610`
- Decision tier: 3 (rung adjudication is a sponsor judgment per MR_019 friction note)
- Pre-resolution check: Tier 1/2 reviewed — the rung-1 envelope explicitly deferred this adjudication to the sponsor at closeout; not resolvable in-mission
- Raised at: 2026-06-10T13:39:05Z window
- Transport attempt (verbatim harness result): "Not sent — terminal has focus. Terminal + mobile suppressed."
- Transport observation: the notification surface suppresses delivery when the terminal session has focus; an attended sponsor receives the question through the session itself. For a future unattended/away sponsor this is correct behavior (push fires when unfocused, as the delivery test showed minutes earlier when it did deliver); recorded as genuine vendor-behavior evidence, not a failure.
- Actual question surface: in-session structured question (AskUserQuestion), with the suppressed-notification attempt recorded
- Timeout behavior: none needed (in-session question blocks for the answer; sponsor present)

## Question
Rung 1 (`LADDER_RUNG1_20260610`) exercised all rung-1 mechanics cleanly but ran ~7 minutes wall clock against a ~90-minute plan. Does rung 1 pass as mechanics evidence, or must it re-run with genuinely larger scope before rung 2?

## Reason
`DURATION_LADDER_PLAN.md` requires each rung to pass before the next unlocks; MR_019 explicitly left this adjudication to the sponsor.

## Decision Type
Ladder rung adjudication

## Options
- Option A (recommended): Pass rung 1 as mechanics evidence; explicitly shift the duration-stress burden to rung 2, which must run genuinely long (larger scope in the POC repo). Risk: if rung 2 also compresses, duration evidence arrives late — mitigated by rung 2's pass criteria requiring duration.
- Option B: Re-run rung 1 with larger scope before any rung-2 work. Risk: delays the ladder for evidence rung 2 would produce anyway.
- Option C: Pass rung 1 and also schedule a parallel larger rung-1-class mission later. Risk: parallel evidence work dilutes the single-ladder narrative.

## Recommended Option
Option A

## Answer
- Answer source: sponsor, in-session structured question surface, 2026-06-10 (after suppressed-notification attempt recorded above)
- Answer: Option A — "Pass — mechanics (Recommended)"
- Answer interpretation: rung 1 is adjudicated passed as mechanics evidence; `DURATION_LADDER_PLAN.md` records the pass and explicitly assigns the duration-stress burden to rung 2, whose pass criteria must include genuine duration.
- Plan delta: none — matches the envelope's planned Decision 1 shape.
- Continuation decision: continue (apply to ladder plan, then raise HDI-TT-002 for the deliberate-timeout leg).
