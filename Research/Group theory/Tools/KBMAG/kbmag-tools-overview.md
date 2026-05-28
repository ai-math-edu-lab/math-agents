---
title: "KBMAG — Overview"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/kbmag
  - convention
  - status/draft
---

# KBMAG — Overview

**KBMAG** (Knuth-Bendix on Monoids and Groups) is a standalone implementation of Knuth-Bendix completion for finitely presented groups and monoids. In this repository: two builds in `kbmag_v1/standalone/bin/kbprog` and `kbmag_source/standalone/bin/kbprog`.

KBMAG is also available as a GAP package (`LoadPackage("kbmag")`) — see `Tools/GAP/package-kbmag.md`.

## Directory contents

| File/Dir | Description |
|---|---|
| `file-formats.md` | `.rws` file format for group/monoid input; `kbprog` flag reference |
| `examples/` | Runnable snippets for specific tasks; one per file; with verbatim output |

## Primary executables

| Binary | Purpose |
|---|---|
| `kbprog` | Knuth-Bendix completion; produces a rewriting system |
| `autgroup` | Automatic groups: computes the automatic structure (word acceptor, multiplier automata) |

## Key flags for kbprog

```
kbprog -wr <file>          # "word reduce" mode: complete and print rules
kbprog -ro <file>          # compute reduction ordering only
kbprog -sw <file>          # read from first word line (for single word problems)
kbprog -cn <n>             # max rules before stopping (default 32768)
kbprog -ml <n>             # max LHS length
```

Full flag list: `kbprog -help` or `kbmag_v1/standalone/bin/kbprog -help`.

## Status

File formats and examples populated in F6.2 (with verified output from actual runs).

## Related material

- [[group-theory-tools-overview]] — parent: decision tree for which tool for which task
- [[_moc-knuth-bendix]] — the KB MOC; KBMAG is the primary KB tool for large groups
- [[file-formats]] — .kbprog format and kbprog flag reference
- [[01-s3-shortlex]] — verified example: confluent system for S3 (8 rules)
- [[02-b23-shortlex]] — verified example: confluent system for B(2,3) (26 rules)
- [[knuth-bendix]] — foundational technique note: what KB does and when it terminates
- [[gap-overview]] — GAP alternative: kbmag can also run inside GAP
