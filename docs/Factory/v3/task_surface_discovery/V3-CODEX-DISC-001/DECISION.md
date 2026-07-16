# V3-CODEX-DISC-001 Decision

## Decision

`DEEPLINK_ASSIST_ONLY`

Mission status: `COMPLETED_BOUNDED_DISCOVERY`.

Research-only and non-enforcing. This decision is evidence for a later human
gate, not permission to implement or operate a transport.

The current evidence does not support a native or programmatic adapter
candidate in this environment. It does support a documented dependency-free
deep-link assist that can open a new local task with an absolute workspace path
and prefilled authored prompt. The human must still review and press Send.

This is a partial friction reduction, not automated task creation and delivery,
worker dispatch, or runtime-control power.

## Why

1. The exact native task create/list/read/send controls were not exposed in this
   Codex task. Current absence is environment-specific, but it prevents a
   supported native adapter recommendation now.
2. The local `codex` JavaScript wrapper exists, but all permitted version/help
   invocations failed with `ENOENT` because its packaged Darwin ARM64 binary is
   absent. Repair was forbidden and not attempted.
3. App-server, SDK, non-interactive CLI, and MCP surfaces document enough
   primitives for later programmatic work, but each needs an executable,
   dependency, process, credential decision, or worker run outside this mission.
4. Desktop deep links are explicitly documented to open a new task, bind an
   absolute `path`, and prefill `prompt`, but explicitly do not send it.
5. With no live probe, no stronger claim about prompt integrity, task identity,
   non-fork behavior, status, interruption, or sandbox enforcement is valid.

## Objective Assessment

| Objective | Result |
| --- | --- |
| Eliminate sponsor copy/paste | Supported in principle by a generated deep link carrying the encoded authored prompt |
| Eliminate manual workspace selection | Supported in principle by the absolute `path` parameter |
| Eliminate manual task creation | Partly supported: opening the link opens a new-task composer |
| Eliminate all human handoff action | Not supported: the sponsor must open the link, review, and press Send |
| Return durable task ID and status | Not supported by the deep-link surface |
| Preserve Factory-authored authority | Compatible in design, but no adapter or transport-integrity proof exists |

## Evidence

- `SOURCE_INVENTORY.md`
- `CAPABILITY_MATRIX.json`
- Official [desktop command reference](https://learn.chatgpt.com/docs/reference/commands.md)
- Official [app-server reference](https://learn.chatgpt.com/docs/app-server.md)
- Official [Codex SDK reference](https://learn.chatgpt.com/docs/codex-sdk.md)
- Official [non-interactive reference](https://learn.chatgpt.com/docs/non-interactive-mode.md)
- Official [Codex MCP/Agents SDK reference](https://learn.chatgpt.com/docs/mcp-server.md)

No `PROBE_RECORD.json` exists because the approval explicitly excluded a live
task probe.

## Boundary Compliance

- No Codex task was created, forked, opened, messaged, or controlled.
- No app-server, MCP server, SDK, CLI worker, automation, background process, or
  scheduled task was started.
- No package, dependency, executable, plugin, credential, auth, or configuration
  was installed, repaired, changed, or inspected.
- No adapter, command-dispatch path, worker execution path, or governance routing
  was implemented.
- Same Second remained clean and unchanged at
  `20554125a422f0fc0afeadf18948b4c8e649a732`.
- Factory changes are documentation and exact-path discovery evidence only.
- At mission closeout, Factory `HEAD` remained
  `5a271bc264eed4ddaa0b1aea0c3d813d5fe19d73`; this mission and its preserved
  predecessor recording changes were honestly uncommitted at that observation.
  A later Factory integration commit does not rewrite the original discovery
  result.

## Proof Limits

This mission proves only the official-source comparison and capability absence
observed in this task. It does not prove:

- deep-link behavior in this installed desktop build;
- exact or byte-preserving prompt delivery;
- task ID, status, output, interrupt, or sandbox observability;
- availability or absence of native controls in another task/account/rollout;
- a functioning local CLI, app-server, SDK, MCP server, or adapter;
- unattended, concurrent, cross-harness, malicious-worker, or production use.

The same actor collected and authored the evidence. No independent verifier or
live transport observation exists.

## Verification Observations

- The normal V3 docs advisory lint initially produced two true-positive
  warnings because the new Markdown evidence files did not state their
  research-only/non-enforcing posture explicitly. The posture was added and the
  lint then passed with zero findings.
- The opt-in natural-language evaluator retains four historical non-blocking
  findings in pre-existing canon. It produced no finding against the new
  discovery artifacts after repair.
- Deterministic repository tests, fixture expectations, JSON parsing, state
  template replay, knowledge lint, Python compilation, and diff checks passed.

## Residual Risks

- Desktop deep-link behavior can change and remains product-version dependent.
- URL length, encoding, sensitive prompt content, and accidental disclosure need
  explicit design limits before any helper is implemented.
- A user may send from the wrong visible workspace unless the app makes the
  resolved path unmistakable.
- A prefilled prompt is editable; its hash does not prove which text the user
  ultimately sent.
- Repairing the CLI or adding an SDK would introduce installation, auth,
  process-lifecycle, sandbox, and evidence questions not resolved here.

## Next Gate

The smallest next decision is whether to form and challenge a separate
non-executing `DEEPLINK_ASSIST_ONLY` helper candidate. Such a candidate could
specify deterministic generation of an encoded `codex://new?path=...&prompt=...`
link plus a visible prompt digest, while retaining the human Send action.

That next decision must not imply implementation. Any implementation, link open,
live task probe, CLI repair, SDK dependency, credential, app-server/MCP process,
worker execution, Same Second change, or fully automated adapter remains a
separate approval boundary.
