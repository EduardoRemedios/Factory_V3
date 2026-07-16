# V3-CODEX-DL-ADOPT-001 Optional Attended-Aid Adoption Decision

## Status

`ADOPTED_OPTIONAL_ATTENDED_AID`

Research-only, advisory, non-enforcing, and non-default.

## Decision

The sponsor approved `V3-CODEX-DL-ADOPT-001` under the exact challenged
optional attended-aid contract on 2026-07-16.

Factory V3 may now recognize the existing deterministic deep-link helper as an
optional attended handoff mechanism inside future missions that:

1. already possess exact authority for the target worker task and workspace;
2. explicitly name the helper as an allowed handoff mechanism;
3. use a short non-sensitive prompt artifact;
4. preserve authored graph/state, repository checks, and durable re-entry
   artifacts as the sources of state and authority;
5. retain deterministic preparation evidence;
6. require human workspace/prompt review and Send;
7. provide manual task creation/copy-paste or authored safe hold as fallback.

Adoption approval alone does not authorize a helper run, link generation/open,
task creation, Send, worker execution, retry, or product change.

## Approval

Sponsor approval:

> Approve V3-CODEX-DL-ADOPT-001 under the exact challenged optional attended-aid contract. Do not begin full automation, push, or merge.

Approved formation:

- `CODEX_DEEPLINK_ATTENDED_ADOPTION_FORMATION_20260716.md`

Approved challenge:

- `CODEX_DEEPLINK_ATTENDED_ADOPTION_CHALLENGE_20260716.md`
- challenge verdict: `PASS`

Repository `commit_before`:

```text
ca244e61ee6732603c6edf239a3392d6c041ccf0
```

## Eligibility

All challenged eligibility conditions are binding:

- separately approved exact mission envelope;
- exact target worker task and workspace authority;
- explicit per-mission naming of the deep-link aid;
- existing regular UTF-8 prompt file;
- non-empty, NUL-free, at most 8,192 bytes;
- non-sensitive classification;
- prompt points to authored durable state;
- existing absolute workspace directory with reviewed resolved path;
- human sponsor available for review and Send;
- manual fallback available.

If any condition is false or unknown, the aid is ineligible.

## Required Use Protocol

For an eligible future mission:

1. prepare or select the exact prompt artifact from authored mission records;
2. run the unchanged helper once for that handoff;
3. retain the resolved workspace, prompt bytes/SHA-256, URL byte count,
   `human_send_required: true`, and `transport_proof: false`;
4. have the human review the workspace/project and complete visible prompt;
5. permit one human Send only under the existing mission authority;
6. do not Send on mismatch, ambiguity, helper failure, sensitive-content
   concern, or unsuitable URL length;
7. use manual fallback or the mission's authored safe-hold rule;
8. record the handoff result and relevant limitations.

Screenshots remain conditional evidence. They are recommended for a new
desktop/harness version, anomaly, dispute, or later evidence review and must not
expose sensitive content.

## Authority Boundary

The adopted aid cannot:

- authorize or activate a child;
- create worker-task authority;
- expand paths, commands, dependencies, or external effects;
- satisfy dependency, verification, evidence, or closeout gates;
- replace expected-revision or repository-state checks;
- convert a derived cursor into authority;
- make session memory authoritative;
- grant standing, scheduled, unattended, or runtime authority.

Human Send is admitted by the separately approved mission envelope, not by the
helper or this decision.

## Explicit Non-Approval

- No live use under this adoption-recording mission.
- No default use or required gate.
- No helper implementation, limit, test, or dependency change.
- No automatic link opening, Send, retry, task reading, task status, interrupt,
  resume, archive, pin, or handoff.
- No worker dispatch, adapter, Codex CLI repair, app-server, SDK, MCP, Agents
  SDK, plugin, connector, credential, scheduler, daemon, background process, or
  concurrency.
- No transport-integrity, full-path UI, hidden-tool, task-identity, reliability,
  malicious-worker-resistance, or production-readiness claim.
- No Same Second change, deployment, push, merge, profile promotion, governance
  routing, runtime authority, or Factory V2 removal.

## Evidence And Limits

The adoption is supported by:

- deterministic stdlib helper implementation and eight focused tests;
- pinned portable fixtures;
- code-only closeout;
- one attended synthetic trial at `PASS_WITH_LIMITATIONS`;
- retained prompt, preparation JSON, observation, screenshot, and closeout;
- formation/challenge review of default-use, sensitive-prompt, evidence-burden,
  retry, state-authority, and worker-authority risks.

The evidence does not prove general desktop reliability, byte-level transport,
task identity/status, product-workspace behavior, unattended execution, or
automation.

## Verification

Adoption recording preserved:

- unchanged helper implementation, tests, limits, and fixtures;
- `python3 -m unittest discover -s tests`: 35 tests passed;
- `bash scripts/knowledge_lint.sh`: pass, 56 checked files and 2 existing active
  pitfalls;
- `./scripts/factoryctl context-index`: pass, 1,597 sources, 17,105 chunks, and
  2,404 facts;
- V3 docs advisory lint: `ADVISORY_PASS`, zero findings/warnings;
- V3 operational-readiness evaluation: `ADVISORY_PASS`, zero
  findings/warnings;
- natural-language pilot: the same four historical non-blocking findings in
  `LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md` and
  `MISSION_CONTROL_CONTRACT.md`; no finding against this adoption record;
- pinned mission-control and serial-graph expectation comparisons: pass;
- mission-record fixture corpus: expected invalid/legacy findings retained;
- serial mission-state template status: `advisory_pass`;
- `python3 -m py_compile scripts/factory_v3_*.py`: pass;
- `git diff --check`: pass;
- Same Second: clean at
  `20554125a422f0fc0afeadf18948b4c8e649a732`;
- retained trial workspace: empty;
- no direct helper command, live link generation/open, task, Send, worker,
  dependency, external effect, push, or merge.

The same Factory task authored the decision record and ran verification. This
is same-actor closeout, not independent machine or task-API verification.

## Next Gate

Use the adopted aid only in the next separately approved useful mission whose
exact envelope satisfies and names this contract. Collect bounded natural
friction, fallback, and anomaly evidence without manufacturing scope.

Any full automation, native task control, task-status adapter, CLI repair,
app-server/SDK/MCP, dependency, credential, or worker-orchestration proposal
requires a new non-executing formation/challenge and separate sponsor approval.
