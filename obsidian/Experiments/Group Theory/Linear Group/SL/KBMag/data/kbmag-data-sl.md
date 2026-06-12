---
title: KBMag data — SL(n,q)
domain: group-theory
project: sl-family
instance: SL(n,q)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-03
author: maumayma
params_kbmag_cn: null (varies per instance; sl35/sl311/sl37 = 100000 confirmed; others inferred same)
params_kbmag_ordering_rpo: true
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, topic/knuth-bendix, topic/kbmag, project/sl-family, status/validated, data]
---

# Data — KBMag on SL(n,q)

## Presentation files

All in `experiments/_inputs/kbmag/`. Confirmed from primary sources (file headers). RPO ordering (`ordering := "recursive"`), cn=100000.

| File | Group | Generators | Order (from header) | Relators | Size |
|---|---|---|---|---|---|
| `sl35` | SL(3,5) | 6 (e_{ij}, i≠j, 1≤i,j≤3) | 372,000 | 18 | 900B |
| `sl37` | SL(3,7) | 6 | ~1.9M (est.) | 18 | 926B |
| `sl43` | SL(4,3) | 12 (e_{ij}, 1≤i,j≤4) | 12,130,560 | ~48 | 2.2KB |
| `sl44` | SL(4,4) | 12 | — | — | 15.2KB |
| `sl45` | SL(4,5) | 12 | — | — | 2.3KB |
| `sl45_wtlex` | SL(4,5) wtlex variant | 12 | — | — | 2.4KB |
| `sl52` | SL(5,2) | 20 | — | — | 5.3KB |
| `sl53` | SL(5,3) | 20 | — | — | 5.3KB |
| `sl62` | SL(6,2) | 30 | — | — | 11.0KB |
| `sl72` | SL(7,2) | 42 | — | — | 20.7KB |
| `sl311` | SL(3,11) | 6 | 212,427,600 | 18 | 977B |

**Naming convention**: sl{n}{q} where n is the matrix dimension and q is the field size (GF(q)). For q ≥ 10, all digits after n encode q (sl311 = SL(3,11)).

## Driver scripts

- `experiments/sl/experiments/sl_bidir.py` — primary driver for bidirectional experiments (separate from standalone KB runs below)
- No driver script found for the standalone KB completion runs in `kb_data/`. These appear to have been run manually or via deleted scripts.

## Completed KB run artifacts (in `kbmag_v1/standalone/kb_data/`)

| Instance | .kbprog | .kbprog.ec | .kbprog.live | .reduce | Complete? |
|---|---|---|---|---|---|
| sl35 | 22.4KB | 16B | 11.7KB | 22.6KB | ✓ |
| sl37 | 70.7KB | 16B | 47.4KB | 62.0KB | ✓ |
| sl43 | 28.9KB | 16B | 12.6KB | 53.2KB | ✓ |
| sl44 | 145.9KB | 16B | 63.3KB | 245.0KB | ✓ |
| sl45 | — | — | **2.9MB** | — | **✗ incomplete** |
| sl52 | 13.8KB | 16B | 5.7KB | 20.7KB | ✓ |
| sl53 | 192.9KB | 16B | 83.4KB | 389.3KB | ✓ |
| sl62 | 49.0KB | 16B | 20.8KB | 82.1KB | ✓ |
| sl72 | 159.0KB | 16B | 68.3KB | 291.3KB | ✓ |
| sl311 | 27.5MB | 16B | 4.8MB | **82.6MB** | ✓ |

**sl45 note**: Only `.kbprog.live` (2.9MB) is committed; no `.kbprog` or `.reduce`. The KB run was interrupted before completion.

**sl311 note**: `.reduce` file (82.6MB) and `.kbprog` (27.5MB) are committed to git — large generated artifacts that should be gitignored per W3 spec.

## Target words for bidirectional search

The `experiments/sl/target/` directory contains target word files and mapping files for each SL instance:
- `sl*_targets.txt` — words to prove equal to identity
- `sl*_mapping.txt` — generator name mapping
- `sl*_kbprog` — copies of the presentation files

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[SL/_progress]] — SL family umbrella
- [[methodology/kbmag-sl-completion-2026-06-03]] — methodology
- [[results/kbmag-results-sl]] — completion table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §7 forensic provenance
