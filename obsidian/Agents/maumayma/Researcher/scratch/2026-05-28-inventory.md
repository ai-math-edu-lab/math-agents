---
name: 2026-05-28-inventory
description: F4.1 read-only inventory of all Research/ notes — classifications, tag issues, re-fetch assessment, F4.2 taxonomy recommendations
metadata:
  type: project
tags: [agent/research, user/maumayma, domain/group-theory, topic/taxonomy, topic/paper-reprocess, status/draft]
author: maumayma
date: 2026-05-28
phase: F4.1
---

# F4.1 Inventory — Research/ subtree (2026-05-28)

**Produced by:** Researcher (read-only pass, NO FILE CHANGES)
**Scope:** All 17 `.md` files in `Research/` as of 2026-05-28.
**Purpose:** Classify each file, document tag issues, assess re-fetch need, and provide taxonomy recommendations for Lead's F4.2 decisions.

---

## 1. Classification Summary

| Category | Count |
|---|---|
| `paper` | 15 |
| `stub/scope-note` | 1 |
| `synthesis` | 1 |
| `concept-note-misplaced` | 0 |
| `unclassifiable` | 0 |
| **Total** | **17** |

**Papers missing `#paper` tag** (currently invisible to `Papers.base`): 3
- `burau4-faithfulness.md` (Open problems/Braid groups)
- `andrews-curtis-conjecture.md` (Open problems/Free groups)
- `kaplansky-zero-divisors.md` (Open problems/Group rings)

**Papers with `#paper` tag** (currently visible to `Papers.base`): 11 ← this matches the observed count from the brief.
Plus `algo-mixing-burnside-slides.md` which has `#concept` not `#paper` (also invisible).

---

## 2. Full File Inventory

### 2.1 Research/Algorithm Cooperation/

---

#### `algo-mixing-burnside-slides.md`
- **Path:** `Research/Algorithm Cooperation/algo-mixing-burnside-slides.md`
- **Classification:** `paper` (document summary of an internal slide deck; has title/authors/year/venue structure)
- **Content summary:** Summary of the project's founding slide deck presenting the Mixer methodology — from TimSort analogy to B(4,3) breakthrough to B(2,5) as target.
- **Current frontmatter:**
  - `domain: methodology`, `project: mixer-core`, `status: validated`
  - `tags: [agent/research, user/maumayma, domain/methodology, project/mixer-core, status/validated, concept]`
- **Tag issues:**
  - `#concept` used as content-type (WRONG — concept is for Concepts/ hub notes; this is a document summary)
  - `#paper` absent (should be present; makes it invisible in Papers.base)
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
- **Known issues in note:** "Witness words claim (~50 words for B(2,5)) not sourced to a specific paper — flag for Validator."
- **Re-fetch needed?** NO — source is `docs/slides/algo-mixing-burnside.md` (local); note content is rich.

---

#### `grobner.md`
- **Path:** `Research/Algorithm Cooperation/grobner.md`
- **Classification:** `paper`
- **Content summary:** Summary of Kreuzer-Myasnikov-Rosenberger (2025 draft) proposing Gröbner bases for word problems in finitely presented groups via SL(2,K) quotient tests.
- **Current frontmatter:**
  - `domain: grobner`, `project: grobner`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/grobner, project/grobner, project/b25, status/draft, paper, risk/high]`
- **Tag issues (MOST SEVERE in corpus):**
  - `domain/grobner` — **unregistered domain** (not in `_meta/tags.md`)
  - `project/grobner` — **unregistered project** (not in `_meta/tags.md`)
  - `project/grobner` + `project/b25` — **multi-project tagging** (doctrine not yet decided)
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - **Inline `#concept/*` tags** in body (lines 57–59 in the file):
    - `#concept/grobner-quotient-filter`
    - `#concept/grobner-infinitude-probe`
    - `#concept/representation-variety`
  - Note: `#paper` IS present ✅, `#risk/high` is appropriate
- **Known issues in note:** Section 7.5 (B(2,5)) and Example 7.9 are "TODO: Continue!" — paper is unfinished draft.
- **Re-fetch needed?** MAYBE — source PDF is `docs/papers/grobner.pdf` (local), but note was written from partial draft (Section 7.5 unfinished). If the PDF has been updated since, re-fetch would capture changes. Low priority since it's a preprint.

---

### 2.2 Research/Group theory/Burnside groups/B25/

---

