---
tags: [agent/exp-b25, log]
---

# Experimenter-B25 — Activity Log

Append-only daily log. Latest at top.

---

## 2026-05-28 — Phase 9 F9.2 orphan wiring pass

Task from Lead / Phase 9 orphan-wiring coordination. Added `## Related material` sections to the 6 B25 experiment data/results files that were graph-dead (zero in/out wikilinks).

### Wikilinks added per note

| Note | Links added | Targets |
|---|---|---|
| `KBMag/data/kbmag-data.md` | 6 | `KBMag/_type`, `_progress`, `kbmag-results`, `kbmag-overlap-scoring-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974` |
| `KBMag/results/kbmag-results.md` | 7 | `KBMag/_type`, `_progress`, `kbmag-data`, `kbmag-overlap-scoring-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974`, `kourovka-11.48-kostrikin-1990` |
| `Reduce Core/data/reduce-core-data.md` | 6 | `Reduce Core/_type`, `_progress`, `reduce-core-results`, `reduce-core-pipeline-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974` |
| `Reduce Core/results/reduce-core-results.md` | 7 | `Reduce Core/_type`, `_progress`, `reduce-core-data`, `reduce-core-pipeline-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974`, `kourovka-11.48-kostrikin-1990` |
| `Rust Bidirectional/data/rust-bidirectional-data.md` | 6 | `Rust Bidirectional/_type`, `_progress`, `rust-bidirectional-results`, `rust-bidirectional-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974` |
| `Rust Bidirectional/results/rust-bidirectional-results.md` | 7 | `Rust Bidirectional/_type`, `_progress`, `rust-bidirectional-data`, `rust-bidirectional-b25-2026-05-22`, `kbmag-tools-overview`, `havas-wall-wamsley-1974`, `kourovka-11.48-kostrikin-1990` |
| **Total** | **39** | |

### Notes
- All 6 files were previously at zero in/out wikilinks; each now has ≥6 outgoing links (exceeds 3-link minimum per convention).
- `kbmag-tools-overview` linked from all 6 — kbprog is named substantively in every file.
- `kourovka-11.48-kostrikin-1990` linked from results notes only (substance test: data notes don't engage with the open question directly).
- No MOC edits made (Researcher's scope; F9.1 handles bidirectional reciprocation from `_moc-burnside`).
- Phase 8 retag pass (F8.4) was already complete; this is a second pass over the same 6 files.

---

## 2026-05-28 — Phase 8 content-type retag pass (F8.4)

Task from Lead / Phase 8 coordination. Applied content-type tags and 6-axis compliance across all 13 notes in `Experiments/Group Theory/Burnside Group/B25/**`.

### Content-type counts (post-retag)

| Content-type tag | Count | Notes |
|---|---|---|
| `#experiment` | 1 | `_progress.md` (umbrella) |
| `#experiment-type` | 3 | All three `_type.md` files |
| `#methodology` | 3 | All three `methodology/*.md` files |
| `#results` | 3 | All three `results/*.md` files |
| `#data` | 3 | All three `data/*.md` files |
| **Total** | **13** | |

### Per-file retag log (before → after)

**`_progress.md`**
- Before: `[..., status/inconclusive, experiment]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/kbmag, topic/proof-search, ..., experiment]`
- Changes: added 6 topic/* tags; content-type unchanged (already `experiment` ✓)

**`KBMag/_type.md`**
- Before: `[..., status/inconclusive, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, ..., experiment-type]`
- Changes: `methodology` → `experiment-type`; added 5 topic/* tags

**`KBMag/data/kbmag-data.md`**
- Before: `[..., status/inconclusive, data]`
- After: `[..., topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, ..., data]`
- Changes: added 4 topic/* tags; content-type unchanged (`data` ✓)

**`KBMag/methodology/kbmag-overlap-scoring-b25-2026-05-22.md`**
- Before: `[..., status/inconclusive, experiment, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer, topic/word-problem, ..., methodology]`
- Changes: removed `experiment` (dual content-type violation); added 6 topic/* tags

**`KBMag/results/kbmag-results.md`**
- Before: `[..., status/inconclusive, experiment]`
- After: `[..., topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/mixer, ..., results]`
- Changes: `experiment` → `results`; added 5 topic/* tags

**`Reduce Core/_type.md`**
- Before: `[..., status/inconclusive, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., experiment-type]`
- Changes: `methodology` → `experiment-type`; added 5 topic/* tags

**`Reduce Core/data/reduce-core-data.md`**
- Before: `[..., status/inconclusive, data]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, ..., data]`
- Changes: added 4 topic/* tags; content-type unchanged (`data` ✓)

**`Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22.md`**
- Before: `[..., status/conjectured, experiment, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., methodology]`
- Changes: removed `experiment` (dual content-type violation); added 5 topic/* tags; `status/conjectured` preserved

**`Reduce Core/results/reduce-core-results.md`**
- Before: `[..., status/inconclusive, experiment]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., results]`
- Changes: `experiment` → `results`; added 5 topic/* tags

**`Rust Bidirectional/_type.md`**
- Before: `[..., status/inconclusive, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., experiment-type]`
- Changes: `methodology` → `experiment-type`; added 5 topic/* tags

**`Rust Bidirectional/data/rust-bidirectional-data.md`**
- Before: `[..., status/inconclusive, data]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., data]`
- Changes: added 5 topic/* tags; content-type unchanged (`data` ✓)

**`Rust Bidirectional/methodology/rust-bidirectional-b25-2026-05-22.md`**
- Before: `[..., status/inconclusive, experiment, methodology]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., methodology]`
- Changes: removed `experiment` (dual content-type violation); added 5 topic/* tags

**`Rust Bidirectional/results/rust-bidirectional-results.md`**
- Before: `[..., status/inconclusive, experiment]`
- After: `[..., topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, ..., results]`
- Changes: `experiment` → `results`; added 5 topic/* tags

### Structural issues resolved

1. **3 `_type.md` files** had `methodology` instead of `experiment-type` — fixed.
2. **3 `results/*.md` files** had `experiment` instead of `results` — fixed.
3. **3 `methodology/*.md` files** had both `experiment` + `methodology` (dual content-type) — `experiment` removed, `methodology` kept.
4. **All 13 files** were missing `#topic/*` tags entirely — fixed with 4–6 topic tags per file passing substance test.
5. **No bare `data`/`results` string violations** found (the `data` tags on `data/*.md` and `results` tags being added to `results/*.md` are both registered content-type tags).

---
