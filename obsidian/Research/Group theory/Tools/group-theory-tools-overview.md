---
title: "Tools — Decision Tree and Directory Map"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - convention
  - status/draft
---

# Tools — Decision Tree and Directory Map

## Which tool for which task?

| Task | Tool | Command |
|---|---|---|
| Compute |G| (finite group) | GAP | `Order(G)` |
| Test if a word equals identity (small group) | GAP | `IsOne(word in FreeGroup / NormalClosure)` |
| Test if a word equals identity (large group) | KBMAG (`kbprog`) | KB completion then reduce |
| Enumerate cosets of a subgroup | GAP | `CosetTable(G, H)` |
| Compute a confluent rewriting system | KBMAG (`kbprog`) | `kbprog -wr <groupfile>` |
| Compute automatic structure | KBMAG (`autgroup`) | `autgroup <groupfile>` |
| Work with KBMAG package from within GAP | GAP + kbmag package | `KnuthBendix(rws)` |
| Present a quotient group | GAP | `NilpotentQuotient(G, n)` |
| List subgroups of a finite group | GAP | `AllSubgroups(G)` |

## GAP installation

Available at: `/opt/homebrew/bin/gap` (version 4.15.1 as of 2026-05-28).

## KBMAG binaries (standalone)

The repo has two standalone `kbprog` builds:
- `kbmag_v1/standalone/bin/kbprog` — primary build used in experiments
- `kbmag_source/standalone/bin/kbprog` — source build

Both are equivalent. Docs: use `kbprog -help`.

## Directory map

| Subdir | Contents |
|---|---|
| `GAP/` | GAP-specific notes: overview, package-kbmag.md, examples/ (runnable snippets) |
| `KBMAG/` | KBMAG standalone: overview, file-formats.md (.rws format), examples/ (runnable snippets) |

## Content status

Tool overviews, examples, and file formats are populated in F6.2 (includes actually running each example and capturing verbatim output).

## Related material

- [[group-theory-overview]] — parent: Research/Group theory/ directory map
- [[gap-overview]] — GAP-specific overview and function reference
- [[kbmag-tools-overview]] — KBMAG standalone overview and binary locations
- [[_moc-knuth-bendix]] — KB completion MOC (KBMAG is the primary implementation)
- [[_moc-presentations-and-orders]] — presentations/orders MOC (GAP's core use case)
- [[_moc-word-problem]] — word problem MOC (both tools serve word-problem decisions)
