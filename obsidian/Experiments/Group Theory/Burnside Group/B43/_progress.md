---
title: B(4,3) experiment progress
domain: group-theory
project: b43
instance: B(4,3)
status: validated
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b43, project/b43, status/validated, experiment]
---

# B(4,3) Experiments — Progress

The **free Burnside group B(4,3)**: free group on 4 generators, exponent 3 (every element has order dividing 3). Finite; its order is 3^29. KB completion terminates here (unlike B(2,5) where it is an open question).

## Active experiment types

- [[B43/KBMag/_type|KBMag]] — KB completion + overlap-scored mixer. **Flagship result**: v10d injection (80 rules, threshold 20k) produces a rule-cascade that reduces convergence time from ~22s (baseline) to ~13.7s (cascade phase).

## Results summary

| Experiment | Status | Key metric | Date |
|---|---|---|---|
| KBMag baseline | `#status/validated` | 22.0s ±0.1s cascade; total ~91s | 2026-03-07 |
| KBMag v10d (b80_at20k) | `#status/validated` | 13.7s ±0.1s cascade; total ~96s | 2026-03-07 |

## Related material

- [[B25/_progress]] — B(2,5) sister experiments; same KBMAG toolchain
- [[B53/_progress]] — B(5,3) experiments; analogous mixing program
- [[kbmag-tools-overview]] — KBMAG tool used in all KB runs
- [[2026-06-02-non-b25-forensic-inventory]] — forensic provenance inventory; §1 covers B43 runs
