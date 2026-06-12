---
title: "Hydra — Structured config composition for complex applications"
year: 2019
venue: "Hydra (open-source, Meta AI; first release 2019)"
url: https://hydra.cc
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

# Hydra — Structured config composition for complex applications

## Overview

Hydra is a Python library for configuring complex applications via hierarchical, composable configs. Unlike MLflow or W&B (which track what happened), Hydra manages what configuration goes IN to an experiment — generating structured configs from defaults + overrides.

Core concepts:
- **Config groups**: directories of YAML files, one per "variant" (e.g., `conf/model/mlp.yaml`, `conf/model/transformer.yaml`). Select at run time.
- **Config composition**: assemble a config from multiple groups (`+model=mlp +optimizer=adam`).
- **Overrides**: any config key can be overridden from the CLI (`python train.py model.lr=0.01`).
- **Structured configs**: Python dataclasses serve as config schemas with type-checking.
- **Multirun**: `--multirun model.lr=0.01,0.001 optimizer.wd=0.0,0.1` runs all combinations — a built-in grid sweep.
- **Output dirs**: Hydra automatically creates `outputs/YYYY-MM-DD/HH-MM-SS/` per run and saves the resolved config there.

## Key design decisions

**Config schema via Python dataclasses**: each config block is a typed dataclass. This gives:
- Type checking at config-load time (wrong type = error before run starts).
- IDE autocompletion for config fields.
- Explicit schema documentation.

**YAML + override syntax**: configs are YAML files; command-line overrides use dot notation (`params.kbmag.cn=100000`). Equivalent to the proposed namespaced params blocks in the JSON schema.

**Reproducibility via saved configs**: every run saves the full resolved config to `outputs/.../.hydra/config.yaml`. This is exactly what `params.json` should contain — the complete configuration at run time.

**Multirun = sweep**: `python mixer.py --multirun params.mixer.batch_size=50,80,100,150 params.mixer.threshold=19000,20000,21000` runs the full grid without a sweep controller. Simpler than W&B sweeps for small grids.

## What applies to the Mixer

1. **Config schema pattern**: Hydra's dataclass-based config schema is the right pattern for formalizing the Mixer's params structure. The `params.kbmag`, `params.mixer`, `params.beam` blocks should be Python dataclasses with typed fields.
2. **Auto-saved config per run**: Hydra's output structure (`outputs/<date>/<time>/.hydra/config.yaml`) is the gold standard for `params.json` — the full resolved config, saved automatically before the run starts.
3. **Multirun for batch sweeps**: the v10d batch_size sweep is a `--multirun` invocation. The current Python script that loops over batch sizes can be replaced by `hydra --multirun params.mixer.batch_size=50,80,100,...`.
4. **CLI overrides**: `python mixer.py params.kbmag.cn=50000` — clean, documented, reproducible.

## What doesn't apply

- **Hydra's launcher/sweeper plugins** (Submitit for SLURM, Optuna for Bayesian search): overkill for the current Mixer scale.
- **Python-application coupling**: Hydra requires calling `@hydra.main()` in the entry point. The existing Mixer Python scripts would need minimal refactoring to adopt this.

## Recommendation

**Adopt Hydra's config structure pattern** for the `params.json` schema — even if the Mixer doesn't use Hydra directly. The dataclass schema disciplines the parameter space; the dot-notation override syntax becomes the CLI interface. Partial adoption: write params as a Hydra-style YAML config (already close to the existing `rpo.toml` structure), then serialize to `params.json` at run start.

If the Mixer scales to larger sweeps (e.g., B(2,5) multi-ordering parameter searches), full Hydra adoption is the natural next step.

## References

- Official docs: https://hydra.cc/docs/intro/
- Structured configs: https://hydra.cc/docs/tutorials/structured_config/schema/
- Multirun: https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/

## Related material in vault

- Synthesis: [[_synthesis-experiment-tracking-schemas]]
- Related tools: [[mlflow]], [[wandb]], [[dvc]]
