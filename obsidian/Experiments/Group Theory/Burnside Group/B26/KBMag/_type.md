---
title: KBMag on B(2,6)
domain: group-theory
project: b26
instance: B(2,6)
experiment_type: kbmag
status: pending
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, topic/knuth-bendix, topic/kbmag, project/b26, status/pending, experiment-type]
---

# KBMag on B(2,6)

KB completion of B(2,6) using KBMAG. The presentation exists at `experiments/_inputs/kbmag/b26` (7.2KB; 2 generators {a,A,b,B}, 116 relators encoding all period-6 patterns). No KB run has been attempted yet. The only existing work is an ANU NQ computation log (`experiments/b26_test/nq_engel_output.log`) exploring the nilpotent quotient structure via the 6th Engel condition.

## Status

**Pending** — presentation exists; no KB run.

## Next steps

1. Run baseline RPO on `b26` presentation
2. Estimate convergence feasibility (B(2,6) is finite but larger than B(4,3))
3. Attempt mixer experiment if baseline converges

## Related material

- [[B26/_progress]] — B(2,6) umbrella
- [[B43/KBMag/_type]] — B(4,3) (converges; useful comparison point)
- [[kbmag-tools-overview]] — KBMAG tool
