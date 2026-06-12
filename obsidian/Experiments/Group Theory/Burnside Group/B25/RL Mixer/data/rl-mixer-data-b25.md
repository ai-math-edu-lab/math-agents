---
title: RL Mixer data — B(2,5)
domain: group-theory
project: rl-mixer
instance: B(2,5)
experiment_type: rl-mixer
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
params_rl_action_space: 80
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/reinforcement-learning, project/rl-mixer, status/inconclusive, data]
---

# Data — RL Mixer on B(2,5)

## Trained checkpoints

| File | Size | Training target |
|---|---|---|
| `experiments/rl_mixer/checkpoints/subword_comm12_7.pt` | 398.6KB | B(2,5) word comm_12_7 |
| `experiments/rl_mixer/checkpoints/subword_comm16_2.pt` | 398.6KB | B(2,5) word comm_16_2 |
| `experiments/rl_mixer/checkpoints/subword_rpo.pt` | 398.4KB | RPO-rule-scored target |

Additional checkpoint dirs exist: `checkpoints/archive/` and `checkpoints/models/` — contents not inventoried.

## Rule bank (external dependency)

- **Required**: `/tmp/all_rules_combined.live` — large B(2,5) combined rule bank
- **Status**: NOT on disk. Must be provided at runtime.
- **Source**: presumably the accumulated B(2,5) rule banks from `b25_bias_bidir/rules/` or `b25_kbmag/server_logs/` (same rule banks used by b25_reduce_core)
- Without this file the RL environment cannot be instantiated: `rl_mixer.RlEnvironment('/tmp/all_rules_combined.live', 5)` will fail

## Rust binary

- **Source**: `experiments/rl_mixer/src/` (Rust crate)
- **Build**: `cd experiments/rl_mixer && maturin develop --release`
- **Binary output**: `target/release/` (compiled; 874MB total for target/ + .venv/)
- **Key modules**: `src/reduce/braid.rs` (correct braid shortenings), `src/reduce/beam.rs` (split beam), `src/actions.rs` (80-action space)

## Training scripts

| Script | Purpose |
|---|---|
| `rl/train_subword_ppo.py` | Subword-level PPO training |
| `rl/train_macro_ppo.py` | Macro-action PPO training |
| `rl/curriculum.py` | Staged training curriculum |
| `rl/config.py` | Training configuration |
| `rl/agent.py` | PPO agent definition |
| `rl/replay_buffer.py` | Experience replay |

## Evaluation scripts

| Script | Purpose |
|---|---|
| `rl/test_all_targets.py` | All-target benchmark: beam vs RL |
| `rl/test_target_comparison.py` | Target-specific comparison |
| `rl/subword_eval.py` | Subword-level evaluation |
| `rl/test_all_rules_comparison.py` | beam vs smart vs RL comparison |

## Disk inventory

| Item | Path | Size |
|---|---|---|
| Total experiment dir | `experiments/rl_mixer/` | **874MB** |
| Compiled Rust target/ | `target/` | ~800MB |
| Python .venv/ | `.venv/` | ~70MB |
| Checkpoints | `checkpoints/*.pt` | ~1.2MB |
| Training scripts | `rl/*.py` | ~300KB |
| Rust source | `src/` | ~50KB |

## Related material

- [[_type]] — parent experiment-type
- [[RL Mixer/_progress]] — RL Mixer umbrella
- [[methodology/rl-mixer-b25-2026-06-03]] — methodology, action space, architecture
- [[results/rl-mixer-results-b25]] — evaluation gaps
- [[kbmag-tools-overview]] — KBMAG tool (rule bank sources)
- [[2026-06-02-non-b25-forensic-inventory]] — §9 forensic provenance
