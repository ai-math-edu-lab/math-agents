---
title: M23 experiment progress
domain: group-theory
project: m23
instance: M23
status: replicated
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/mathieu, topic/m23, project/m23, status/replicated, experiment]
---

# M23 Experiments — Progress

The **Mathieu group M23**: one of the 26 sporadic simple groups, order 10,200,960. KB completion under RPO terminates here (863,186 equations). Mixing was tested across 18+ parameter variants.

## Active experiment types

- [[M23/KBMag/_type|KBMag]] — KB completion + overlap-scored mixing. **Key finding (`#status/replicated`)**: all 18 mixing variants are slower than the RPO-only baseline. Mixing harms M23 KB convergence.

## Results summary

| Experiment | Status | Key metric | Date |
|---|---|---|---|
| KBMag baseline | `#status/replicated` | 1,103.8s (primary) / 1,023.0s (v2) | ~2026-04 |
| KBMag mixing (18 variants) | `#status/replicated` | All slower: +28% (best v10f7) to +76% (worst v10f6) | ~2026-04 |

**Validator verdict**: `#status/replicated` — independently verified all 19 result JSONs. See [[2026-06-02-m23-mixing-negative-result]] for full verdict.

## Related material

- [[M22/_progress]] — M22 (related Mathieu group; limited data)
- [[B43/_progress]] — B(4,3) (mixing helps; contrast)
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §4 covers M23 runs
