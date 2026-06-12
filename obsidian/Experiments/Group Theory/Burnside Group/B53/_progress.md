---
title: B(5,3) experiment progress
domain: group-theory
project: b53
instance: B(5,3)
status: inconclusive
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, project/b53, status/inconclusive, experiment]
---

# B(5,3) Experiments — Progress

The **free Burnside group B(5,3)**: free group on 5 generators, exponent 3. Finite (order = 3^2282?). Harder than B(4,3); KB convergence not yet achieved under any mixing strategy tried.

## Active experiment types

- [[B53/KBMag/_type|KBMag]] — KB completion + overlap-scored server mixing. 97h+ run reached 11.7M RPO rules, in PLATEAU, no convergence.
- [[B53/Rust Bidirectional/_type|Rust Bidirectional]] — Bidirectional KB search with 4 ordering sources + dynamic conjugation. **144/153 target words proved at 1733s** (v5); 9 hardest unsolved.

## Results summary

| Experiment | Status | Key metric | Date |
|---|---|---|---|
| KBMag v10 (97h server run) | `#status/inconclusive` | RPO=11.7M, shortlex=41.9M at 97h; PLATEAU; not converged | ~2026-04 |
| Rust Bidirectional v5 (4 orderings + dynamic conj) | `#status/inconclusive` | 144/153 words proved at 1733s; 9 remain | ~2026-03 |

## Related material

- [[B43/_progress]] — B(4,3) experiments (same methodology, converges)
- [[B25/_progress]] — B(2,5) experiments
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §2 covers B53 runs
