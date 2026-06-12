---
title: biased-kb-agents-b25-2026-06-03
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: biased-kb-agents
status: inconclusive
reconstructed_on: 2026-06-03
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, project/b25, status/inconclusive, methodology]
---

# Experiment — Biased KB Agents on B(2,5)

## Reconstruction notes

This experiment was performed prior to the K3 documentation convention. Reconstructed 2026-06-03 from the W2 forensic archaeology inventory ([[2026-06-02-b25-forensic-inventory]] § Section 3 and § Section 6), surviving rule banks in `experiments/burnside/b25_bias_bidir/rules/`, kbprog.log headers in each rule bank directory, and the driver scripts `experiments/burnside/b25_bias_bidir/scripts/run_biased_agents.sh` and `launch_agents.sh`.

**Critical limitation**: the driver script that created the `3705_run4_*` and `3705_run5_*` rule bank batches is **missing from disk**. Parameters for these runs were decoded from kbprog.log headers and folder names. See W2 inventory § Folder-name parameter decoding.

**Invalidation**: ALL surviving rule banks in this experiment targeted INVALID words (word_3705 or word_3707, both derived from the buggy `braid_reduce_fast` chain — see [[Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]] § The critical bug). The valid target for this experiment type is **word_7245** (`experiments/b25_reduce_core/corrected/final_beam.txt`). Valid biased-agent runs on word_7245 have NOT yet been performed.

## Hypothesis

Biased kbprog agents seeded with specific structural patterns from B(2,5) target words will generate rule banks that, when applied to those targets, produce greater length reduction than general-purpose rule banks at equal rule count.

Specifically for comm_12_9: biased agents seeded on the X-core pattern (`ABabAbabABaBAbabABABabAbaBABaBAbabb`), boundary words, and the full lifted/coreless form will produce rules that close the reduction gap beyond word_7245.

## Problem set

- Group: B(2,5)
- Primary target: comm_12_9 = [c12, c9], current best 7,245 chars (word_7245)
- Secondary: the 119 benchmark words in `b25_reduce_core/benchmark_run/words/`
- Underlying presentation: `kbmag_v1/standalone/kb_data/b25_full` (59 equations, standard B(2,5))

## Mixer agents involved

All runs use `kbmag_source/standalone/bin/kbprog` (the modified binary with biasing extensions). Not the same binary as KBMag experiment type (`kbmag_v1`).

### Run4 batch (6 agents)

Targeting word_3705 (INVALID). Parameters reconstructed from kbprog.log headers and folder names. sp value not encoded in folder names — inferred as ~0.5 from log special-equation percentages (~50% observed).

| Agent | Ordering | sk | sp (inferred) |
|---|---|---|---|
| `3705_run4_sl_k12` | shortlex | 12 | ~0.5 |
| `3705_run4_sl_k16` | shortlex | 16 | ~0.5 |
| `3705_run4_sl_k20` | shortlex | 20 | ~0.5 |
| `3705_run4_rpo_k14` | RPO | 14 | ~0.5 |
| `3705_run4_rpo_k20` | RPO | 20 | ~0.5 |
| `3705_run4_wt_k16` | wtlex | 16 | ~0.5 |

### Run5 batch (4 agents)

Targeting word_3705 (INVALID). sp value encoded in folder name. Explores higher sp values and word-equality mode.

| Agent | Ordering | sk | sp |
|---|---|---|---|
| `3705_run5_sl_k0_sp50` | shortlex | 0 | 0.50 |
| `3705_run5_sl_k3_sp99` | shortlex | 3 | 0.99 |
| `3705_run5_sl_k4_sp95` | shortlex | 4 | 0.95 |
| `3705_run5_weq_cn100k` | shortlex | 6 | ~1.0 (word-equality, cn=100k) |

### Word-equality batch (2 agents, earlier series)

Targeting word_3707 (INVALID). Predate run4/run5 naming. sp=0.70, sk=6 confirmed from kbprog.log headers.

| Agent | Ordering | sk | sp |
|---|---|---|---|
| `weq_rpo` | RPO | 6 | 0.70 |
| `weq_sl` | shortlex | 6 | 0.70 |

## Scheduler config

Not applicable — these are standalone `kbprog` processes, not orchestrated by a Python mixer. Each agent runs until killed or until its maxeqns limit is reached.

Common parameters: `me=50,000,000 -ms 500,000,000 -t 5000 -cn 5000` (except `3705_run5_weq_cn100k`: `-cn 100000`).

## Termination criteria

Each agent runs until killed externally or until maxeqns=50M equations accumulated. No agent is known to have reached confluence. Run5 agents were likely stopped when rule counts plateaued or when the INVALID target was discovered.

## Baselines

