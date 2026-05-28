---
tags: [agent/lead, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/literature-batch, status/draft]
author: maumayma
project: b25
brief_date: 2026-05-28
audience: Researcher
---

# Brief — Bulk-ingest Kuznetsov's B(2,5)-related papers from math-net.ru

Sender: Lead (relaying Maria's brief verbatim, with gating notes).
Recipient: Researcher.

## Source

Author publication page: https://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=36514

Alexander Alexeevich Kuznetsov — ~28 papers (2005-2025) specializing in B(2,5) and exponent-5 group computation.

## Already in vault (skip — do not re-ingest)

In `Research/Group theory/Burnside groups/B25/`:

- `kuznetsov-shlepkin-2009.md`
- `kuznetsov-shlepkin-2010.md`
- `kuznetsov-tarasov-shlepkin-2009.md`

Plus the existing synthesis: `_synthesis-kuznetsov-b25-algorithmic-line.md` (3-paper synthesis from the earlier /research smoke test — likely merges or gets superseded by R3's broader synthesis).

## Filter criteria (WIDE — when in doubt, include)

**Include** if the paper engages with any of:

1. B(2,5) explicitly (highest priority)
2. Burnside groups of exponent 5 (any rank)
3. Two-generated periodic groups (the broader class B(2,5) sits in)
4. Cayley graphs of Burnside-class groups
5. Computational/algorithmic work on Burnside groups (any exponent) **IF** the methodology directly informs B(2,5) work. Substance test: check the paper's actual methodology, not just the title.

**Exclude:**

- Papers purely about other Burnside exponents (B(2,3), B(4,3), etc.) where methodology is exponent-specific and doesn't generalize.
- Pure algebra papers with no algorithmic / computational angle.

**Borderline → default include**, let topic-tagging do the discrimination at retrieval time.

## R1 — Inventory pass (no writes, report-only)

1. Fetch the publication page via `defuddle`.
2. Extract full paper list with titles + years + math-net.ru links.
3. Apply filter criteria. Classify each:
   - `INCLUDE` — meets the wide filter, not yet in vault
   - `INCLUDE-borderline` — borderline filter call, default include
   - `SKIP-out-of-scope` — clearly outside filter
   - `SKIP-already-in-vault` — duplicate of an existing summary (grep first to confirm)
4. Write inventory report to `obsidian/Agents/maumayma/Researcher/scratch/2026-05-28-kuznetsov-mathnet-inventory.md`.

Format:
```markdown
| Year | Title (English) | Link | Decision | Reason |
|------|-----------------|------|----------|--------|
```

**Gate**: report to Lead via `maestri ask`. Lead reviews + surfaces borderline calls to Maria. Lead green-lights R2 after Maria's call.

## R2 — Batch ingest (gated on R1 approval)

Run /research batch workflow on the approved INCLUDE list. Per `[[single-paper]]`:

1. Each paper gets full structured summary (Abstract → TL;DR → Problem → Approach → Key result → Assumptions → Limitations → Replication evidence → Why this paper matters → Quotes → Open questions → Related material).
2. **Step 13 structural-placement check applies** — every paper lands in `Research/Group theory/Burnside groups/B25/` (or whichever Burnside subdir is most specific). **Don't put any at `Research/Group theory/` root** (that was the smoke-test bug; the fix is in `[[research-folder-convention]]` and step 13 of `[[single-paper]]`).
3. **Translation discipline**: Russian-source abstracts/quotes translated to English with `[trans.]`. `language: ru` in frontmatter. Per `[[paper-summary]]` translation note.
4. **Citation count lookup**: Semantic Scholar / Google Scholar / arXiv stats best-effort. If math-net.ru is the only source and no external index covers, leave `citation_count: null` with `quality_notes: source-text-incomplete-only-abstract-available` (if applicable). Don't fabricate.
5. **6-axis tags mandatory.** Substance-test every `#topic/*`.
6. **Connection graph**: bidirectional `cites:` / `cited_by:` to existing B25 papers. Especially: most papers will cite the 3 Kuznetsov papers already in vault — populate the back-links **on both ends** (per Phase 8 F8.4 discipline).
7. **Step 17 outgoing-wikilinks check** (≥3 per note) before save.

**Mid-batch gate**: after **first 3 papers**, report progress to Lead. Lead K3 reviews — checks structural placement, tag substance, translation quality on the first batch. Either green-lights continuation or flags fixes for the rest.

**No commits during the batch.** Single end-of-batch commit (or piece-by-piece if token budget demands; default end-of-batch).

## R3 — Post-batch sweep

1. **Concept-hub creation**: if any concept appears in 2+ newly-ingested papers, create `Concepts/<concept-name>.md` stub via `[[concept-note]]` template. Existing hub `Concepts/cayley-table-closure-algorithm.md` already covers a likely candidate — extend its `appears_in:` rather than duplicate.
2. **Synthesis note**: if the batch coheres (likely — same author, same research line over 20 years), write `Research/Group theory/Burnside groups/B25/_synthesis-kuznetsov-b25-publications.md` using `[[synthesis]]` template. Cross-reference with existing `_synthesis-kuznetsov-b25-algorithmic-line.md` — **likely merge or supersede** (your call based on whether the new synthesis subsumes the old).
3. **MOC update**: add all new papers to `Research/Group theory/_MOCs/_moc-burnside.md`. Maintain alphabetical or chronological order — pick one and stay consistent across the MOC.
4. **Re-run `_meta/scripts/find-graph-orphans.py`** — confirm orphan count stays at 0. Every new note must have ≥3 wikilinks per Phase 9 discipline.

**End gate**: report to Lead. Lead K3 reviews the synthesis + concept hubs + MOC update + orphan count.

## Constraints

- **No fabrication.** If a paper has only abstract available (math-net.ru paywall, ISI/MathSciNet/eLib blocked), summarize from abstract + visible content. Add `quality_notes: source-text-incomplete-only-abstract-available`. Don't claim methodology or results that aren't in the visible text.
- **No project tag bloat.** Papers get `#project/b25` only if directly about B(2,5). Exponent-5 generalizations and Cayley-graph methodology papers stay project-untagged (topic-tagged only — `#topic/burnside`, `#topic/exponent-5`, `#topic/cayley-graphs`, etc.).
- **PDF extraction tool**: your `extract_pdf.py` (at `obsidian/Agents/maumayma/Researcher/scratch/`) may be needed if math-net.ru serves PDFs via redirect. Use as needed.

## Token discipline

Effort estimate: R1 ~10 min, R2 ~5-10 min per paper × maybe 10-15 papers = 60-120 min, R3 ~20 min. Total ~90-150 min. Heavy on tokens.

If you hit a token wall mid-batch: **checkpoint with Lead**, save partial state to log, resume in next session. Don't push through a half-broken batch.

## Out of scope

- Other authors on math-net.ru (Shlepkin, Tarasov, Khukhro, etc.). Separate brief if Maria wants those.
- Non-Burnside Kuznetsov work (other topics — skip via filter).
- Re-ingesting the 3 existing Kuznetsov papers (skip).

## Deliverable

- **R1**: inventory at `obsidian/Agents/maumayma/Researcher/scratch/2026-05-28-kuznetsov-mathnet-inventory.md`.
- **R2 + R3**: paper notes + concept hubs + synthesis + MOC update + log entries in `Researcher/log.md`.
- **Final report to Lead**: counts (papers ingested / skipped with reason / new concept hubs) + any out-of-scope issues.

## Gates summary

| Stage | Gate |
|---|---|
| R1 inventory complete | Lead K3 → Maria (borderline calls) → Lead green-lights R2 |
| R2 first 3 papers complete | Lead K3 (structural placement + tag substance + translation quality) |
| R2 + R3 complete | Lead K3 → consolidated report to Maria → commit ritual |
