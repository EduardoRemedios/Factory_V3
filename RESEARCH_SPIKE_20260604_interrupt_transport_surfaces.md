# Research Spike: Human-Interrupt Transport Surfaces For Long-Running V3 Missions (D3)

## Status
Research-only, planning-only sponsor input. Completed 2026-06-04. This spike approves nothing: no Telegram bot, token, polling, webhook, live messaging, unattended runs, new profiles, or harness dependencies. It informs the Track D decisions in `RAW_BRIEF_20260604_long_running_mission_path.md`.

## Question
For the target end state — a multi-hour V3 mission that pauses only to ask the sponsor a question answered from a phone — which transport should carry the interrupt: (a) Codex-native mobile surfaces, (b) Claude-native mobile surfaces, or (c) a self-built Telegram bridge?

## Headline Finding
Both harness vendors shipped the transport natively in the first half of 2026. The mission-asks/human-answers-from-phone loop now exists first-party in both ecosystems. The self-built Telegram relay (raw brief D4) is no longer needed for v1; what remains V3's job is the governance layer — making the mission write the structured interrupt record, capture the answer, and record the plan delta regardless of which transport carried the message.

## Findings

### (a) Codex-native surfaces
- Codex shipped in the ChatGPT mobile app on 2026-05-14 (preview, iOS and Android, all plans). From the phone you can "answer a question, review what Codex found, change direction, approve what comes next," across all threads on a connected machine. Files, credentials, and execution stay on the host; updates (terminal output, diffs, test results, screenshots, approvals) stream to the phone through a secure relay with no inbound ports.
- OpenAI's stated framing matches the V3 vision almost verbatim: "As agents take on longer-running work... you need to be able to easily answer a question... change direction, approve what comes next." Example workflows include answering a mid-task decision point from a commute.
- Hooks are GA: `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SessionStart`, `SubagentStart/Stop`, `UserPromptSubmit`, `Stop`, plus a `notify` setting that runs an external program — a natural emission point for V3 advisory telemetry and interrupt-event mirroring without touching mission cognition.
- Headless automation exists: `codex exec` runs non-interactively; `codex exec resume --last` / `resume <id>` continues a run with transcript, plan history, and approvals intact — a harness-native analog of V3 reentry.
- Trajectory: 2026-06-02 "Codex for every role, tool, and workflow" (role plugins, Sites preview); press coverage describes OpenAI "building the superapp out in the open — and evolving it out of Codex." Windows full computer control steerable from phone shipped 2026-05-29.
- Sponsor note: a further OpenAI release was rumored for 2026-06-04 (X chatter about a "superapp" with a possible mobile intent surface). As of this spike's searches, the latest confirmed announcements are 2026-06-02. Re-check after the announcement lands; the direction of travel only strengthens option (a).

### (b) Claude Code-native surfaces
- Remote Control (research preview since 2026-02-25, Claude Code v2.1.51+): bridges a local Claude Code session to claude.ai/code and the Claude iOS/Android apps via `/rc`, `claude --remote-control`, or `claude remote-control` server mode. Conversation stays synced across terminal, browser, and phone; the session runs entirely on the local machine; outbound HTTPS only with short-lived scoped credentials.
- Mobile push notifications (v2.1.110+): Claude pushes to the phone "when a long-running task finishes or when it needs a decision from you to continue" — the interrupt notification, first-party. Pushes can also be requested in-prompt ("notify me when the tests finish").
- Known limits: the local process must stay alive (session dies if the terminal closes); ~10-minute network-outage timeout; one remote session per interactive process (server mode supports up to 32); requires claude.ai OAuth (Pro/Max/Team/Enterprise), not API keys.
- Channels: first-party plugin path that pushes events from Telegram, Discord, or iMessage into a running session, with a documented build-your-own channel reference. If a chat-app interrupt surface is ever still wanted, this is now a supported pattern on the Claude side rather than a bespoke bridge.
- Dispatch: message a task from the Claude mobile app and it spawns a Desktop session — the "start a mission from the phone" direction.
- Long-run/automation primitives: headless `-p` with `--resume <session-id>` and named sessions; `/loop` and `/schedule`; Auto Mode (2026-03-24); Routines (April 2026) run scheduled cloud tasks where each execution writes a state file the next one reads — strikingly close to AMC's checkpoint/reentry model, vendor-implemented.

### (c) Self-built Telegram bridge
- Still feasible (watch `.factory-v3/.../interrupts/*.json`, notify an allowlisted chat, write the answer back, keep a replay log) and remains fully transport-independent and vendor-neutral.
- But it now duplicates what both vendors ship natively, adds a bot token and identity surface V3 must then govern (AMC explicitly gates this), and creates maintenance the native relays absorb. Claude's Channels reduces the build cost on one side but does not remove the governance cost.
- Verdict: demote to fallback. Revisit only if (i) vendor surfaces prove unreliable in trials, (ii) a single surface across both harnesses becomes mandatory, or (iii) the sponsor wants interrupts in the same chat app as the future PPOS product surface (Track 1) — and even then, keep product and governance bots strictly separate.

