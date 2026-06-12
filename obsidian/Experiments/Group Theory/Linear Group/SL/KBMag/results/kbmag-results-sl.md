---
title: KBMag results — SL(n,q)
domain: group-theory
project: sl-family
instance: SL(n,q)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, topic/knuth-bendix, topic/kbmag, project/sl-family, status/validated, results]
---

# Results — KBMag on SL(n,q)

## Results table

All runs use RPO ordering (`-rec`), cn=100000. Completed = kbprog reached confluence. Timing from `sl_bidir.py` docstring where available; disk artifact sizes from forensic inventory. Dates unknown (driver script not preserved).

| Run ID | Instance | Group order | Outcome | Wall-clock (solo RPO) | Final rules (approx.) | .reduce size | Validated by |
|---|---|---|---|---|---|---|---|
| sl35-kbmag | SL(3,5) | 372,000 | **Completed** | **3.4s** | ~454 | 22.6KB | kbmag_v1 conf_check |
| sl52-kbmag | SL(5,2) | — | **Completed** | **0.3s** | ~379 | 20.7KB | kbmag_v1 conf_check |
| sl43-kbmag | SL(4,3) | 12,130,560 | **Completed** | **2.2s** | ~621 | 53.2KB | kbmag_v1 conf_check |
| sl53-kbmag | SL(5,3) | — | **Completed** | **80.5s** | ~3,429 | 389.3KB | kbmag_v1 conf_check |
| sl37-kbmag | SL(3,7) | ~1.9M | **Completed** | — | — | 62.0KB | kbmag_v1 conf_check |
| sl44-kbmag | SL(4,4) | — | **Completed** | — | — | 245.0KB | kbmag_v1 conf_check |
| sl62-kbmag | SL(6,2) | — | **Completed** | — | — | 82.1KB | kbmag_v1 conf_check |
| sl72-kbmag | SL(7,2) | — | **Completed** | — | — | 291.3KB | kbmag_v1 conf_check |
| sl311-kbmag | SL(3,11) | 212,427,600 | **Completed** | — | — | **82.6MB** | kbmag_v1 conf_check |
| sl45-kbmag | SL(4,5) | — | **Incomplete** | — | — | — (only .live: 2.9MB) | None |

**Wall-clock data gap**: timing recorded only for 4 instances where `sl_bidir.py` docstring has baseline data. The remaining 5 completed instances have artifact sizes but no recorded timing.

## Scaling analysis

From the 4 timed instances:

| Instance | Order | Time | Rules |
|---|---|---|---|
| SL(5,2) | — | 0.3s | 379 |
| SL(4,3) | 12.1M | 2.2s | 621 |
| SL(3,5) | 372k | 3.4s | 454 |
| SL(5,3) | — | 80.5s | 3,429 |

KB completion time does not correlate simply with group order. SL(5,3) takes 80.5s (37× slower than SL(4,3)) despite both being n=5 or n=4 cases. The field size q appears to dominate: SL(5,2) (q=2) converges in 0.3s while SL(5,3) (q=3) takes 80.5s.

SL(3,11): 212M-order group, `.reduce` file is 82.6MB — substantially larger than the others. KB termination confirmed. Timing not recorded.

## Version history

All runs appear to be a single-pass standalone KB completion (RPO ordering). No versions or parameter variants found. No mixing experiment exists for the SL family (sl_bidir.py experiments have no output on disk yet).

## Main findings

1. **All 9 tested instances complete**: KB terminates for every SL(n,q) tested. SL groups are finite and Steinberg presentations are effective for KB completion.

2. **Field size q drives cost more than n**: SL(5,2) (0.3s) vs SL(5,3) (80.5s) — changing q from 2 to 3 adds 2 orders of magnitude in time.

3. **sl311 largest artifact** (SL(3,11), order 212M): `.reduce` file is 82.6MB, committed to git. The KB run completed but the artifact is a large committed file that should be gitignored (W3 spec).

4. **sl45 incomplete**: Only `.kbprog.live` (2.9MB) committed — KB run was interrupted before completion. No timing or final rule count.

## Open questions

1. What is the completion time for sl311? The 82.6MB `.reduce` suggests many rules; the timing was not recorded.
2. What happened to sl45? The incomplete KB run suggests the run was killed (perhaps due to resource limits with SL(4,5)).
3. Do the sl_bidir.py bidirectional experiments improve on the standalone KB times? No output runs exist yet to compare.

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[SL/_progress]] — SL family umbrella
- [[data/kbmag-data-sl]] — per-instance artifact sizes
- [[methodology/kbmag-sl-completion-2026-06-03]] — methodology, Steinberg presentation structure
- [[kbmag-tools-overview]] — KBMAG tool
- [[B43/KBMag/results/kbmag-results-b43]] — B(4,3) results (Burnside group; finite; converges with mixing)
- [[2026-06-02-non-b25-forensic-inventory]] — §7 forensic provenance
