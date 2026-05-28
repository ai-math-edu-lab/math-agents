---
tags: [agent/dev, log]
---

# Developer — Activity Log (Math)

Append-only. Latest at top.

---

## 2026-05-28 — Phase 8: Experiments.base content-type views

**Routed by:** Lead.

**Added 4 new views:**
- `By experiment-type` — groupBy `experiment_type` frontmatter property (single-value; no formula needed since `#experiment-type` isn't a `*`-namespace tag family).
- `Methodology inventory` — filter `file.hasTag("methodology")`.
- `Results inventory` — filter `file.hasTag("results")`.
- `Data inventory` — filter `file.hasTag("data")`.

**Required global-filter refactor (flagged to Lead).** The base's original global filter included `file.hasTag("experiment")`, which restricted EVERY view to umbrella `_progress.md` notes only. The new inventory views (filtering on `#methodology` / `#results` / `#data`) would intersect to zero. Fix: dropped that clause from the global filter and re-added it as a view-level filter to all 7 pre-existing views. Verified each existing view's row-count is unchanged via `obsidian base:query`.

**Filter-shape gotcha caught + documented.** Bases doesn't allow `and:` and `or:` as siblings at the same level; nesting `or:` inside `and:` is the legal form. Applied to `Validated — promotable` and `Rejected / disproven — lessons` after adding the `file.hasTag("experiment")` view-level filter.

**Verification via `obsidian base:query`** (no live UI render needed; CLI returns the underlying row set):
- `Latest`: 1 row (one umbrella note exists)
- `Methodology inventory`: 3 rows
- `Results inventory`: 3 rows
- `Data inventory`: 3 rows
- `Validated — promotable`: 0 rows (correct — no validated experiments yet)

**Updated [[Architecture/Mixer/Bases/_README.md]]** with Experiments.base section: design rationale, global-filter refactor justification, single-value-vs-multi-value groupBy reasoning, the `or:`-nesting gotcha. Carries forward the Papers.base lesson that Bases multi-value groupBy does NOT fan out — future contributor should not re-investigate.

**Files touched:** `Architecture/Mixer/Bases/Experiments.base` (rewritten), `Architecture/Mixer/Bases/_README.md` (extended).

**Pending:** Experimenter-B25's content-type retag pass is the predecessor for full-population verification. Inventory views will fill in further as their retag lands.

---

## 2026-05-28 — Phase 8 F8.3: generic-filename sweep in Architecture/Mixer/Components/

**Routed by:** Lead.

**Result:** sweep clean, no action needed. Verified all 18 .md files in `Architecture/Mixer/Components/` against [[naming-conventions]] Rules 1, 3, 5. Zero generic-name violations (`results|data|notes|summary|overview|_overview|_placeholder|engine|paper` as standalone filenames). `scheduler.md` and `transport.md` (in Mixer Core/) confirmed unique vault-wide — Rule 1 satisfied.

**Side observation (flagged to Lead, no action taken):** `Architecture/Mixer/Components/UI/` is a single-content-file dir containing only `ui-overview.md` — matches Maria's new merge-option framing as an anti-pattern. But the merge option doesn't cleanly apply: no parent component .md exists for UI to merge into, and flattening the dir would be a directory rename (out of scope this brief).

**Files touched:** none (verification only).

---

## 2026-05-28 — F7.1 naming convention: 3 _overview.md renames in Architecture/Mixer/Components/

**Routed by:** Lead.

**Done:**
- `KBMag/_overview.md` → `kbmag-overview.md`
- `Mixer Core/_overview.md` → `mixer-core-overview.md`
- `UI/_overview.md` → `ui-overview.md`
- 8 wikilink updates across 5 files (KBMag/kbmag-v1.md ×3 including a YAML `related:` list entry; KBMag/kbmag-source.md ×2; Mixer Core/braid-reduce.md ×1; Mixer Core/reduce-coreless.md ×1; Documentation/Code Review/2026-05-22-stale-component-inventory.md ×1).
- The cross-area Code Review reference was disambiguated by parenthetical-context ("KBMag directory overview") since its source file lives outside any Component dir and Obsidian's nearest-folder bare-wikilink rule wouldn't apply.
- Verification: `grep -rn '_overview' Architecture/` → 0 matches post-fix.

**Out-of-scope refs flagged (Rule 2, not touched):** Agents/<user>/log.md historical entries with bare `[[_overview]]`; _meta doctrine textual mentions; Lead scratch briefs.

**K3 verdict:** MERGE.

---

## 2026-05-28 — Papers.base "By topic" view fix (Bases groupBy quirk)

**Routed by:** Lead.

**Done:**
- Added formula `topic_tags: file.tags.filter(value.startsWith("#topic/"))`.
- Retargeted `By topic` view's `groupBy.property` to `formula.topic_tags`.
- Added `Architecture/Mixer/Bases/_README.md` with rationale + decision log (Obsidian's Bases saver strips YAML comments).

**Key empirical finding (saved in [[project-obsidian-bases-quirks]]):** Bases groupBy on multi-value properties (native OR formula-list) does NOT fan out into one row per element — each note gets one row with the whole list as a single composite group key. The brief's literal "one row per topic per paper" was unachievable; what shipped is `#topic/*`-scoped group labels instead of the prior noisy mix. Maria chose "accept current state" given Obsidian's native tag pane + Phase 6 MOCs already cover per-topic drill-down.

**K3 verdict:** MERGE-stands (revised after honest expectation-reversed report).

---

## 2026-05-22 — Task B: b25_reduce_core documentation (Phases 1–4)

**Routed by:** Lead

**Completed:**
- Phase 1 — dependency trace from `experiments/b25_reduce_core/`. Written to [[b25-reduce-core-deps-2026-05-22]].
- Phase 2 — in-use component notes (K3 pattern):
  - [[kbmag-source]] — `kbmag_source/standalone/`, kbprog + b25_lifted
  - [[braid-reduce]] — Rust beam-search binary
  - [[reduce-coreless]] — Python word-reduction utilities
  - [[_overview]] (KBMag) — two-directory split, framing corrected per Lead directive
- Phase 3 — stale-component inventory: [[2026-05-22-stale-component-inventory]]
- Phase 4 — test methodology notes (K3 pattern):
  - [[kgram-overlap-verification]], [[special-rule-overlap-verification]]
  - [[gap-word-equality]], [[gap-confluence-verification]]
  - [[traced-braid-reduction]], [[containment-verification]]
  - [[kbmag-ordering-sweep]]

**Vault location corrected mid-session:**
Initial writes landed in `/Users/maumayma/Documents/Obsidian/BOTBOTBOT/Architecture/Mixer/` (trading-project vault — wrong). All 12 notes were copied to the correct location: `/Users/maumayma/Documents/Obsidian/Math/Architecture/Mixer/`. BOTBOTBOT Mixer subtree subsequently deleted. Root cause: read `_common.md` from BOTBOTBOT without verifying which vault this project uses. Internalized rule: **Math vault = algo_mixing project; BOTBOTBOT = trading project. Always use Math vault paths explicitly for this project.**

**KBMag framing corrected per Lead directive:**
Initial framing treated `kbmag_source/` as the primary component and `kbmag_v1/` as stale. Corrected: `kbmag_v1/` is the project-wide main KBMag installation; `kbmag_source/` is a narrow secondary retained only for the biased-KB b25_reduce_core workflow. Applied to: `_overview.md` (rewritten), `kbmag-source.md` (scope blockquote added), stale inventory (kbmag_v1 moved to new "Active project infrastructure" category).

---
