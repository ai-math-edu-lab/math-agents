---
tags: [agent/lead, user/maumayma, domain/group-theory, topic/vault-tooling, topic/connection-graph, status/draft]
author: maumayma
project: mixer-core
audience: Researcher (F9.1) + Experimenter-B25 (F9.2)
brief_date: 2026-05-28
---

# Brief — Phase 9: Wire 25 orphan technical/foundation notes into the connection graph

Sender: Lead (relaying Maria's brief verbatim, with sequencing notes).
Recipients: Researcher (F9.1) + Experimenter-B25 (F9.2) — parallel.

## Why this matters (the inversion problem)

Graph orphan audit found **25 notes with zero wikilinks in OR out**. These are not housekeeping — they are the most substantively important technical content in the vault:

- **Tools/GAP + Tools/KBMAG** (9 files): operational knowledge B(2,5) experiments depend on directly
- **Word Problem stack** (5 files): theoretical foundation for the entire B(2,5) program
- **Group theory General overviews + subnotes** (3+ files): foundational notes
- **B25 experiment data/results** (6 files): empirical artifacts

Phase 6 populated the new dirs with real content but skipped the cross-linking step. **The graph view is currently structurally inverted**: MOCs, papers, and concept hubs form dense clusters at the top while the technical foundations they all rest on are isolated orphans at the periphery. Healthy knowledge graphs have foundations as central hubs, not orphans.

## Doctrine context (Lead applied as preconditions, all landed)

- `_meta/research-folder-convention.md` § Cross-linking discipline — new section, applies to Research/.
- `_meta/experiment-folder-convention.md` § Cross-linking discipline — new section, applies to Experiments/ subtree.
- `_meta/skills/research/workflows/single-paper.md` step 15 — new "verify ≥3 outgoing wikilinks before saving" step. Future /research runs cannot land orphan-on-creation papers.

Both convention files document the link discipline both agents must apply (parent overview, MOC, siblings/concepts/papers, substance test, bidirectional reciprocation, housekeeping exemption).

## F9.1 — Researcher

**Scope**: 19 files in `Research/Group theory/{General, Word Problem, Tools}/**`.

For each orphan note, **add or update a `## Related material` section** before EOF with 3-7 substantive wikilinks. Discipline:

1. **Up-link to parent overview**: every note in a subdir links to its parent `<subject>-overview.md`. Examples:
   - `decidability-landscape.md` → `[[word-problem-overview]]`
   - `01-group-order.md` → `[[gap-overview]]` and `[[group-theory-tools-overview]]`
2. **MOC inclusion**: every note links to relevant MOC(s) in `Research/Group theory/_MOCs/`:
   - Word Problem notes → `[[_moc-word-problem]]`
   - KB notes → `[[_moc-knuth-bendix]]`
   - Burnside-adjacent → `[[_moc-burnside]]`
   - Presentations / Cayley graphs → `[[_moc-presentations-and-orders]]`
3. **Sibling cross-links**: notes in the same dir that share substantive topics (e.g. `automatic-groups.md` ↔ `dehn-function.md` if they cover related techniques).
4. **Concept hubs**: when a note introduces or relies on a concept, link to `Concepts/<name>.md`. **If the concept appears in 2+ orphan notes but no hub exists, create the stub** (use [[concept-note]] template — short, frontmatter-heavy).
5. **Paper-bridging**: link to specific papers in `Research/Group theory/**/*.md` when a note's content was developed in or builds on that paper. Substance test — only link when the paper is genuinely the source.
6. **MOC bidirectional update**: each MOC's "Concepts" / "Techniques" / "Tools" sections **must be updated** to include wikilinks back to the now-linked orphans. Without this, the wiring is one-way.

## F9.2 — Experimenter-B25

**Scope**: 6 files in `Experiments/Group Theory/Burnside Group/B25/{KBMag, Reduce Core, Rust Bidirectional}/{data, results}/*.md`.

For each orphan note, add a `## Related material` section. Discipline:

1. **Up-link to parent `_type.md`** (methodology family root) — **mandatory**.
2. **Up-link to `_progress.md`** at the B25 root — **mandatory**.
3. **Sibling link `data` ↔ `results`** within the same experiment-type dir — **mandatory**.
4. **Cross-link to methodology dir** if data/results were produced by a specific methodology run.
5. **Tools cross-link**: if the experiment used KBMAG or GAP, link to `[[kbmag-tools-overview]]` / `[[gap-overview]]` in `Research/Group theory/Tools/`. **Mandatory when the tooling is named.**
6. **Paper-bridging**: link to papers in `Research/Group theory/Burnside groups/B25/**` that informed the methodology (havas-newman-1980, kourovka entries, etc.) when relevant.

## Coordination

- **F9.2 in flight alongside the Phase 8 retag pass** (`be6fgh3av`): Experimenter-B25's content-type retag work is in progress. F9.2 can fold into the same pass OR run as a second pass over the same files — Experimenter-B25's call on which is lower-overhead. Same files get touched either way.
- **Bidirectional MOC updates require Researcher's authority** — Experimenter-B25 should not edit MOC files. When F9.2 links into MOCs (e.g. via `[[_moc-burnside]]`), the reciprocal back-link is Researcher's responsibility, not Experimenter-B25's. F9.1 handles all the MOC-side reciprocation.

## Verification — Researcher writes orphan-detection script

Maria's spec:

```python
# _meta/scripts/find-graph-orphans.py
# Counts notes with zero incoming AND zero outgoing wikilinks
# Excludes _meta/skills/, .obsidian/
# Expected post-Phase-9: orphan count drops from 25 → ≤2 (only intentional standalones)
```

Researcher writes the script (or adapts one Maria provides), saves to `_meta/scripts/`, and re-runs after F9.1 + F9.2 land. Report before/after counts to Lead. Script lives in `_meta/scripts/` (new dir if needed; treat as meta-tooling per [[naming-conventions]] Rule 2).

## Constraints (both subtasks)

- **Substance test on every wikilink** — reject aspirational links.
- **No content rewrites** — only add `## Related material` sections + wikilinks within. The substance of each note stays as Phase 6 / B25 experiment work wrote it.
- **Bidirectional discipline mandatory** — every newly-linked target gets reciprocated. MOCs especially must surface the technical content they should be pointing at.

## Deliverable

**F9.1 (Researcher)**: count of wikilinks added per note; MOC sections updated; concept hubs created; before/after orphan count.
**F9.2 (Experimenter-B25)**: same fields scoped to B25 subtree.

Lead consolidates into a Phase 9 summary report.

## Effort estimate

~60 min total — F9.1 ~45 min (19 files + bidirectional MOC updates), F9.2 ~15 min (6 files in tight scope). Parallel.
