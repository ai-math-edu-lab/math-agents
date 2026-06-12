---
title: RL Mixer experiment progress (B25)
domain: group-theory
project: rl-mixer
instance: B(2,5)
status: inconclusive
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/reinforcement-learning, project/rl-mixer, status/inconclusive, experiment]
---

# RL Mixer — Progress (B(2,5))

Reinforcement-learning approach to B(2,5) word reduction. A PPO-trained agent selects word-reduction strategies (80 macro actions: 10 strategies × 8 position buckets) applied to B(2,5) commutator words. Implemented as a Rust+Python (PyO3/maturin) hybrid in `experiments/rl_mixer/`.

Domain classification: **group-theory** per F12.3 contribution-wins-over-methodology (the contribution is B(2,5) word reduction; the methodology is RL).

## Status

Three trained `.pt` checkpoints exist (subword_comm12_7.pt, subword_comm16_2.pt, subword_rpo.pt). No training logs or experiment output directories preserved on disk. Status: **inconclusive** — models trained but evaluation results not recorded.

## Active experiment types

- [[RL Mixer/_type|RL Mixer]] — PPO training + macro action evaluation on B(2,5) word reduction

## What exists

| Item | Status |
|---|---|
| Rust source + compiled binary | Present (`experiments/rl_mixer/src/`, compiled `target/`) |
| Python training scripts | Present (`rl/train_subword_ppo.py`, `train_macro_ppo.py`, etc.) |
| Trained checkpoints (3) | Present (`checkpoints/subword_comm12_7.pt`, etc.; ~398KB each) |
| Training logs | **Missing** |
| Evaluation output dirs | **Missing** |
| Rule bank (`/tmp/all_rules_combined.live`) | **Not on disk** — external runtime dependency |

## Related material

- [[B25/_progress]] — B(2,5) umbrella
- [[B25/Reduce Core/_progress]] — beam search approach (structural parallel)
- [[2026-06-02-non-b25-forensic-inventory]] — §9 covers RL Mixer forensic provenance