## Assessment Against Interrupt-Bridge Requirements
| Requirement | Codex mobile | Claude Remote Control | Self-built Telegram |
| --- | --- | --- | --- |
| Phone notification on decision needed | Yes (app notifications; iOS task-completion notifications) | Yes (push "when it needs a decision") | Yes (bot message) |
| Reply path back into the running session | Yes, native | Yes, native | Requires relay writing into interrupt file + mission polling |
| Identity control | ChatGPT account + device auth | claude.ai OAuth + device auth | Self-managed allowlist + token custody (V3-governed) |
| Credential handling | Vendor relay, no inbound ports | Vendor relay, outbound HTTPS, short-lived scoped credentials | Bot token stored locally; V3 must define custody |
| Session survives across devices | Yes (relay keeps state synced) | Yes while local process lives; ~10 min outage timeout | N/A (transport only) |
| Headless/resume primitives | `codex exec`, `codex exec resume` | `-p`, `--resume`, named sessions, Routines state files | N/A |
| Replayable interrupt record | Not provided — V3 must author it | Not provided — V3 must author it | Only if the bridge writes it — V3 must author it |
| Cost | Plan-included | Plan-included | Free API + build/maintenance time |

The last row but one is the decisive observation: no transport produces V3's interrupt record. That discipline lives in the mission protocol (AMC) on every option, which is why transport choice does not change Mission 012's design.

## Implications For The Raw Brief
1. D1 (Mission 012 file-based interrupt trial) is unchanged and remains correct: the interrupt lifecycle artifacts are transport-agnostic and must be proven regardless.
2. D4 (interrupt bridge implementation) is demoted from "build a local Telegram relay" to "adopt vendor-native transport + AMC record discipline," with two small optional adapters: a Codex `notify`/hooks emitter that mirrors interrupt/telemetry events into `.factory-v3/` evidence, and (if ever needed) a Claude Channels plugin. The AMC Telegram boundary stays untouched — nothing here approves live Telegram.
3. D5 (mission runner) is partially absorbed by vendor primitives: `codex exec resume` and Claude Routines' state-file pattern can host reentry. A thin `factoryctl mission-run` wrapper may still be worth it for halt/interrupt detection and enforcement, but it should orchestrate vendor resume primitives rather than reinvent session management.
4. The first remote-interrupt trial (candidate `V3-OP-003` profile) should use Codex in the ChatGPT mobile app, since Codex is the POC's named harness — with the mission required to write the AMC interrupt record and plan delta for every phone-answered decision. Claude Remote Control should be profiled as the comparison harness.
5. Add two Phase 4 harness capability profiles in Factory_V3 (initially `insufficient_evidence`, per existing convention): Codex mobile steering, and Claude Code Remote Control + Routines.
6. Re-check this spike after the rumored 2026-06-04 OpenAI announcement; if a mobile intent surface ships, update the Codex profile rather than this spike's conclusions, which it would reinforce.

## Sequenced Recommendation
1. Mission 012: file-based interrupts (unchanged).
2. Mission 013 candidate: same mission class, but interrupts answered from the phone via Codex mobile, with AMC records authored for each — the first true remote-interrupt evidence.
3. Parallel Factory_V3 work: harness capability profile entries; optional hooks-based telemetry emitter design (advisory only).
4. Telegram bridge: fallback only; no build.

## Boundaries Restated
This spike does not approve live Telegram automation, bot tokens, Channels plugins, unattended runs, vendor-relay trust decisions for production scope, new operational profiles, default-mode promotion, or any POC dependency. Each requires its own named approval.

## Sources
- OpenAI, "Work with Codex from anywhere" (2026-05-14): https://openai.com/index/work-with-codex-from-anywhere/
- OpenAI Developers, Codex hooks: https://developers.openai.com/codex/hooks
- OpenAI Developers, Codex non-interactive mode: https://developers.openai.com/codex/noninteractive
- OpenAI, "Codex for every role, tool, and workflow" (2026-06-02): https://openai.com/index/codex-for-every-role-tool-workflow/
- The New Stack, "OpenAI's superapp is taking shape as Codex goes beyond coding": https://thenewstack.io/openais-superapp-takes-shape/
- Claude Code docs, Remote Control: https://code.claude.com/docs/en/remote-control
- Claude Code docs (referenced from Remote Control page): Channels, Dispatch, Scheduled tasks, Claude Code on the web
- Anthropic, "Claude Code on the web": https://www.anthropic.com/news/claude-code-on-the-web
- VentureBeat, "Claude Code's 'Tasks' update lets agents work longer and coordinate across sessions": https://venturebeat.com/orchestration/claude-codes-tasks-update-lets-agents-work-longer-and-coordinate-across
- MindStudio, "Claude Code Q1 2026 Update Roundup" and Routines articles: https://www.mindstudio.ai/blog/claude-code-q1-2026-update-roundup
