# Human Decision Interrupt — HDI-RUNG2-001 (Rung-2 Transport Choice)

## Status
Research-only and non-enforcing mission evidence: structured sponsor-decision record for the duration-ladder rung-2 transport choice. It approves the transport selection only; the rung-2 run itself still requires its own envelope and explicit sponsor Go, and no live messaging automation is approved by this record.

## Record
- Decision ID: `HDI-RUNG2-001`
- Mission ID: `RUNG2_PREP_20260611` (decision taken in-thread at session start, before the mission envelope was written; this mission records it)
- Decision tier: 3 (transport choice for rung 2 was the named open sponsor decision in `LADDER_STATUS.md` gate 1, raised 2026-06-10)
- Raised at: 2026-06-10 (recorded as the open gate-1 decision in `LADDER_STATUS.md` v0.2 after Claude Code Remote Control returned "disabled by your organization's policy")
- Answered at: 2026-06-11, Claude Code session thread, structured option prompt
- Transport for this decision itself: in-session thread (sponsor attending); no notification surface used

## Question
Which transport should rung 2 use for the live phone-answered Tier 3 interrupt, given that Claude Code Remote Control is disabled by the sponsor's organization policy?

## Options (as named in `LADDER_STATUS.md` gate 1)
- Option A: Sponsor's org admin enables Remote Control in the claude.ai admin settings for Claude Code; rung 2 stays on the Claude Code harness.
- Option B: Run rung 2 under the Codex harness with Codex mobile as the transport — the trial plan's secondary candidate, already proven by POC Mission 013's two phone-answered interrupts.
- Option C: Any other transport, which would need its own naming and approval (live Telegram remains unapproved).

## Answer
- Answer source: sponsor, Claude Code session thread, 2026-06-11 ("Codex mobile (option b)" selected from the structured option prompt; mission A proceed confirmation: "sure proceed with mission A")
- Answer: Option B — rung 2 runs under the Codex harness with Codex mobile (ChatGPT app surface) as the live interrupt transport.

## Named Consequences
- The rung-2 mission executes under the Codex harness in the POC repository (`V3_POC_App_Creation`); Claude Code's role for rung 2 is envelope drafting and evidence review, not execution.
- The `INTERRUPT_TRANSPORT_TRIAL_PLAN.md` secondary candidate becomes the selected rung-2 transport; this matches the plan's stated condition ("if the trial mission runs under a Codex harness").
- The rung-2 harness and model identity must be recorded in the rung-2 envelope and mission record per `MUTABLE_HARNESS_STATE.md`; transport availability remains org-policy-gated runtime state, so the envelope must record the transport's observed working state at mission start.
- Remote Control (Option A) is not closed permanently: if the org policy changes, a future rung or trial may name it again with its own approval. No comparison trial is approved by this record.
- This decision does not change the rung-2 pass criteria: genuine duration per `HDI-TT-001`, budget-and-waypoint measured criteria per `HDI-TT-002`, one live Tier 3 interrupt answered from the sponsor's phone while genuinely away from the terminal, and pause/reentry from authored artifacts alone.

## Plan Delta
None — `DURATION_LADDER_PLAN.md` rung 2 already required "the live transport" without hard-coding which; the transport trial plan already named Codex mobile as the secondary candidate under exactly this condition.
