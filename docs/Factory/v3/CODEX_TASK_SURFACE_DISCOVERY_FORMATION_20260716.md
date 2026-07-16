# Codex Task-Surface Discovery Formation - 2026-07-16

## Status

Research-only, non-executing mission-formation output for candidate mission
`V3-CODEX-DISC-001`.

This artifact does not start a Codex worker, create or message a task, open a
deep link, run app-server or MCP server, install an SDK, change credentials,
write outside Factory V3, approve unattended work, grant runtime-control power, or
promote a V3 profile.

## Source Evidence

- `ATTENDED_SERIAL_EPIC_PILOT_001_REVIEW_20260716.md`
- `CODEX_SDK_ORCHESTRATION_DIRECTION.md`
- `MISSION_FORMATION_DIRECTION.md`
- `MISSION_CONTROL_CONTRACT.md`
- `SERIAL_MISSION_GRAPH_CONTRACT.md`
- `SERIAL_MISSION_STATE_KERNEL.md`
- `GOVERNANCE_BOUNDARIES.md`
- OpenAI Codex manual, refreshed 2026-07-16:
  - [ChatGPT desktop app commands](https://learn.chatgpt.com/docs/reference/commands.md)
  - [Codex app-server](https://learn.chatgpt.com/docs/app-server.md)
  - [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk.md)
  - [Use Codex with the Agents SDK](https://learn.chatgpt.com/docs/mcp-server.md)

Local formation inspection found a `codex` wrapper on `PATH`, but every
`codex --version` or help invocation failed because its packaged native binary
was absent (`ENOENT`). The current Factory task did not expose native Codex
task-management tools such as create/list/read/send. These are capability
observations, not universal product claims.

## Mission Formation Result

### Route

`CANDIDATE_V3_ENVELOPE`

The manual attended pilot established the need and the governance prerequisites.
A tightly bounded read-only discovery mission can now compare task-transport
surfaces. It is not approved for execution by this formation artifact.

### Problem Statement

Factory V3 can author and validate one safe next action, but the sponsor still
manually creates the next Codex task and copies its re-entry instruction. The
missing capability is a transport adapter that can carry an already-authorized
handoff; it is not permission for the adapter to choose work, grant authority,
or mutate mission state.

### Desired Outcome

Produce a source-backed capability report and a recommendation for the smallest
surface that could:

1. create a genuinely new, non-forked Codex task;
2. bind it to an exact local workspace;
3. transfer an exact authored re-entry prompt without sponsor copy/paste;
4. return a durable task/thread identifier;
5. expose status and final output to Factory for evidence;
6. preserve human approval, sandbox, state-kernel, and safe-hold boundaries.

### Non-Goals

- No product or Factory implementation.
- No workspace-write worker trial.
- No worker-selected mission, child activation, authority, or verification.
- No SDK, package, CLI, plugin, or MCP installation or repair.
- No credential creation, inspection, logging, or use.
- No scheduled task, automation, background process, daemon, or unattended run.
- No sub-agent or concurrent-worker orchestration.
- No Same Second modification, push, merge, PR, deployment, or integration.
- No claim that a desktop-only or account-specific surface is portable.

### Assumptions

- Factory authored state remains the authority source; a transport may carry an
  admitted action but may not derive authority from session memory or output.
- The first useful adapter should target the Codex desktop workflow that
  produced the attended evidence, before considering a broader SDK service.
- Read-only discovery may inspect docs, command help, schemas, and currently
  exposed tool metadata. A live synthetic task probe is a separate execution
  effect and must be explicitly included in a later sponsor Go.
- Desktop deep links can prefill a workspace and prompt but, per current
  documentation, do not send automatically.
- App-server and SDK surfaces support thread start/resume and turns, but local
  availability, auth, dependency, sandbox, and evidence behavior must be proven
  rather than inferred from documentation.

### Unknowns

- Under which Codex desktop task types native create/read/send task tools are
  exposed, and whether their availability is stable enough for an adapter.
- Whether a native tool can guarantee non-forked creation and exact workspace
  selection in this harness.
- Whether prompt delivery is byte-preserving or needs canonical hashing.
- Which task status, output, interruption, and error fields are observable.
- Whether task identifiers remain resolvable across app restarts and tasks.
- Whether the desktop surface provides a supported machine interface or only a
  harness-private capability.
- What repair is needed for the local broken `codex` installation; repair is
  outside this candidate.
- Which authentication path app-server/SDK would require in this environment.

### Options

| Option | Description | Value | Risk / limitation | Formation verdict |
| --- | --- | --- | --- | --- |
| A | Native Codex desktop task tools, when exposed | Closest to the successful manual workflow; potentially no dependency or credential change | Availability is task/session-specific and absent in the current task; support contract is unclear | Preferred discovery target |
| B | `codex://threads/new` deep link with encoded `path` and `prompt` | Documented, reversible, dependency-free, and easy to hash/decode | Prefills only; the sponsor must still press Send, so it cannot meet the full objective | Baseline/fallback only |
| C | Codex app-server or Codex SDK | Documented programmatic thread/turn/status primitives and explicit sandbox controls | Current CLI package is broken; SDK installation/auth would expand authority and dependencies | Docs/schema research only in first spike |
| D | Codex MCP server plus Agents SDK | Useful later if Codex is one worker inside broader orchestration | Adds dependencies, credentials, long-running process, handoffs, and trace governance well beyond the current need | Reject for first spike |
| E | Scheduled tasks or automation | Can start background work | Unattended behavior violates the current boundary and does not solve an approval-bound fresh handoff safely | Forbidden |

### Recommended Route

Run a separately approved read-only spike that evaluates Option A first,
measures Option B as the documented manual baseline, and limits Option C to
documentation, local help/schema availability, and boundary analysis. Do not
use Option D or E.

If Option A is unavailable or unsupported, return `NO_ADAPTER_CANDIDATE` rather
than repairing/installing Codex or silently switching to SDK/MCP execution.

## Human Decisions Needed

1. Approve or reject execution of this exact read-only discovery contract.
2. Decide whether one explicitly synthetic, no-filesystem-write task creation
   and prompt-delivery probe is authorized if native task tools are exposed.
3. If native tools are unavailable, decide later whether CLI repair or an SDK
   dependency deserves a separate formation mission; neither is pre-approved.

## Pre-Resolved Decisions

- Same Second is read-only and out of scope.
- No dependency, credential, scheduled work, worker dispatch, or workspace
  write is authorized.
- Task transport never grants authority and never activates a child.
- The state kernel must admit exactly one action before any future adapter call.
- A failure to create, bind, identify, or observe a task must fail closed.
- Desktop deep-link prefill is not equivalent to automated prompt delivery.

## Verification And Evidence Needs

- Refreshed official-source inventory with retrieval date and exact URLs.
- Current-session capability inventory distinguishing available, unavailable,
  documented, and inferred surfaces.
- Exact local CLI path and failure output, with no repair attempt.
- Capability matrix for new-task creation, non-forking, workspace binding,
  exact prompt transfer, task ID, status/output, interrupt, sandbox, auth,
  dependency, and external-effect behavior.
- Canonical prompt fixture plus SHA-256 before and after any approved transport.
- If a live probe is separately approved: task ID, creation call, read-only
  sandbox and approval-policy evidence, transport-recorded input bytes or
  canonical JSON, exact nonce observation, tool-call count, terminal status,
  and proof that no repository file changed. Worker echo alone is not proof of
  exact prompt transport.
- Negative observations for unavailable surface, wrong workspace, altered
  prompt, missing task ID, ambiguous status, permission request, and timeout.
- Comparison with the manual attended pilot and an explicit recommendation of
  `NATIVE_ADAPTER_CANDIDATE`, `DEEPLINK_ASSIST_ONLY`, or
  `NO_ADAPTER_CANDIDATE`.

## Candidate Mission Contract

### Mission ID

`V3-CODEX-DISC-001`

### Objective

Determine, without workspace writes or unattended behavior, whether a currently
available Codex task surface can remove sponsor task-creation and prompt-copying
friction while leaving Factory V3 as the sole mission authority.

### Success Criteria

1. Inventory native desktop, deep-link, app-server, SDK, and MCP options from
   official sources and current local capability evidence.
2. Prove which options are actually available in the approved harness without
   installing or repairing anything.
3. Record an observable contract for creation, workspace binding, exact prompt
   transfer, task identity, status/output, failure, and sandbox behavior.
4. If and only if the later execution Go explicitly authorizes the synthetic
   probe and native task tools are exposed, create one non-forked read-only task
   using a fixed no-command/no-write/no-tool prompt, observe its output and
   transport trace, and record no repository change.
5. End with one of the three bounded recommendations and a separate next gate;
   do not implement an adapter.

### Authorized Scope

- Read-only inspection of Factory V3 canons and official Codex documentation.
- Read-only inspection of local executable paths, version/help/schema metadata,
  and current task-tool metadata.
- New evidence artifacts only under
  `docs/Factory/v3/task_surface_discovery/V3-CODEX-DISC-001/`.
- One synthetic task probe only if separately and explicitly included in that
  approval; the probe may not run commands, inspect product files, or write.

### Forbidden Scope

- Same Second writes or integration.
- Any implementation of a worker adapter.
- SDK/package installation, CLI repair, credential or config changes.
- App-server/MCP long-running process, Agents SDK, subagents, concurrency,
  scheduled tasks, automations, background processes, or unattended execution.
- Workspace-write or danger-full-access sandbox.
- Product commands, verification commands, Git mutation, external service
  access, network actions beyond reading official public documentation, push,
  merge, PR, deployment, or runtime-control power.

### Allowed Tools And Commands

- `rg`, `sed`, `find`, `ls`, `wc`, `shasum`, `python3 -m json.tool`
- read-only `git status`, `log`, `show`, `diff`, `rev-parse`, `branch`
- Codex manual fetch helper and official OpenAI documentation reads
- `command -v codex`, `codex --version`, and `codex <surface> --help`; failure
  is evidence and must not trigger repair
- read-only task-tool discovery/list/read calls when available
- one native create/read probe only under the separate explicit probe approval,
  with read-only sandbox, non-interactive/no-escalation approval policy, a fixed
  prompt, and zero permitted worker tool calls

### Dependency Policy

No new dependencies. Do not repair the existing Codex package or install an
SDK, MCP client, CLI, plugin, or package manager artifact.

### Budget And Checkpoint Rules

- No duration, call, file, or output floor.
- Checkpoint after source inventory, capability inventory, optional synthetic
  probe, and final comparison.
- Stop immediately when the recommendation is supported.
- Record command-sourced UTC timestamps and exact tool/surface identity when
  exposed.
- Required discovery outputs are `SOURCE_INVENTORY.md`,
  `CAPABILITY_MATRIX.json`, `DECISION.md`, and, only when the probe is explicitly
  approved and runs, `PROBE_RECORD.json`.

### Human Interrupt Rules

Tier 3 approval is required before any live task creation not already explicit
in the execution Go, prompt send, dependency or installation, credential/auth
change, config mutation, long-running process, workspace write, worker command,
external write, or scope expansion.

### Halt And Fallback Rules

- Halt on absent native task tools, ambiguous non-forked semantics, wrong
  workspace, prompt mismatch, missing task ID, unobservable terminal status,
  any worker tool call, permission escalation, auth request, CLI/package
  failure, or any write.
- Preserve the observation; do not repair or switch surfaces automatically.
- Fall back to `DEEPLINK_ASSIST_ONLY` when only prefill is supported.
- Return `NO_ADAPTER_CANDIDATE` when no bounded surface meets the contract.
- Route any later install/repair or workspace-write proposal to a new mission
  and explicit sponsor decision.

### Re-Entry Instructions

A future discovery task must read this formation artifact, its challenge,
current Factory canons, the latest official Codex documentation, the latest
checkpoint, and current repository state. It must not accept chat memory or a
previous task summary as capability evidence or authority. Any stale source,
changed tool surface, repository drift, or missing approval requires safe hold.

## Recommended Next Step

Run the challenge review and present the repaired candidate for a separate
sponsor Go/no-go. Do not start discovery execution from this artifact.

This is candidate mission-formation output only. It does not authorize
execution until the human explicitly approves the mission contract.
