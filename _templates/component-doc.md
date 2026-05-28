---
title: <component name>
location: <repo path, e.g. mixer-core/src/scheduler/mod.rs OR experiments/burnside/>
domain: <group-theory | ai | cs | methodology>
hot_path: false                    # true if on mission.md's hot-paths list
status: production                 # production | paper | deprecated | draft
public_api:
  - "TypeName (path:LINE) — one-line role"
  - "function_name() (path:LINE) — one-line role"
invariants:
  - id: kebab-case-id
    summary: "One-sentence statement of the invariant"
    why: "What bug it prevents, what failure it encodes, or what design constraint it satisfies"
related: [mixer-core, scheduler]   # bare names of other Components/ notes
tests:
  unit: <path or "none">
  integration: <path or "none — argued in `[[<review>]]`">
known_issues:
  - "<issue 1, one line>"
tags: [agent/dev, user/<handle>, domain/<one>, topic/<one+>, status/<production|paper|deprecated>]
---

# <Component name> — <one-line tagline a human would understand>

## What it is

<One paragraph, 2-4 sentences. Plain English.>

## Why it exists

<One paragraph. The problem this solves or the design constraint it satisfies. If history matters, say so.>

## How it fits in the system

<2-4 sentences or a tiny ASCII flow. Wikilinks to neighbors.>

## Critical invariants — why each one exists

For each invariant in frontmatter, write a short narrative paragraph here.

### <invariant-id-from-frontmatter>
<2-4 sentences on why this matters, with concrete examples or past failures.>

## Public surface — what other components touch

The most common entry points:
- `<Type::method()>` — <plain English>

For the full type-and-line index, see frontmatter `public_api` or the upstream code.

## Hot path?

<One sentence.>

## Tests

<Short paragraph naming files and coverage. Machine-readable paths in frontmatter `tests`.>

## Related

- `[[<sibling>]]` — <how they interact>
- `[[<linked decision note>]]`

## Recent changes

- <YYYY-MM-DD> `<branch>` — <one-line summary> — `[[<review note>]]`
