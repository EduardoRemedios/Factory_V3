# Codex Deep-Link Attended Trial Formation - 2026-07-16

## Status

Research-only, non-enforcing, and non-executing mission-formation output for
candidate trial `V3-CODEX-DL-TRIAL-001`.

This artifact does not create the trial workspace or prompt file, run the
helper, generate or open a link, create a Codex task, send a prompt, capture a
screenshot, start a worker, modify Same Second, add a dependency or credential,
or add runtime-control power.

## Mission Formation Result

### Route

`CANDIDATE_V3_ENVELOPE`

Implemented `V3-CODEX-DL-001` proves deterministic local input validation and
URL construction only. One separately approved attended synthetic trial is now
the smallest useful way to observe installed-desktop acceptance, workspace
binding, composer prefill, human Send, fixed response, and no-write behavior.

### Problem Statement

Factory V3 can now generate a deterministic human-Send deep link, but no live
evidence shows that this desktop build opens it as a genuinely new task with the
expected workspace and prompt. Unit tests cannot observe the composer or the
task response.

The trial must test that narrow interaction without drifting into product work,
task automation, SDK/MCP execution, or a claim of byte-perfect transport.

### Desired Outcome

Run, only after a separate sponsor Go, one attended trial that:

1. prepares one exact empty disposable workspace;
2. writes one pinned non-sensitive prompt artifact;
3. generates one deterministic deep link with the implemented helper;
4. lets the sponsor inspect the new-task composer and workspace;
5. lets the sponsor press Send exactly once;
6. observes one exact acknowledgment with no tool, command, permission, or file
   activity;
7. preserves human observations and before/after filesystem evidence;
8. closes with bounded supported and unsupported claims.

### Non-Goals

- No Same Second or other product repository.
- No coding, repository inspection, command execution, testing, file access, or
  implementation by the new task.
- No automatic link open, automatic Send, task ID API, task status API, native
  task control, task reading, task messaging, archive, pin, handoff, or resume.
- No Codex CLI, app-server, SDK, MCP, Agents SDK, dependency, credential,
  configuration, plugin, automation, scheduler, daemon, or background process.
- No proof of byte-preserving transport, malicious-worker resistance,
  cross-harness behavior, production readiness, or unattended operation.
- No retry, prompt rewrite, alternate workspace, or second task under the same
  approval.

### Assumptions

- The sponsor is present to inspect the composer, press Send, and return the
  fixed acknowledgment plus observation answers.
- The desktop app accepts a `codex://new` link when the sponsor clicks it.
- A new empty local directory is sufficient as a desktop workspace for this
  no-tool task.
- The fixed prompt is non-sensitive and safe to appear in a URL, screenshot,
  transcript, and Factory evidence.
- Absence of visible tool/activity cards is sponsor-observed evidence, not a
  machine-verifiable trace.
- The current Factory task cannot read the new task. One short sponsor-mediated
  result transfer remains necessary.

### Unknowns

- Whether the installed app accepts the generated link.
- Whether the exact resolved workspace is visibly confirmable before Send.
- Whether composer text matches the prompt byte-for-byte or only visually.
- Whether a technical task/thread ID is visible.
- Whether opening the workspace causes any local metadata write.
- Whether the new task follows the no-tool instruction without invoking a
  surface hidden from sponsor observation.
- Whether screenshots capture enough UI context for later review.

## Exact Trial Inputs

### Workspace

```text
/Users/eduardodosremedios/codex_deeplink_trial_001_workspace
```

Preparation may create this directory only after trial execution approval. It
must be absent or empty at preflight. If it exists and is non-empty, safe-hold;
do not delete or reuse its contents.

The directory is retained after closeout unless the sponsor later authorizes
cleanup.

### Prompt Artifact

Future evidence path:

```text
docs/Factory/v3/deeplink_assist/V3-CODEX-DL-TRIAL-001/PROMPT.txt
```

Exact UTF-8 content, including final newline:

```text
Mission V3-CODEX-DL-TRIAL-001.
This is a synthetic no-tool, no-write deep-link observation.
Do not use tools, run commands, read files, or modify anything.
Reply with exactly this single line and nothing else:
V3-CODEX-DL-TRIAL-001 ACK 7F3C2A9E
```

Pinned input facts:

