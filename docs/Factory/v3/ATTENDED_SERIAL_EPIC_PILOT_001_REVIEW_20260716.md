# Attended Serial-Epic Pilot 001 Evidence Review

## Status

Research-only evidence review. `V3-SS-EPIC-001` passed its approved attended,
serial, synthetic-data-only mission in the Same Second repository. The three
children completed in dependency order, a fresh non-forked Codex task replayed
the C01 handoff before C02 activation, and parent verification closed at
revision 18/event sequence 19.

Decision: `PASS_BOUNDED_ATTENDED_PILOT`.

This review records evidence; it does not merge or push Same Second, approve a
worker adapter, start Codex SDK/MCP execution, create runtime authority, promote
a V3 profile, or wire a required gate.

## Evidence Scope

- Product repository: `/Users/eduardodosremedios/same_second`
- Baseline `main`: `7f154e88da652e45bc1a48ce1f5efcd88bc1d8ae`
- Mission branch: `codex/v3-ss-epic-001`
- C01 handoff: `baf0adec14c3d1d9c77922ece528c3b926de7d56`
- C02 implementation: `aff13a4b399a93ff763f105d62d0a5637365cd11`
- C03 implementation: `77b3532ad2f1c67253474afe3f5497bbad23115a`
- Parent verification state: `f8060fcd23231cca842ebac3067fe97bc2c672d2`
- Mission closeout commit: `20554125a422f0fc0afeadf18948b4c8e649a732`
- Authored state: parent `completed`, revision 18, event sequence 19
- Push/merge/deployment: none

The product branch was clean at closeout and at the Factory replay inspection.
It has no configured Git remote. Same Second was not modified during this
Factory review.

## Mission Outcome

The approved reveal-first mission completed these required children serially:

1. `moment-capture-domain`: deterministic moment, inclusive capture window,
   capture admission, coarse-or-unknown synthetic location, and participant
   state.
2. `reveal-engine`: admitted-capture aggregation, deterministic globe points
   and clusters, sparse fallback, mosaic, and local SVG share artifact.
3. `integrated-participant-experience`: local prompt/capture/reveal experience,
   participant, rejected, missed, and spectator paths, loopback server, and
   attended browser QA.

The fresh non-forked resume task recorded a passing C01 replay before event 8
activated C02. Git chronology then shows C02 activation, implementation,
verification, and completion before C03 activation. No child was concurrently
active or start-authorized.

## Original And Replay Observations

The execution task reported:

- 18 Python tests passing;
- 6 Node tests passing;
- Python compilation passing;
- serial graph advisory pass with zero findings;
- loopback desktop and 390x844 browser QA passing;
- one capture-transition timer defect and one four-pixel mobile-overflow defect
  found during attended QA and repaired inside the active C03 envelope;
- the loopback server stopped after QA.

A later Factory closeout task, distinct from the C02/C03 execution task,
replayed the final tree and observed:

- the same 18 Python and 6 Node tests passing;
- Python compilation and `git diff --check` passing;
- graph advisory `ADVISORY_PASS` with zero findings;
- state status `advisory_pass` at revision 18/event 19, no eligible child, and
  safe next action `none` because the parent is complete;
- all C01/C02/C03 artifact hashes matching their authored evidence;
- every post-handoff commit staying inside its active child path envelope;
- no dependency manifest, external-request implementation path, merge commit,
  or listener remaining on port 8765.

## Builder And Verifier Provenance

C01 building and deterministic verification occurred in the originating Codex
desktop task. C02, C03, browser QA, and parent verification occurred in the new
non-forked resume task. The later Factory replay occurred in a third Codex
desktop task. The harness did not expose model identifiers in the product
evidence.

These are different task boundaries but the same harness family. C02/C03
builder and verifier roles were not different independent actors. The Factory
replay independently reran deterministic checks and inspected chronology, but
it did not reproduce the attended browser interaction. Browser observations
are structured same-task evidence, not durable screenshot evidence.

## Friction And FP/FN Observations

- The state kernel and authored handoff admitted exactly one safe action across
  the task boundary.
- The sponsor still had to create the new task and copy the re-entry prompt.
  That is transport friction, not an authored-state failure.
- Browser QA supplied two useful implementation true positives that the initial
  deterministic tests did not expose: timer scope and narrow-layout overflow.
- The Factory graph/state validators produced no observed false positive or
  false negative for the invariants they claim to check.
- The absence of an automated capture-transition browser regression leaves a
  narrower implementation-test durability limit; the attended replay passed,
  but future changes could regress that behavior without the current Node tests
  detecting it.

## Proof Scope And Limits

Supported within this bounded local pilot:

- graph/state artifacts governed a useful three-feature serial mission;
- a fresh non-forked task reconstructed the committed C01 waypoint;
- dependency, one-active-child, verification/evidence, and parent-closeout
  rules held across the recorded transition sequence;
- the local synthetic reveal-first behavior passed deterministic and attended
  checks;
- invalid transport assumptions were not used as state or authority.

Not supported:

- automated task creation or prompt delivery;
- unattended or scheduled execution;
- worker dispatch, concurrency, runtime authority, required-gate readiness, or
  profile promotion;
- real camera, photograph, notification, moderation, location, storage, scale,
  privacy, security, demand, retention, deployment, or production behavior;
- malicious-worker resistance or cross-harness behavior.

The Same Second README still contains stale bootstrap wording alongside its
prototype section. That documentation inconsistency is non-blocking for this
pilot result and remains for a separately authorized product integration step.

## Decision And Next Gate

Record `V3-SS-EPIC-001` as the first bounded passed attended serial-epic pilot.
The manual graph/state/re-entry evidence prerequisite for read-only Codex
task-surface discovery is now satisfied.

The next gate is sponsor review of
`CODEX_TASK_SURFACE_DISCOVERY_FORMATION_20260716.md` and its challenge. Any
live task creation, prompt send, SDK/MCP process, dependency installation,
workspace write, or worker execution requires a separate exact approval.
