# V3-CODEX-DISC-001 Source Inventory

## Status

Research-only and non-enforcing. Completed read-only discovery on 2026-07-16.
No live task probe ran.

This inventory distinguishes documented product behavior from capability
observed in this exact Codex desktop task. Documentation is not treated as
proof that a surface is locally available.

## Mission Basis

- Approved candidate:
  `../../CODEX_TASK_SURFACE_DISCOVERY_FORMATION_20260716.md`
- Challenge result:
  `../../CODEX_TASK_SURFACE_DISCOVERY_CHALLENGE_20260716.md`
- Sponsor approval: execute the challenged contract without a live task probe;
  do not install or repair Codex, add dependencies or credentials, start
  app-server/MCP, modify Same Second, implement an adapter, or add
  runtime-control power.
- Factory repository baseline:
  `5a271bc264eed4ddaa0b1aea0c3d813d5fe19d73`
- Observation timestamp: `2026-07-16T06:39:54Z`

The pre-existing uncommitted attended-pilot, formation, challenge, and canon
updates were preserved. They were not mistaken for discovery-created state.

## Official Codex Sources

The OpenAI Codex manual helper reported that its local manual cache was current
on 2026-07-16. The retrieved manual SHA-256 was
`084f81886e62bd0d8eafdc9cbc0b297f026880dbd212bf55796759fe9115ccc9`.

| Source | Material documented | Discovery use |
| --- | --- | --- |
| [ChatGPT desktop app commands](https://learn.chatgpt.com/docs/reference/commands.md) | `codex://threads/new` and `codex://new` open a new local task; `prompt` prefills composer text; `path` selects an absolute local workspace; the prompt is not sent automatically | Establishes the dependency-free assisted baseline, not an automated adapter |
| [Codex app-server](https://learn.chatgpt.com/docs/app-server.md) | JSON-RPC `thread/start`, `thread/resume`, `thread/fork`, `turn/start`, `turn/interrupt`, thread IDs, `cwd`, sandbox overrides, and streamed terminal events | Establishes a possible later programmatic transport; no server was started |
| [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk.md) | TypeScript and Python clients can start/resume Codex threads; installation is required; the Python SDK controls a pinned local app-server runtime | Establishes a later dependency-bearing option; no SDK was installed or imported |
| [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode.md) | `codex exec` can create/resume sessions, set sandbox behavior, and emit JSONL including thread and turn events | Establishes a later CLI option; the local executable could not launch |
| [Use Codex with the Agents SDK](https://learn.chatgpt.com/docs/mcp-server.md) | `codex mcp-server` exposes `codex` and `codex-reply`, including `cwd`, sandbox, approval policy, and returned thread ID | Confirms a broader server/dependency/credential lane excluded from this mission |
| [Scheduled tasks](https://learn.chatgpt.com/docs/automations.md) | Scheduled runs create background or unattended work | Confirms that scheduling is a different continuity model and remains forbidden |

## Factory Sources

- `../../ATTENDED_SERIAL_EPIC_PILOT_001_REVIEW_20260716.md`
- `../../CODEX_SDK_ORCHESTRATION_DIRECTION.md`
- `../../MISSION_CONTROL_CONTRACT.md`
- `../../SERIAL_MISSION_GRAPH_CONTRACT.md`
- `../../SERIAL_MISSION_STATE_KERNEL.md`
- `../../GOVERNANCE_BOUNDARIES.md`
- `../../ROADMAP_TO_FULL_VISION.md`

These sources preserve the ownership split: Factory authors and admits mission
state; a future transport may carry one admitted action but may not derive or
expand it.

## Current-Task Capability Observation

The exposed tool-name inventory was checked for the exact native controls
`create_thread`, `fork_thread`, `list_threads`, `read_thread`,
`send_message_to_thread`, `handoff_thread`, `set_thread_pinned`,
`set_thread_archived`, and `set_thread_title`.

Result: none was exposed in this task. No approximate or unrelated tool was
treated as a substitute. This observation is task- and rollout-specific; it is
not a universal claim about Codex desktop.

No task was created, opened, forked, messaged, handed off, pinned, archived, or
renamed.

## Local CLI Observation

`command -v codex` returned:

```text
/Users/eduardodosremedios/.nvm/versions/node/v24.14.0/bin/codex
```

The path is a symbolic link to
`../lib/node_modules/@openai/codex/bin/codex.js`. Each permitted read-only
invocation exited `1` with `ENOENT` while attempting to spawn the absent native
binary at the package's Darwin ARM64 vendor path:

- `codex --version`
- `codex app-server --help`
- `codex mcp-server --help`
- `codex exec --help`

The package was not repaired, reinstalled, updated, or authenticated. No server
or worker process began.

## Repository And No-Touch Observations

- Factory V3 remained on `main` at
  `5a271bc264eed4ddaa0b1aea0c3d813d5fe19d73` while evidence-only files were
  authored under the approved path.
- Same Second remained at
  `20554125a422f0fc0afeadf18948b4c8e649a732` with a clean worktree.
- No dependency manifest, credential, configuration, task, service, external
  write, Git commit, push, merge, or deployment was created.
- An initial combined shell inspection was rejected before execution because
  it contained disallowed temporary-file cleanup syntax. The inspection was
  rerun without temporary files; the rejection caused no state change.

## Provenance And Limits

The same Codex task performed source collection, capability inspection, and
evidence authoring. Deterministic validation can check artifact shape and
repository state, but there is no independent actor and no live transport
observation.

Because the sponsor explicitly excluded a probe, this mission cannot establish
prompt byte preservation, native task IDs, non-fork behavior, workspace binding,
status streaming, interruption, or sandbox enforcement in a newly created
desktop task. It also cannot establish whether native controls are available in
another task type, account, rollout, or future version.
