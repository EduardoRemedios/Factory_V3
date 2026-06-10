# Human Decision Interrupt — HDI-RUNG1-001

## Status
Research-only and non-enforcing mission evidence: structured interrupt record for the active rung-1 mission. Approves nothing.

## Record
- Interrupt ID: `HDI-RUNG1-001`
- Mission ID: `LADDER_RUNG1_20260610`
- Decision tier: 3 (sponsor roadmap decision; not resolvable from the envelope)
- Pre-resolution check: Tier 1 reviewed — the envelope pre-resolves artifact descriptions but explicitly defers the "next named decision" wording to this interrupt; Tier 2 inapplicable because the choice changes roadmap direction, not wording detail
- Raised at: 2026-06-10T13:30:51Z (CP2)
- Transport: thread-based (sponsor in-session); simulated-transport rung per `DURATION_LADDER_PLAN.md` rung 1
- Timeout behavior: no fixed timeout (sponsor in-session per envelope); if the session ends unanswered, the mission stays paused at CP2 and reenters per the envelope reentry rule

## Question
The state docs (`docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`) name a single "next operational-readiness decision scope": the V3-with-Codex POC application build. That scope has substantially completed — the sponsor-approved final eval `PASS_NAMED_POC` (20/22) exists through POC Mission 020. What should the named next operational-readiness decision become?

## Reason
WP3 must rewrite the "next decision" language in three documents; writing it without a sponsor answer would be the mission inventing roadmap direction.

## Decision Type
Roadmap priority (next named operational-readiness decision)

## Options
- Option A (recommended): Name the `V3-OP-003` promotion decision via the duration ladder and transport trial as the next operational-readiness decision, recording the POC scope as achieved-for-named-scope with its existing exclusions. Risk: long-running focus could deprioritize remaining POC limitations (real-data boundary, Garmin/Hermes spikes) — mitigated by keeping them as named separately-governed lanes.
- Option B: Keep the POC-centric next decision and extend it (real-data boundary, Garmin spike) as the next named scope. Risk: state docs would understate the now-active long-running lane, and the ladder would run without a named decision anchor.
- Option C: Name both as parallel next decisions. Risk: two "next" decisions dilute the single-anchor convention the state docs currently use.

## Recommended Option
Option A

## Answer
- Answer source: sponsor, in-session structured question (AskUserQuestion surface), 2026-06-10
- Answer: Option A — "V3-OP-003 ladder (Recommended)"
- Answer interpretation: WP3 rewrites the "next operational-readiness decision" language in the three state docs to name the `V3-OP-003` promotion decision via the duration ladder and transport trial; the POC scope is recorded as achieved-for-named-scope with all existing exclusions intact; real-data boundary, Garmin, and Hermes remain named separately governed lanes.
- Plan delta: none — the answer matches the envelope's planned WP3 shape; no scope, file, or command change.
- Continuation decision: continue to WP3.
