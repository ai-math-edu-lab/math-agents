---
title: E35 experiment progress
domain: group-theory
project: e35
instance: E35
status: inconclusive
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/generalized-tetrahedron-group, project/e35, status/inconclusive, experiment]
---

# E35 Experiments — Progress

**E35** (Rosenberger-Scheer notation): generalized tetrahedron group
`E35 = <a, b, c | a² = b³ = c³ = (ac)² = (bc)² = (abababab²abab²ab²)² = 1>`

3 generators: a (order 2), b (order 3), c (order 3). **Finiteness is OPEN** — one of 5 unsettled cases in the Rosenberger-Scheer classification of generalized tetrahedron groups.

Source file: `experiments/_inputs/kbmag/e35` (652 bytes, 6 equations).

## Active experiment types

- [[E35/KBMag/_type|KBMag]] — overlap-scored RPO+shortlex mixing. Run for 2087s; RPO reached 1.18M rules, shortlex 1.76M; **user-interrupted, not converged**. Status: inconclusive.

## Results summary

| Experiment | Status | Key metric | Date |
|---|---|---|---|
| KBMag overlap-scored mixing | `#status/inconclusive` | RPO=1.18M, shortlex=1.76M at 2087s (476 injections); interrupted | 2026-03-03 |

## Related material

- [[B43/_progress]] — B(4,3) (converges; contrast)
- [[B53/_progress]] — B(5,3) (open question; methodological parallel)
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §5 covers E35 forensic provenance
