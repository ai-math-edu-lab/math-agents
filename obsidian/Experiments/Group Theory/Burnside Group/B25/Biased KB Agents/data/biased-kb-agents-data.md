---
title: Biased KB Agents B(2,5) Data
domain: group-theory
project: b25
experiment_type: biased-kb-agents
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, project/b25, status/inconclusive, data]
---

# Biased KB Agents B(2,5) — Data

## Input presentation

File: `kbmag_v1/standalone/kb_data/b25_full` (or a copy thereof — run4/run5 agents read either this file directly or a copy in their run directory)

All runs use the **standard B(2,5) presentation**: 59 equations, 2 generators {a,b}, exponent 5. NOT the lifted {a,b,m} presentation. This is the same presentation used by the KBMag experiment type.

Binary: `kbmag_source/standalone/bin/kbprog` (the modified binary with `-sw`/`-sp`/`-sk` biasing extensions). NOT `kbmag_v1/standalone/bin/kbprog`.

## Target words (ALL INVALID — see invalidation note)

| File | Length (chars) | Status | Notes |
|---|---|---|---|
| `b25_bias_bidir/targets/word_3705.txt` | 3,705 | **INVALID** | Derived from buggy braid chain; different group element than [c12,c9] |
| `b25_bias_bidir/targets/word_7264.txt` | 7,264 | Uncertain | Pre-correction pipeline output; validity unclear |
| `b25_bias_bidir/targets/word_best.txt` | unknown | Uncertain | Content unknown without reading |
| `b25_bias_bidir/targets/word_coreless.txt` | unknown | Uncertain | Coreless form of some reduction |

**Valid target for future runs**: `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars, abelianization (0,0), #status/conjectured per Validator 2026-05-22)

## Rule banks (surviving)

Located at `experiments/burnside/b25_bias_bidir/rules/`.

| Directory | Ordering | sk | sp | Target | Mode | Rule count | Size | mtime |
|---|---|---|---|---|---|---|---|---|
| `3705_run4_sl_k12/` | shortlex | 12 | ~0.5 | word_3705 (INVALID) | biased | 1,798,675 | 154MB | 2026-04-06 |
| `3705_run4_sl_k16/` | shortlex | 16 | ~0.5 | word_3705 (INVALID) | biased | 633,337 | 52MB | 2026-04-06 |
| `3705_run4_sl_k20/` | shortlex | 20 | ~0.5 | word_3705 (INVALID) | biased | 434,633 | 32MB | 2026-04-06 |
| `3705_run4_rpo_k14/` | RPO | 14 | ~0.5 | word_3705 (INVALID) | biased | 1,113,892 | 93MB | 2026-04-06 |
| `3705_run4_rpo_k20/` | RPO | 20 | ~0.5 | word_3705 (INVALID) | biased | 417,447 | 32MB | 2026-04-06 |
| `3705_run4_wt_k16/` | wtlex | 16 | ~0.5 | word_3705 (INVALID) | biased | 673,675 | 66MB | 2026-04-06 |
| `3705_run5_sl_k0_sp50/` | shortlex | 0 | 0.50 | word_3705 (INVALID) | biased | 1,352,697 | 118MB | 2026-04-07 |
| `3705_run5_sl_k3_sp99/` | shortlex | 3 | 0.99 | word_3705 (INVALID) | biased | 2,317,435 | 133MB | 2026-04-07 |
| `3705_run5_sl_k4_sp95/` | shortlex | 4 | 0.95 | word_3705 (INVALID) | biased | 2,282,905 | 133MB | 2026-04-07 |
| `3705_run5_weq_cn100k/` | shortlex | 6 | ~1.0 | word_3705 (INVALID) | word-equality, cn=100k | 3,220,901 | 212MB | 2026-04-07 |
| `weq_rpo/` | RPO | 6 | 0.70 | word_3707 (INVALID) | word-equality | 893,692 | 52MB | 2026-04-06 |
| `weq_sl/` | shortlex | 6 | 0.70 | word_3707 (INVALID) | word-equality | 974,337 | 57MB | 2026-04-06 |

**Total**: ~1.2GB across 12 rule banks. Each bank directory contains: `input` (copy of b25_full), `input.kbprog.live` (rule bank), `kbprog.log` (agent log), `target.txt` (target word used for biasing).

## Scripts

| Script | Location | What it does | Status |
|---|---|---|---|
| `run_biased_agents.sh` | `b25_bias_bidir/scripts/` | Launches 6 biased agents targeting X-core patterns of the lifted word; outputs to `b25_reduce_core/runs/` | Output directory missing — runs not completed or deleted |
| `launch_agents.sh` | `b25_bias_bidir/scripts/` | Launches 5 agents targeting word_4882; outputs to `b25_reduce_core/runs_4882/agents/` | Output directory missing — word_4882 INVALID target |
| run4/run5 driver | **MISSING FROM DISK** | Created the 12 surviving rule banks in `b25_bias_bidir/rules/` | Driver deleted; params reconstructed from kbprog.log headers |

## Missing runs (ghost directories)

| Expected location | Referenced by | Status |
|---|---|---|
| `experiments/b25_reduce_core/runs/` (sl_core_a, rpo_core_a, etc.) | `b25_bias_bidir/scripts/run_biased_agents.sh` | Directory does not exist; runs never completed or were deleted |
| `experiments/b25_reduce_core/runs_4882/agents/` | `b25_bias_bidir/scripts/launch_agents.sh` | Directory does not exist; word_4882 is INVALID anyway |

## Constants (common to all surviving runs)

| Parameter | Value | Note |
|---|---|---|
| Generators | a, b | |
| Exponent | 5 | |
| maxeqns (`-me`) | 50,000,000 | Except weq_cn100k: cn=100,000 |
| maxstates (`-ms`) | 500,000,000 | |
| tidyint (`-t`) | 5,000 | |
| confnum (`-cn`) | 5,000 | Except weq_cn100k: 100,000 |
| Binary | kbmag_source/standalone/bin/kbprog | NOT kbmag_v1 |

## Related material

- [[Biased KB Agents/_type|Biased KB Agents on B(2,5)]] — parent experiment-type description
- [[_progress|B(2,5) Progress Note]] — umbrella progress note
- [[biased-kb-agents-results]] — sibling results table
- [[biased-kb-agents-b25-2026-06-03]] — methodology note for these runs
- [[kbmag-tools-overview]] — KBMAG tool reference; kbmag_source binary details
- [[havas-wall-wamsley-1974]] — source of b25_full presentation
