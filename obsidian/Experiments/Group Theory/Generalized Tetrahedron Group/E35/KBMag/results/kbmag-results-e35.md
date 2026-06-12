---
title: KBMag results — E35
domain: group-theory
project: e35
instance: E35
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/generalized-tetrahedron-group, topic/knuth-bendix, topic/kbmag, topic/mixer, project/e35, status/inconclusive, results]
---

# Results — KBMag on E35

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | RPO rules at end | Shortlex rules | Validated by |
|---|---|---|---|---|---|---|---|
| e35-mix-2026-03 | 2026-03-03 | threshold=100k, batch_frac=0.001, periodic=600s, cn=5000 | **Inconclusive — user interrupt at 2087s** | 2087s | ~1,180,332 | ~1,760,000 | None |

## Trajectory

| Time | RPO rules | Shortlex rules | Phase | Events |
|---|---|---|---|---|
| t=10s | threshold | — | — | First injection |
| t=1988s | 1,167,039 | 1,738,606 | EXPLORATION (471) | Ongoing |
| t=2056s | 1,175,104 | 1,749,284 | EXPLORATION (474) | — |
| t=2087s | ~1,180,332 | ~1,760,000 | EXPLORATION | **Interrupted** |

Both agents growing continuously at ~250–280 rules/s (RPO) and ~330–380 rules/s (shortlex) at interrupt. No cascade detected; no PLATEAU phase reached (unlike B(5,3) which at least reached PLATEAU by 97h).

## Comparison to B53

B(5,3) at 2087s: RPO ~650k, shortlex ~1.2M (estimate from 97h trajectory). E35 appears to generate rules faster than B(5,3) in the first 35 min. Whether this is because E35 is more complex or because the presentations have different densities is unknown.

At 97h, B(5,3) had 11.7M RPO rules in PLATEAU. E35 at 2087s (35 min) already has 1.18M RPO rules in EXPLORATION. Whether E35 would reach PLATEAU under longer runs is unknown.

## Version history

**e35-mix-2026-03**: Only run. Interrupted at 35 min. No comparison run found.

## Main findings

1. **No convergence in 35 min**: E35 does not respond to overlap-scored mixing with any cascade in the time observed.

2. **Both agents in sustained EXPLORATION**: Unlike B(5,3) which reached PLATEAU at 97h, E35 at 35 min shows no growth deceleration. The rule generation rate is roughly constant.

3. **Finiteness remains open**: KB termination is a sufficient condition for finiteness. No KB termination was observed; this does not settle the finiteness question (KB non-termination in finite time ≠ group is infinite).

4. **487 → 2333 contrast**: B(4,3) converges at 2333 rules after a cascade. E35 at the same elapsed time has 500× more rules and no cascade. The problem is structurally different.

## Open questions

1. Would a longer run (10h+) reach PLATEAU like B(5,3), or keep growing?
2. Is there a presentation of E35 (rewriting the relators, different generator ordering) that is more KB-amenable?
3. Is there a published theoretical result bounding whether KB can terminate for generalized tetrahedron groups?

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[E35/_progress]] — E35 umbrella
- [[data/kbmag-data-e35]] — presentation, run location
- [[methodology/kbmag-overlap-scoring-e35-2026-06-03]] — methodology
- [[kbmag-tools-overview]] — KBMAG tool
- [[B53/KBMag/results/kbmag-results-b53]] — B(5,3) KBMag results (PLATEAU at 97h; structural comparison)
- [[2026-06-02-non-b25-forensic-inventory]] — §5 forensic provenance
