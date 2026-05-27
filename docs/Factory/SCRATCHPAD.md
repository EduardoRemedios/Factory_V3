# Factory Scratchpad — Cross-Run Pitfalls Index

> **Purpose:** Keep a compact, governed list of active cross-run pitfalls. This file is not a run diary.
>
> **Mandatory read rule:** Read `## Active Pitfalls (Mandatory)` before any Factory run, sprint execution, or brief drafting.
>
> **Run diary rule:** Session narratives belong in `docs/Factory/runs/<RUN_ID>/RETRO.md` and are optional reading.

---

## Active Pitfalls (Mandatory)

Keep this section to a hard cap of 12 entries.

Format:
`<ID> | <Tag> | <Pitfall (one sentence)> | <Evidence RUN_ID:path> | <Status>`

- FP-001 | scope | When execution reveals contract ambiguity, harden contracts first; do not start feature expansion on top of drift. | (add evidence after first run) | ACTIVE
- FP-002 | consistency | Promotion-sensitive evidence records need explicit non-promotion language in the same paragraph as any V3 approval or operational-status wording. | RUN_20260527_0732_v3_phase4_first_capture_candidate_plan:docs/Factory/v3/real_run_corpus/RR_20260527_001_phase4_candidate_status_update.md | ACTIVE

---

## Promotion Rules (Governance)

- Add an entry only when there is concrete run evidence and a clear repeat-risk.
- Keep each pitfall to one sentence and one primary tag.
- Set `Status` to `DEPRECATED` only when superseded by a locked test, stage contract update, or policy/spec change.
- Review this list at least once per week or before drafting the next sprint brief.
- Do not duplicate run narrative details here; keep only reusable pitfalls.

---

## Tag Vocabulary (Controlled)

Use only these tags unless explicitly extended:
- `scope`
- `reason_codes`
- `contracts`
- `paths`
- `verification`
- `consistency`
- `contract_lock`
- `prompts`
- `timestamps`
- `fingerprints`
- `evidence_chain`
- `runtime_patterns`

---

## Run Retro Index (Optional Reading)

(Add entries here as runs are completed)
