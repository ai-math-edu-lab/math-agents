---
tags: [agent/research, log]
---

# Researcher — Activity Log (Math)

Append-only. Latest at top.

---

## 2026-05-28 — R2 batch ingest: Kuznetsov mathnet.ru bulk (17 papers)

**Source:** https://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=36514

**Summary:** R1 inventory → R2 ingest of 14 clear-INCLUDE + 3 promoted borderlines = 17 papers total. 3 already-in-vault (skip). 6 out-of-scope (skip). 2 borderlines dropped (#4 Boolean 2-groups, #16 conference duplicate).

**New notes (17):**

*B25/ subdir (14 papers):*
- `kuznetsov-2019.md` — growth functions, Cayley graph diameters, quotient groups B_k
- `kuznetsov-2020.md` — confluent irreducible rewriting systems for finite groups; applied to exponent-5
- `kuznetsov-kuznetsova-2025.md` — supercomputer computation of center of B₀(2,5)
- `kuznetsov-kuznetsova-2021.md` — minimum word length for noncyclic abelian subgroups in B₀(2,5) (length 16)
- `kuznetsov-safonov-2018.md` — Cayley graph geometry of inversion-automorphism centralizer (|C|=5^16)
- `kuznetsov-kuznetsova-2018.md` — resource-efficient growth function algorithm; diameters ~105 (2-gen) and ~69 (4-gen) for B₀(2,5)
- `kuznetsov-kuznetsova-2017.md` — Cayley graph diameter of permutation-automorphism centralizer (|C|=5^17, D=33)
- `kuznetsov-2016.md` — growth function algorithm for B_k, k=15,16,17
- `kuznetsov-karchevsky-2016.md` — conference companion to above
- `kuznetsov-kuznetsova-2013.md` — fast Hall polynomial multiplication for exponent-5 groups (foundational)
- `kuznetsova-kuznetsov-safonov-2013.md` — parallel variant of growth function algorithm
- `kuznetsov-2011.md` — subgroup ⟨xy,yx⟩ of B₀(2,5): |G|=5^14, class 6, derived length 3
- `kuznetsov-filippov-2010-sjim.md` — centralizer of inversion automorphism: generators, order (5^16), solvability, nilpotency
- `kuznetsov-filippov-2010-vmj.md` — companion publication to above (shorter, Vladikavkaz journal)

*Burnside groups/ (3 borderline papers, not B25-specific):*
- `kuznetsov-safonov-2014.md` — Hall's polynomials for exponent-7 two-generator groups
- `kuznetsov-safonov-2015.md` — Hall's polynomials for exponent-3 Burnside groups (conference note)
- `kuznetsov-2015-cayley-exp3.md` — Hall's polynomials + Cayley graph diameters for exponent-3 groups

**Structural changes:**
- 6 new topic tags registered in `_meta/tags.md` § Axis 4: restricted-burnside, growth-functions, cayley-graphs, finite-group-enumeration, rewriting-systems, center-of-group
- `_moc-burnside.md` extended with 4 new sections covering all 17 papers
- Bidirectional cited_by sweep: havas-wall-wamsley-1974, kuznetsov-shlepkin-2009, kuznetsov-shlepkin-2010, kuznetsov-tarasov-shlepkin-2009, kuznetsov-kuznetsova-2013, kuznetsov-filippov-2010-sjim all updated
- Orphan count: 0 new orphans (pre-existing isolated note: _meta/skills/research/INSTALL.md, not related to batch)

**Quality notes:** all 17 papers are abstract-only (mathnet.ru paywall / Russian journal limited access). 14 Russian-source papers have [trans.] on abstracts. Citation counts null throughout (Semantic Scholar rate-limited; papers not in English-language indexes). All notes carry quality_notes: source-text-incomplete-only-abstract-available.

**R3 (completed same session):**
- Synthesis: `Research/Group theory/Burnside groups/B25/_synthesis-kuznetsov-b25-publications.md` — 20 papers, supersedes + complements _synthesis-kuznetsov-b25-algorithmic-line.md
- Concept hub: `Concepts/growth-functions-burnside.md` — appears_in 8 papers
- Concept hub: `Concepts/cayley-graphs-of-burnside-groups.md` — appears_in 6 papers; distinct from cayley-table-closure-algorithm (graph vs. table)
- Old synthesis: added "partially superseded" notice with forward link to new synthesis (retained as algorithm deep-dive)
- Orphan script: added INSTALL.md exclusion pattern (housekeeping, naming-conventions Rule 2)
- Final orphan count: 0 (169 notes scanned)

---

## 2026-05-28 — /research batch: Kuznetsov B(2,5) Cayley-table line (3 papers + concept hub + synthesis)

**Source:** 3 local PDFs in `~/Downloads/` — filenames misleadingly transliterated as `ketnesov_*`; actual author is Kuznetsov A.A. (Кузнецов) of the Krasnoyarsk school.

**PDF extraction tooling:** none of `pdftotext`, `mutool`, `nuextract-cli`, `defuddle` (CLI) were installed; the built-in Read tool returns only file size for PDFs. Wrote a throwaway `uv run` script `Agents/maumayma/Researcher/scratch/extract_pdf.py` (pypdf, ~10 lines) per Researcher discipline "Throwaway scripts only" rule.

**New notes (5):**

- `Research/Group theory/Burnside groups/B25/kuznetsov-shlepkin-2009.md` — paper 2 (foundational of the B(2,5) pair); Trudy IMM 15(2), 125–132. Introduces Algorithm I (row-collision Cayley-table closure) on free Burnside groups; computes $K_{27}(2,5)$ on a PC; |P_27(2,5)| = 92,228,348 exact. tags: burnside, b25, restricted-burnside, word-problem, cayley-table-closure, finite-group-enumeration, computer-algebra; project: b25.
- `Research/Group theory/kuznetsov-tarasov-shlepkin-2009.md` — paper 1 (the general algorithm); Vestnik NSU 9(2), 47–54. Generalization of Algorithm I to arbitrary finitely-presented periodic groups. Placed at Group theory/ domain level (not B(2,5)-specific). tags: cayley-table-closure, word-problem, finitely-presented-groups, periodic-groups, coset-enumeration, finite-group-enumeration; no #project/* (substance test: borderline).
- `Research/Group theory/Burnside groups/B25/kuznetsov-shlepkin-2010.md` — paper 3 (B(2,5)/B_0(2,5) divergence extension); Trudy IMM 16(2), 133–138. Associativity-test variant of Algorithm I + finite/infinite dichotomy theorems + cluster-scale K_35(2,5) (~104h on 125 nodes) + Theorem 3 (coincidence up to length 29) + Theorem 4 (973 candidate-divergence relations at lengths 30–35; failure of any one would prove B(2,5) infinite). tags as paper 2 + project: b25.
- `Concepts/cayley-table-closure-algorithm.md` — concept hub (introduces "Kuznetsov's Algorithm I"); appears_in: all 3 Kuznetsov papers; introduced_in: kuznetsov-shlepkin-2009.
- `Research/Group theory/Burnside groups/B25/_synthesis-kuznetsov-b25-algorithmic-line.md` — synthesis; project: b25. Recommends 4 concrete Mixer / Experimenter-B25 actions (|P_s(2,5)| baseline verification, direct test of the 2 length-30 candidate relations, pre-register a Kuznetsov-Algorithm-I Mixer Agent, attempt to obtain the full 973-relation list).

**Taxonomy registration:**

- Added `#topic/cayley-table-closure` to `_meta/tags.md` Axis 4 list. Substance test passes (3 papers in this batch + concept hub).

**Bidirectional updates (3 papers):**

- `havas-wall-wamsley-1974.md`: added 3 new `cited_by:` entries (kuznetsov-shlepkin-2009/2010, _synthesis-kuznetsov-b25-algorithmic-line) + matching Related material bullet.
- `kourovka-11.48-kostrikin-1990.md`: same 3 added.
- `b25-finiteness-11.48-kostrikin.md`: same 3 added (was previously empty `cited_by: []`); Related material section updated.

**MOC update:**

- `_moc-burnside.md`: added new "Cayley-table-closure attack (Kuznetsov line, Russian, 2009–2010)" section after the existing "Mixer attack" section. 4 new wikilinks (all 3 papers + synthesis).

**Project framing on output:** added explicit "Mixer / B(2,5) project framing" sections to papers 2 and 3 + the synthesis, per user instruction (Q3 confirmed papers are Mixer/B(2,5) relevant). Paper 1 (general algorithm) stays descriptive; no project framing.

**Translation discipline:** all 3 papers are Russian-language. Abstracts translated to English with `[trans.]` markers. Quotes translated and tagged. `language: ru` recorded in frontmatter. Original Russian not preserved in vault per doctrine.

**Verification checks per paper note:** all 5 new notes include Related material sections with ≥3 substantive wikilinks (parent overview + MOC + siblings/concepts/papers) per Phase 9 cross-linking discipline. Notation: all `[[...,...]]` patterns (e.g. commutator brackets in `[[kuznetsov-shlepkin-2010]]`) use backticks per F8.2 paper-summary-template rule — verified by inspection.

**Filename discipline:** filenames are `kuznetsov-shlepkin-2009.md`, `kuznetsov-tarasov-shlepkin-2009.md`, `kuznetsov-shlepkin-2010.md` (correct transliteration; user's local `ketnesov_*.pdf` filenames not propagated to vault). Per user confirmation on Q1.

**Open items / suggested next actions (for Experimenter-B25 / Lead):**

1. Verify `|P_s(2,5)|` baseline counts $s = 1, \ldots, 27$ from kuznetsov-shlepkin-2009 §3 Table 2 against current B(2,5) enumeration pipelines.
2. Direct test of the 2 length-30 candidate-divergence relations from kuznetsov-shlepkin-2010 Theorem 4 through KBMAG + Rust bidirectional — highest-leverage single experiment.
3. Pre-register a Kuznetsov-Algorithm-I Mixer Agent for B(2,5) attack (element-enumeration witness stream complementing KB rule-derivation).
4. Attempt to obtain the full 973-relation list (paper reproduces only excerpts).

**Open citation-count gap:** none of the 3 papers' citation counts could be located via standard channels at write time — typical for 2009–2010 Russian-language Trudy/Vestnik papers; recorded as `citation_count: null` in all 3 frontmatters with note in `quality_notes:`. Not flagged as blocker.

**No restructuring of existing notes.** Only additions + bidirectional sweep.

---

## 2026-05-28 — Phase 11: Pre-commit audit drift fixes (6 items)

**#2** experiment.md: added `user/<handle>`, `topic/<one+>`, `project/<subproject>` to tags example
**#3** code-review.md: added `user/<handle>`, `topic/<one+>` to tags example; reordered content-type tag to end
**#4** decision.md: added `user/<handle>`, `topic/<one+>` to tags example
**#5a** component-doc.md L4: domain enum updated from `group-theory | combinatorics | numerical | algorithms | methodology | infra | api` → `group-theory | ai | cs | methodology`
**#5b** component-doc.md L20: added `user/<handle>`, `topic/<one+>` to tags example; changed `domain/<…>` → `domain/<one>`
**#10** single-paper.md: resolved duplicate step 13 — renumbered: Write note=13, Apply tags=14, Update hubs=15, Verify wikilinks=16, Report back=17
**#11** INSTALL.md L8: fixed `Documents/Obsidian/Math/\`` → `\`~/Documents/Obsidian/Math/\`` (missing opening backtick + leading tilde)

---

## 2026-05-28 — Phase 9 F9.1 — orphan wiring + orphan-detection script

**Before:** 9 orphans (both-way zero in/out) — 3 Research/ targets + 6 B25 experiment files (F9.2).

**F9.1 scope — 18 notes wired (Research/Group theory/):**

*Critical orphans fixed (3 → 0):*
- group-theory-overview.md: added 7 outgoing links (all 4 MOCs, synthesis, tool overview, WP overview)
- general-group-theory-overview.md: added 4 outgoing links (parent, MOC, synthesis, WP overview)
- package-kbmag.md: added 6 outgoing links (gap-overview, tools overview, kbmag overview, MOC, technique, example)

*In-orphan fixed (1 → 0):*
- _synthesis-existing-papers.md: added 3 outgoing links; now has 2 incoming (group-theory-overview + _moc-burnside)

*Zero-outgoing technique notes fixed (2):*
- dehn-function.md: added 5 outgoing links
- automatic-groups.md: added 6 outgoing links

*Zero-outgoing GAP example notes fixed (5):*
- 01-group-order.md, 02-coset-enumeration.md, 03-word-equality.md, 04-exponent-subgroups.md, 05-kbmag-package.md: 5-6 outgoing each

*Zero-outgoing KBMAG example and format notes fixed (3):*
- 01-s3-shortlex.md, 02-b23-shortlex.md, file-formats.md: 5-6 outgoing each

*Overview notes with zero outgoing fixed (4):*
- gap-overview.md: added 9 outgoing links (examples + MOCs + tool overview)
- kbmag-tools-overview.md: added 7 outgoing links
- group-theory-tools-overview.md: added 6 outgoing links
- word-problem-overview.md: added 7 outgoing links

*MOC bidirectional updates (2):*
- _moc-knuth-bendix: added [[package-kbmag]] to Practical tools section
- _moc-burnside: added Synthesis section with [[_synthesis-existing-papers]]

**Concept hubs created:** 0 (no concept appeared in 2+ orphan notes without an existing hub)

**F9.2 (B25 experiment files) — wired by Experimenter-B25 in parallel.** Each data/results file now has 1 incoming (sibling) and 6-7 outgoing.

**Script:** _meta/scripts/find-graph-orphans.py (written this phase) — confirmed 0 orphans post-F9.1+F9.2.

**After:** 0 orphans. Target was ≤2.

---

## 2026-05-28 — Phase 8 (F8.1–F8.5)

**F8.1 — Deleted 4 _placeholder.md files:**
- General/basics/_placeholder.md
- General/orders-and-finiteness/_placeholder.md
- General/presentations-and-relations/_placeholder.md
- Word Problem/techniques/_placeholder.md
All parent dirs have real content from F6.2 (6, 2, 5, 3 notes respectively).

**F8.2 — GAP A: Commutator orphan fix (all $[[ patterns → backticks):**
- havas-wall-wamsley-1974.md L96-97: `$[[2,1,2,1,1,2], [2,1,2,1,1]]$` and `$[[2,1,2,2,1,1], [2,1,2,2,1]]$` → backtick-wrapped (these had `]]` terminators → confirmed phantom wikilinks)
- kourovka-11.48-kostrikin-1990.md L55: `$[[[[[[x,y],y],y],y],y],y]$` → backtick (no `]]` terminator, but doctrine consistency)
- _synthesis-existing-papers.md and _moc-burnside.md: same pattern fixed
- Note: algo-mixing-burnside-slides.md L136-137 `$$[[a,b],c]...$$` left as-is — display math with no `]]` terminator, safe.
- paper-summary.md doctrine updated: backticks PROMOTED to primary (LaTeX demoted as NOT SAFE for `[[...]]`-containing expressions). Added empirical rationale and 'Why LaTeX doesn't work' explanation.

**F8.4 — GAP B: Bidirectional cited_by sweep:**
Root cause: F4.4 populated forward `cites:` but didn't systematically sweep target papers for `cited_by:` updates. 6 papers had missing back-links.
Fixed:
- havas-wall-wamsley-1974: added ← algo-mixing-burnside-slides
- grobner: added ← problems-people, kaplansky-zero-divisors
- problems-people: added ← kaplansky-zero-divisors, andrews-curtis-conjecture, grobner
- algo-mixing-burnside-slides: added ← b25-finiteness-11.48-kostrikin
- braid-b4-membership-6.24-makanin: added ← burau4-faithfulness
- havas-robertson: added ← grobner
Post-fix verification: Python citation graph re-run confirms 0 missing back-links.

**F8.4a — Promoted verification script:**
Python citation graph checker promoted from scratch to `_meta/scripts/verify-bidirectional-links.py`. Re-run at any time: `python3 _meta/scripts/verify-bidirectional-links.py`. Confirmed clean from new location.

**F8.5 — Domain frontmatter audit re-verify:**
All 18 `domain:` fields in Research/ verified: 15 papers (13 group-theory, 1 methodology, 1 cs) + 3 non-paper notes. No anomalies.
The algo-mixing-burnside-slides `$$[[a,b],c]$$` display math confirmed safe (no `]]` terminator → no phantom wikilink formed, confirmed by grep).

---

## 2026-05-28 — Phase 7 (F7.1–F7.4) + MOC pass

**F7.1 — Naming convention doctrine:**
- Created `_meta/naming-conventions.md` (vault-wide naming rules: unique filenames, lowercase kebab-case, `_` prefix reserved for MOC/synthesis, avoid generic words)
- Appended naming section to `_meta/research-folder-convention.md` linking to new doc

**F7.2 — Renames (14 files total):**
*Research/ _overview.md renames (7):*
- `Research/Group theory/_overview.md` → `group-theory-overview.md`
- `Research/Group theory/General/_overview.md` → `general-group-theory-overview.md`
- `Research/Group theory/Open problems/_overview.md` → `open-problems-catalog.md`
- `Research/Group theory/Tools/_overview.md` → `group-theory-tools-overview.md`
- `Research/Group theory/Tools/GAP/_overview.md` → `gap-overview.md`
- `Research/Group theory/Tools/KBMAG/_overview.md` → `kbmag-tools-overview.md`
- `Research/Group theory/Word Problem/_overview.md` → `word-problem-overview.md`

*Experiments/ results.md renames (3):*
- KBMag/results/results.md → kbmag-results.md
- Reduce Core/results/results.md → reduce-core-results.md
- Rust Bidirectional/results/results.md → rust-bidirectional-results.md

*Experiments/ data.md renames (3):*
- KBMag/data/data.md → kbmag-data.md
- Reduce Core/data/data.md → reduce-core-data.md
- Rust Bidirectional/data/data.md → rust-bidirectional-data.md

*MOC renames (4):* burnside-moc → _moc-burnside; knuth-bendix-moc → _moc-knuth-bendix; word-problem-moc → _moc-word-problem; presentations-and-orders-moc → _moc-presentations-and-orders

*Architecture/ `_overview.md` files: NOT renamed* (Developer territory; wikilinked from Architecture/ component notes)

*Wikilinks/path refs fixed (7):* problems-people.md, kaplansky-zero-divisors.md (open-problems-catalog), _moc-word-problem (tools overview), _moc-presentations-and-orders (GAP overview), _moc-knuth-bendix (KBMAG overview), automatic-groups.md (path ref), group-theory-overview.md (self-ref)
  - *Follow-up fix (10 stale intra-MOC wikilinks):* MOC 'Related MOCs' sections still used pre-rename names (burnside-moc, knuth-bendix-moc, word-problem-moc, presentations-and-orders-moc). Fixed with sed across all 4 MOC files. Root cause: rename-then-grep loop didn't catch renamed files referencing each other. Doctrine note added to _meta/naming-conventions.md.

**F7.3 — Domain frontmatter audit:**
- All Research/ paper notes were missing `domain:` frontmatter field (only had `#domain/*` tag)
- Added `domain: group-theory` to 13 notes, `domain: methodology` to 1 (algo-mixing-burnside-slides), `domain: cs` to 1 (grobner)
- Papers.base "Domain" column will now show correct values instead of "None"

**F7.4 — /research skill workflow updates:**
- `_meta/skills/research/workflows/single-paper.md`: added step 12 on unique filenames (before writing the note; grep to verify uniqueness; reference naming-conventions.md)
- `_meta/skills/research/SKILL.md`: added to "What this skill does NOT do" — does not create generic-filename notes; every paper gets a uniquely-identifying name

**MOC pass (complete):** 4 MOCs created and renamed to `_moc-<topic>.md` convention in `Research/Group theory/_MOCs/`:
- _moc-burnside.md: 7 curated wikilinks with annotations
- _moc-knuth-bendix.md: 10 curated wikilinks with annotations
- _moc-word-problem.md: 10 curated wikilinks with annotations
- _moc-presentations-and-orders.md: 11 curated wikilinks with annotations
Total: 38 curated wikilinks across 4 MOCs

---

## 2026-05-28 — F6.3 Updateable synthesis wired

**Action:** Wrote full synthesis at `Research/Group theory/General/_synthesis-existing-papers.md`.
**Coverage:** 15 papers. Sections: settled results, open/contested questions, cross-cutting themes, empirical open questions for Experimenter, refresh notes.
**Refresh trigger documented:** "Re-run on every new paper landing in Research/Group theory/**, or when Lead routes /research --reconnect group-theory."
**Status:** #status/validated (initial synthesis complete; will be kept current on refresh passes).

---

## 2026-05-28 — F6.2 Research/Group theory/ content population

**Action:** Wrote all substantive content for the new F6.1 directory structure. GAP and KBMAG examples were actually run and output captured verbatim.

**Notes created:**
- General/basics/ (6 notes): group.md, subgroup.md, homomorphism.md, normal-subgroup.md, quotient-group.md, group-action.md. Reference: Dummit & Foote 3rd ed. throughout.
- General/presentations-and-relations/ (5 notes): free-groups.md, presentations.md, tietze-transformations.md, coset-enumeration.md, cayley-graphs.md. References: Lyndon-Schupp + D&F.
- General/orders-and-finiteness/ (2 notes): order-exponent.md, classification-fsg.md.
- Word Problem/ (2 notes): decidability-landscape.md (full content, verbatim theorem citations), target-words.md (general methodology, no project framing).
- Word Problem/techniques/ (3 notes): knuth-bendix.md, dehn-function.md (brief), automatic-groups.md (brief).
- Tools/GAP/examples/ (5 notes): 01-group-order.md, 02-coset-enumeration.md, 03-word-equality.md, 04-exponent-subgroups.md, 05-kbmag-package.md. All verified on GAP 4.15.1 at /opt/homebrew/bin/gap.
- Tools/KBMAG/examples/ (2 notes): 01-s3-shortlex.md (S3, 8 rules), 02-b23-shortlex.md (B(2,3) fuller presentation, 26 rules). Both verified on kbmag_v1/standalone/bin/kbprog.
- Tools/GAP/package-kbmag.md: verified with S3 example (Confluent: true, Size: 6, Rules: 7).
- Tools/KBMAG/file-formats.md: .kbprog format documentation with examples.

**GAP/KBMAG verification notes:**
- All 5 GAP examples: verified on GAP 4.15.1 (2026-05-28) ✅
- S3 kbprog example: verified, 8 rules ✅
- B(2,3) kbprog example: verified, 26 rules with presentation (a³, b³, (ab)³, (ab⁻¹)³) ✅
- B(2,3) with minimal 3-relator presentation: diverges (incomplete — kbprog ran >10 min, killed). Documented in 02-b23-shortlex.md with explanation.
- No examples unverified for other reasons.

---

## 2026-05-28 — F6.2.5 Commutator notation phantom wikilinks fix

**Action:** Fixed phantom Obsidian wikilink nodes caused by bare `[[...]]` commutator notation in paper body prose.

**Pattern searched:** `\[\[[0-9,x-z]` and `\[\[\[\[\[\[` across all vault `.md` files.

**Matches found and fixed (3 instances in 2 files):**
- `havas-wall-wamsley-1974.md` line 95-96: `[[2,1,2,1,1,2], [2,1,2,1,1]]` → `$[[2,1,2,1,1,2], [2,1,2,1,1]]$` (LaTeX math)
- `kourovka-11.48-kostrikin-1990.md` line 54: `[[[[[[x,y],y],y],y],y],y]` → `$[[[[[[x,y],y],y],y],y],y]$` (LaTeX math)
- `target-words.md` lines 33-34 and 42: `[[x, y], z]` patterns → LaTeX math; `[[[[[[2,1],...]]]` → backtick code

**Doctrine update:** Appended notation convention to `_templates/paper-summary.md` under "Notation conventions" section. Rule: bare `[[...]]` in body prose is forbidden; use LaTeX or backticks.

**Visual verification:** Cannot render Obsidian graph view from this session; Researcher flagging to Lead to spot-check that orphan '2,1,2,1,1,2]' nodes are gone after next Obsidian reload.

---

## 2026-05-28 — F6.1 Research/Group theory/ restructure

**Action (restructure authority):** Created new directory scaffold for Research/Group theory/. No paper or concept notes moved — only new scaffold files added and one stub deleted.

**Before → After:**

BEFORE:
```
Research/Group theory/
├── Burnside groups/B25/ (unchanged)
├── General/Include.md  ← one-line scope stub
└── Open problems/ (unchanged)
```

AFTER:
```
Research/Group theory/
├── _overview.md                              ← NEW (directory map)
├── Burnside groups/B25/ (unchanged)
├── General/
│   ├── _overview.md                          ← NEW (scope vs WP vs Tools)
│   ├── basics/_placeholder.md               ← NEW (F6.2 content)
│   ├── presentations-and-relations/_placeholder.md ← NEW
│   ├── orders-and-finiteness/_placeholder.md ← NEW
│   └── _synthesis-existing-papers.md        ← NEW (updateable synthesis stub, F6.3)
│   [General/Include.md DELETED — scope replaced by new structure]
├── Open problems/ (unchanged)
├── Word Problem/
│   ├── _overview.md                          ← NEW
│   ├── decidability-landscape.md             ← NEW (stub, F6.2)
│   ├── target-words.md                       ← NEW (stub, F6.2)
│   └── techniques/_placeholder.md           ← NEW (F6.2 creates per-technique notes)
└── Tools/
    ├── _overview.md                          ← NEW (decision tree)
    ├── GAP/
    │   ├── _overview.md                      ← NEW
    │   ├── package-kbmag.md                  ← NEW (stub, F6.2)
    │   └── examples/                         ← NEW (F6.2 creates runnable snippets)
    └── KBMAG/
        ├── _overview.md                      ← NEW
        ├── file-formats.md                   ← NEW (stub, F6.2)
        └── examples/                         ← NEW (F6.2 creates runnable snippets)
```

**Status:** F6.1 complete. Next: F6.2 (populate content — bulk work ~60-90 min, checkpoint after Tools/ GAP examples are verified runs).

---

## 2026-05-28 — F4.4 Concept hub population (Phase 4 v2)

**Action:** Populated Concepts/ hubs with appears_in: frontmatter and created 3 new concept stubs.

**Existing hubs updated (5):**
- `verification-methods-for-group-equality`: added appears_in: [havas-robertson, havas-wall-wamsley-1974, 2-relator-word-problem]; updated to 6-axis tags; removed project:none
- `kb-mixing-stagnation`: added introduced_in: + appears_in: [algo-mixing-burnside-slides]; updated to 6-axis tags
- `mixable-api`: added introduced_in: + appears_in: [algo-mixing-burnside-slides, grobner]; updated to 6-axis tags
- `burau4-faithfulness` (Concepts/): added introduced_in: + appears_in: [burau4-faithfulness, braid-b4-membership]; updated to 6-axis tags; removed project:none
- `kaplansky-zero-divisors` (Concepts/): added introduced_in: + appears_in: [kaplansky-zero-divisors]; updated to 6-axis tags; removed project:none

**New concept stubs created (3, extracted from grobner.md inline content):**
- `Concepts/grobner-quotient-filter.md` — SL(n, Q_R) quotient test as fast-fail word-problem oracle
- `Concepts/grobner-infinitude-probe.md` — minimal polynomial test for group infinitude
- `Concepts/representation-variety.md` — SL(n,K) representation variety as algebraic coordinate system on G

**Papers updated with key_concepts: (5):**
- havas-robertson → [[Concepts/verification-methods-for-group-equality]]
- havas-wall-wamsley-1974 → [[Concepts/verification-methods-for-group-equality]]
- algo-mixing-burnside-slides → [[Concepts/kb-mixing-stagnation]], [[Concepts/mixable-api]]
- Open problems/Braid groups/burau4-faithfulness → [[Concepts/burau4-faithfulness]]
- Open problems/Group rings/kaplansky-zero-divisors → [[Concepts/kaplansky-zero-divisors]]

**2+ papers rule:** verification-methods qualifies (3 papers). Other hubs are singletons in Research/ — key_concepts: added anyway since hubs exist. Grobner 3 stubs are singleton exceptions (extracted from inline).

**Status:** F4 (F4.1-F4.4) complete. Next: F6.1 (restructure Research/Group theory/ dirs).

---

## 2026-05-28 — F4.3 Paper migration (Phase 4 v2)

**Action:** Migrated all 16 research notes (15 papers + 1 synthesis) to new paper-summary template.
**No file changes skipped — full migration complete.**

**Per-note log (before tags → after tags, abbreviated):**

| Note | Before (key tags) | After (key tags) | Changes |
|---|---|---|---|
| havas-wall-wamsley-1974 | domain/group-theory, project/b25, paper | same + topic/burnside, topic/b25, topic/word-problem, topic/coset-enumeration, topic/nilpotent-quotient | +topics, +new frontmatter |
| havas-robertson | domain/group-theory, project/b25, paper | same - project/b25 + topic/word-problem, topic/coset-enumeration, topic/knuth-bendix, topic/finitely-presented-groups | -project (substance test fail), +topics |
| havas-newman-1980 | domain/group-theory, project/burnside-other, paper | same - project/burnside-other + topic/burnside, topic/b25, topic/coset-enumeration, topic/word-problem, topic/nilpotent-quotient, topic/finitely-presented-groups | -deprecated project, +topics |
| kourovka-2022 | domain/group-theory, project/b25, paper | same + topic/burnside, topic/b25, topic/word-problem, topic/braid-groups, topic/finitely-presented-groups | +topics |
| problems-people | domain/group-theory, project/b25, paper | same + topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/coset-enumeration, topic/mixer, topic/finitely-presented-groups | +topics |
| kourovka-11.48-kostrikin-1990 | domain/group-theory, project/b25, paper | same + topic/burnside, topic/b25, topic/word-problem, topic/finitely-presented-groups | +topics |
| b-exponent-5-adian-4.2b | domain/group-theory, project/b25, paper, score/2 | same - score/2 + relevance: 2 + topic/burnside, topic/b25, topic/word-problem, topic/finitely-presented-groups | -deprecated score, +relevance frontmatter, +topics |
| b25-finiteness-11.48-kostrikin | domain/group-theory, project/b25, paper, score/3 | same - score/3 + relevance: 1 + topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/kbmag, topic/mixer | -deprecated score, +relevance, +topics |
| braid-b4-membership-6.24-makanin | domain/group-theory, project/none, paper, score/2 | same - project/none - score/2 + relevance: 2 + topic/braid-groups, topic/word-problem, topic/decidability | -deprecated, +topics |
| 2-relator-word-problem-9.29-merzlyakov | domain/group-theory, project/none, paper, score/1 | same - project/none - score/1 + relevance: 3 + topic/word-problem, topic/decidability, topic/finitely-presented-groups | -deprecated, +topics |
| burau4-faithfulness | domain/group-theory, project/none, score/2 | same - project/none - score/2 + **#paper ADDED** + relevance: 2 + topic/braid-groups, topic/word-problem | -deprecated, +paper tag, +topics |
| andrews-curtis-conjecture | domain/group-theory, project/none, score/2 | same - project/none - score/2 + **#paper ADDED** + relevance: 2 + topic/word-problem, topic/finitely-presented-groups | -deprecated, +paper tag, +topics |
| kaplansky-zero-divisors | domain/group-theory, project/none, score/1 | same - project/none - score/1 + **#paper ADDED** + relevance: 3 + topic/group-rings, topic/finitely-presented-groups | -deprecated, +paper tag, +topics |
| algo-mixing-burnside-slides | domain/methodology, project/mixer-core, **concept** | same - concept + **#paper ADDED** + topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer | concept→paper, +topics |
| grobner | **domain/grobner**, **project/grobner**, project/b25, paper | **domain/cs** - domain/grobner - project/grobner + topic/word-problem, topic/grobner-basis, topic/knuth-bendix, topic/finitely-presented-groups + key_concepts frontmatter | domain migrated, project/grobner dropped, inline concept tags → frontmatter |
| _overview.md (synthesis) | domain/group-theory, project/none, concept | same - project/none - concept + **#synthesis** + topic/burnside, topic/b25, topic/word-problem, topic/braid-groups, topic/finitely-presented-groups | concept→synthesis, -project/none, +topics |

**Orphan status (all 16 notes):** ALL = connected (has both incoming and outgoing wikilinks). No isolated or in-orphan notes in Research/.

**New topics introduced (substantive, 2+ papers each):**
- topic/finitely-presented-groups (6 papers)
- topic/nilpotent-quotient (2 papers: havas-wall-wamsley + havas-newman)
- topic/braid-groups (2 papers: braid-b4-membership + burau4-faithfulness)
- topic/decidability (2 papers: braid-b4-membership + 2-relator-word-problem)
- topic/grobner-basis (1 paper, grobner.md — domain migration justified this)
- topic/group-rings (1 paper, kaplansky-zero-divisors — primary topic)

**Deprecated tags removed everywhere:** #project/none (5 files), #score/* (6 files), #project/burnside-other (1 file), #domain/grobner (1 file), #project/grobner (1 file), #concept on paper notes (2 files)

**Inline #concept/* tags removed from grobner.md body:** 3 instances (grobner-quotient-filter, grobner-infinitude-probe, representation-variety) → moved to key_concepts: frontmatter as Concepts/ wikilinks (stubs to be created in F4.4)

**Re-fetch status:** 3 papers without source documents (burau4-faithfulness, andrews-curtis-conjecture, kaplansky-zero-divisors) — marked #status/draft with quality_notes explaining citation gaps. No defuddle attempted (no URLs available).

**Bidirectional link updates:** cites:/cited_by: populated for all notes based on cross-references observed during migration.

**Status:** F4.3 complete. F4.4 (concept hub population) is next.

---

## 2026-05-28 — F4.1 Inventory pass (Phase 4 v2)

**Action:** Read-only walk of all 17 `.md` files in `Research/`. No file changes.
**Output:** `Agents/maumayma/Researcher/scratch/2026-05-28-inventory.md`
**Classifications:** 15 paper, 1 stub/scope-note (`Include.md`), 1 synthesis (`_overview.md`)
**Key findings:**
- 0/17 files have `#topic/*` tags — connection-graph axis is entirely unset
- 3 papers missing `#paper` tag (invisible to Papers.base): `burau4-faithfulness`, `andrews-curtis-conjecture`, `kaplansky-zero-divisors`
- 6 files have stale `project/none`
- 6 files have undocumented `#score/1–3` tags (+ `_overview.md` which defines the rubric)
- 1 unregistered domain (`domain/grobner`), 2 unregistered projects (`project/grobner`, `project/burnside-other`)
- `grobner.md` has 3 inline `#concept/*` tags in body (doctrine violation)
- `algo-mixing-burnside-slides.md` has `#concept` instead of `#paper`
- Papers.base "By topic" view confirmed noisy (groups by all tag values, no topic tags exist yet)
- Re-fetch needed for: `burau4-faithfulness` (no source), `andrews-curtis-conjecture` (no source), `kaplansky-zero-divisors` (no source)
**6 F4.2 taxonomy recommendations**: provided in inventory note
**Status:** Reported to Lead; awaiting F4.2 verdict before F4.3 begins.

---


---

## 2026-05-22 — Open problems catalog: Research/Group theory/Open problems/

**Authority:** Researcher restructure authority over Research/.

**Directories created (new subtree):**
- Research/Group theory/Open problems/
- Research/Group theory/Open problems/Burnside groups/
- Research/Group theory/Open problems/Braid groups/
- Research/Group theory/Open problems/Group rings/
- Research/Group theory/Open problems/Free groups/

**Notes created (7 problem notes + 1 overview):**

Burnside groups/:
- [[b25-finiteness-11.48-kostrikin]] — Kourovka 11.48, score/3 (flagship Mixer target)
- [[b-exponent-5-adian-4.2b]] — Kourovka 4.2b, score/2

Braid groups/:
- [[burau4-faithfulness]] (Open problems version) — well-known open problem, score/2
- [[braid-b4-membership-6.24-makanin]] — Kourovka 6.24, score/2

Group rings/:
- [[kaplansky-zero-divisors]] (Open problems version) — Kaplansky ~1956, score/1

Free groups/:
- [[andrews-curtis-conjecture]] — Andrews-Curtis 1965, score/2
- [[2-relator-word-problem-9.29-merzlyakov]] — Kourovka 9.29, score/1

Entry point: [[_overview]] → Research/Group theory/Open problems/_overview.md

**Score distribution:** score/3: 1, score/2: 4, score/1: 2

**Sources used:** Kourovka 2022.pdf (direct re-extraction via pdfminer.six); [[problems-people]]; [[algo-mixing-burnside-slides]]; existing Concepts/ notes [[burau4-faithfulness]], [[kaplansky-zero-divisors]].

**Flags raised in catalog:**
- Burau₄ faithfulness, Kaplansky, and Andrews-Curtis (classical) have no Kourovka problem numbers — flagged in known_issues; paper acquisition needed.
- "~50 witness words" claim (slide deck) flagged for Validator (no source citation).
- 3 problems-people domains not yet cataloged: Cayley graph (Ushakov), ATP (Lisitsa), Todd-Coxeter (Ginzburg).

**No moves of existing notes performed in this task.**

---

## 2026-05-22 — K3 paper summaries batch write

**Task:** Populate Research/ with summaries of all 6 papers in docs/papers/.

**Extraction status:**
- All 5 PDFs: text-extractable via pdfminer.six. No image-only scans; nuextract-cli not needed.
- Problems-people.docx: extracted via zipfile XML parsing.

**Notes created:**
- [[havas-robertson]] → Research/Group theory/Burnside groups/B25/havas-robertson.md
- [[havas-wall-wamsley-1974]] → Research/Group theory/Burnside groups/havas-wall-wamsley-1974.md
- [[havas-newman-1980]] → Research/Group theory/Burnside groups/havas-newman-1980.md
- [[kourovka-2022]] → Research/Group theory/General/kourovka-2022.md
- [[problems-people]] → Research/Group theory/General/problems-people.md
- [[grobner]] → Research/Mixer Applications/grobner.md

**Flags raised:**
1. Havas-Robertson.pdf is NOT the commutator target-word paper — it is a general computational FPG tools paper (1994, DIMACS). Target words comm_12_9 / comm_13_10 come from [[havas-wall-wamsley-1974]] generator numbering. Known_issues noted in havas-robertson frontmatter.
2. grobner.pdf is a DRAFT (October 2025) with two sections labeled 'TODO: Continue!' (section 7.5 on B(2,5), example 7.9). The Mixer connection is direct: Myasnikov is co-author AND listed in Problems-people.docx as building the Mixer.
3. Two new Mixer-candidate problems flagged in problems-people.md: Burau₄ faithfulness (braid groups) and Kaplansky zero-divisors conjecture — no Research/ notes exist for these yet. Suggest Lead route to Researcher for follow-up or flag as out-of-scope.
4. Kourovka 2022 problem 11.48 (Kostrikin): B(2,5) infinite iff [x,y,y,y,y,y,y] is not a product of fifth powers in the free group. Still open as of 2022.

**No restructuring performed.**

---

## 2026-05-22 — Correction A: Restructure paper notes into B25/

**Authority:** Researcher restructure authority over Research/.
**Reason:** All four moved notes are B(2,5)-specific in content; grouping under B25/ matches the domain of use and reduces navigation overhead.

**Moves:**
- Research/Group theory/Burnside groups/havas-wall-wamsley-1974.md → Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974.md
- Research/Group theory/Burnside groups/havas-newman-1980.md → Research/Group theory/Burnside groups/B25/havas-newman-1980.md
- Research/Group theory/General/kourovka-2022.md → Research/Group theory/Burnside groups/B25/kourovka-2022.md
- Research/Group theory/General/problems-people.md → Research/Group theory/Burnside groups/B25/problems-people.md

**Unchanged:**
- Research/Group theory/Burnside groups/B25/havas-robertson.md (already in B25/)
- Research/Mixer Applications/grobner.md (cross-domain; stays in Mixer Applications)

**Verified via obsidian move (backlinks auto-updated by Obsidian).**

---

## 2026-05-22 — Part 2: Verdicts + Corrections + Concepts

**Commutator naming convention sourced (1974hww re-read):**
Confirmed against experiments/b25_reduce_core/verify_reduction.py:4.
comm_12_9 = c12, c9 = 2,1,2,1,1,2], 2,1,2,1,1 using 1974hww generator numbers.
comm_13_10 = c13, c10 = \[\[2,1,2,2,1,1], 2,1,2,2,1]].
Added to havas-wall-wamsley-1974.md §Findings we should remember.

**Notes created:**
- [[kourovka-11.48-kostrikin-1990]] → Research/Group theory/Burnside groups/B25/ (CRITICAL)
- [[burau4-faithfulness]] → Concepts/
- [[kaplansky-zero-divisors]] → Concepts/

**Correction B cross-links added to:**
- havas-wall-wamsley-1974.md
- havas-robertson.md
- havas-newman-1980.md
- kourovka-2022.md
- grobner.md (added [[problems-people]] + experiment links)
- problems-people.md

**All B25 notes now link to:**
- [[Experiments/Group Theory/Burnside Group/B25/_progress]]
- [[Experiments/Group Theory/Burnside Group/B25/Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]]
- (bidirectional notes linked where appropriate)

**No restructuring beyond Correction A (already logged).**
**All notes remain status/draft pending Lead/Validator review.**

---

## 2026-05-22 — Part 2 slide deck synthesis

**Source:** docs/slides/algo-mixing-burnside.md (Stepanov & Matveeva)

**Notes created:**
- [[algo-mixing-burnside-slides]] → Research/Mixer Applications/
- [[mixable-api]] → Concepts/
- [[kb-mixing-stagnation]] → Concepts/

**Content decisions:**
- Included: B(m,n) order table (verbatim), B(4,3) relators (verbatim), overnight run log (verbatim), confluence check numbers, validation strategy, future work.
- Excluded: group axioms pedagogy, Rust engineering rationale, TimSort step-by-step slides (motivating example summarized in 1 paragraph).
- Flagged: 'witness words ~50' claim for Validator — no source cited in deck.
- Flagged: deck says n≥8000 for infinite Burnside; correct bound is n≥665 (Adyan, per havas-newman-1980).
- Noted: flamegraph.svg exists alongside deck (referenced in related_artifacts frontmatter); content not analyzed.

**Experiments mentioned in deck without notes (for Experimenter-B25 backfill):**
1. B(2,4) mixing — 159 rules mixed, ~1s, |B(2,4)|=4096 verified
2. B(3,3) mixing — 63 rules mixed, ~0.3s, |B(3,3)|=2187 verified
3. B(4,3) stagnation failure (C implementation, ~2000 rules, several days)
4. B(4,3) overnight breakthrough — r2l_rpo_loop + rpo_iter, 0.55h, 2333 rules, 54 shares
5. B(4,3) confluence verification — 1,702,360 pairs, 0 failures, 3689.00s