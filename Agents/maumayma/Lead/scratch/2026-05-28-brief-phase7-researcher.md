---
tags: [agent/lead, user/maumayma, domain/methodology, topic/vault-tooling, topic/naming-convention, topic/taxonomy, status/draft]
author: maumayma
project: mixer-core
audience: Researcher
brief_date: 2026-05-28
---

# Brief — Phase 7: Naming convention + duplicate cleanup + domain frontmatter audit

Sender: Lead (relaying Maria's brief verbatim, with sequencing notes).
Recipient: Researcher.

## Context (Maria's three observations)

1. **Generic filenames** showing up multiple times in Bases views — `_overview` × 3+ in Components view, `results` × 3 + `data` × 1 in Experiments view. No way to distinguish them from the row alone. Obsidian community consensus: filenames must uniquely identify a note without folder context for anything wikilinked or queried via Bases.
2. **`domain` frontmatter shows `None`** in the Papers view for at least the grobner paper. F4.2 migrated `#domain/grobner` → `#domain/cs` (tag), but it's unclear whether the `domain:` frontmatter field was updated alongside the tag in F4.3 — possibly only the tag was changed.
3. **No registered naming convention doctrine** to prevent recurrence.

## Sequencing — Phase 7 vs. in-flight MOC pass

You're mid-MOC pass (~minutes in). **Lead's recommended pivot: option (a) — interrupt at next natural break.**

- (a) Pause MOC pass at next natural break (likely the current MOC, then stop). Write F7.1 (~15 min). Resume MOC pass with the F7.1 naming convention applied to all 4 MOCs. Avoids the F7.2 rename sweep having to immediately re-process freshly-created MOC files.
- (b) Finish all 4 MOCs with current naming. Then write F7.1 + run F7.2 rename sweep over both the MOCs and the duplicate-filename targets. More rework, but no MOC-pass interruption.

(a) is lower-overhead unless you're already deep into MOC #2 (then your call — finish it and pivot). Either way, Phase 7 lands today.

## F7.1 — Naming convention doctrine (~15 min)

Add a section to `_meta/research-folder-convention.md` AND create `_meta/naming-conventions.md` for vault-wide rules (covering Components, Experiments, MOCs too). Doctrine to encode:

1. **Public-facing notes** (Research/papers, Concepts/hubs, Components, Experiments, Architecture/docs, MOCs): filenames must uniquely identify the note without folder context. Pattern: `<subject>-<qualifier>.md`. Examples: `kbmag-source-overview.md` not `_overview.md`; `rust-bidirectional-b25-results.md` not `results.md`; `mixer-core-engine.md` not `engine.md`.
2. **Internal housekeeping notes** (`Agents/<user>/<role>/log.md`, README.md, scratch entries): generic names OK because they're path-qualified in agent prompts and never wikilinked by bare name. **Don't rename these.**
3. **Lowercase-kebab-case** for filenames (consistent with kepano + GitHub-style standardization).
4. **`_<name>.md` prefix** reserved for index/MOC notes that should sort to the top of their dir (`_synthesis-<topic>.md`, `_moc-<topic>.md`). **Don't use `_` for content notes.**
5. **Avoid generic words alone** — `data`, `results`, `overview`, `notes`, `summary` — always qualified with a subject prefix.

## F7.2 — Rename duplicates (~30 min, dep on F7.1)

Inventory + rename pass:

1. `find <vault> -name "_overview.md"` — list all hits. For each: rename to `<parent-dir-name>-overview.md`, OR merge content into a sibling content file if the overview is the only thing in the dir. Your judgment per-dir.
2. `find <vault> -name "results.md"` — list all. For each in `Experiments/`: rename to `<experiment-technique>-results.md` (technique = the experiment-type subdir name).
3. `find <vault> -name "data.md"` — same pattern.
4. Other generic filenames you spot via inventory.

**Wikilink update**: Obsidian GUI updates wikilinks automatically on rename. If you're renaming from CLI, **grep + fix wikilinks manually**. (You're working from Claude Code, so CLI + grep is the default path. `rg "`[[<old-name>]]`" <vault>` then update each.)

**Do NOT touch**: `Agents/<user>/<role>/log.md` and `README.md` files. These are internal housekeeping, path-qualified, not wikilinked by bare name.

Log every rename to `Agents/maumayma/Researcher/log.md` with before → after.

## F7.3 — Domain frontmatter audit (~10 min, parallel with F7.2)

Grep all paper notes in `Research/` for `domain:` frontmatter and verify:

1. Field is **present**.
2. Value **matches the `#domain/*` tag** (e.g. if note has `#domain/cs`, `domain:` should be `cs` not `None` or empty or `grobner`).
3. Value **matches a registered domain** in `_meta/tags.md` (current registered: `group-theory`, `ai`, `cs`, `methodology`).

Fix any mismatches. Log per-paper diffs.

Specific known case from Maria: `grobner.md` paper — F4.3 migrated `#domain/grobner` → `#domain/cs` tag, may not have updated `domain:` frontmatter. Confirm and fix.

## F7.4 — Update `/research` skill workflow (~5 min, dep on F7.1)

- In `_meta/skills/research/workflows/single-paper.md`, add a step **before writing the note**: "Filename must uniquely identify the paper across the vault. Pattern: `<first-author>-<year>` or `<arxiv-id>`. Don't use generic names like `paper`, `note`, `summary`."
- Add to `_meta/skills/research/SKILL.md` "what this skill does NOT do" section: "Does not create notes with generic filenames (`results.md`, `data.md`, `_overview.md`, etc.). Every paper gets a uniquely-identifying name."

## Sequencing inside Phase 7

F7.1 (doctrine) first. F7.2 (renames) and F7.3 (domain audit) in parallel — independent. F7.4 (skill update) last — depends on F7.1.

## Out of scope

- Renaming agent log files, role READMEs, `_meta/` doctrine files (path-qualified, not wikilinked by bare name).
- Renaming directories themselves (handle separately if needed).
- Doctrine work for content-type / topic / status tag axes (covered by [[tags]]; this is naming-only).

## Deliverable

Report back to Lead with:
- New doctrine notes (`_meta/research-folder-convention.md` update + new `_meta/naming-conventions.md`).
- Count of renames (per pattern: `_overview.md` × N, `results.md` × N, `data.md` × N, other × N).
- Count of paper notes fixed for `domain:` frontmatter mismatch.
- Confirmation that `/research` skill workflow is updated.
- Resumption status of MOC pass (which MOCs are done, which remain).