- bytes: `245`
- SHA-256:
  `913c411439695f29ce0ad95ab0310486025b7ef4743beca87687e4baf9bb0784`
- expected response:
  `V3-CODEX-DL-TRIAL-001 ACK 7F3C2A9E`

## Options

| Option | Value | Risk / limitation | Formation verdict |
| --- | --- | --- | --- |
| A. Human-attended link/composer/task observation | Tests the actual desktop surface while keeping Send human-controlled | Sponsor-mediated evidence and one manual result transfer remain | Recommended |
| B. Computer-use or GUI automation | Could capture UI programmatically | Adds desktop-control authority and may itself open/send incorrectly | Reject for first trial |
| C. Native task tools, CLI, SDK, app-server, or MCP | Could automate task identity/status later | Unavailable or separately governed; changes the surface under test | Defer |

## Trial Sequence

1. Preflight:
   - verify Factory repository state and approved contract;
   - verify Same Second remains untouched;
   - verify the exact workspace path is absent or empty;
   - create only that directory;
   - write the exact prompt artifact;
   - record the empty workspace snapshot.
2. Generate:
   - run `scripts/factory_v3_codex_deeplink.py` once;
   - require exit `0`, pinned prompt bytes/hash, exact resolved workspace,
     `human_send_required: true`, and `transport_proof: false`;
   - persist the JSON as `PREPARE.json`;
   - present the generated link to the sponsor without opening it.
3. Human composer checkpoint:
   - sponsor clicks the link;
   - confirms a new task opened;
   - confirms the visible workspace is the exact trial workspace or records
     `unknown`;
   - visually compares the complete composer prompt;
   - captures a pre-Send screenshot if possible;
   - does not Send on any mismatch.
4. Human Send:
   - sponsor presses Send once only after the checkpoint passes.
5. New-task observation:
   - expected response is the single pinned acknowledgment;
   - any tool call, command, permission request, file activity, extra prose,
     wrong nonce, error, or ambiguity fails safe;
   - sponsor captures a post-response screenshot if possible.
6. Return:
   - sponsor returns the acknowledgment and structured observations to the
     originating Factory task;
   - the manual result transfer is recorded as residual friction.
7. Closeout:
   - compare the workspace before/after;
   - retain artifacts;
   - record supported/unsupported claims, provenance, screenshot availability,
     and any mismatch;
   - do not retry automatically.

## Human Decisions Needed

1. Approve or reject execution of this exact attended trial.
2. During execution, decide whether the visible composer/workspace checkpoint
   passes before pressing Send.
3. If the trial safe-holds, decide later whether a repaired trial is warranted.

## Pre-Resolved Decisions

- Trial ID: `V3-CODEX-DL-TRIAL-001`.
- Use this Factory task for preparation and closeout.
- Use the exact workspace, prompt, hash, nonce, and expected response above.
- One generated link, one click, one Send, and one new task maximum.
- New task is no-tool and no-write.
- Human review and Send are mandatory.
- Sponsor observation is required because no task-reading API is available.
- Screenshots are preferred evidence; absence must be recorded, not hidden.
- Worker echo is supplementary evidence, not transport-integrity proof.
- Any mismatch safe-holds; there is no automatic retry.
- Same Second remains outside scope.

## Verification And Evidence Needs

Required future artifacts under
`docs/Factory/v3/deeplink_assist/V3-CODEX-DL-TRIAL-001/`:

- `PROMPT.txt`
- `PREPARE.json`
- `HUMAN_OBSERVATION.md`
- `CLOSEOUT.md`
- optional sponsor-provided screenshot files or durable screenshot references

Required observations:

- prompt bytes/hash match the pinned values;
- helper output matches the exact workspace and boundary flags;
- workspace preflight is absent-or-empty;
- sponsor reports new-task open, workspace result, composer result, Send count,
  response, visible activity/tool result, permission result, task ID if visible,
  and screenshot availability;
- workspace after-state matches before-state;
- Factory and Same Second repository states are recorded;
- same-actor/harness and sponsor-mediated limitations remain explicit.

## Candidate Trial Contract

### Objective

Observe one attended synthetic use of the deterministic deep-link helper against
the installed Codex desktop app without permitting the new task to use tools,
read files, run commands, or write.

### Success Criteria

