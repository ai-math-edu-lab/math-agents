---
title: SL(n,q) experiment progress
domain: group-theory
project: sl-family
instance: SL(n,q)
status: validated
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, project/sl-family, status/validated, experiment]
---

# SL(n,q) Experiments — Progress

**SL(n,q)**: special linear groups over finite fields GF(q), presented via Steinberg generators (elementary matrices e_{ij}(t)). All instances are **known finite**. Experiments test KB completion timing and the bidirectional word-reduction approach on these groups.

Presentations from `experiments/_inputs/kbmag/sl{n}{q}`. File naming: `sl35` = SL(3,5), `sl43` = SL(4,3), `sl311` = SL(3,11), etc.

## Experiment types

- [[SL/KBMag/_type|KBMag]] — KB completion (RPO). Confirmed complete for 9 instances (sl35 through sl72); sl45 incomplete. sl311 has the largest reduce file (82.6MB). Status: `#status/validated` for completed instances.
- [[SL/Bidirectional Search/_type|Bidirectional Search]] — `sl_bidir.py` framework using RPO + greedy word reducers. No output runs on disk yet. Status: `#status/pending`.

## Instance table

| Instance | Group | Order | KB status | Reduce file |
|---|---|---|---|---|
| sl35 | SL(3,5) | 372,000 | Completed | 22.6KB |
| sl37 | SL(3,7) | ~1.9M | Completed | 62.0KB |
| sl43 | SL(4,3) | 12,130,560 | Completed | 53.2KB |
| sl44 | SL(4,4) | — | Completed | 245.0KB |
| sl45 | SL(4,5) | — | **Incomplete** | — (only .live) |
| sl52 | SL(5,2) | — | Completed | 20.7KB |
| sl53 | SL(5,3) | — | Completed | 389.3KB |
| sl62 | SL(6,2) | — | Completed | 82.1KB |
| sl72 | SL(7,2) | — | Completed | 291.3KB |
| sl311 | SL(3,11) | 212,427,600 | Completed | **82.6MB** (committed) |

## Related material

- [[kbmag-tools-overview]] — KBMAG tool
- [[B43/_progress]] — B(4,3) (Burnside group; different KB convergence story)
- [[2026-06-02-non-b25-forensic-inventory]] — §7 covers SL* forensic provenance
