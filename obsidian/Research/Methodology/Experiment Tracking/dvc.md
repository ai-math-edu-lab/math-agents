---
title: "DVC — Data Version Control for ML pipelines and artifacts"
year: 2017
venue: "DVC (open-source, Iterative AI; first release 2017)"
url: https://dvc.org
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

# DVC — Data Version Control for ML pipelines and artifacts

## Overview

DVC extends git with large-file versioning and pipeline tracking. The core problem it solves: git is bad at binary files (models, datasets, run outputs) but experiment reproducibility requires versioning them alongside code.

Core concepts:
- **`.dvc` files**: lightweight git-tracked pointers to large files stored in a DVC cache (local dir, S3, GCS, Azure, etc.).
- **Stages**: pipeline stages defined in `dvc.yaml`; each stage has inputs, outputs, and a command.
- **DAG**: stages form a directed acyclic graph; `dvc repro` re-runs only stages whose inputs changed.
- **DVC Experiments** (added 2021): lightweight experiment tracking on top of git — `dvc exp run`, `dvc exp show`, `dvc exp compare`. Stores params (from `params.yaml`) and metrics (from `metrics.json`) as git notes.
- **Params**: read from a `params.yaml` file; DVC tracks which stages depend on which params; runs only when params change.

## Key design decisions

**Git-native**: DVC stores all metadata in git; large artifacts go to the cache. This means full versioning history is in the git log — including which exact data/model was used for which run.

**`params.yaml` convention**: DVC expects a `params.yaml` file at the project root (or per-stage). Each stage declares which params it depends on; `dvc repro` re-runs a stage only if those params changed. This is equivalent to the proposed `params.json` — the standard location for params per run.

**Metrics JSON**: `dvc metrics show` reads from a designated JSON file (`metrics.json` by default). Fields: any flat JSON key-values. The existing `results.json` would serve as the DVC metrics file with minor renaming.

**Pipeline DAG**: for the Mixer, the DAG is: `generate_relators → run_kbmag_agents → inject_rules → check_confluence → log_results`. DVC `dvc.yaml` codifies this; `dvc repro` re-runs the minimal affected stages when params change.

## What applies to the Mixer

1. **Large artifact versioning**: KB rule banks (millions of rules, potentially GB-scale) cannot go in git. DVC's `.dvc` pointer + cache is the standard solution. The B(2,5) rule banks (`experiments/burnside/*/rules_*.txt`) are exactly the kind of artifact DVC was designed for.
2. **`params.yaml` as the canonical param file**: maps directly to the proposed `params.json` (or a `params.yaml` sibling — DVC works with either). If `params.yaml` is the source of truth, `params.json` can be auto-generated from it.
3. **Metrics file = `results.json`**: minor rename or DVC config pointing to the existing file. `dvc metrics show` then enables cross-run comparison from the CLI.
4. **Run reproducibility**: `dvc repro --params params.kbmag.cn=50000` re-runs only the affected stages. Combined with git SHA tracking, this gives full reproducibility.

## What doesn't apply

- **Data science-focused features** (feature stores, model registry, remote experiments): not relevant.
- **S3/cloud artifact storage**: only needed if the team needs to share large artifact files; for local research, the DVC local cache is sufficient.

## Recommendation

**DVC is the right tool for artifact versioning** (KB rule banks, large results files) but is heavier to set up than MLflow for run tracking. **Recommendation**: use MLflow for run tracking (params + metrics + small artifacts), DVC for large artifact versioning (rule banks, relator files). The two tools are complementary and commonly used together.

**Minimal DVC adoption path**: add a `dvc.yaml` pipeline and `params.yaml` to the Mixer repo; point metrics to `results.json`. This gives git-native run comparison and artifact versioning with ~1 day setup effort.

## References

- Official docs: https://dvc.org/doc
- DVC experiments: https://dvc.org/doc/user-guide/experiment-management
- params.yaml convention: https://dvc.org/doc/command-reference/params

## Related material in vault

- Synthesis: [[_synthesis-experiment-tracking-schemas]]
- Related tools: [[mlflow]], [[wandb]], [[hydra]]
