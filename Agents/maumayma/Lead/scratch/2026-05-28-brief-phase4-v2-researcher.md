---
tags: [agent/lead, user/maumayma, domain/group-theory, topic/taxonomy, topic/paper-reprocess, status/draft]
author: maumayma
project: mixer-core
audience: Researcher
brief_date: 2026-05-28
supersedes: 2026-05-28-brief-phase6-researcher.md (the four "Phase 4 Additions" section only — F6.1/F6.2/F6.3 still stand)
---

# Brief — Phase 4 v2 (supersedes the earlier reprocess brief)

Sender: Lead (relaying Maria's brief verbatim, with redirect notes for the in-flight work).
Recipient: Researcher.
**Supersedes**: any in-flight "Phase 4 reprocess" work based on the earlier brief, AND the "Phase 4 — Additions to in-flight reprocess" section at the bottom of [[2026-05-28-brief-phase6-researcher]]. Those four additions are NOT to be applied as a standalone patch — they get folded into F4.3 below after F4.2 decisions land.

**Phase 6 sequencing is unchanged**: F6.1 / F6.2 / F6.3 still queue behind Phase 4. F6 dirs (`Word Problem/`, `Tools/`, etc.) do not conflict with Phase 4 paper migration, but to keep Researcher attention focused, finish Phase 4 first.

---

## Why this brief exists

The `Papers.base` dashboard (just rebuilt by Lead in Phase 5) surfaced a pile of historical tag debt across the existing paper notes. Maria's inventory of observed issues (in 11 papers visible to the base):

- **Zero `#topic/*` tags on any paper.** Connection-graph axis is unused. Every paper currently has only administrative tags. The "By topic" view is useless until topics are populated.
- **Score tags** (`#score/1`, `#score/2`, `#score/3`) on some papers. Undocumented in [[tags]]. Either a stale relevance-scoring convention or someone's ad-hoc judgement.
- **`#project/none`** on 2 papers (Word Problem + Braid). Stale 7-axis escape hatch — project is now optional, "none" is not a valid value.
- **`#project/burnside-other`** on `havas-newman-1980`. Tag is unregistered in current [[tags]] (dropped during Phase 1).
- **`#domain/grobner`** on the grobner paper. Unregistered domain — current registered domains are `group-theory`, `ai`, `cs`, `methodology`.
- **Multiple `#project/*` tags** on grobner (`project/grobner` + `project/b25`). Doctrine is unclear on whether multi-project is allowed.
- **Inline `#concept/*` tags** on grobner (4 of them). Concepts are supposed to live in `Concepts/<name>.md` hubs, linked via `key_concepts:` frontmatter — not inline tags on papers.
- **Two content-type tags** on grobner (`#concept` AND `#paper`). One paper note should have one primary content-type.
- **No `language:` frontmatter** on any paper. Phase 1 introduced this field; F4.3 must populate it.
- **6 of ~17 papers missing the `#paper` content-type tag** (which is why only 11 surface in `Papers.base`'s `file.hasTag("paper")` filter).
- **No `key_concepts`, `extends`, `contradicts`, `replicates`, `cites`, `cited_by`, `citation_count`** frontmatter on any paper.

---

## F4.1 — Researcher: inventory pass first (NO CHANGES YET)

Walk `Research/` and produce ONE report at `Agents/maumayma/Researcher/scratch/2026-05-28-inventory.md` listing:

- **Every `.md` file in `Research/`.** Walk the full subtree.
- **Per file**: current frontmatter + current tags + filesystem path + one-sentence content summary.
- **Per file classification** (pick one):
  - `paper` — proper paper summary (gets full migration in F4.3)
  - `stub / scope-note` — placeholder like `Research/Group theory/General/Include.md` (delete or leave alone, NOT a paper)
  - `synthesis` — multi-paper view (migrates to new synthesis template)
  - `concept-note-misplaced` — content that should live in `Concepts/` (move + relink)
  - `unclassifiable` — flag to Lead
- **Per file**: assessment of whether existing frontmatter has enough info to migrate (skip re-fetch) OR whether Researcher needs to re-fetch the source URL via defuddle.
- **Recommendations to Lead for F4.2** — your judgement call on each of the 6 open taxonomy questions in F4.2 below. Brief — one sentence per question is fine; Lead will weigh them.

**Hard constraint: no file changes in this phase.** This is a read-only walk + report.

Report back to Lead via `maestri ask` with: counts per classification + the inventory note's path. Lead opens F4.2.

---

## F4.2 — Lead's responsibility (NOT Researcher)

Based on F4.1's inventory + Researcher's recommendations, Lead decides and writes into `_meta/tags.md`:

1. **Score tags** (`#score/1-3`): drop entirely / formalize as `relevance: <int>` frontmatter / migrate to `quality_notes` text?
2. **`#project/burnside-other`**: re-register (and add `#project/b43`, `#project/b53` for symmetry) OR drop in favor of `#topic/burnside-43 #topic/burnside-53`?
3. **`#domain/grobner`**: re-register Gröbner as a domain OR migrate that paper to `#domain/cs` / `#domain/methodology` with `#topic/grobner-basis`?
4. **Multi-project tagging**: explicitly allow or forbid in `_meta/tags.md`. Default suggestion (per Maria): allow when a paper genuinely contributes to multiple projects, with a doctrine note.
5. **Inline `#concept/*` tags**: forbid on papers. Concepts MUST live in `Concepts/<name>.md` hubs and link via `key_concepts:` frontmatter. Lead makes this explicit in `_meta/tags.md`.
6. **Multiple content-type tags**: one primary per note. A paper that introduces a major concept gets `#paper` + a `Concepts/<name>.md` hub stub created separately.

Lead writes the decisions into `_meta/tags.md` BEFORE F4.3 begins. F4.3 cannot start until the taxonomy questions are resolved.

Lead pings Researcher with `TYPE: VERDICT` + the decisions + the `_meta/tags.md` commit. That unblocks F4.3.

---

## F4.3 — Researcher: migrate every paper note (the actual reprocessing)

**Gated on F4.2.** Do not start until Lead returns the F4.2 decision verdict.

For each note classified as `paper` in F4.1:

1. **Re-read the note + fetch source URL via defuddle** (or skip re-fetch where the inventory's "has enough info" judgement says safe).
2. **Re-write under the new [[paper-summary]] template:**
   - Body order: Abstract → TL;DR → Problem → Approach → Key result → Assumptions → Limitations → Replication evidence → Why this paper matters → Quotes → Open questions surfaced → Related material in vault
   - Abstract: verbatim copy (or translate if non-English, append `[trans.]`)
   - Numbers / theorems verbatim with section citations
   - Quotes max 2, short, verbatim, with section refs
3. **Migrate frontmatter to new schema** (per [[paper-summary]] template):
   - Add `language: <iso>` (look at source URL / paper to determine; default `en`)
   - Add `methodology_type: <theoretical|empirical|review|methodology|tutorial>`
   - Add `citation_count: <int>` + `citation_count_date: YYYY-MM-DD` (best-effort from Semantic Scholar / Google Scholar / arXiv stats). **Don't fabricate.** If you can't find one, omit the field (don't write 0 or "unknown").
   - Add `key_concepts: []` with wikilinks to `Concepts/<name>.md` hubs (create hubs for concepts appearing in 2+ papers in F4.4; don't create singleton hubs)
   - Add `extends: []`, `contradicts: []`, `replicates: []`, `cites: []`, `cited_by: []` (populate from cross-paper grep)
   - Add `quality_notes` ONLY if there's something specific to say (citation profile, replication status, reception). Otherwise omit.
   - **Remove `project: none` entirely** if present (absent ≠ "none" in the new doctrine)
4. **Re-tag using the 6-axis taxonomy** (per [[tags]]):
   - Mandatory: `#agent/research`, `#user/<owner>`, `#domain/<one>`, `#topic/<many — substance test>`, `#paper`, `#status/<lifecycle>`
   - Topic tags: **substance test** (paper genuinely engages with the topic, not just mentions). Typically 4–10, no upper bound. Lowercase-hyphenated-specific. Reuse existing topics before inventing new ones.
   - Project tag: only if note is scoped to a named project. Per Lead's F4.2 decision on multi-project, allow accordingly.
   - **Remove score tags** per F4.2 decision (drop / migrate / keep as text).
   - **Remove inline `#concept/*` tags** from papers. Move concept content to `Concepts/<name>.md` hubs in F4.4.
   - **Remove `#project/none`** everywhere.
5. **Translate non-English text.** Both the abstract (in the Abstract section) and any quotes used in body get `[trans.]` markers. Original-language text is NOT preserved in the vault (per current doctrine in [[tags]] § Vault language).
6. **Substance test for topics: read the paper before tagging.** Don't auto-tag from directory path. A paper sitting in `Research/Group theory/Burnside groups/B25/` still needs Researcher to confirm it engages with `#topic/burnside` and `#topic/b25` before tagging.
7. **Bidirectional link update**: every `cites: [[X]]` gets a matching `cited_by: [[this-paper]]` added to X's frontmatter. Same for `extends` / `replicates` / `contradicts`.
8. **Log every migration** to `Agents/maumayma/Researcher/log.md` with before-tags → after-tags.

---

## F4.4 — Researcher: concept hub population

**After F4.3 completes.**

- List every concept appearing in 2+ papers' `key_concepts:` frontmatter.
- For each, ensure `Concepts/<concept-name>.md` exists using [[concept-note]] template.
- Populate each hub's `appears_in: []` with wikilinks to all papers that reference it.
- If a concept is currently embedded inline in a paper (like the grobner paper's inline `#concept/grobner-quotient-filter` etc.), extract the concept's content into the new hub and link from the paper.

---

## Constraints (do NOT violate)

- **Don't strip authorship.** `author:` and `#user/*` preserved across migration.
- **Don't fabricate citation counts.** If you can't find one, omit the field.
- **Don't fabricate concept content.** If a concept hub doesn't have enough info to write a definition, leave it as a stub with `#status/draft` and flag to Lead.
- **Substance-test topic tags by reading paper content**, not by inferring from directory path.
- **Hold F4.3 until Lead returns F4.2 decisions.** Don't start migration with unresolved taxonomy questions.

---

## Deliverable per phase

- **F4.1**: inventory note at `Agents/maumayma/Researcher/scratch/2026-05-28-inventory.md`. Report to Lead with classifications + count per category + your recommendations on each of the 6 F4.2 questions.
- **F4.2 (Lead)**: updates to `_meta/tags.md` with the new doctrine decisions. Lead writes back to Researcher unblocking F4.3.
- **F4.3 (Researcher)**: per-paper migration log in `Agents/maumayma/Researcher/log.md`. Final report listing every paper migrated with before/after tag diffs.
- **F4.4 (Researcher)**: list of concept hubs created/populated + count of bidirectional links repaired.

---

## Redirect notes for the work you already started

You acked Phase 6 with sequencing "Phase 4 additions first ~30 min". **Stop** that work — the "Phase 4 additions" were a patch-style approach to the OLD Phase 4 brief. The NEW brief above (F4.1–F4.4) is a much more rigorous reprocess that supersedes both the old brief AND the four-item addendum at the bottom of [[2026-05-28-brief-phase6-researcher]].

New sequence:

1. **F4.1** — inventory pass, no file changes (start now, ~30 min).
2. Wait for Lead's F4.2 verdict (taxonomy decisions in `_meta/tags.md`).
3. **F4.3** — paper migration (gated on F4.2).
4. **F4.4** — concept hub population (after F4.3).
5. **F6.1** — restructure `Research/Group theory/` dirs (~10 min).
6. **F6.2** — populate new dirs (bulk, ~60–90 min, checkpoint after Tools/ GAP examples).
7. **F6.3** — wire updateable synthesis (~15 min).

Ack on receipt with: confirmation you've abandoned the in-flight "Phase 4 additions" work + when F4.1 inventory will land.
