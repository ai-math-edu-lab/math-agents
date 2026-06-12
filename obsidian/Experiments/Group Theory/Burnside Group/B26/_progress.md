---
title: B(2,6) experiment progress
domain: group-theory
project: b26
instance: B(2,6)
status: pending
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, project/b26, status/pending, experiment]
---

# B(2,6) Experiments — Progress

The **free Burnside group B(2,6)**: free group on 2 generators of exponent 6. Finiteness is proven (Holt et al.). No KB mixing experiment exists yet.

## Status

Exploratory. The only artifact is `experiments/b26_test/nq_engel_output.log` — raw output from the ANU NQ (nilpotent quotient) program computing a class-30 quotient of B(2,6) using the 6th Engel condition. This is a presentation-derivation step (same methodology used to derive the B(2,5) presentation from NQ output), not yet a KB run.

The NQ computation was truncated at weight-10 Engel checks in the log; no final class or order output was captured.

## What exists

| Item | Location | Status |
|---|---|---|
| NQ/Engel output log | `experiments/b26_test/nq_engel_output.log` (27.8KB) | Exploratory computation; driver script missing |
| KB presentation | `experiments/_inputs/kbmag/b26` (7.2KB; 2 generators {a,A,b,B}, 116 relators; all period-6 patterns confirming B(2,6)) | Input exists — no KB run yet |
| Any KB run | None | Pending |

## Next steps

1. Complete or recover NQ computation to derive a B(2,6) KBMAG presentation
2. Run KB baseline on the presentation
3. Attempt mixer experiment

## Related material

- [[KBMag/_type]] — B(2,6) KBMag experiment-type stub (pending — no run yet)
- [[B43/_progress]] — B(4,3) (converges easily; useful calibration)
- [[B25/_progress]] — B(2,5) (harder analog; open question)
- [[2026-06-02-non-b25-forensic-inventory]] — §8 covers B26 forensic provenance
