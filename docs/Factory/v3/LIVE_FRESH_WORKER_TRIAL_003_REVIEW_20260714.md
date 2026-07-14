# Live Fresh-Worker Trial 003 Evidence Review

## Status

Research-only evidence review. `V3-FW-TRIAL-003` passed its external
commitment-and-reveal re-entry gate at 23 of 23 fields and completed its three
serial children. A later Factory closeout inspection found one product-contract
defect that the original four-test suite missed. Separately authorized recovery
`V3-FW-TRIAL-003-R1` repaired that exact-path ordering defect, added one
regression test, aligned the pinned expected output, and closed locally.

This review records bounded evidence. It does not integrate the product work,
approve an attended serial epic, promote a profile, create worker dispatch,
wire a required gate, or add runtime authority.

## Evidence Scope

- Standalone worker repository:
  `/Users/eduardodosremedios/same_second_trial003_worker`
- Sanitized baseline: `535cac98e94bd4c8f527cb04961e2289303074e9`
- Pause-leg handoff: `621c74b`
- Committed re-entry brief: `47bf33f433b1f8a8e34a13a4bd2ef9d36c861226`
- Frozen comparison: `15047e553ee1f1162c11b6234039aabc838fa2a2`
- Original parent closeout: `b8794062bb9f380a2b723deb1b47ca8ad0d4ba04`
- R1 implementation: `9d18906bd6fb4443e61e684954f6300306c13298`
- R1 evidence closeout: `7e9c0fa7a600e5486585e6204eb0a42b3b514013`
- Canonical Same Second repository: unchanged by Trial 003 and R1
- Remote/push: none in the standalone worker repository

The retained authored Trial 003 state is parent `completed`, revision 15,
event sequence 16. Its graph and state pass the Factory V3 advisory checks.
R1 does not rewrite that completed state or its append-only events; it records
the later recovery separately.

## Commitment-And-Reveal Outcome

The pause leg committed only the answer-key commitment and ordinary handoff
artifacts in the sanitized worker repository. The fresh non-forked resume task
then committed a complete re-entry brief before the sponsor revealed the exact
external payload path. Before parsing, the fresh worker reproduced both:

- byte length: 4,985 bytes;
- SHA-256:
  `e577b9819f67aade38766403d5af1a3d1654024effe7d4bb1a0a5734e5202507`.

The frozen comparison passed all 17 continuation-critical and all 6
completeness fields. Git chronology shows checkpoint, brief, then comparison;
the reveal path first appears in the comparison commit. These observations
support accidental-discovery resistance under the sanitized workspace and
human-controlled reveal used here. They do not prove access control or private
context absence.

## Original And Replay Observations

The original fresh resume task reported four passing tests, valid fixture exit
0, invalid fixture exit 2, and exact matches against both pinned outputs. The
parent verification therefore closed the bounded mission.

During later Factory closeout, direct contract-to-code inspection found that
`error_sort_key` removed underscores from `path` before sorting. The existing
contract requires exact `(path, code, message)` ordering. A discriminating
capture with both `capture_id` and `captured_at` errors reproduced the mismatch:
the normalized implementation placed `captured_at` first, while exact string
ordering places `capture_id` first. The original four tests and pinned invalid
expected output encoded the wrong order and therefore did not catch it.

Under R1, the implementation now sorts on the exact tuple. One regression test
distinguishes exact ordering from underscore-normalized ordering. The invalid
expected file retains the same three error objects and changes only the order
of its first two objects. Replay produced:

- 5 unit tests passing;
- Python compilation passing;
- valid fixture exit 0 with exact pinned-output match;
- invalid fixture exit 2 with exact pinned-output match;
- graph advisory pass and state advisory pass;
- unchanged SHA-256 values for the contract, both input fixtures, and the
  original Trial 003 state and events;
- clean worker worktree after the two R1 commits.

## Builder And Verifier Provenance

The pause leg and Factory closeout/recovery work occurred in the originating
Codex desktop task. The re-entry brief, reveal comparison, product
implementation, and original closeout occurred in a separate, new, non-forked
Codex desktop task. The harness did not expose model identifiers.

The R1 implementer and R1 verifier were the same closeout task. The closeout
task was distinct from the fresh resume task but used the same harness family.
Accordingly, R1 has deterministic replay evidence but not independent
different-actor recovery verification. Git proves artifact chronology and
content; it cannot prove absence of private model context.

## Verification False-Negative Classification

The original four-test suite produced a real implementation-verification false
negative: all tests passed while the code contradicted the exact-path sorting
contract. The pinned invalid expected output shared the defect, so fixture
comparison could not expose it.

This is not a demonstrated false negative in Factory's mission-record,
mission-control, graph, or state advisory validators. Those tools do not claim
to validate the synthetic reveal domain contract. No advisory-validator false
positive was observed in this trial or recovery. The lesson is that a pinned
fixture is only as strong as its independently checked contract oracle.

## Authoring Friction

- External custody and human reveal required explicit path discipline and a
  two-task handoff.
- The complete 23-field brief was verbose but eliminated Trial 001's shape
  omissions.
- The sanitized standalone repository avoided Trial 002's co-location failure
  but required separate retention and provenance bookkeeping.
- The original parent closeout was overconfident because passing fixtures were
  treated as sufficient without a discriminating contract-order test.
- R1 required a separate human scope expansion to update the pinned expected
  output honestly after the code correction exposed its ordering defect.

## Proof Scope And Limits

Supported within this bounded local trial:

- a fresh non-forked task reconstructed the committed waypoint completely;
- external commitment verification preceded answer-key parsing;
- serial graph/state artifacts admitted continuation and closeout;
- the exact-path product defect is repaired in the retained standalone output;
- no dependency, push, or canonical product integration occurred.

Not supported:

- filesystem isolation, malicious-worker resistance, or cryptographic secrecy;
- exact file-read chronology or absence of private/session context;
- cross-machine, cross-harness, or different-model behavior;
- an attended multi-feature product epic;
- worker dispatch, concurrency, unattended operation, scheduling, runtime
  authority, required-gate readiness, profile promotion, or production use.

Deterministic fixtures do not prove live fresh-worker behavior or attended
serial-epic behavior. The live result is supplied by this one bounded task
handoff; the fixtures only make its local transformations replayable.

## Decision And Next Gate

Record Trial 003 as a bounded fresh-worker re-entry protocol pass with a
separately repaired product artifact. Do not erase the original false-negative
finding and do not treat the recovery as if it occurred before parent closeout.

The next gate is non-executing formation and challenge of one attended
serial-epic pilot candidate using the existing graph/state artifacts. Any pilot
execution requires a separate exact human Go. Read-only Codex SDK/MCP discovery
remains later, after manual attended serial-epic evidence.
