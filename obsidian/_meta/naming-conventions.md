---
tags: [meta, convention]
---

# Naming Conventions — Math Vault

Vault-wide rules for filenames. These apply to all notes that get wikilinked or queried via Bases. Last updated 2026-05-28 (Phase 7, Researcher).

---

## Rule 1 — Unique filenames for public-facing notes

**Public-facing notes** (Research/ papers, Concepts/ hubs, Architecture/ components and docs, Experiments/ methodology and results, MOCs) must have filenames that uniquely identify the note **without folder context**. Obsidian resolves bare wikilinks `[[filename]]` by filename alone; duplicate filenames cause ambiguous resolution.

**Pattern:** `<subject>-<qualifier>.md`

| Instead of | Use |
|---|---|
| `_overview.md` | `kbmag-tools-overview.md`, `gap-overview.md`, `word-problem-overview.md` |
| `results.md` | `reduce-core-results.md`, `rust-bidirectional-results.md` |
| `data.md` | `kbmag-data.md`, `reduce-core-data.md` |
| `engine.md` | `mixer-core-engine.md` |
| `summary.md` | `b25-experiment-summary.md` |
| `notes.md` | `kb-ordering-notes.md` |

---

## Rule 2 — Exception: internal housekeeping notes

**Internal housekeeping notes** may use generic names because they are **path-qualified in agent prompts and never wikilinked by bare name**:

- `Agents/<user>/<role>/log.md` — append-only agent log
- `README.md` files in any directory
- `scratch/` entries in agent home dirs

Do **not** rename these. The underscore (`_`) prefix convention (Rule 4) also does not apply to `log.md`.

---

## Rule 3 — Lowercase kebab-case for all filenames

All filenames use **lowercase-kebab-case**:
- `havas-wall-wamsley-1974.md` ✅
- `HavasWallWamsley1974.md` ❌
- `havas wall wamsley.md` ❌

Applies to new files and renames. Existing correctly-named files are not renamed solely to change case if they have no other issues.

---

## Rule 4 — `_` prefix reserved for index/MOC notes

The `_<name>.md` prefix is **reserved for notes that act as a directory index or Map of Content** and should sort to the top of their directory:

- `_synthesis-<topic>.md` — multi-paper synthesis (updateable)
- `_moc-<topic>.md` — Map of Content (LYT pattern)
- `_overview.md` — DEPRECATED (too generic; see Rule 1). Replace with `<subject>-overview.md`.

**Do NOT use `_` prefix on content notes** (individual definitions, paper summaries, concept hubs, methodology notes).

---

## Rule 5 — Avoid generic words unqualified

These words are generic and ambiguous alone. Always prefix with a subject:

- ❌ `data.md` → ✅ `kbmag-data.md`
- ❌ `results.md` → ✅ `rust-bidirectional-results.md`
- ❌ `overview.md` → ✅ `group-theory-overview.md`
- ❌ `notes.md` → ✅ `kb-ordering-notes.md`
- ❌ `summary.md` → ✅ `b25-experiment-summary.md`
- ❌ `paper.md` → ✅ (use author-year: `havas-1980.md`)

---

## Paper note filenames

For paper summaries in `Research/`, use:
- `<first-author>-<year>.md` for single-topic papers: `havas-1980.md`, `burnside-1902.md`
- `<first-author>-<coauthor>-<year>.md` for 2-author papers: `havas-newman-1980.md`
- `<arxiv-id>.md` for preprints without stable citation: `2410.12345.md`
- Descriptive name for problem notes: `b25-finiteness-11.48-kostrikin.md`

---

## Wikilink update on rename

When renaming a file via CLI (not Obsidian GUI), Obsidian does NOT automatically update wikilinks. Required steps:

```sh
# 1. Rename the file
mv old-name.md new-name.md

# 2. Find all wikilinks to the old name across the whole vault
grep -r "\[\[old-name\]\]" <vault-root> --include="*.md" -l

# 3. Update each wikilink manually
sed -i '' 's/\[\[old-name\]\]/[[new-name]]/g' <affected-file>

# 4. CRITICAL: also grep the newly-renamed file(s) themselves
# Renamed files that cross-reference each other won't be caught by step 2.
# After a batch rename, check each renamed file for stale references to siblings:
grep -n "old-name-1\|old-name-2\|..." <renamed-file.md>
```

Log every rename to `Agents/<user>/Researcher/log.md` with before → after.

---

## History

- 2026-05-28: Created (Phase 7, Researcher) — driven by Maria's observation of `_overview` × 10 generic filenames causing ambiguity in Bases views.
