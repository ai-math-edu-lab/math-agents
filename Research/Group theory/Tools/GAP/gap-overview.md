---
title: "GAP — Overview"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - convention
  - status/draft
---

# GAP — Overview

**GAP** (Groups, Algorithms, Programming) is the primary computer algebra system for group theory. Installed at `/opt/homebrew/bin/gap` (version 4.15.1 as of 2026-05-28).

## Directory contents

| File/Dir | Description |
|---|---|
| `examples/` | Runnable code snippets, one task per file, with verbatim output (all examples actually run and verified) |
| `package-kbmag.md` | GAP's `kbmag` package — using Knuth-Bendix from within GAP |

## Starting GAP

```
gap
```

or for a specific file:
```
gap myscript.g
```

## Key functions (reference)

- `Order(G)` — compute |G|
- `CosetTable(G, H)` — coset enumeration (Todd-Coxeter)
- `NilpotentQuotient(G, c)` — nilpotent quotient of class c
- `FreeGroup(n)` — free group on n generators
- `ParseRelators(F, relators)` — parse relators string

## Status

Examples and package-kbmag note populated in F6.2 (with verified output).

## Related material

- [[group-theory-tools-overview]] — parent: decision tree for which tool for which task
- [[_moc-knuth-bendix]] — the KB MOC; GAP kbmag package is a primary KB tool
- [[_moc-presentations-and-orders]] — MOC covering order and coset enumeration (core GAP tasks)
- [[01-group-order]] — verified example: compute |G|
- [[02-coset-enumeration]] — verified example: enumerate cosets of a subgroup
- [[03-word-equality]] — verified example: test word equality
- [[04-exponent-subgroups]] — verified example: compute exponent and list subgroups
- [[05-kbmag-package]] — verified example: KB completion via the kbmag GAP package
- [[package-kbmag]] — full kbmag package documentation