#### `havas-newman-1980.md`
- **Path:** `Research/Group theory/Burnside groups/B25/havas-newman-1980.md`
- **Classification:** `paper`
- **Content summary:** Havas & Newman (1980) survey of computer-assisted Burnside group results: B(2,5)=5^34 confirmed, B(4,3) order, coset enumeration, p-quotient algorithm.
- **Current frontmatter:**
  - `domain: group-theory`, `project: burnside-other`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/burnside-other, status/draft, paper]`
- **Tag issues:**
  - `project/burnside-other` — **unregistered project** (not in `_meta/tags.md`)
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — content is rich and complete; source PDF at `docs/papers/1980hn.pdf`.

---

#### `havas-robertson.md`
- **Path:** `Research/Group theory/Burnside groups/B25/havas-robertson.md`
- **Classification:** `paper`
- **Content summary:** Havas & Robertson (1994) survey of computational tools for finitely presented groups: coset enumeration, Reidemeister-Schreier, KB, Tietze transformations; three worked examples.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/draft, paper]`
- **Tag issues:**
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Note:** Note itself says this paper is NOT specific to B(2,5) — `project: b25` may be wrong. See F4.2 taxonomy question 4 (multi-project). The paper's relevance is via KB discussion; `project/b25` may be over-scoped.
- **Re-fetch needed?** NO — content is rich; source PDF at `docs/papers/Havas-Robertson.pdf`.

---

#### `havas-wall-wamsley-1974.md`
- **Path:** `Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974.md`
- **Classification:** `paper`
- **Content summary:** The foundational B(2,5) paper: |B(2,5)|=5^34, class 12, full consistent commutator power presentation, generator numbering 1–34 that defines comm_12_9 and comm_13_10.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/draft, paper]`
- **Tag issues:**
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — content is exceptionally rich with verbatim formulas and generator table.

---

#### `kourovka-11.48-kostrikin-1990.md`
- **Path:** `Research/Group theory/Burnside groups/B25/kourovka-11.48-kostrikin-1990.md`
- **Classification:** `paper`
- **Content summary:** Dedicated note on Kourovka Problem 11.48 (Kostrikin, 1990): is [x,y,y,y,y,y,y] a product of fifth powers? Unpacks the equivalence to B(2,5) infiniteness.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: conjectured`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/conjectured, paper]`
- **Tag issues:**
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
  - `status: conjectured` — this is a math-claim status per [[tags]] (Validator's verdict layer), but here it describes an open mathematical problem, not a Validator verdict. Minor misuse but not harmful.
- **Re-fetch needed?** NO — source is `docs/papers/Kourovka 2022.pdf` (local); content is complete and precise.

---

#### `kourovka-2022.md`
- **Path:** `Research/Group theory/Burnside groups/B25/kourovka-2022.md`
- **Classification:** `paper`
- **Content summary:** Summary of the Kourovka Notebook No. 20 (2022), covering only Burnside-relevant entries (Problem 11.48, 11.36, 11.37, 12.32, 19.33) and Gröbner-relevant entries (Problems 7.25 and 11.10b via [[grobner]]).
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/draft, paper]`
- **Tag issues:**
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — source PDF is `docs/papers/Kourovka 2022.pdf` (local); note covers the relevant sections well.

---

#### `problems-people.md`
- **Path:** `Research/Group theory/Burnside groups/B25/problems-people.md`
- **Classification:** `paper` (internal document summary — follows paper-summary structure)
- **Content summary:** Internal project document listing algorithms and implementers for the algo_mixing B(2,5) effort, plus Mixer design constraints (API boundary, memory, serialization). Source: Problems-people.docx.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/draft, paper]`
- **Tag issues:**
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
  - `domain: group-theory` — the document is equally about `methodology` (Mixer architecture). Could argue for `#domain/methodology`. See substance test in F4.3.
- **Re-fetch needed?** NO — source is `docs/papers/Problems-people.docx` (local, internal).

---

### 2.3 Research/Group theory/General/

---

#### `Include.md`
- **Path:** `Research/Group theory/General/Include.md`
- **Classification:** `stub/scope-note`
- **Content summary:** One-line scope placeholder ("Include general postulants, rules, logic of Group Theory, Word Problem, target words calculation, GAP package docs..."). No frontmatter.
- **Current frontmatter:** NONE
- **Current tags:** NONE
- **Action:** Delete in F6.1 (per F6 brief; its scope is replaced by new `General/`, `Word Problem/`, `Tools/` subdirectory structure).
- **Re-fetch needed?** N/A

