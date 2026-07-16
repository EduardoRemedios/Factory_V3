# Codex Deep-Link Optional Attended-Aid Adoption Challenge - 2026-07-16

## Status

Research-only, advisory, non-enforcing, and non-executing challenge over
`CODEX_DEEPLINK_ATTENDED_ADOPTION_FORMATION_20260716.md`.

This review does not adopt or run the helper, create or send a task, start a
worker, modify an operational profile, add a gate, or begin full automation.

## Challenge Result

### Verdict

`PASS` for a separate sponsor adoption decision under the challenged candidate
contract.

The evidence supports an optional attended aid only. The repaired contract
prevents adoption from becoming default use, standing task authority, a
transport-proof claim, or an implicit worker adapter.

## Critical Findings

None after repair.

The central authority risk was that “adopt the helper” could be interpreted as
permission to create a task whenever a derived next action exists. The contract
now requires an already-approved exact mission envelope that explicitly names
the aid. The helper, link, cursor, and human Send grant no authority.

## High Findings

1. **Adoption could silently become default task creation.**
   - Risk: future agents may use the helper whenever a handoff looks useful.
   - Repair adopted: use is optional, per-mission explicit, and ineligible
     without exact worker-task and workspace authority.

2. **URL construction can expose prompt content.**
   - Risk: prompts may appear in terminals, transcripts, OS/app handling, or
     screenshots.
   - Repair adopted: only short non-sensitive prompts are eligible; secrets,
     credentials, regulated data, production data, and real personal data are
     forbidden. Manual fallback remains available.

3. **One successful screenshot could be overclaimed as transport proof.**
   - Risk: visual correspondence may be treated as byte-perfect transport,
     exact full-path binding, task identity, or hidden-tool proof.
   - Repair adopted: every preparation retains
     `transport_proof: false`; the candidate lists unsupported claims and
     requires honest unknowns.

4. **The aid could replace authored re-entry state.**
   - Risk: a concise prompt or session memory may become the practical source
     of truth.
   - Repair adopted: prompts must point to authored durable artifacts; graph,
     state, expected revision, authority, and repository checks remain
     authoritative.

5. **Evidence collection could erase the friction benefit or leak data.**
   - Risk: mandatory screenshots and verbose records for every use may cost more
     than copy/paste and create another disclosure surface.
   - Repair adopted: deterministic preparation fields and human match result are
     required; screenshots are conditional and must remain non-sensitive.

6. **Mismatch handling could become an automatic retry loop.**
   - Risk: regenerating links or editing prompts may hide the first failure and
     exceed authority.
   - Repair adopted: no Send on mismatch; use manual fallback or authored safe
     hold. Retry requires separate mission authority.

7. **Human Send could be confused with adoption authority.**
   - Risk: pressing Send starts a worker task even if the underlying mission did
     not authorize it.
   - Repair adopted: Send is admitted only by the approved mission envelope.
     Adoption approval alone cannot start a worker.

## Medium/Low Findings

- The existing 8,192-byte ceiling is a local policy, not a compatibility
  promise. The candidate preserves that wording.
- Desktop project-name display may not prove the full resolved path. Human
  review must record ambiguity rather than infer identity.
- The helper still requires a click, Send, and manual result/evidence return.
  This is friction reduction, not human elimination.
- Natural use may reveal that the evidence protocol is too heavy. That is an
  observation for later review, not authority to weaken it mid-mission.
- Manual copy/paste can itself introduce error, but it remains the safest
  available fallback when URL use is unsuitable.

## Assumptions To Resolve

No assumption blocks a separate adoption decision.

Natural use should test, without manufactured scope:

- whether the optional aid reduces total attended handoff time;
- whether pre-Send workspace/prompt review is consistently practical;
- whether helper failures or URL-size concerns occur;
- whether manual fallback is understandable and sufficient;
- whether desktop-version drift changes the observed behavior.

These observations do not need a new schema or required validator.

## Authority Gaps

- Adoption is not approved by formation or challenge.
- No live helper run, link, click, Send, task, or worker is approved.
- No future mission may use the aid unless its exact envelope names it.
- No helper code/limit change, dependency, credential, CLI repair, app-server,
  SDK, MCP, task API, adapter, automatic Send, task status, push, merge, or
  profile promotion is approved.

## Verification Gaps

- Only one synthetic desktop observation exists.
- No byte-level transport trace or task API exists.
- No product-workspace or long-prompt use has been observed.
- No cross-version, account, harness, or concurrent reliability evidence
  exists.
- Sponsor observation is not independent machine telemetry.
- Static source checks cannot prove the absence of every possible external
  effect, though the helper's small stdlib surface narrows the risk.

These gaps limit claims but do not block optional attended adoption.

## Fallback Triggers

Adoption recording must halt on:

- requested helper implementation or limit change;
- default-use or standing-authorization language;
- required-gate or profile-promotion language;
- live helper/task execution;
- automation, dependency, credential, CLI repair, SDK/MCP, adapter, push, or
  merge request.

Later mission use must not Send and must fall back or safe-hold on:

- missing explicit mission authority;
- sensitive or uncertain prompt classification;
- invalid, oversized, or mutable prompt artifact;
- wrong or ambiguous resolved workspace;
- helper error or unexpected output;
- composer workspace/project or prompt mismatch;
- inability to review the complete prompt;
- unexpected task, permission, activity, or product effect;
- request to retry without separate authority.

## Recommended Repairs

All required repairs are incorporated:

1. per-mission explicit eligibility rather than default use;
2. strict non-sensitive prompt classification;
3. authored state and mission authority remain controlling;
4. required deterministic preparation fields;
5. mandatory human review and Send;
6. explicit unsupported claims and `transport_proof: false`;
7. optional, risk-based screenshots rather than universal capture;
8. manual fallback or authored safe hold on mismatch;
9. no automatic retry;
10. full automation kept in a separate later lane.

## Execution Readiness

`READY FOR SEPARATE SPONSOR ADOPTION DECISION`.

A later approval should name `V3-CODEX-DL-ADOPT-001` and adopt only the optional
per-mission attended policy in the candidate contract. It must not authorize a
live task, helper code change, default use, standing authorization, automatic
Send, task status, SDK/MCP, adapter implementation, push, or merge.

Challenge `PASS` is not adoption or execution authority.
