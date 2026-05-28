---
tags: [agent/dev, user/maumayma, domain/cs, topic/obsidian-bases, topic/vault-tooling, status/draft]
author: maumayma
project: vault-tooling
---

# Bases — design notes

Per-file rationale for non-obvious choices in this directory. Obsidian's Bases saver strips YAML comments, so this file holds what would otherwise be a comment in the `.base` source.

## `Papers.base` — `By topic` view

**Choice.** Group by `formula.topic_tags`, where the formula is `file.tags.filter(value.startsWith("#topic/"))`. Tags remain the single source of truth; no `topics: []` frontmatter property duplication; no per-paper migration.

**Why not the duplicated `topics: []` frontmatter property.** Tested empirically (see [[papersbase-by-topic-fix-2026-05-28]]): Bases groupBy on a multi-value property — whether native (`file.tags`) or formula-computed list — groups each paper by its *whole list as a single key*, producing one row per paper, not one row per tag. A dedicated `topics: []` field would therefore yield the same behavior, with the added cost of duplication and migration. The formula approach gets the same result with no schema cost.

**Quirk.** `file.tags` returns tags with the leading `#` (e.g. `#topic/burnside`), so the filter predicate is `value.startsWith("#topic/")`, not `"topic/"`. The visible group label renders chips with the prefix intact (`topic/burnside`).

**Known limitation.** A true "one row per topic per paper" fan-out is not supported by Bases groupBy in this Obsidian build. The user-facing improvement is purely that group labels are now scoped to `topic/*` chips instead of the prior noisy mix (`agent/research`, `user/maumayma`, `domain/group-theory`, `paper`, `status/draft`, …).

**Audit path.** If Bases ever adds list-fan-out semantics for groupBy, this view will start fanning out automatically with no further config change.

## Decision log

**2026-05-28 (Maria):** This is the final shape. Considered three alternatives after the visual verification surfaced the multi-value groupBy limitation:

- **A. Accept current state** ← chosen. Topic-chips-per-row inventory is a real cleanliness improvement over the original noisy-all-namespaces baseline. Per-topic drill-down is covered elsewhere: Obsidian's native tag pane handles "click `#topic/burnside` → see all papers", and Phase 6 MOCs (`Research/Group theory/_MOCs/<topic>.md`) provide curated reading paths.
- B. Re-route to a per-top-level-topic view pattern (`By Burnside`, `By Word Problem`, …). Rejected as a high-maintenance trap — views proliferate as topics multiply.
- C. Drop the view entirely. Rejected — the current improvement ships real value over baseline.

Next contributor: do NOT re-investigate multi-value `groupBy` fan-out on this view. The Bases version constraint is documented above (§ Why not the duplicated `topics: []` frontmatter property). If Bases gains list-fan-out semantics, the view starts working richly with zero config change.

## `Experiments.base` — content-type views (Phase 8, 2026-05-28)

**Added views.** `By experiment-type`, `Methodology inventory`, `Results inventory`, `Data inventory`. Driven by the content-type tag taxonomy (`#experiment`, `#methodology`, `#results`, `#data`, `#experiment-type`) introduced in [[tags]] and the Experiment-tree mapping table.

**Global filter refactor — preserves existing-view semantics.** Original global filter was `file.folder.startsWith("Experiments") AND file.ext == "md" AND file.hasTag("experiment")`. The third clause restricted the entire base to umbrella `_progress.md` notes — fine when `#experiment` was the only experiment-tree content-type, but it makes the new inventory views (which filter on `#methodology` / `#results` / `#data`) intersect to zero.

Fix: dropped `file.hasTag("experiment")` from the global filter; added it as a view-level filter to every pre-existing view (`Latest`, `By project`, `By instance`, `Validated — promotable`, `Rejected / disproven — lessons`, `Inconclusive — need more`, `Pending Validator`). Each existing view's output is identical to before — verified via base:query (`Methodology inventory` returns 3 rows; `Validated — promotable` returns 0 rows just like before; etc.). This was the only path to make the new inventory views work; flagged to Lead in the report.

**`By experiment-type` uses the `experiment_type` frontmatter property as groupBy, NOT a tag formula.** Reason: `#experiment-type` is a single content-type tag (marks the umbrella `_type.md` notes), not a multi-value namespace like `#topic/*`. The experiment-family identity that drives grouping already lives in the `experiment_type` frontmatter property — single-value, native groupBy. No formula needed, no multi-value-as-key composite-group issue.

**Known limitation (same as Papers.base).** Bases multi-value groupBy still does NOT fan out into one row per element in this Obsidian build. If a future inventory view groups on a multi-value list, each note will appear once with its whole list as the composite group key. Do NOT re-investigate. See § Papers.base above for the empirical confirmation.

**`or:` filter shape gotcha.** Bases filter trees don't allow `and:` and `or:` as siblings at the same level — they must nest. The legal shape for "umbrella note AND (status validated OR proven OR replicated)" is:

```yaml
filters:
  and:
    - file.hasTag("experiment")
    - or:
        - status == "validated"
        - status == "proven"
        - status == "replicated"
```

Not:

```yaml
filters:
  and:
    - file.hasTag("experiment")
  or:                    # ← wrong: sibling of `and:`, semantics undefined
    - status == "validated"
    - status == "proven"
    - status == "replicated"
```

The original `Validated — promotable` and `Rejected / disproven — lessons` views had bare `or:` (no global-AND clause), which is valid. After the global filter refactor each one needs the nested form.