- KBMag general-purpose shortlex run (same presentation, no biasing): `runs/b25/20260320_065252` (351K rules at termination)
- KBMag general-purpose RPO: `runs/b25/20260320_054109` (550K rules at termination)
- Merged master bank: ~25.7M rules from 12+ unbiased runs

## Seeds

Not applicable — deterministic given same input, ordering, and target word.

## Metric

- Rule count at termination (more is better for coverage, fewer is better for injection efficiency)
- Special-equation percentage (measures bias effectiveness — higher = more target-aligned rules)
- Downstream reduction: does applying these rule banks to the target word reduce it further than the master bank alone?

## Anti-pattern check

- **Tuning on test target**: ALL runs in this experiment tested rule banks on the same target word they were biased on (word_3705 or word_3707). This is the known tuning-on-test problem. Any reduction improvement on these targets would be suspect. The benchmark (119 words, no biasing) partially addresses this — but the benchmark was run against the INVALID targets; a valid benchmark pass (targeting word_7245 and related words) has not been done.

## Setup

- Driver scripts: `b25_bias_bidir/scripts/run_biased_agents.sh` (X-core targets, intended output in `b25_reduce_core/runs/`), `b25_bias_bidir/scripts/launch_agents.sh` (word_4882 target, output in `b25_reduce_core/runs_4882/agents/`). Driver for run4/run5 batches: missing from disk.
- Rule banks live at: `experiments/burnside/b25_bias_bidir/rules/`
- Provenance: kbprog.log files in each rule bank directory contain command + CWD

## Results — Summary

See results note [[biased-kb-agents-results]] for the full table. Top-line:

- 12 surviving rule banks, all targeting INVALID words (word_3705 or word_3707)
- Total storage: ~1.2GB
- Rule counts range from 417K (`3705_run4_rpo_k20`) to 3.2M (`3705_run5_weq_cn100k`)
- No downstream reduction improvement documented (all validation was on INVALID targets)
- Ghost runs: `b25_reduce_core/runs/` (intended output of `run_biased_agents.sh` with X-core targets) does not exist on disk

## Validation

None documented for reduction improvement. The rule banks themselves are valid B(2,5) KB rules — they are correct rewriting rules for B(2,5) as a group. Their invalidity is specifically in their bias: they are over-represented with rules useful for the wrong coset (word_3705/word_3707, not [c12,c9]).

## Final verdict

**`#status/inconclusive`**

### Why

The experiment as executed is invalid due to target invalidation: all surviving rule banks were biased on words derived from the buggy `braid_reduce_fast` chain. The methodology is sound — biased kbprog agents should produce more targeted rule banks than general-purpose runs — but no valid execution of this experiment has been performed. The question of whether biased agents on word_7245 would improve reduction beyond the current 7,245-char best is the primary open question.

### What to do next

1. **HIGHEST priority**: Re-run `run_biased_agents.sh` pointing to `corrected/final_beam.txt` (word_7245) as the target. Update the script's target path (currently points to now-invalid word files).
2. Sweep agent parameters on word_7245: vary sk (4, 8, 12), sp (0.5, 0.7, 0.9), ordering (sl, rpo, wt). Use the run5 naming convention.
3. After collecting new rule banks, apply to word_7245 via the Reduce Core pipeline and measure improvement.
4. Run the 119-word benchmark with new biased banks to check for generalization (substance test: does sk=8 on word_7245 improve OTHER benchmark words, or only word_7245?).

### Lead notified

- Date: 2026-06-03 (reconstruction; no prior Lead notification for these runs)

---

## Literature

- [[havas-robertson]] — KB completion (§2.9); the `-sw`/`-sp`/`-sk` biasing is an extension of the standard KB tidy cycle prioritisation described here.
- [[havas-wall-wamsley-1974]] — provides the B(2,5) presentation used as input.
- [[kourovka-11.48-kostrikin-1990]] — theoretical stakes for any successful biased reduction of comm_12_9.

## Related material

- [[Biased KB Agents/_type|Biased KB Agents on B(2,5)]] — parent experiment-type description
- [[_progress|B(2,5) Progress Note]] — umbrella progress note; biased KB runs are listed under "What's stuck"
- [[biased-kb-agents-data]] — sibling data note: rule bank paths, target word files, parameter tables
- [[biased-kb-agents-results]] — sibling results table
- [[reduce-core-pipeline-b25-2026-05-22]] — downstream consumer of these rule banks; the bug that invalidated all targets is documented there
- [[kbmag-tools-overview]] — KBMAG tool reference; `kbmag_source` binary documented here
- [[2026-06-02-b25-forensic-inventory]] — W2 inventory that reconstructed these runs from disk archaeology