---

### 2.4 Research/Group theory/Open problems/

---

#### `_overview.md`
- **Path:** `Research/Group theory/Open problems/_overview.md`
- **Classification:** `synthesis`
- **Content summary:** "Open Problems in Group Theory — Mixer/AI Feasibility Catalog" — scores 7 open problems (B(2,5) finiteness, exponent-5 groups, Burau₄, B₄ membership, Kaplansky, AC conjecture, 2-relator word problem) on Mixer feasibility 1–3 with a scoring rubric and scoring justifications.
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: draft`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/draft, concept]`
- **Tag issues:**
  - `project/none` — stale, should be absent
  - `#concept` used as content-type (this is a synthesis note, not a concept hub)
  - Zero `#topic/*` tags
  - `score/1–3` scoring rubric embedded inline (defines the scoring system used by the individual problem notes)
- **Note:** This note is the parent document for the 6 problem notes beneath it. The scoring rubric defined here is the source of the `#score/1`, `#score/2`, `#score/3` tags on those notes. See taxonomy question 1.
- **Re-fetch needed?** N/A (internally generated synthesis).

---

#### `braid-b4-membership-6.24-makanin.md`
- **Path:** `Research/Group theory/Open problems/Braid groups/braid-b4-membership-6.24-makanin.md`
- **Classification:** `paper`
- **Content summary:** Dedicated note on Kourovka Problem 6.24 (Makanin, 1980): is the membership problem for B₄ decidable? History: decidable for n≤3, undecidable for n≥5, open for n=4.
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: conjectured`, `score: 2`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/conjectured, paper, score/2]`
- **Tag issues:**
  - `project/none` — stale, should be absent
  - `score/2` inline tag — undocumented (see taxonomy question 1)
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — source is `docs/papers/Kourovka 2022.pdf` (local); content is complete.

---

#### `burau4-faithfulness.md`
- **Path:** `Research/Group theory/Open problems/Braid groups/burau4-faithfulness.md`
- **Classification:** `paper`
- **Content summary:** Open problem note on Burau₄ faithfulness (Burau 1936, open since): is the Burau representation of B₄ injective? History: faithful for n≤3, unfaithful for n≥5, open for n=4.
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: conjectured`, `score: 2`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/conjectured, score/2]`
- **Tag issues:**
  - **MISSING `#paper`** ❌ (invisible to Papers.base)
  - `project/none` — stale, should be absent
  - `score/2` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `source_path: ""` — no source document; content written from general knowledge
- **Re-fetch needed?** YES (partial) — no source document. For F4.3, Researcher should defuddle a canonical source (Bigelow 1999 for n≥5 unfaithful; Long-Paton 1993 for n≥6; Birman's "Braids, Links, and Mapping Class Groups" for status) to add proper citation. Note as `#status/draft`.

---

#### `b-exponent-5-adian-4.2b.md`
- **Path:** `Research/Group theory/Open problems/Burnside groups/b-exponent-5-adian-4.2b.md`
- **Classification:** `paper`
- **Content summary:** Kourovka Problem 4.2b (Adian, 1973): do infinite finitely generated groups of exponent 5 exist? Equivalent to B(m,5) being infinite. History: Novikov-Adian covers n≥665; exponent 5 open.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: conjectured`, `score: 2`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/conjectured, paper, score/2]`
- **Tag issues:**
  - `score/2` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — source is `docs/papers/Kourovka 2022.pdf` (local); content complete.

---

#### `b25-finiteness-11.48-kostrikin.md`
- **Path:** `Research/Group theory/Open problems/Burnside groups/b25-finiteness-11.48-kostrikin.md`
- **Classification:** `paper`
- **Content summary:** Kourovka Problem 11.48 (Kostrikin, 1990) from a Mixer-attack angle: why KB mixing is score/3 for this problem, how KB termination → finiteness proof, existing experimental infrastructure.
- **Current frontmatter:**
  - `domain: group-theory`, `project: b25`, `status: conjectured`, `score: 3`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/b25, status/conjectured, paper, score/3]`
- **Tag issues:**
  - `score/3` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Note:** The problem content substantially overlaps with `kourovka-11.48-kostrikin-1990.md` in Burnside groups/B25/. The two notes serve different angles (mathematical unpacking vs. Mixer-attack rationale), but there may be consolidation potential. Flag for F4.3.
- **Re-fetch needed?** NO — content written from Kourovka 2022 (local) + project knowledge.

---

#### `2-relator-word-problem-9.29-merzlyakov.md`
- **Path:** `Research/Group theory/Open problems/Free groups/2-relator-word-problem-9.29-merzlyakov.md`
- **Classification:** `paper`
- **Content summary:** Kourovka Problem 9.29 (Merzlyakov, 1984): do 2-relator groups with undecidable word problem exist? Context: 1-relator groups decidable (Magnus 1932); general FPGs undecidable (Novikov-Boone 1955-57); 2-relator case open.
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: conjectured`, `score: 1`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/conjectured, paper, score/1]`
- **Tag issues:**
  - `project/none` — stale, should be absent
  - `score/1` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `#paper` present ✅
