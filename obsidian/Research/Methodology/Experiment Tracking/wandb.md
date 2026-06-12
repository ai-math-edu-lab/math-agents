---
title: "Weights & Biases (W&B) — Experiment tracking with sweeps"
year: 2018
venue: "Weights & Biases (cloud SaaS + open-source core; founded 2018)"
url: https://wandb.ai
language: en
domain: methodology
status: draft
methodology_type: review
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/experiment-tracking
  - topic/reproducibility
  - paper
  - status/draft
---

# Weights & Biases (W&B) — Experiment tracking with sweeps

## Overview

W&B is a cloud-first ML experiment tracking service with strong sweep (hyperparameter search) management. Core concepts mirror MLflow (runs, params, metrics, artifacts) but with cloud sync by default and richer sweep orchestration.

Key features:
- **Config**: hierarchical dict (`wandb.config.update({"kbmag": {"cn": 100000}})` — native nested support).
- **Sweeps**: distributed hyperparameter search; agents on multiple machines pull configs from a central sweep; supports grid, random, Bayesian search strategies.
- **Dashboard**: cloud-hosted; rich interactive plots, run comparison, query language.
- **Artifacts**: versioned files with lineage tracking (artifact A → produced by run B → consumed by run C).

## Key design decisions

**Hierarchical config is native**: W&B config supports nested dicts directly, unlike MLflow's flat-key default. `wandb.config.kbmag.cn = 100000` works without dotted-key serialization. This is the closest analog to the proposed `params.kbmag`, `params.mixer` namespace blocks.

**Cloud-first**: W&B syncs all run data to cloud in real-time. For local/offline use there's `WANDB_MODE=offline`, but the default workflow assumes connectivity. **This is the primary concern for a small academic group** — cloud dependency adds complexity, potential cost, and data privacy considerations for unpublished research.

**Sweep agent model**: a sweep is defined as a YAML config; agents are launched on compute nodes and pull next hyperparameter assignment from the sweep controller. This maps well to the Mixer's batch-sweep pattern (e.g., the v10d batch_size × injection_threshold grid).

## What applies to the Mixer

1. **Hierarchical config notation**: W&B's nested config is the right model for the proposed `params.kbmag` / `params.mixer` blocks.
2. **Sweep management**: the v10d batch sweep (80 × injection_threshold) is exactly a W&B sweep — grid search over two params, one run per cell. W&B sweeps handle this automatically.
3. **Artifact lineage**: linking a run's output (results.json) to the input TOML config via artifact lineage is a useful provenance record.

## What doesn't apply

- **Cloud dependency**: for a small academic group working on unpublished math research, cloud sync is undesirable. Use `WANDB_MODE=offline` if W&B is adopted, accepting reduced dashboard functionality.
- **ML-specific auto-logging** (PyTorch, sklearn, etc.): irrelevant for Rust KB agents.
- **Pricing**: the free tier has team/project limits that may become binding if the vault scales.

## Tradeoff vs. MLflow

W&B is more polished for sweep orchestration and has better native nested-config support. MLflow is simpler, offline-first, and has no cloud dependency. For the Mixer's use case: **MLflow for run tracking, W&B's config hierarchy as the design inspiration for the namespaced JSON schema**.

## Recommendation

Don't adopt W&B as the primary tracking tool (cloud dependency). **Do** use W&B's config structure design as a reference for the proposed `params.json` namespace blocks: `{"params": {"kbmag": {...}, "mixer": {...}}}` mirrors W&B's native nested config and can be implemented in any tracking backend.

## References

- Official docs: https://docs.wandb.ai/
- Wandb.init() API: https://docs.wandb.ai/ref/python/init
- Sweep config: https://docs.wandb.ai/guides/sweeps/define-sweep-configuration

## Related material in vault

- Synthesis: [[_synthesis-experiment-tracking-schemas]]
- Related tools: [[mlflow]], [[hydra]], [[dvc]]
