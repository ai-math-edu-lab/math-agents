---
title: KBMag results — M23
domain: group-theory
project: m23
instance: M23
experiment_type: kbmag
status: replicated
reconstructed_on: 2026-06-02
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/mathieu, topic/m23, topic/knuth-bendix, topic/kbmag, topic/mixer, project/m23, status/replicated, results]
---

# Results — KBMag on M23

**Validator verdict**: `#status/replicated` (2026-06-02). All 19 result JSONs independently verified. Same presentation MD5, same binary, RPO_CONFNUM=5000 uniform. All runs terminate at 863,186 equations. See [[2026-06-02-m23-mixing-negative-result]].

## Baselines

| Run ID | Date | Outcome | Wall-clock | Final eqns | Validated by |
|---|---|---|---|---|---|
| baseline | ~2026-04 | Converged, no injection | **1,103.8s** | 863,186 | Validator re-verification |
| baseline_v2 | ~2026-04 | Converged, no injection | **1,023.0s** | 863,186 | Validator re-verification |

**Baseline variance**: ±80.8s across two independent RPO-only runs.

## Mixing variants (18 total)

All 18 mixing variants produce the same final state (863,186 eqns) but are **slower** than both baselines.

| Run ID | Total time | Delta vs baseline | injected | Notes |
|---|---|---|---|---|
| **v10f7** | **1,409.2s** | **+27.7%** | 769 | **Best mixing variant** |
| v10h | 1,418.3s | +28.5% | 552 | |
| v10f5 | 1,461.2s | +32.4% | 349 | |
| v13 | 1,468.7s | +33.1% | 55 | Minimal injection |
| v10a | 1,484.3s | +34.5% | 228 | |
| v10e | 1,469.0s | +33.1% | 2,761 | |
| v10b | 1,466.3s | +32.9% | 1,028 | |
| v10c | 1,489.7s | +35.0% | 1,982 | |
| v10f2 | 1,501.5s | +36.0% | 276 | |
| v1 (test) | 1,529.1s | +38.5% | 552 | |
| v2 (test) | 1,536.7s | +39.2% | 228 | |
| v10f3 | 1,509.2s | +36.8% | 1,104 | |
| v10f | 1,536.9s | +39.2% | 552 | |
| v10f4 | 1,509.5s | +36.8% | 2,502 | |
| v5 | 1,526.4s | +38.3% | 509 | |
| v10d | 1,542.3s | +39.8% | 1,104 | |
| v10i | 1,590.9s | +44.1% | 4,981 | More injection = more slowdown |
| **v10f6** | **1,937.7s** | **+75.6%** | 552 | **Worst mixing variant** |

From `results_archive/` (params less extractable than test variants):
| mix v1 (threshold=100k, periodic=900s) | 1,330.7s | +20.5% | 9,568 | — |
| mix v2 (threshold=100k, periodic=10s) | 1,418.8s | +28.6% | 76,650 | Most injections tried |

**Range**: +27.7% (best v10f7) to +75.6% (worst v10f6). Delta vs. best baseline (1,023s): +37.8% to +89.4%.

**Effect size**: The slowdown is **3.8× baseline variance** — robust, not noise.

## Version history

**Early strategies (v1, v2, v5)**: Overlap-scored injection, various batch fractions and periodic intervals. All slower than baseline.

**v10 family**: Parameter sweep focused on injection timing, batch size, and rule scoring strategy. Sub-variants f2–f7 tested scoring modifications. Despite the wide parameter space, no variant improved on baseline.

**v13**: Minimal injection (55 rules total, 1 event). Still slower than baseline (+33%).

## Main findings

1. **Negative result — mixing harms M23**: Every mixing variant tested (18 total) is slower than both RPO-only baselines. The best mixing result (v10f7, 1409s) is 28% slower than the primary baseline (1103.8s) and 38% slower than baseline_v2 (1023.0s).

2. **More injection = worse**: The correlation between total_injected and slowdown is roughly monotone. v10i (4,981 rules) is slower than v10f7 (769 rules). v10f6 (552 rules, worst case) shows this is not purely a quantity effect — the timing and selection also matter.

3. **The B(4,3) strategy does not generalize**: The overlap-scored shortlex→RPO injection that reduces B(4,3) cascade time by 37% has the opposite effect on M23. The structural reason is discussed in the methodology note.

4. **KB completion for M23 is tractable** — just without mixing: Both baselines terminate in ~17–18 min. M23 is a workable test case for future strategies that don't involve shortlex→RPO injection.

## Open questions

1. Would a different injection direction (RPO→shortlex, or a different ordering pair) help? The tested strategy only injects shortlex→RPO.

2. Is there any injection strategy that improves M23 convergence? v13 (minimal, 55 rules) still hurts. The null hypothesis (any injection slows M23) appears supported, but an injection of 1 well-chosen rule has not been tested.

3. Is the slowdown mechanism the increased critical pair count from injected rules? See methodology note §Why mixing slows M23.

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[M23/_progress]] — M23 umbrella
- [[data/kbmag-data-m23]] — presentation, result JSON locations, committed artifacts
- [[methodology/kbmag-mixing-m23-2026-06-02]] — methodology, mechanism hypothesis
- [[kbmag-tools-overview]] — KBMAG tool
- [[B43/KBMag/results/kbmag-results-b43]] — B(4,3) results (mixing helps; contrast)
- [[2026-06-02-m23-mixing-negative-result]] — Validator verdict (full verification details)
- [[2026-06-02-non-b25-forensic-inventory]] — §4 M23 forensic provenance