- **Re-fetch needed?** NO — source is `docs/papers/Kourovka 2022.pdf` (local); content complete.

---

#### `andrews-curtis-conjecture.md`
- **Path:** `Research/Group theory/Open problems/Free groups/andrews-curtis-conjecture.md`
- **Classification:** `paper`
- **Content summary:** Andrews-Curtis Conjecture (Andrews-Curtis 1965): every balanced presentation of the trivial group is AC-reducible. AC moves defined. History and computational search for counterexamples (Akbulut-Kirby, Bridson). Score/2 for Mixer.
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: conjectured`, `score: 2`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/conjectured, score/2]`
- **Tag issues:**
  - **MISSING `#paper`** ❌ (invisible to Papers.base)
  - `project/none` — stale, should be absent
  - `score/2` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `source_path: ""` — no source document in `docs/papers/`
- **Re-fetch needed?** YES — no source document. For F4.3, defuddle canonical source: Andrews-Curtis 1965 (Proc. Amer. Math. Soc. 16, 192–195) or a review paper. Note as `#status/draft`.

---

#### `kaplansky-zero-divisors.md`
- **Path:** `Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors.md`
- **Classification:** `paper`
- **Content summary:** Kaplansky Zero-Divisors Conjecture (~1956): group ring F[G] has no zero-divisors for torsion-free G. History: proved for orderable, hyperbolic, one-relator cases; general case open. Score/1 for Mixer (structural theorem gap too wide).
- **Current frontmatter:**
  - `domain: group-theory`, `project: none`, `status: conjectured`, `score: 1`
  - `tags: [agent/research, user/maumayma, domain/group-theory, project/none, status/conjectured, score/1]`
- **Tag issues:**
  - **MISSING `#paper`** ❌ (invisible to Papers.base)
  - `project/none` — stale, should be absent
  - `score/1` inline tag — undocumented
  - Zero `#topic/*` tags
  - No `language:` frontmatter field
  - `source_path: ""` — no source document in `docs/papers/`
- **Re-fetch needed?** YES (partial) — no source document. For F4.3, defuddle Linnell survey "Zero divisors and group von Neumann algebras" or Kaplansky's original. Note as `#status/draft`.

---

## 3. Taxonomy Issue Summary

| Issue | Count of affected files |
|---|---|
| Zero `#topic/*` tags | 16 of 17 (all except stub `Include.md`) |
| Missing `#paper` tag | 3 (`burau4-faithfulness`, `andrews-curtis`, `kaplansky-zero-divisors`) |
| `project/none` present | 5 (`_overview.md`, `braid-b4-membership`, `burau4-faithfulness`, `2-relator-word-problem`, `andrews-curtis`, `kaplansky-zero-divisors`) — **6 files actually** |
| `#score/1–3` inline tags | 6 of 17 (all 6 Open problems problem notes + `_overview.md` scoring rubric) |
| Missing `language:` field | 16 of 17 (all except stub `Include.md`) |
| Unregistered `domain/grobner` | 1 (`grobner.md`) |
| Unregistered `project/burnside-other` | 1 (`havas-newman-1980.md`) |
| Unregistered `project/grobner` | 1 (`grobner.md`) |
| Multi-project tagging | 1 (`grobner.md`: `project/grobner` + `project/b25`) |
| Inline `#concept/*` in body | 1 (`grobner.md`, 3 instances) |
| `#concept` tag on paper (wrong type) | 1 (`algo-mixing-burnside-slides.md`) |
| Missing key_concepts / extends / contradicts / replicates / cites / cited_by | all 17 |

