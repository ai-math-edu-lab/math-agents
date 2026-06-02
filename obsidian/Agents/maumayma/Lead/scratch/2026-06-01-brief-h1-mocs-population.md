---
tags: [agent/lead, user/maumayma, domain/methodology, topic/moc, topic/vault-tooling, status/draft]
author: maumayma
project: mixer-core
brief_date: 2026-06-01
audience: Researcher
status_queued: send alongside B1 GO post-A3-K3
---

# Brief — H1: MOC population (corrected scope after vault verification)

Sender: Lead.
Recipient: Researcher.
**Status**: QUEUED. Do not route to Researcher until A3 K3 passes. Run in parallel with B1 (Burau₄ source inventory).

## Background (the divergence from the doctrine entry)

Maria's 2026-06-01 entry in [[naming-conventions]] originally said "_moc files... none exist yet" — Lead's verification showed **5 MOC files already exist** (4 in `Research/Group theory/_MOCs/`, 1 in `Research/AI in Math/_MOCs/`) and 40 inbound `[[_moc-*]]` wikilinks across the vault resolve correctly (not dangling). Maria has fixed the doctrine line directly.

**Corrected H1 scope** (after vault verification): create 1 new MOC + 1 new top-level index + reciprocation sweep on the existing 5.

## Existing MOCs (verify, don't recreate)

- `Research/Group theory/_MOCs/_moc-burnside.md` (Phase 6 MOC pass)
- `Research/Group theory/_MOCs/_moc-knuth-bendix.md` (Phase 6)
- `Research/Group theory/_MOCs/_moc-word-problem.md` (Phase 6)
- `Research/Group theory/_MOCs/_moc-presentations-and-orders.md` (Phase 6)
- `Research/AI in Math/_MOCs/_moc-ai-in-math.md` (AI in Math batch)

## H1 sub-tasks

### H1.a — Net-new `_moc-algorithm-cooperation.md`

Path: `Research/Algorithm Cooperation/_MOCs/_moc-algorithm-cooperation.md` (create `_MOCs/` subdir if it doesn't exist).

Coverage:
- **A3 papers** (just landed in Part A): the 5 Algorithm Cooperation papers ingested in A2 (#5 Korf IDA*, #6 GRASP, #8 Gomes-Selman portfolios, #9 ManySAT, #10 CEGAR) + the new A3 synthesis (`_synthesis-combinatorial-search-methods.md`).
- **Mixer thesis cluster**: the existing concept hubs `[[Concepts/kb-mixing-stagnation]]` and `[[Concepts/mixable-api]]`, plus `[[algo-mixing-burnside-slides]]` (the B(4,3) breakthrough record).
- **Cross-cluster cross-links** to the existing 5 MOCs where the cooperation thesis applies: ⚡ flag papers/notes that have documented "partial-No oracle + complete rewriter" structural relevance (Maria's pattern).

Use LYT discipline per the existing MOCs (short curated wikilink lists + one-line annotations). Substance test on every link — no link-everything.

### H1.b — Net-new top-level `Research/_moc-index.md`

Path: `Research/_moc-index.md`.

Single entry point for agents. **Maria's explicit addition**: must list **all** MOCs — the 5 existing + the new `_moc-algorithm-cooperation` = **6 total**. Not just the new one.

Layout:
- Brief 1-paragraph framing: "This is the index of all topic MOCs in the vault. Agents start here to navigate the research subtrees."
- Numbered or grouped list of all 6 MOCs with a 1-line description per MOC (what topic it covers, where it lives).
- Group theory MOCs grouped together; cross-domain MOCs (AI in Math, Algorithm Cooperation) separate.
- Tag with `#topic/moc` content-type if that pattern is in use.

This is a small file (~30-50 lines). LYT pattern.

### H1.c — Bidirectional reciprocation sweep on existing 5 MOCs

Per [[research-folder-convention]] § Cross-linking discipline: every note linking a MOC must be reciprocated from the MOC's body (substance test, not link-everything).

For each of the 5 existing MOCs, sweep the inbound `[[_moc-<topic>]]` links and verify the MOC body lists the relevant notes back:

- `_moc-burnside.md`: 19+ inbound from Burnside groups/B25/ — verify the MOC body surfaces the foundational ones (Kuznetsov line, Havas-Wall-Wamsley, B(2,5) experiments) with annotations. Substance test: aspirational links (paper mentions Burnside in passing) don't qualify.
- `_moc-knuth-bendix.md`: inbound from KB papers + Tools/KBMAG/. Verify KB techniques + tool refs surfaced.
- `_moc-word-problem.md`: inbound from Word Problem techniques + decidability. Verify the canonical Novikov-Boone-line refs surfaced.
- `_moc-presentations-and-orders.md`: inbound from presentations + group orders. Verify Tietze / coset enum / classification refs surfaced.
- `_moc-ai-in-math.md`: already richly reciprocated in the AI-in-Math batch but verify per the substance test.

For each MOC, log to `Researcher/log.md`: count of inbound links checked, count of new reciprocated entries added, count rejected per substance test.

## Doctrine reminders

- LYT discipline: short curated lists + one-line "why this is here" annotations. **No auto-generated dumps from grep.**
- Step-17 ≥3 outgoing wikilinks per new MOC (trivially met by the index page; for `_moc-algorithm-cooperation` ensure substantive coverage).
- Tag-register-before-use: `topic/moc` is already registered; reuse. Any other new topics (e.g. `topic/algorithm-cooperation` if not already from B-pass) register first.
- **H2 carryover** (separate from H1, mentioned here for context): the paper-summary.md template + single-paper.md Step 15 were patched same-day to add `domain:` and `status:` as explicit frontmatter properties. New MOCs and notes you create after this point should include them. Lead will verify A2 papers' properties at K3 (cheap admin task — backfill any missing).

## Sequencing

H1 runs **after** A3 K3 passes, **in parallel** with B1 (Burau₄ source inventory). The two work surfaces are disjoint (Research/Algorithm Cooperation/_MOCs/ + Research/_moc-index.md vs. Research/Group theory/Open problems/Braid groups/). Researcher can interleave or do sequentially based on token budget.

## Deliverable

- 1 new MOC at `Research/Algorithm Cooperation/_MOCs/_moc-algorithm-cooperation.md`
- 1 new top-level `Research/_moc-index.md` listing all 6 MOCs
- Updates to the 5 existing MOC bodies per the bidirectional reciprocation sweep
- Per-MOC log entries summarizing the sweep counts
- Re-run `find-graph-orphans.py` afterward — orphan count should remain 0 (or drop if any pre-existing not-yet-fully-linked MOCs gain new connections)
- Final report to Lead with: counts of links added per MOC, count rejected per substance test, any structural observations
