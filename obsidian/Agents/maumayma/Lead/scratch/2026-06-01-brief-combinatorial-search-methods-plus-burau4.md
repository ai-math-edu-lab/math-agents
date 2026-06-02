---
tags: [agent/lead, user/maumayma, domain/methodology, topic/combinatorial-search, topic/burau-groups, topic/literature-scan, status/draft]
author: maumayma
project: mixer-core
brief_date: 2026-06-01
audience: Researcher
---

# Brief — Combinatorial search methodology synthesis (Part A) + Burau₄ deep-fill (Part B)

Sender: Lead (relaying Maria's brief, with explicit-GO gate structure).
Recipient: Researcher.

Two-part literature program **paired** for thematic coherence: Part A is the general methodology landscape for taming large combinatorial / group-theoretic search problems; Part B is a specific deep-fill on Burau₄ faithfulness that frames the problem as combinatorial-search to connect with A's framework.

## Sequencing

**Strictly sequential.** Part A completes (through A3 synthesis + Lead K3 + Maria approval) **before** Part B starts. Rationale: Part B's framing depends on Part A's vocabulary and pattern catalog.

```
A1 (propose) → Lead K3 + Maria approval → EXPLICIT GO → A2 (ingest) → A3 (synthesis) → Lead K3 sample-review → EXPLICIT GO → B1 (source inventory) → Lead K3 + Maria approval → EXPLICIT GO → B2 (acquire + summarize) → B3 (upgrade + synthesis) → Lead K3 final → consolidated commit
```

**Explicit-GO discipline applies at every phase boundary.** Per `feedback_explicit_go_gates`: completing a phase and reporting it is NOT a green-light. WAIT for a literal GO/PROCEED token from Lead before advancing.

---

## Part A — Combinatorial search methodology

### Goal

Map the general methodology landscape for **taming huge combinatorial spaces and finding structure / patterns in them**. This is a **methodology landscape**, NOT a B(2,5) deep-dive — Maria already has B(2,5) covered. The audience is someone who needs to know what techniques exist and which ones have a Mixer-shaped (cooperating partial oracles) structural motif.

### Topic areas to cover

Maria's explicit topic spread (5 areas; aim for 1-3 sources per area, 8-12 total):

1. **Knuth-Bendix completion & rewriting systems as search**, including failure/stagnation modes. Cross-link existing `[[Concepts/kb-mixing-stagnation]]`.
2. **Coset enumeration (Todd-Coxeter)** + **automatic-groups machinery** (relevant to KBMAG usage in this vault — cross-link `[[kbmag-tools-overview]]` if it exists).
3. **Modern search heuristics over combinatorial structures**: beam search, A* / IDA*, SAT/SMT encodings of group-word problems, Gröbner-basis methods as a search paradigm. Cross-link `[[Concepts/grobner-quotient-filter]]`, `[[Concepts/grobner-infinitude-probe]]`.
4. **ML/RL for combinatorial search & conjecture-finding**: AlphaTensor / AlphaDev / FunSearch / GNN-guided proof search and similar. **What's actually shown vs. hype.** Cross-link the existing `Research/AI in Math/` subtree heavily — many of these papers already have notes there.
5. **The recurring "partial-No oracle running alongside a complete rewriter" pattern** — this is the **structural motif behind the whole Mixer thesis**. Find where it appears in the literature under other names (e.g. portfolio solvers in SAT, dual oracle in proof complexity, "lazy oracles" in CEGAR, "abstraction-refinement" in model checking, etc.).

### A1 — Candidate proposal (no fetching, ~15 min)

Per `[[literature-scan]]` workflow Phase 1:

- Propose 8-12 candidate sources spanning the 5 topic areas above.
- Format: numbered list with author + year + venue + one-line claim + **topic-area label** (which of the 5).
- Mix foundational + recent.
- Surface honest gaps: if a topic area has thin literature, say so rather than padding.
- **REPORT TO LEAD. WAIT for explicit GO from Lead** (after Maria's approval) before A2.

### A2 — Ingest (gated on explicit GO from Lead)

- Per-paper /research at the appropriate `Research/<subtree>/<paper-id>.md`. Step-13 structural placement applies — substance-test each paper for the right home (Group theory / AI in Math / Algorithm Cooperation / etc.).
- Bidirectional cited_by sweep, especially into existing AI-in-Math notes if any A2 paper overlaps (AlphaTensor, FunSearch, AlphaEvolve, etc. already live in `Research/AI in Math/`).
- Step-17 ≥3 wikilinks per note.
- Register new `#topic/*` tags in `_meta/tags.md` BEFORE applying them (per the now-standing tag-register-before-use doctrine).

### A3 — Synthesis

Write `_synthesis-combinatorial-search-methods.md` at `Research/Algorithm Cooperation/` (lean — the Mixer-cooperation thesis is the natural anchor; substance test for the right exact location).

**Maria's specific synthesis ask: flag which methods look Mixer-shaped (cooperating partial oracles), since that's the project thesis.** Make this a dedicated section in the synthesis, not just a passing mention.

Standard synthesis sections per `[[synthesis]]` template: the question, sources reviewed, convergence, disagreement, settled, contested, open, methodology notes, recommendation. Plus the Mixer-shaped methods section.

**Lead K3 after A3** → explicit GO for B1.

---

## Part B — Burau₄ faithfulness deep-fill

### Context

The two existing notes are stubs written from general knowledge with **no source papers acquired** — see their `quality_notes`:
- `[[Concepts/burau4-faithfulness]]`
- `Research/Group theory/Open problems/Braid groups/burau4-faithfulness.md`

Maria's earlier Phase 4 review marked both as `#status/draft` permanently until URLs surface. They've now surfaced via this brief.

### B1 — Source inventory (no fetching, ~10 min)

Identify and fetchability-check Maria's named sources:

1. **Bigelow 1999, JAMS** — n≥5 unfaithful. arXiv likely available.
2. **Long-Paton 1993** — n≥6. Older; may need JSTOR / library access.
3. **Burau 1936** — original. German. Likely Springer historical archive; may need scan.
4. **Garside normal form** — original Garside 1969 + standard treatment. Check Birman's textbook.
5. **Birman "Braids, Links, and Mapping Class Groups"** — survey status. Textbook, chapter likely scannable.

Plus:
6. **Post-2020 progress on n=4 case** — search arXiv / MathSciNet for any updates since 2020. Maria explicitly wants this.
7. **Kourovka Notebook number check** — does Burau₄ faithfulness have a Kourovka problem number? Vault already has `Research/Group theory/Open problems/.../kourovka-2022.md` — grep for "Burau" in that note + the broader Kourovka tree.

Report fetchability per source. **Honest "can't acquire" flags expected** — Maria's brief says "surface anything sparse/contradictory rather than padding." If a 1936 German paper isn't fetchable, say so + propose what to do (skip / find translation / cite via secondary).

**REPORT TO LEAD. WAIT for explicit GO** before B2.

### B2 — Acquire + summarize (gated on explicit GO)

- Per-paper /research at `Research/Group theory/Open problems/Braid groups/<paper-id>.md` for each fetchable source.
- For sources not fully acquirable: `quality_notes: source-text-incomplete-<describe>` per the AlphaProof / Kuznetsov-abstract-only pattern. **Do NOT fabricate methodology from titles or secondary sources.**
- Apply standard 6-axis tags + bidirectional cited_by.

### B3 — Upgrade existing notes + synthesis

- **Upgrade `[[Concepts/burau4-faithfulness]]`**: replace the "general knowledge" content with verbatim cites from the acquired sources. Populate `cites:`, `cited_by:`, `extends:` frontmatter. Update `appears_in:` to track which new B2 notes reference it.
- **Upgrade `Research/Group theory/Open problems/Braid groups/burau4-faithfulness.md`**: same — verbatim results with section citations, full body sections per `[[paper-summary]]` template, populate connection-graph frontmatter.
- **Write `_synthesis-burau4-faithfulness.md`** at `Research/Group theory/Open problems/Braid groups/` per `[[synthesis]]` template. **Maria's framing ask**: explicitly frame the Burau₄ kernel-element search and short-braid enumeration as a **combinatorial-search problem**, linking back to Part A's synthesis and the methodology pattern catalog. This is the bridge that makes the pairing valuable.

**Lead K3 final** → consolidated commit (Part A + Part B together, or separate commits — Lead's call based on diff size at end).

---

## Hard constraints (both parts)

- **No padding.** Surface sparse / contradictory literature rather than inventing breadth.
- **No `#status/validated` flips without Maria's review.** Even after Lead K3 passes, hold tags at `#status/draft` and let Maria flip them after reading the syntheses.
- **No fabrication.** Don't invent methodology from titles, secondary sources, or general knowledge. The Burau₄ upgrade specifically replaces general-knowledge stubs with verbatim cites — repeating the stub pattern would defeat the purpose.
- **Standard doctrine**: step-13 placement, ≥3 wikilinks per note, tag-register-before-use, bidirectional cited_by, arxiv-id filenames where applicable.
- **Token budget**: this is a multi-phase task. Checkpoint with Lead after each phase. Save state + ping if you hit a token wall.

## Deliverable

- **Part A**: `_synthesis-combinatorial-search-methods.md` + per-paper notes in their appropriate Research/ subdirs + cross-links into existing concept hubs and `Research/AI in Math/`.
- **Part B**: 5+ new paper notes in `Research/Group theory/Open problems/Braid groups/` + upgraded `[[Concepts/burau4-faithfulness]]` and the existing problem note + `_synthesis-burau4-faithfulness.md` with explicit framing as combinatorial search.
- **Final report to Lead**: counts (papers per part), Mixer-shaped methods identified in Part A, fetchability outcomes in Part B, any sparse/contradictory findings worth surfacing to Maria.

## Effort estimate

- A1: ~15 min (no fetching)
- A2: ~5-10 min per paper × 8-12 papers = 40-120 min
- A3: ~30 min synthesis
- B1: ~10 min source inventory
- B2: ~5-10 min per source × 5+ sources = 25-50 min
- B3: ~30 min for upgrades + synthesis
- **Total: ~2-4 hours** split across sessions. Token-budget guidance: split A and B across separate sessions if needed.
