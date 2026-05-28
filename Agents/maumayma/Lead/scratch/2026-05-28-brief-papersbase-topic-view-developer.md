---
tags: [agent/lead, user/maumayma, domain/cs, topic/obsidian-bases, topic/vault-tooling, status/draft]
author: maumayma
project: mixer-core
audience: Developer
brief_date: 2026-05-28
---

# Brief — Papers.base "By topic" view fix (Bases syntax)

Sender: Lead.
Recipient: Developer.

## Context

`Architecture/Mixer/Bases/Papers.base` has a "By topic" view that Lead added in Phase 5 with a placeholder syntax:

```yaml
- type: table
  name: By topic
  groupBy:
    property: file.tags
    direction: ASC
  ...
```

The view groups by `file.tags` — which fans out across **every** tag namespace (`#agent/*`, `#user/*`, `#domain/*`, `#topic/*`, `#paper`, `#status/*`, etc.), producing noisy groupings. Researcher confirmed during F4.1 inventory and again at F4.3 completion: the view is unusable as a topic browser.

After F4.3 migration (just landed today), every paper note in `Research/` now carries multiple `#topic/*` tags from the substance-tested set: `topic/burnside`, `topic/b25`, `topic/word-problem`, `topic/knuth-bendix`, `topic/finitely-presented-groups`, etc. The data is in place; the view's groupBy logic is wrong.

## The ask

Fix the "By topic" view in `Architecture/Mixer/Bases/Papers.base` so it groups only on `#topic/*` subtags, producing one row-per-topic-per-paper.

## Two candidate approaches

**Option (i) — Dedicated `topics: []` frontmatter property**

- Add a `topics: [burnside, b25, word-problem, ...]` list field to each paper's frontmatter (mirroring the `#topic/*` tags).
- Bases `groupBy.property: topics` would fan out cleanly on the list.
- Pro: cleanest Bases querying (no tag-parsing acrobatics); list-property groupBy is well-established Bases syntax.
- Con: data duplication (topics live in both `tags:` and `topics:`); requires Researcher to migrate all 16 paper notes to add the new field; future paper notes must remember to populate both.

**Option (ii) — Bases formula scoping groupBy to `topic/*` prefix**

- Add a formula that extracts only `topic/*` tags from `file.tags`, then groupBy that formula.
- Candidate syntax (unverified by Lead): `formulas: topic_tags: file.tags.filter(t => t.startsWith("topic/"))` or similar. Bases formula language for array filtering isn't documented in any local `.base` file Lead surveyed.
- Pro: no data duplication; no Researcher migration; uses tags as the single source of truth.
- Con: requires Bases to support `.filter()` on `file.tags` (or equivalent), which Lead couldn't verify locally. If Bases doesn't support this, fall back to (i).

## Your call

Developer has Bases expertise; pick the more robust path given actual Bases capabilities in the installed Obsidian version. If (ii) works, it's clearly better (no duplication, no migration). If Bases formulas can't filter `file.tags`, (i) is the fallback.

If (i): also produce a one-paragraph migration note for Researcher (which they'll do — Lead routes when you confirm syntax). Per-paper edit is mechanical (add `topics: []` mirroring existing `#topic/*` tags).

## Deliverables

1. Updated `Architecture/Mixer/Bases/Papers.base` with the fixed "By topic" view.
2. Verify the view renders correctly in Obsidian against the now-populated paper notes (Research/ has 16 notes with topic tags as of F4.3).
3. One-line note in the `.base` file's YAML (a comment) or a sibling `_README.md` documenting which approach was chosen and why.
4. If approach (i) chosen: the Researcher migration note (Lead routes).
5. Report back to Lead with: which option you picked, the working syntax, screenshot or copy of the rendered view if practical.

## Out of scope

- Don't touch other Bases files (`Components.base`, `Concepts.base`, `Experiments.base`) unless they have the same bug — and if they do, file separately. This brief is scoped to `Papers.base`.
- Don't extend the schema beyond fixing this one view. Other Phase-5-era views (`By project (project-scoped only)`, `By language`, `Non-English papers`, `By domain`, etc.) work and should be preserved as-is.

## Constraint

This is a Bases-config change, not a code change. No tests required. K3 review from Lead on receipt.

## References

- `[[Architecture/Mixer/Bases/Papers.base]]` — the file to fix
- `[[tags]]` § Axis 4 — the topic-tagging doctrine the view needs to surface
- `[[2026-05-28-inventory]]` — F4.1 inventory note where Researcher first observed the noise
- `[[Agents/maumayma/Researcher/log.md]]` — F4.3 migration log with the full topic-tag picture per paper
