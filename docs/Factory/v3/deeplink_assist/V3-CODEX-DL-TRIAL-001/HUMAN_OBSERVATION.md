# V3-CODEX-DL-TRIAL-001 Human Observation

## Status

`PASS_WITH_LIMITATIONS`

Research-only, advisory, and non-enforcing attended-trial evidence. Do not
infer missing observations.

## Preflight

- Trial approval: explicit
- Formation SHA-256:
  `5a83d3585d66c6aa9c1164c2e26fb5a49a746237cb738ecf16683b4773fc7d4a`
- Challenge SHA-256:
  `b067e1146a40d2be384ad4005bf19aae2df914ec5fe956f23f43f428b4cbfa66`
- Workspace:
  `/Users/eduardodosremedios/codex_deeplink_trial_001_workspace`
- Workspace preflight: absent before preparation; created empty
- Workspace before entries: `[]`
- Expected prompt bytes: `245`
- Expected prompt SHA-256:
  `913c411439695f29ce0ad95ab0310486025b7ef4743beca87687e4baf9bb0784`
- Expected response:
  `V3-CODEX-DL-TRIAL-001 ACK 7F3C2A9E`
- Action ceiling: one helper run, one click, one Send, one task, no retry

## Sponsor Composer Checkpoint

Complete after clicking the prepared link and before Send:

- new task opened:
  `SUPPORTED_WITH_LIMITATION` — the post-response screenshot shows one trial
  task titled `Mission V3-CODEX-DL-TRIAL-001`
- exact trial workspace visibly confirmed:
  `PROJECT_NAME_MATCH` — sidebar shows
  `codex_deeplink_trial_001_workspace`; full absolute path is not visible
- complete composer prompt visually matched:
  `POST_SEND_MESSAGE_MATCH` — the screenshot shows the complete submitted
  message matching the pinned prompt; no pre-Send screenshot exists
- pre-Send screenshot captured: `NO`
- pre-Send screenshot reference: `not_available`
- safe to press Send once: `not_recorded_before_send`

Do not press Send if the task is not new, the workspace is wrong or unknown, or
the prompt differs/cannot be reviewed.

## Sponsor Post-Send Observation

Complete after the one permitted Send:

- Send count:
  `ONE_VISIBLE_USER_MESSAGE` — not independently observed before Send
- sponsor-returned response:
  `V3-CODEX-DL-TRIAL-001 ACK 7F3C2A9E`
- returned response matched expected single line: `YES`
- visible tool or command activity: `NONE_VISIBLE`
- visible file read or write activity:
  `NONE_VISIBLE`; Factory after-state also remained empty
- permission request: `NONE_VISIBLE`
- extra prose or ambiguity: `NO_EXTRA_PROSE_VISIBLE`
- technical task/thread ID if visible: `not_visible`
- post-response screenshot captured: `YES`
- post-response screenshot reference:
  `POST_RESPONSE_SCREENSHOT.png`
- post-response screenshot SHA-256:
  `834f972872296ebc55b3121533be660437d55ecc3705309ca69a8fda5de72b59`

## Factory After-State Observation

- workspace after entries: `[]`
- workspace before/after match: `YES`
- prompt bytes/hash remain pinned: `YES`
- Same Second remains clean at
  `20554125a422f0fc0afeadf18948b4c8e649a732`

The exact returned acknowledgment, complete visible submitted prompt, matching
project name, absent visible activity cards, and unchanged workspace are
supported by the screenshot plus Factory after-state evidence.

The sponsor initially reported uncertainty about whether the procedure was
performed correctly, then supplied the post-response screenshot. No retry
occurred. The screenshot resolves the visible prompt/response/project/activity
questions sufficiently for a bounded pass, but not the pre-Send checkpoint,
full absolute path, task ID, or byte-level transport questions.

## Evidence Limits

Sponsor observation and screenshots are attended evidence, not a task API or
byte-level transport trace. The post-response screenshot proves visible UI
content only. It cannot prove exact composer bytes, sent-message bytes, hidden
activity, or task identity.
