# Factory V3 Deterministic Serial Mission-State Kernel

## Version
v0.4

## Status
Research-only, advisory, and non-enforcing.

Version v0.2 records the 2026-07-13 live Trial 001 fail-closed observation and
the v0.1 limitation that administrative terminal halt is not a kernel
transition. It changes no state schema, CLI, or authority behavior.

Version v0.3 records Trial 002's second fail-closed observation: the fresh task
reported pre-brief exposure of the co-located key, and the kernel admitted safe
hold before product work. It changes no state schema, CLI, or authority behavior.

Version v0.4 records Trial 003's successful external commitment-and-reveal
continuation through three serial children and parent closeout, plus its separate
R1 product repair after later review found a test false negative. It changes no
state schema, CLI, or authority behavior.

This kernel calculates and persists state decisions for an authored serial
mission graph. It does not dispatch workers, execute implementation or
verification commands, grant runtime authority, schedule work, create leases,
route governance, or integrate with required gates.

## Purpose
Bridge `SERIAL_MISSION_GRAPH_CONTRACT.md` and a possible future worker adapter
with the smallest deterministic state mechanism that can be exercised before
any adapter exists. Factory owns transition admission and authored mission
state. A future worker remains responsible for tactical implementation and
test/fix cycles inside one separately activated child envelope.

## Artifacts

- Kernel and CLI: `scripts/factory_v3_serial_mission_state.py`
- State template: `templates/V3_SERIAL_MISSION_STATE_TEMPLATE.json`
- Event template: `templates/V3_SERIAL_MISSION_EVENTS_TEMPLATE.jsonl`
- Fixtures: `tests/fixtures/factory_v3_serial_mission_state/`
- Focused tests: `tests/test_factory_v3_serial_mission_state.py`

The implementation uses only the Python standard library and imports the
existing serial graph validator to reject invalid graph inputs.

## Authored State
The versioned JSON state is authoritative. It records:

- mission and graph identity, including a canonical graph digest;
- monotonic state revision and event sequence;
- parent status and one current serial child slot;
- child status, dependencies, requiredness, start authorization, verification,
  evidence, and repository-state reference;
- last safe checkpoint;
- open decisions and safe-hold reason;
- parent verification and evidence;
- current repository-state reference.

The graph remains the authored contract for objective, authority ceiling,
paths, commands, and dependency policy. The state cannot silently change that
contract: graph digest, mission ID, child IDs, dependencies, and requiredness
are checked on every load.

## Append-Only Events
Every accepted mutation appends one versioned JSONL event with:

- sequence and deterministic event ID;
- mission and optional child ID;
- transition name, actor reference, supplied timestamp, and authority basis;
- evidence and repository-state references;
- prior and resulting state revisions;
- transition-specific public data.

Events contain no chain-of-thought, transcript, hidden planner state, or
vendor-private cognition. Invalid transitions produce an error and append no
success event.

The filesystem cannot atomically update two files. The implementation therefore
does not claim cross-file atomicity. It appends and `fsync`s the event first,
then writes and `fsync`s a temporary state file and atomically replaces the
authored state. A crash between those operations can leave the event ahead of
state. Every command checks sequence and revision linkage first and fails with
`event_state_divergence`; it does not guess, truncate the append-only log, or
continue from session memory. Repair requires an explicit evidence-backed
reconciliation outside the failed command.

## Deterministic Transitions

| CLI command | Pure transition | Admission summary |
| --- | --- | --- |
| `init` | `initialize` | Valid graph, new state/event paths, explicit actor/timestamp/authority |
| `activate` | `activate_child` | Known child, matching revision, no active slot, dependencies complete |
| `checkpoint` | `checkpoint` | Named checkpoint, repository-state and evidence references |
| `verification-pending` | `mark_verification_pending` | Current active child only |
| `record-verification` | `record_verification_result` | Current verifying child; pass requires `PROVED` evidence |
| `complete-child` | `complete_child` | Passing child verification and proved evidence |
| `safe-hold` | `enter_safe_hold` | Explicit reason; preserves the current serial child slot |
| `resume` | `resume` | Authored-state source, matching repo state, authority basis, one safe next action |
| `record-parent-verification` | `record_parent_verification` | All required children complete; pass requires proved evidence |
| `close` | `close_parent` | Required children, child evidence, and parent verification all pass |

Failed child or parent verification enters safe hold. Recovery is not implied.
A later `resume` must carry an explicit authority basis and exactly one bounded
safe action; the prior failure stays authored until the child is moved back to
verification pending and a new result is recorded.

## Derived Decisions
`status` and `eligible` validate graph, state, and event linkage, then derive:

- dependency-eligible children;
- exactly one safe next-action recommendation;
- parent closeout eligibility.

These values are cursors only. `derived_cursors_grant_authority` is always
`false`, and activation still requires an explicit authority basis. Session
memory is never accepted as state or authority.

## CLI Discipline
All output is deterministic JSON. Mutations use optimistic concurrency through
`--expected-revision`. Exit code `0` means the command was accepted; exit code
`2` means input, consistency, or transition rejection; exit code `3` means a
persistence operation failed and event/state divergence must be checked. The
CLI makes no network calls and has no command-execution path.

Example read-only status:

```bash
python3 scripts/factory_v3_serial_mission_state.py status \
  --state docs/Factory/v3/templates/V3_SERIAL_MISSION_STATE_TEMPLATE.json \
  --events docs/Factory/v3/templates/V3_SERIAL_MISSION_EVENTS_TEMPLATE.jsonl \
  --graph docs/Factory/v3/templates/V3_SERIAL_MISSION_GRAPH_TEMPLATE.json \
  --mission-id EPIC-001
```

## Source-Of-Truth And Recovery Limits
- Authored JSON state is the mission-state source of truth.
- The graph is the authority/dependency contract and is digest-pinned by state.
- Events are append-only transition evidence, not a second authority source.
- Derived eligibility and next-action output cannot activate a child.
- State/event divergence blocks all subsequent commands.
- The kernel does not auto-repair, replay external effects, or infer missing
  authority from an event, cursor, chat transcript, or session memory.

## Evidence Limits And Next Gates
Deterministic fixtures prove local transition semantics and persistence checks
for the covered inputs. Live Trial 001 additionally showed the kernel preserving
safe hold after a 19/23 re-entry comparison and preventing C02 from starting.
It did not prove artifact-sufficient continuation, attended serial-epic
behavior, worker-adapter safety, runtime authority, or operational profile
readiness. Kernel v0.1 also has no terminal halt transition, so the separately
recorded human closeout does not rewrite the authored safe-hold state.

Trial 002 further showed that correct safe-hold mechanics do not make a
co-located answer-key channel operationally suitable. File-read custody and
human-controlled reveal remain outside the kernel's authority and proof scope.

Trial 003 supplied one bounded successful continuation: a fresh task passed all
23 scored re-entry fields under external commitment-and-reveal, then completed
the three-child state graph at revision 15/event 16. A later product-contract
defect was repaired under separate R1 authority without rewriting that authored
state/event history. This supports the kernel's local transition role; it does
not prove an attended multi-feature epic or worker-adapter safety.

The next decisions remain separate and ordered. The three-sample
evidence-integrity review is complete at `KEEP_OPTIONAL_NO_SCHEMA_CHANGE`:

1. form and challenge a non-executing attended serial-epic pilot candidate;
2. make a separate decision on its exact execution envelope;
3. only later consider read-only Codex SDK/MCP discovery.
