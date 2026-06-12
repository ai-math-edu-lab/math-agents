---
title: KBMag KB completion on SL(n,q)
domain: group-theory
project: sl-family
instance: SL(n,q)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-03
author: maumayma
git_sha_or_local: local (tracking not retrofitted)
experiment_id: sl-kbmag-completion
wall_time_s: null (range 0.3s–80.5s across instances; see results table)
params_kbmag_ordering_rpo: true
params_kbmag_cn: 100000
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, topic/knuth-bendix, topic/kbmag, project/sl-family, status/validated, methodology]
---

# Experiment — KBMag Standalone Completion on SL(n,q)

## Reconstruction notes

Reconstructed 2026-06-03 from: presentation files in `experiments/_inputs/kbmag/sl{n}{q}`, completed KB artifacts in `kbmag_v1/standalone/kb_data/sl*`, and the `sl_bidir.py` docstring (which records baseline RPO solo times for SL(3,5), SL(5,2), SL(4,3), SL(5,3)). No driver scripts for the standalone KB completion runs were found on disk — these runs may have been done manually or via deleted scripts. Dates unknown.

## What this experiment type is

Knuth-Bendix completion of SL(n,q) groups using their Steinberg presentations. The **Steinberg presentation** of SL(n,q) uses n(n-1) generators — one for each off-diagonal position e_{ij} in an n×n matrix — with Chevalley-Steinberg relations:
- `e_{ij}^q = 1` (each generator has order q = field size)
- `[e_{ij}, e_{kl}] = e_{il}` if j=k (and related commutator relations)

For SL(3,q) this gives 6 generators; for SL(4,q), 12 generators; for SL(n,q), n(n-1) generators.

KB completion terminates for SL(n,q) because these groups are finite — the confluent rule system is finite and deterministically computable. The experiment measures how long KB takes to terminate and how large the final system is.

## Why we ran this

SL(n,q) groups provide a benchmark for the KBMAG tool:
1. **Known-finite baseline**: unlike Burnside groups (open finiteness questions), SL(n,q) always terminates — useful for validating the KB setup
2. **Scalability benchmark**: how does KB completion time grow as group order grows? (sl35 order=372k in 3.4s; sl53 order~50M in 80.5s)
3. **Rule bank source**: the completed rule banks can serve as input to word-reduction experiments (`sl_bidir.py`)

## Presentations

All presentations use RPO ordering (`ordering := "recursive"`) with cn=100000.

| File | Group | Generators | Order | Relators |
|---|---|---|---|---|
| `sl35` | SL(3,5) | 6 (e_{ij}) | 372,000 | 18 |
| `sl37` | SL(3,7) | 6 | ~1.9M | 18 |
| `sl43` | SL(4,3) | 12 | 12,130,560 | ~48 |
| `sl44` | SL(4,4) | 12 | — | — |
| `sl45` | SL(4,5) | 12 | — | — |
| `sl52` | SL(5,2) | 20 | — | — |
| `sl53` | SL(5,3) | 20 | — | ~100 |
| `sl62` | SL(6,2) | 30 | — | — |
| `sl72` | SL(7,2) | 42 | — | — |
| `sl311` | SL(3,11) | 6 | 212,427,600 | 18 |

## Termination criteria

- kbprog reports `System is confluent` (always achievable for finite groups)

## Baselines (from sl_bidir.py docstring — RPO solo runs)

| Instance | Time | Rules |
|---|---|---|
| SL(3,5) | 3.4s | 454 rules |
| SL(5,2) | 0.3s | 379 rules |
| SL(4,3) | 2.2s | 621 rules |
| SL(5,3) | 80.5s | 3,429 rules |

## Validation

- kbprog internal confluence check confirms the final system
- For SL(3,5): independently verifiable via GAP (`Size(SL(3,5)) = 372000`, group order matches)
- Validation: **kbmag_v1 confluence check** (internal); for math claims, GAP order verification

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[SL/_progress]] — SL family umbrella
- [[data/kbmag-data-sl]] — per-instance artifact sizes and locations
- [[results/kbmag-results-sl]] — completion table
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §7 forensic provenance
