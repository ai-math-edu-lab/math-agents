---
title: G5 experiment progress
domain: group-theory
project: g5
instance: G5
status: validated
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/g5, project/g5, status/validated, experiment]
---

# G5 Experiments — Progress

**G5**: A small group from the KBMAG standard test suite. KB completion converges to **16 equations in 0.5s** — effectively instantaneous. Used as the **seed experiment** for validating the `g_kbmag` mixing infrastructure before applying it to harder groups (G7, E35, M23, B43).

## Status

Validated (trivially). G5 converges so quickly that no injection fires before convergence. The g5_mix.py driver ran successfully; `results.json` records `confluent: true, elapsed: 0.5, total_injected: 0`.

## What exists

| Item | Location | Notes |
|---|---|---|
| Driver | `experiments/g_kbmag/g5_mix.py` | Also used for G7 (g7 input) |
| Run outputs | `experiments/g_kbmag/runs_g5_mix/` (~71MB) | Full KBMAG tree; shortlex `.reduce` (32.8MB) dominates |
| results.json | `experiments/g_kbmag/runs_g5_mix/results.json` | confluent=true, elapsed=0.5, injected=0 |
| kb_data files | `kbmag_v1/standalone/kb_data/g5` + `g5.kbprog`, `.kbprog.live`, `.reduce`, `.diff1`, `.diff2`, `.wa` | All committed; small (16 rules) |

**Note**: kbprog logs record `CWD: .../experiments/g5_kbmag/...` (old path before rename to `g_kbmag/`). The run is valid; the path in log headers is stale.

## Experiment type docs

Full triad (methodology/data/results) is deferred: G5 converges in 0.5s without any mixing intervention, making it a plumbing test rather than a research result. A single KBMag methodology note will be written when the g_kbmag pipeline is formally documented.

## Related material

- [[G7/_progress]] — G7 (harder; injection fired but run interrupted)
- [[kbmag-tools-overview]] — KBMAG tool
- [[2026-06-02-non-b25-forensic-inventory]] — §6 covers G5/G7 forensic provenance