**Papers.base "By topic" view — confirmed noise:** The view uses `groupBy: property: file.tags`. Since zero papers have `#topic/*` tags, Bases groups by ALL tag values — creating one row per administrative tag (`agent/research`, `user/maumayma`, `domain/group-theory`, etc.). The view is currently non-functional as a topic browser. Note: even after F4.3 populates `#topic/*` tags, the groupBy will still include administrative tags. A proper topic view would need either a dedicated `topics:` frontmatter property (separate from the full `tags:` array) or a filter on tag values starting with "topic/". Flagging to Lead for a Papers.base developer fix after F4.3.

---

## 4. Re-fetch Assessment

| File | Re-fetch? | Reason |
|---|---|---|
| `algo-mixing-burnside-slides.md` | NO | Source is local `docs/slides/` |
| `grobner.md` | MAYBE | Source PDF is local but paper was draft with TODO sections; check for updates |
| `havas-newman-1980.md` | NO | Source PDF local; content complete |
| `havas-robertson.md` | NO | Source PDF local; content complete |
| `havas-wall-wamsley-1974.md` | NO | Source PDF local; content complete with verbatim formulas |
| `kourovka-11.48-kostrikin-1990.md` | NO | Source PDF local; content precise |
| `kourovka-2022.md` | NO | Source PDF local; covers relevant sections |
| `problems-people.md` | NO | Source is local internal .docx |
| `Include.md` | N/A | Stub — to be deleted |
| `_overview.md` | N/A | Synthesis — internally generated |
| `braid-b4-membership-6.24-makanin.md` | NO | Source PDF local (Kourovka 2022) |
| `burau4-faithfulness.md` | YES (partial) | No source document; needs canonical citation (Bigelow 1999, Long-Paton 1993) |
| `b-exponent-5-adian-4.2b.md` | NO | Source PDF local |
| `b25-finiteness-11.48-kostrikin.md` | NO | Content written from Kourovka + project knowledge |
| `2-relator-word-problem-9.29-merzlyakov.md` | NO | Source PDF local |
| `andrews-curtis-conjecture.md` | YES | No source document; needs canonical citation (Andrews-Curtis 1965) |
| `kaplansky-zero-divisors.md` | YES (partial) | No source document; needs Linnell survey or Kaplansky original |

---

## 5. Taxonomy Recommendations for F4.2 (one sentence each)

**Q1 — Score tags (#score/1–3):** Migrate to `relevance: <int>` frontmatter property (1–3 scale preserved, queryable by Bases, not polluting the tag pane) and add score justification to `quality_notes` text; drop the inline `#score/*` hashtags entirely.

**Q2 — #project/burnside-other:** Drop in favor of topic tags (`#topic/burnside-43`, `#topic/burnside-53` as needed) — the project axis is for named workstream-scoped notes, not for grouping papers by which group they study; `havas-newman-1980` covers multiple Burnside groups and is better served by broad `#topic/burnside` tagging.

**Q3 — #domain/grobner:** Migrate `grobner.md` to `#domain/cs` (Gröbner basis algorithms are a CS/computer algebra technique) with `#topic/grobner-basis` for fine-grain retrieval; re-registering `grobner` as a first-class domain would give it equal standing with `group-theory` which overstates its scope in this vault.

**Q4 — Multi-project tagging:** Allow (cap at 2 projects) when a paper genuinely contributes to multiple named project workstreams, with a doctrine note in `_meta/tags.md`; `grobner.md` is a legitimate case (Gröbner approach workstream + B(2,5) evidence), but `project/grobner` needs to be registered first.

**Q5 — Inline #concept/* tags on papers:** Forbid on paper notes; concept content belongs in `Concepts/<name>.md` hubs linked via `key_concepts:` frontmatter — the 3 inline tags in `grobner.md` should be extracted to stubs in `Concepts/` in F4.4.

**Q6 — Multiple content-type tags:** One primary per note; `algo-mixing-burnside-slides.md` should get `#paper` only (it is a document summary), with concept content extracted to a `Concepts/` hub in F4.4 if needed.

---

## 6. Potential F4.3 Consolidation Flag

`kourovka-11.48-kostrikin-1990.md` (in `Burnside groups/B25/`) and `b25-finiteness-11.48-kostrikin.md` (in `Open problems/Burnside groups/`) both cover Kourovka Problem 11.48 — the former from a mathematical angle, the latter from a Mixer-attack angle. They are distinct enough to keep separate, but `key_concepts:` and `cites:` links should cross-reference them. Flag to Lead if consolidation is preferred.

---

## 7. Log Entry

This inventory produced as part of Phase 4 v2, F4.1. No file changes made. Results reported to Lead via `maestri ask`.
