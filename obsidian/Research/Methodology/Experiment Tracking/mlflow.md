---
title: "MLflow — Experiment tracking and model registry"
year: 2018
venue: "MLflow (open-source, Databricks; first release 2018)"
url: https://mlflow.org
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

# MLflow — Experiment tracking and model registry

## Overview

MLflow is a Python library for tracking ML experiments, versioning models, and packaging code for reproducibility. Core concepts:
- **Experiment**: a named collection of runs (e.g. "b43-mixer-v10d").
- **Run**: one execution instance with logged params, metrics, artifacts, tags, and source code info.
- **Params**: key-value pairs logged at run start (one value per key per run; immutable once logged).
- **Metrics**: key-value pairs with optional step/timestamp (can be logged multiple times across the run duration — useful for loss curves, convergence trajectories).
- **Artifacts**: files (JSON, plots, model checkpoints, TOML configs) associated with a run.
- **Tags**: metadata strings (run name, git SHA, hostname, user).

## Key design decisions

**Flat params by default**: MLflow's params API takes `mlflow.log_params({"cn": 100000, "batch": 80})` — flat dict. Nested configs can be logged by serializing to JSON artifact, or by using dotted-key convention (`mlflow.log_params({"kbmag.cn": 100000, "mixer.batch": 80})`). This aligns with the vault's namespaced `params.kbmag` / `params.mixer` proposal.

**Metrics with steps**: `mlflow.log_metric("rpo_rules", 20000, step=1)` — logs a time-series. Perfect for the Mixer's injection_history (each injection event is a step).

**Artifact logging**: arbitrary files. The existing `results.json` can be logged as-is; the params TOML can be logged as an artifact alongside the structured `params.json`.

**Local or remote backend**: MLflow can track to a local `mlruns/` directory (no server needed) or to a remote tracking server (PostgreSQL + S3). For a small academic group: local or a shared NFS server.

**Model registry**: not relevant for the Mixer (it tracks algorithms, not ML models). Skip.

## What applies to the Mixer

1. **The Experiment/Run hierarchy** maps directly: Experiment = "b43-kbmag-mixing" or "b25-bidirectional"; Run = one execution with specific params.
2. **Metric time-series** for injection_history: each injection event can be logged as a step (step = injection index; metric values = n_injected, slex_rules, rpo_rules).
3. **Artifact logging** for results.json and the TOML config file — both captured per run.
4. **Auto-logging of git SHA** via `mlflow.set_tag("git_sha", subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip())`.
5. **Comparison UI** (MLflow UI): runs the web UI locally, allows side-by-side parameter and metric comparison across runs. Directly addresses the vault Bases view use case.

## What doesn't apply

- **ML-model-specific features** (model registry, autolog for PyTorch/sklearn): not relevant for Rust/Python KB experiments.
- **MLflow Projects**: declares runnable environments; overkill for small-group academic use where the `uv` lockfile already handles this.
- **Remote tracking server**: MLflow defaults to local `mlruns/` — appropriate for the Mixer; no server needed.

## Tradeoff vs. alternatives

| Factor | MLflow | W&B | Hydra | DVC |
|---|---|---|---|---|
| Nested configs | Dotted keys or artifact | Native dict | Native dataclasses | N/A |
| Offline-first | ✓ (local mlruns/) | ✗ (cloud-first) | ✓ | ✓ |
| Sweep management | Limited | First-class | First-class | Limited |
| Git integration | Manual tags | Auto | Manual | First-class |
| Setup complexity | Low | Medium | Low | Medium |

## Recommendation

MLflow is the closest fit for the Mixer's immediate needs: simple, offline-first, flat-params logging with optional artifact attachment, and a built-in comparison UI. The Mixer already has `results.json`; MLflow logging can wrap the existing file-write with a single `mlflow.log_artifact(run_dir / "results.json")` call.

## References

- Official docs: https://mlflow.org/docs/latest/
- Zaharia et al. (2018) "Accelerating the Machine Learning Lifecycle with MLflow" — IEEE Data Engineering Bulletin (the original MLflow paper, if needed for academic citation).
- MLflow tracking: https://mlflow.org/docs/latest/tracking.html

## Related material in vault

- Synthesis: [[_synthesis-experiment-tracking-schemas]] (the proposed Mixer schema)
- Related tools: [[wandb]], [[hydra]], [[dvc]]
- Cross-vault: [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] (the param space being tracked IS the combinatorial-search parameter problem)
