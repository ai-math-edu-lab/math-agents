---
tags: [agent/lead, user/maumayma, domain/cs, topic/vault-tooling, topic/naming-convention, status/draft]
author: maumayma
project: mixer-core
audience: Developer
brief_date: 2026-05-28
---

# Brief — Apply F7.1 naming convention to Architecture/ `_overview.md` files

Sender: Lead.
Recipient: Developer.
Context: Researcher completed Phase 7 (naming convention + duplicate-filename cleanup) across `Research/` and `Experiments/`. They correctly flagged `Architecture/` as outside their write scope.

## What to do

Three files in `Architecture/Mixer/Components/` violate the new F7.1 naming convention (`_overview.md` is now deprecated per [[naming-conventions]] § Rule 4):

1. `Architecture/Mixer/Components/KBMag/_overview.md` → rename to `kbmag-overview.md`
2. `Architecture/Mixer/Components/Mixer Core/_overview.md` → rename to `mixer-core-overview.md`
3. `Architecture/Mixer/Components/UI/_overview.md` → rename to `ui-overview.md`

(Lowercase-kebab-case per Rule 3. Subject prefix per Rule 5 — generic `overview.md` always qualified.)

## Wikilink update step (mandatory)

Researcher flagged that component notes in `Architecture/Mixer/Components/` use bare `[[_overview]]` wikilinks to reference these files. After rename, all such wikilinks need updating to the new filenames.

```sh
# Find all wikilinks to _overview from within Architecture/
rg -n '\[\[_overview\]\]|\[\[KBMag/_overview\]\]|\[\[Mixer Core/_overview\]\]|\[\[UI/_overview\]\]' /Users/maumayma/Documents/Obsidian/Math/Architecture/

# Plus any deeper-path variants
rg -n '_overview' /Users/maumayma/Documents/Obsidian/Math/Architecture/
```

Update each match to point at the new filename. **Context-sensitive** — `[[_overview]]` in a KBMag component note resolves to `KBMag/_overview.md` (by Obsidian's nearest-folder resolution), so the rename target depends on which dir the wikilink lives in.

## Reference doctrine

- [[naming-conventions]] — `_meta/naming-conventions.md` — the rules Researcher encoded in F7.1.
- [[research-folder-convention]] — `_meta/research-folder-convention.md` — has the appended naming section.

Both are also concise enough to read in one pass.

## Out of scope

- `_meta/agents/*.md` doctrine files (path-qualified per [[naming-conventions]] § Rule 2).
- `Agents/<user>/<role>/log.md` and README.md files (same — path-qualified).
- Other `Architecture/` notes that don't have generic-filename violations.
- Touching Researcher's renames (already done).

## Deliverable

- 3 renames completed.
- Wikilink updates per file (count of grep matches resolved).
- Confirmation in `Agents/maumayma/Developer/scratch/` or via `maestri ask` REPORT to Lead.

## K3 review

Light-touch — purely naming/wikilink, no behavior change, no tests required. Lead reviews on receipt.