1. Exact workspace is created empty and remains unchanged.
2. Exact prompt artifact matches 245 bytes and the pinned SHA-256.
3. Helper output passes all pinned field checks and is persisted.
4. Sponsor observes a new-task composer with the exact prompt visually and an
   exact or explicitly `unknown` workspace observation.
5. Sponsor presses Send exactly once only after the composer checkpoint.
6. New task returns exactly
   `V3-CODEX-DL-TRIAL-001 ACK 7F3C2A9E`.
7. No visible tool, command, file, permission, or extra-response activity
   occurs.
8. Before/after workspace snapshots match.
9. Evidence records sponsor mediation, screenshot availability, missing task ID
   if applicable, and lack of byte-level transport proof.

Workspace observation `unknown` may support a partial result but cannot produce
a full PASS. Full PASS requires the exact workspace to be visibly confirmed.

### Authorized Scope

- Create the exact empty disposable workspace directory.
- Create/update only the four required trial artifacts under the exact Factory
  evidence directory.
- Run the implemented helper once and read its JSON.
- Present the generated link to the sponsor.
- Sponsor may click the link, inspect the composer/workspace, capture
  screenshots, and press Send once.
- New Codex task may produce only the fixed text response and use no tools.
- Read-only filesystem/repository inspection for before/after evidence.
- Active canon updates required to record the result.

### Forbidden Scope

- Same Second or any other product repository.
- More than one link generation, click, Send, or task.
- Prompt editing, alternate prompt/workspace/nonce, retry, or recovery.
- Any new-task tool, command, file read, file write, permission request, network
  use, browser/GUI/computer-use tool, plugin, connector, skill, or sub-agent.
- Automatic link opening or automatic Send.
- Codex CLI, app-server, SDK, MCP, Agents SDK, dependency, credential, config,
  scheduler, daemon, background process, concurrency, deployment, push, merge,
  PR, adapter, required gate, profile, or runtime-control changes.

### Allowed Tools And Commands

Preparation/closeout task only:

- `mkdir` for the one exact workspace after approval
- `apply_patch` for the exact Factory evidence/canon files
- `python3 scripts/factory_v3_codex_deeplink.py` once
- `shasum -a 256`, `wc -c`, `find`, `stat`, `ls`, `rg`, `sed`
- read-only Git commands
- repository/advisory verification commands

`open`, `pbcopy`, `osascript`, browser/computer-use automation, `codex`,
app-server, MCP, package managers, network clients, and task-control tools are
forbidden. The sponsor performs the one link click and Send manually.

### Dependency Policy

No new dependencies, packages, plugins, credentials, authentication, or
configuration.

### Budget And Checkpoint Rules

- No duration or action floor.
- One link, click, Send, and task maximum.
- Checkpoint after preflight, helper generation, pre-Send human inspection,
  response observation, and before/after comparison.
- Pause indefinitely at the human checkpoint if necessary; no scheduled wake.
- Stop immediately on success or first mismatch.

### Human Interrupt Rules

The sponsor must explicitly confirm the composer/workspace checkpoint before
Send. The sponsor must return the response and observation answers for closeout.
No missing answer may be inferred.

Any request for retry, prompt change, workspace change, tool use, permission,
automatic task reading, cleanup, or broader automation requires a new human
decision.

### Halt And Fallback Rules

Safe-hold without Send when:

- workspace exists and is non-empty;
- prompt bytes/hash differ;
- helper output differs or fails;
- the link does not open a new task;
- workspace is wrong or ambiguous;
- composer prompt differs or cannot be reviewed.

Safe-hold after Send when:

- response differs or includes extra text;
- any visible tool/command/file/permission activity occurs;
- task behavior is ambiguous;
- workspace after-state changes.

Preserve evidence and do not retry. Manual task creation/copying remains the
fallback.

### Re-Entry Instructions

Read this formation artifact, its challenge, helper documentation/closeout,
current canons, and current repository state. Confirm explicit sponsor approval
for this exact trial. Do not create the workspace or prompt, generate a link, or
ask the sponsor to click until approval is verified.

After the sponsor leaves for the new task, resume only from the persisted
`PREPARE.json` and returned human observations. Session memory or worker echo
alone is not sufficient evidence.

## Recommended Next Step

Run the challenge review and present the repaired attended trial for a separate
sponsor Go/no-go. Do not prepare or execute the trial from this artifact.

This is candidate mission-formation output only. It does not authorize execution
until the human explicitly approves the mission contract.
