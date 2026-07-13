# Live Fresh-Worker Trial 002 Evidence Review

## Status

Research-only evidence review. `V3-FW-TRIAL-002` ended
`FAIL_CLOSED_SAFE_HOLD` on 2026-07-13 before a re-entry brief existed. This
review closes the contaminated trial; it does not authorize recovery, Trial 003
execution, an external write, an attended serial epic, profile promotion, or
runtime orchestration.

## Evidence Scope

- Product repository: `/Users/eduardodosremedios/same_second`
- Trial branch: `codex/v3-fw-trial-002`
- Pause checkpoint commit: `cd8ac5bfce6731c1857831a5f9a1574e21312c4f`
- Protocol safe-hold commit: `0d66fa906fa8e6b7fbf6423ee9c3ff41a62602e9`
- Authored state: revision 7, event 8, parent and active child at `safe_hold`
- Brief, comparison, validator, and focused test: absent

The fresh task reported that its initial broad repository scan exposed
`SEALED_ANSWER_KEY.json` and Trial 001 content before a Trial 002 brief commit.
The harness supplied no independent access log or transcript artifact, so exact
read timing and exposed bytes remain actor-reported. Git independently proves
that no brief or product artifact was committed and that the safe-hold commit
changed only authored state and events.

## Observed Protocol Outcome

The pause leg successfully committed a 23-path value-free template, explicit
empty interrupts and decisions, split 17-field critical versus 6-field
completeness scoring, graph/state/event artifacts, and a handoff checkpoint.
Before those reconstruction repairs could be tested, ordinary fresh-task
repository orientation encountered the co-located sealed key and forbidden
prior-trial material. The fresh task correctly treated the exposure as a
protocol failure, entered safe hold, and performed no C02 product work.

## Primary Finding

Trial 002 made the answer-key payload and its read prohibition visible inside
the same initial workspace that the worker had to inspect. That design relied
on task-specific read ordering taking effect before normal repository discovery.
It therefore tested co-located procedural secrecy as well as artifact
sufficiency, and failed at the former before measuring the latter.

This does not show that the repaired checkpoint or template was insufficient.
It shows that co-location is too fragile for the intended fresh-task protocol.

## What The Trial Demonstrated

- The kernel admitted safe hold and removed C02 start authorization at revision
  7/event 8.
- The worker stopped before authoring a contaminated brief or comparison.
- No validator, test, dependency, external effect, or product implementation was
  created.
- Protocol failure remained durable evidence instead of being rewritten into a
  pass.

## What The Trial Did Not Demonstrate

- It did not test artifact reconstruction or the 17/6 comparison policy.
- It did not prove exact file-read chronology, private-context absence, or
  access-control isolation.
- It did not prove an external commitment-and-reveal channel.
- It did not prove cross-harness behavior, attended serial-epic behavior,
  worker dispatch, concurrency, endurance, runtime authority, or profile readiness.

## State And Closeout Distinction

The state-kernel v0.1 CLI has no terminal `halt` transition. Authored state
therefore remains at `safe_hold` revision 7/event 8. The product-repository
closeout records the human decision to halt and close Trial 002 rather than
resume it. No synthetic terminal transition is appended.

## Validator Observations

The halted mission record passes the advisory mission-record validator with no
findings. No mission-record-validator false positive or false negative was
observed. The gap is in live protocol design: the validators do not claim to
enforce file-read isolation or answer-key custody.

## External Commitment-And-Reveal Requirements

A later candidate should separate the answer-key commitment from its payload:

1. commit only a versioned SHA-256 commitment, canonical byte length, and reveal
   verification rule inside the initial workspace;
2. keep the exact answer-key payload outside the fresh worker's initial
   workspace, Git object database, prompt, attachments, summaries, and indexed
   repository context;
3. require the fresh worker to commit the brief before a human-controlled reveal;
4. after reveal, require stdlib verification that the payload bytes reproduce
   the pre-handoff commitment before any comparison;
5. safe-hold on early reveal, digest mismatch, missing commitment metadata,
   stale state, or more than one safe next action; and
6. classify any successful result as accidental-discovery resistance under a
   human-controlled reveal, not malicious-worker isolation or access control.

The external payload location, custody, reveal action, and authorized writer
must be named in a separately approved execution envelope. This review does not
select or create that channel.

## Decision And Next Gate

Close `V3-FW-TRIAL-002` as a failed, fail-closed trial. Do not resume C02. The
next gate is non-executing formation and challenge of a `V3-FW-TRIAL-003`
candidate using an external commitment-and-reveal answer-key protocol. Any
external placement or live Trial 003 execution requires another explicit human
Go. An attended serial-epic pilot remains later and contingent on sufficient
fresh-worker evidence.
