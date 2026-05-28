---
tags: [agent/dev, user/maumayma, topic/obsidian-bases, topic/vault-tooling, status/draft]
author: maumayma
project: vault-tooling
date: 2026-05-28
---

# Plan — Papers.base "By topic" view fix

Sender: Developer.
Sources: [[2026-05-28-brief-papersbase-topic-view-developer]].

## Decision

**Option (ii) — Bases formula filtering `file.tags`.** No frontmatter migration needed.

## Bases-syntax verification (from local skill docs)

- `file.tags` is a `List` of tags (no `#` prefix; confirmed by reading one paper note's frontmatter).
- `list.filter(expression)` is documented; the per-element identifier is `value`.
- `string.startsWith(query)` is documented.
- `list.map(expression)` is documented; can strip the `topic/` prefix from group labels.
- `groupBy.property` accepts a property reference; `formula.<name>` is a first-class property reference in Bases (used in `order:` and `properties:` blocks). Will be verified by rendering.

## Files touched

- `Architecture/Mixer/Bases/Papers.base` — one new formula, one view's `groupBy` retargeted, one YAML comment documenting the choice.

## Userspace surfaces

- Bases config only. No mixer protocol, no pyo3 ABI, no Python API, no KBMAG format touched. No tests required (per brief: "No tests required").

## The change

Add a new formula:

```yaml
formulas:
  topic_tags: 'file.tags.filter(value.startsWith("topic/")).map(value.replace("topic/", ""))'
```

Retarget the "By topic" view's groupBy:

```yaml
- type: table
  name: By topic
  groupBy:
    property: formula.topic_tags
    direction: ASC
  order: ...
```

The `.map(value.replace(...))` step produces clean group labels (`burnside`, `b25`) instead of `topic/burnside`, `topic/b25`. If groupBy on a formula yielding a list does NOT fan out one-row-per-element (i.e., if it groups by the whole list as one key), the fallback is to drop `.map(...)` and re-test — or to materialize a frontmatter property (option i). Will be confirmed at verification.

## Verification — actual results

Walked the view in Obsidian via `obsidian-cli` (eval + dev:screenshot). Findings:

1. **Tag prefix:** `file.tags` returns tags with the leading `#` (e.g. `#topic/burnside`). The filter predicate had to be `value.startsWith("#topic/")`, not `"topic/"`. Confirmed via a debug `file.tags.join(",")` formula.
2. **`.map()` is unnecessary:** Bases renders the chips inside the group header. Stripping the prefix has no visible benefit, so the final formula is just `file.tags.filter(value.startsWith("#topic/"))`.
3. **groupBy fan-out NOT supported:** Tested both `groupBy.property: file.tags` (native multi-value) and `groupBy.property: formula.topic_tags` (formula-list). Both group each paper by its *whole tag list as a single key* — one row per paper, not one row per tag. Lead's prior observation "fans out across every tag namespace" reflected the noisy chip cluster in the group header, not actual row fan-out.
4. **What the fix actually delivers:** group labels are scoped to `#topic/*` chips only (was: noisy mix of `agent/research`, `user/maumayma`, `domain/group-theory`, `paper`, `status/draft`, …). Each paper still appears as one row.

## Fallback verdict

Option (i) — dedicated `topics: []` frontmatter — would NOT have helped either: the same multi-value-key behavior would apply to any list property. So the Researcher migration in option (i) would be pure cost with no benefit. Option (ii) stays as the best achievable outcome under current Bases capabilities.

## Final state

- `formulas.topic_tags: file.tags.filter(value.startsWith("#topic/"))`
- `views[By topic].groupBy.property: formula.topic_tags`
- `Architecture/Mixer/Bases/_README.md` added with per-file design notes (Obsidian strips YAML comments on save, so doc lives in a sibling note).

## Out of scope

- Other views in Papers.base.
- Other .base files (Components, Concepts, Experiments).
