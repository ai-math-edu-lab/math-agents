---
tags: [meta]
---

# People

Human contributors to this vault. One note per person. The vault has a human index.

## Convention

Each person gets a note `People/<handle>.md` with this shape:

```yaml
---
title: <handle or full name>
domain_focus: [group-theory, biology]      # primary domains
projects: [mixer-core, b25]                # active Mixer subprojects (or [] for none)
author: <handle>                           # this person's handle
tags: [meta, user/<handle>]
---

# <Display name>

## Who
<2-3 sentence bio. Affiliation, interests.>

## Currently working on
<What they're spending time on now.>

## Key contributions in this vault
<Wikilinks to their important notes / experiments / syntheses.>

## Contact (optional)
<email / handle if they're OK with that being in the vault>
```

## When to create a People entry

- When a new human contributor starts using the vault.
- When a colleague's first note appears in the vault (Researcher or Lead should ping the human to create a People entry).

## Authorship convention

Every note in the vault carries `author: <handle>` in frontmatter and `#user/<handle>` in tags. That handle should resolve to a `People/<handle>.md` note. If you cite a colleague's work, link `[[People/<handle>]]` alongside the note wikilink.
