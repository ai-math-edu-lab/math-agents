---
title: Bidirectional Search on SL(n,q)
domain: group-theory
project: sl-family
instance: SL(n,q)
experiment_type: bidirectional
status: pending
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/sl-steinberg, topic/bidirectional, topic/knuth-bendix, project/sl-family, status/pending, experiment-type]
---

# Bidirectional Search on SL(n,q)

RPO KB + greedy word reducers approach applied to SL(n,q) target words, implemented in `experiments/sl/experiments/sl_bidir.py`. If all target words reduce to identity under the accumulated rule banks, the group is proven finite (already known for SL(n,q), but the experiment benchmarks the word-reduction approach vs. standalone KB completion).

## Status

**Pending** — `sl_bidir.py` is on disk (27KB Python script); target word files exist in `experiments/sl/target/`; no output run directories on disk.

## Driver

- `experiments/sl/experiments/sl_bidir.py` — supports groups: sl35, sl52, sl43, sl53 (from docstring)
- `experiments/sl/experiments/run_sweep.sh` — sweep runner
- `experiments/sl/reducer_agent.py` — reducer

## Documented baseline timings (from sl_bidir.py docstring)

| Group | RPO solo time | RPO rules |
|---|---|---|
| SL(3,5) | 3.4s | 454 |
| SL(5,2) | 0.3s | 379 |
| SL(4,3) | 2.2s | 621 |
| SL(5,3) | 80.5s | 3,429 |

## Related material

- [[SL/_progress]] — SL family umbrella
- [[KBMag/_type]] — KBMag standalone completion (separate approach)
- [[B53/Rust Bidirectional/_type]] — B(5,3) bidirectional (analogous methodology)
