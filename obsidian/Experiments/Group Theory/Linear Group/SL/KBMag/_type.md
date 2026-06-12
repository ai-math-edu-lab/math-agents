---
title: KBMag on SL(n,q)
domain: group-theory
project: sl-family
instance: SL(n,q)
experiment_type: kbmag
status: validated
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, topic/knuth-bendix, topic/kbmag, project/sl-family, status/validated, experiment-type]
---

# KBMag on SL(n,q)

KB completion of SL(n,q) groups using the Steinberg presentation and KBMAG's RPO ordering. All 9 completed instances converge to a confluent system (SL(n,q) is finite; KB completion terminates for finite groups given sufficient resources). The runs in `kb_data/` are standalone RPO completions — no mixing was applied to the SL family.

## Experiment subtree

- [[methodology/kbmag-sl-completion-2026-06-03|Methodology]] — presentation structure, Steinberg generators, KB convergence
- [[data/kbmag-data-sl|Data]] — per-instance files, completed run artifacts
- [[results/kbmag-results-sl|Results]] — completion table for all SL instances

## Related material

- [[SL/_progress]] — SL family umbrella
- [[kbmag-tools-overview]] — KBMAG tool
- [[Bidirectional Search/_type]] — sl_bidir.py approach (word reduction, separate)
