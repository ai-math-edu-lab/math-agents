---
title: RL Mixer on B(2,5)
domain: group-theory
project: rl-mixer
instance: B(2,5)
experiment_type: rl-mixer
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/reinforcement-learning, project/rl-mixer, status/inconclusive, experiment-type]
---

# RL Mixer on B(2,5)

PPO-trained reinforcement-learning word reduction for B(2,5) commutator words. The RL agent selects among 80 macro actions (10 reduction strategies × 8 position buckets) to reduce B(2,5) words. Rust+Python (PyO3/maturin) hybrid in `experiments/rl_mixer/`.

## Experiment subtree

- [[methodology/rl-mixer-b25-2026-06-03|Methodology]] — PPO setup, action space, training targets, architecture
- [[data/rl-mixer-data-b25|Data]] — checkpoints, scripts, rule bank dependency
- [[results/rl-mixer-results-b25|Results]] — what is and isn't known; gaps in evaluation record

## Related material

- [[RL Mixer/_progress]] — RL Mixer umbrella
- [[B25/Reduce Core/_type]] — beam search approach (same domain; algorithmic contrast)
- [[B25/KBMag/_type]] — KBMag approach (same domain)
