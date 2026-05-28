---
tags: [agent/lead, user/maumayma, domain/group-theory, topic/vault-structure, topic/moc, status/draft]
author: maumayma
project: mixer-core
audience: Researcher
brief_date: 2026-05-28
queued_for: post-F4.3 (and probably post-F4.4 so concept-hub data is in)
---

# Brief — MOC creation pass (post-F4.3 addendum)

**Status**: QUEUED. Do not route until F4.3 + F4.4 land — MOCs need real topic tags + concept hubs to curate against.

Sender: Lead (relaying Maria's brief).
Recipient: Researcher (restructure authority over `Research/`).

## Ask

Create **one MOC per major topic** in `Research/Group theory/` using the **LYT pattern** (Nick Milo, Linking Your Thinking): short curated wikilink lists with annotations. Not exhaustive auto-generated lists — a Researcher-curated subset with the wikilink + one-line "why this is here" annotation each.

Initial topic set (Maria's call):

- **burnside** — Burnside groups generally + B(2,5), B(4,3), B(5,3) collateral
- **word-problem** — word-problem decidability + algorithms (Novikov-Boone, free / abelian / hyperbolic / automatic decidable cases)
- **knuth-bendix** — KB completion, orderings, rewriting techniques
- **presentations-and-orders** — group presentations, Tietze, coset enumeration, |G| computation, finiteness/infinity arguments

The topic set is not exhaustive; if F4.3 surfaces another topic with 3+ papers warranting curation, add a MOC for it and flag to Lead.

## LYT MOC pattern

For each MOC, the body shape is roughly:

```markdown
# <Topic> — Map of Content

**One-paragraph framing** — what this topic covers, who it's for, what questions a reader navigates here for.

## Core papers
- `[[<paper-1>]]` — one-line annotation: why this paper is foundational for the topic
- `[[<paper-2>]]` — annotation
- ...

## Techniques / methods
- `[[<paper-or-concept>]]` — annotation
- ...

## Open problems
- `[[<paper>]]` — annotation
- ...

## Related concepts
- [[Concepts/<name>]] — annotation
- ...

## Adjacent MOCs
- `[[<other-MOC>]]` — when to navigate over there
```

**Curation discipline**: every wikilink earns its place with a "why this is on this MOC" annotation. No auto-generated dumps. If a paper barely touches the topic, it doesn't belong in the MOC even if its `#topic/*` tag matches. MOCs are reading paths, not query results.

## Location decision (defer to Researcher's restructure authority)

Several reasonable homes:
- `Research/Group theory/_MOCs/<topic> MOC.md` (sorted to top via underscore)
- `Research/Group theory/MOCs/<topic> MOC.md`
- Per-subdir adjacent to existing material (e.g. `Burnside groups/_burnside MOC.md`)
- Collapsed into the existing `_overview.md` notes that F6.1 creates (e.g. `Word Problem/_overview.md` IS the word-problem MOC)

**Pre-decision flag**: F6.1 creates `_overview.md` at `Research/Group theory/`, `General/`, `Word Problem/`, `Tools/`. Those overviews may serve as MOCs or as separate doc-types — Researcher decides whether to (a) collapse word-problem MOC into `Word Problem/_overview.md`, or (b) keep `_overview.md` as a sibling "decision tree / scope doc" and put the MOC at `Research/Group theory/_MOCs/word-problem MOC.md`. State the choice in the deliverable.

## Sequencing

- Wait until F4.3 + F4.4 are done. MOCs need real `#topic/*` tags + populated `Concepts/` hubs to curate against. Running this before F4.3 would just produce thin lists.
- Likely also wait until F6.1 lands so the `_overview.md` collision question is resolved.
- After: ~60–90 min for 4 MOCs at LYT depth.

## Constraints

- **LYT discipline**: short curated lists + annotations, NOT exhaustive tag-query dumps.
- **No invented relationships**: each annotation reflects content Researcher has actually read.
- **6-axis tags** per [[tags]]: `#agent/research #user/maumayma #domain/group-theory #topic/<the-topic-this-MOC-covers> #topic/moc #status/draft` plus `#convention` if MOCs become a doctrine. No `#project/*` (MOCs are domain-foundational, not project-scoped).
- **Bidirectional**: every paper / concept linked from a MOC adds the MOC to its frontmatter `related_mocs:` (new field — register in [[tags]] if Researcher creates it) or just keeps the link discoverable via backlinks.

## Deliverable

- 4 MOCs (or however many the topic set settles on) created.
- Location decision documented in `Agents/maumayma/Researcher/log.md`.
- List of MOC → paper/concept link counts so we can see curation density.
