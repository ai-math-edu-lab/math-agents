---
title: RL Mixer results — B(2,5)
domain: group-theory
project: rl-mixer
instance: B(2,5)
experiment_type: rl-mixer
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/reinforcement-learning, project/rl-mixer, status/inconclusive, results]
---

# Results — RL Mixer on B(2,5)

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | Best reduction | Validated by |
|---|---|---|---|---|---|---|
| comm12_7 training | Unknown | PPO, 80 macro actions, subword target | Checkpoint saved (`subword_comm12_7.pt`) | Unknown | Unknown | None |
| comm16_2 training | Unknown | PPO, 80 macro actions, subword target | Checkpoint saved (`subword_comm16_2.pt`) | Unknown | Unknown | None |
| rpo-scored training | Unknown | PPO, 80 macro actions, RPO scoring | Checkpoint saved (`subword_rpo.pt`) | Unknown | Unknown | None |
| beam baseline | Unknown | beam_width=1024, max_steps=50000, secs=15 | Not recorded | Unknown | Unknown | None |

**Critical gap**: No evaluation outputs preserved. The trained agents exist as `.pt` files but their performance relative to beam search is unknown.

## What is and isn't known

**Known**:
- Training completed for 3 targets (checkpoints are ~398KB each, indicating a small policy network was trained to some convergence)
- The Rust environment supports beam_width=1024 and 80 discrete macro actions
- Target words: comm_12_7, comm_16_2, and an RPO-scored variant

**Unknown**:
- Best word length achieved by the RL agent on any target
- Whether the RL agent outperforms fixed-order beam search on any metric
- Training episode count, reward curve, convergence status
- Which rule bank was used during training (`/tmp/all_rules_combined.live` — not on disk)
- Wall-clock for training and evaluation

## Comparison context

The closest documented result in the same domain: `b25_reduce_core` beam search achieved **7,245 chars** for comm_12_9 (the best-known reduction as of 2026-04-11). The RL Mixer targets comm_12_7 and comm_16_2, which are different words — no direct comparison available.

## Version history

Three `.pt` checkpoints suggest at least 3 training runs. Whether these are sequential refinements or independent runs for different targets is unclear (the naming suggests independent targets: each checkpoint is specialized to a specific word).

## Main findings

**No findings recordable** — evaluation results were not preserved. The experiment is `#status/inconclusive` because:
1. Training completed (artifacts exist) but evaluation was not recorded
2. No comparison to beam search baseline is documented
3. The rule bank used for training is not on disk, making reproduction difficult

## What would complete this

1. Run `rl/test_all_rules_comparison.py` with the rule bank and all 3 checkpoints
2. Record: best word length, wall-clock vs. beam, and reward trajectory
3. Pre-register a hypothesis before re-running (per [[experiment-folder-convention]] § Pre-registration)
4. Provide the `/tmp/all_rules_combined.live` rule bank (the B(2,5) combined rule bank from the KBMag server run)

## Open questions

1. Does the RL agent generalize across B(2,5) words, or is it overfit to its training target?
2. The subword PPO and macro PPO are separate training regimes — which performed better?
3. Is the 80-action space (10 strategies × 8 position buckets) sufficient, or does the agent saturate quickly on a given word?

## Related material

- [[_type]] — parent experiment-type
- [[RL Mixer/_progress]] — RL Mixer umbrella
- [[data/rl-mixer-data-b25]] — checkpoints, scripts
- [[methodology/rl-mixer-b25-2026-06-03]] — methodology, architecture
- [[B25/Reduce Core/results/reduce-core-results]] — beam search results (7,245 chars; algorithmic baseline)
- [[B25/_progress]] — B(2,5) umbrella
- [[2026-06-02-non-b25-forensic-inventory]] — §9 forensic provenance
