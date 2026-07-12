# Factory V3 Evidence-Integrity Three-Sample Review

## Version
v0.1

## Status
Research-only advisory evidence review.

Decision: `KEEP_OPTIONAL_NO_SCHEMA_CHANGE`.

This review does not promote optional fields, change validator behavior, repair
historical records, create a required gate, authorize a live fresh-worker
trial, or add runtime behavior.

## Question
Across the first three natural uses of the optional evidence-integrity fields,
which authoring friction and mission-record validator false-positive or
false-negative patterns recur strongly enough to justify a policy change?

## Samples

| Sample | Artifact | Mission shape |
| --- | --- | --- |
| S1 | `docs/Factory/runs/RUN_20260712_1309_v3_mission_reentry_proof_impl/MISSION_RECORD.json` | Deterministic mission-control re-entry decision cases |
| S2 | `docs/Factory/v3/mission_records/MR_20260712_032_serial_mission_graph_contract.json` | Serial mission-graph contract and advisory validator |
| S3 | `docs/Factory/v3/mission_records/MR_20260712_033_serial_mission_state_kernel.json` | Deterministic authored-state kernel and persistence checks |

The synthetic optional-field fixture is validator design evidence, not a fourth
natural sample.

## Method
The review compared each record's:

- original/replay/audit observations and evidence-reference durability;
- builder/verifier actor and session relationships;
- boundary-claim status, proof scope, evidence, and explicit limit;
- visual-evidence use;
- `commit_before` and `commit_after` state;
- friction notes;
- false-positive and false-negative notes;
- current advisory validator result.

Each record was also run directly through
`scripts/factory_v3_mission_record_lint.py`.

## Comparison

| Dimension | S1 | S2 | S3 | Adjudication |
| --- | --- | --- | --- | --- |
| Observation provenance | Original + post-run audit | Original + replay | Original + replay | Useful in all three; preserves later checks without superseding the original claim |
| Evidence durability | Repository closeout reference | Thread-local output only | Mixed repository fixtures and thread-local output | Prefer durable repository evidence when it already exists; honest thread-local limitations remain valid |
| Verifier provenance | Same actor/session, `not_independent` | Same actor/session, deterministic separation only | Same actor/session, deterministic separation only | Recurring limitation, not independent-verification evidence |
| Boundary claims | One proved scope claim; one contradicted live-proof claim | One proved scope claim; one missing live-proof claim | Two proved bounded claims; one missing live-proof claim | Strongest recurring value: claims stay bounded and deterministic evidence is not inflated into live proof |
| Visual evidence | Omitted for non-visual work | Empty list | Empty list | Correctly unused; no case yet tests natural visual-evidence authoring |
| Commit state | `commit_after: not_recorded` | `commit_after: not_recorded` | `commit_after: same_commit` | Two uncommitted closeouts lose final commit identity; S3 demonstrates the preferred same-commit convention once commit authority exists |
| Model identity | Not recorded | Not recorded | GPT-5 recorded | Harness-state coverage improved only in S3; too little evidence for policy change |
| Validator result | Advisory pass, zero findings | Advisory pass, zero findings | Advisory pass, zero findings | No false positive on the three valid natural records |

## Recurring Authoring Friction

### 1. Manual inventory verbosity
S1 explicitly reports verbose path/evidence inventory. S2 and S3 also repeat
commands, evidence references, boundary claims, and file lists already present
in closeout or tests. The burden is real, but the samples do not show that any
specific optional block is dispensable: provenance and bounded claims improve
audit precision in each mission.

Decision: retain optional blocks. Prefer references to durable closeout,
fixture, and test artifacts over repeating raw output or prose.

### 2. Non-independent verification
All three samples used the same actor and session. The fields correctly exposed
that limit and prevented an independence claim. This is a recurring evidence
gap, not a reason to require a second actor for every bounded mission.

Decision: keep provenance optional and honest. Do not reinterpret deterministic
separation as actor or session independence.

### 3. Uncommitted final state
S1 and S2 use `commit_after: not_recorded`, honestly reflecting closeout before
an authorized commit but weakening later commit-pinned replay. S3 uses
`commit_after: same_commit`, resolving its final hash as the commit that adds
the record.

Decision: keep `not_recorded` valid. Prefer `same_commit` when a record will be
committed with the mission changes, or a real hash for a later backfill. Do not
create follow-up commits solely to stamp hashes and do not rewrite S1 or S2.

### 4. Evidence-reference durability
S2 and part of S3 cite thread-local command output that is not durable. S1
points to a repository closeout, and S3 also points to tests and pinned fixture
output. The optional field makes the limitation visible but cannot manufacture
missing logs.

Decision: prefer durable repository evidence when already authorized and
useful. Keep honest non-durable references valid rather than expanding mission
scope merely to persist logs.

## False-Positive Review
All three natural records return `ADVISORY_PASS` with zero findings. No supplied
field was rejected despite honest same-actor verification, absent/empty visual
evidence, missing or contradicted boundary claims, and `commit_after:
not_recorded`.

Finding: no observed mission-record validator false positive across the three
samples. Three same-day, same-harness records are insufficient to estimate a
general false-positive rate.

## False-Negative Review
No demonstrated mission-record validator false negative was found. S2 and S3
use “false-negative” notes for implementation invariants found during final
review or deterministic tests. Those are valuable engineering findings, but
they are outside the mission-record validator's contract and therefore do not
show that the record validator accepted a malformed optional block.

The validator also cannot prove the truth of self-authored evidence references,
actor identities, or boundary claims. Zero findings means the supplied shape is
internally valid; it does not make the evidence independent or externally true.

Finding: future records should distinguish:

- `mission_record_validator`: an unexpected acceptance or rejection of the
  record shape;
- `implementation_or_domain_check`: a product, validator-under-development, or
  mission invariant found by tests/review;
- `not_observed`: no case in the sample.

This is authoring guidance only. No field or validator change is justified by
the three samples.

## Decision
`KEEP_OPTIONAL_NO_SCHEMA_CHANGE`

Reasons:

1. Observation provenance and bounded claims improved replay precision in all
   three missions.
2. Verifier provenance consistently prevented false independence claims.
3. The recurring burden is manual verbosity and evidence durability, not a
   malformed or unusable schema.
4. No mission-record validator false positive or demonstrated false negative
   recurred across the natural records.
5. The corpus is narrow: one date, one repository, one harness, same-actor
   verification, no natural visual-evidence case, and no live fresh worker.

## Next Gate
The evidence-integrity review gate is complete. The next separate decision is
whether to authorize the live fresh-worker artifact-sufficiency trial using the
serial graph and authored state artifacts. This review does not authorize that
trial. After a separately approved trial decision, the roadmap still requires
an attended serial-epic pilot before worker-adapter or orchestration claims.
