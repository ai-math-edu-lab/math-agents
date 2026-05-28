---
title: KBMag B(2,5) Data
domain: group-theory
project: b25
experiment_type: kbmag
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, project/b25, status/inconclusive, data]
---

# KBMag B(2,5) — Data

## Input presentation

File: `kbmag_v1/standalone/kb_data/b25_full`

B(2,5) presentation: 2 generators {a, b}, exponent 5. The `b25_full` file contains 59 equations encoding `a^5 = b^5 = 1` plus all commutator-based relators up to weight 5 in the Hall-Wiegold basis. This is the standard computational presentation for B(2,5) used in the KBMAG literature.

Inverse expansion for mixing scripts: uppercase letters stand for inverses (A = a⁻¹ = a⁴, B = b⁻¹ = b⁴). Expansion rule: `A → aaaa`, `B → bbbb`. Applied to shortlex rules before injection to make all rules work over the lowercase {a,b} alphabet that RPO uses.

Note: `kbmag_source/` (a second kbmag copy) is unused. `kbmag_debug/` was deleted.

## Scripts

| Script | Location | Description |
|--------|----------|-------------|
| b25_mix.py (v1) | `experiments/burnside/b25_kbmag/b25_mix.py` | RPO+shortlex mixing, Aho-Corasick scoring |
| b25_mix_v2.py | `experiments/burnside/b25_kbmag/b25_mix_v2.py` | Same strategy, bisect+cached-prep (10x less memory, 15x faster injection) |
| bench_v3.py | `experiments/burnside/b25_kbmag/bench_v3.py` | Synthetic benchmark comparing v1 vs v2 at 13M RPO/25M slex scale |
| standalone.py | `experiments/burnside/b25_kbmag/standalone.py` | Single-agent baseline (RPO or shortlex only) |

## Constants

| Parameter | Value | Note |
|-----------|-------|------|
| Generators | a, b | |
| Exponent | 5 | |
| RPO confnum | 5,000 | tidy interval |
| Shortlex confnum | 5,000 | tidy interval |
| tidyint | 5,000 | |
| maxeqns | unlimited | set to 10^9 effectively |
| maxstates | unlimited | |
| STATUS_INTERVAL | 60s | logging cadence |

## Surviving run logs

- `experiments/burnside/b25_kbmag/server_logs/b25_scoring.log` — server run log (b25_mix.py, threshold=20k, ~30min of data starting 06:00:01). Hostname: `/home/maria/algo_mixing/` (remote server).
- KB rule banks: `runs/b25/20260320_054109/`, `runs/b25/20260320_054957/`, `runs/b25/20260320_055128/`, `runs/b25/20260320_055557/`, `runs/b25/20260320_065252/`, `runs/b25/20260320_065653/` — these may contain rule `.live` files for each ordering.

Note: `runs/b25/` is in the repository root, not under `experiments/`.

## Related material

- [[KBMag/_type|KBMag on B(2,5)]] — parent experiment-type description (what this technique is and why we ran it)
- [[_progress|B(2,5) Progress Note]] — umbrella standing progress note for all B25 work
- [[kbmag-results]] — sibling results table for this experiment type
- [[kbmag-overlap-scoring-b25-2026-05-22]] — methodology note for the overlap-scored mixing run that produced these rule banks
- [[kbmag-tools-overview]] — KBMAG tool reference; `kbprog` binary and input format documented here
- [[havas-wall-wamsley-1974]] — source of the `b25_full` presentation file (59 equations) that `kbprog` reads as input for all runs listed above
