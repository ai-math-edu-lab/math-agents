---
title: algo-mixer (mixer-core)
kind: our-repo
upstream: git@github.com:ai-math-edu-lab/algo-mixer.git
license: unspecified
ownership: we-own
obtain: git clone git@github.com:ai-math-edu-lab/algo-mixer.git
build: uv sync   # also triggers maturin to rebuild the mixer-core pyo3 bindings after any mixer-core/src change
test: cargo test -p mixer-core && uv run pytest tests/
versions_in_use:
  - "main — all Mixer-based and Burnside experiment code to date"
local_patches: []
capabilities:
  - "orchestration: run N algorithm processes on one problem with scheduled item exchange (Mixer engine)"
  - "group theory: word reduction over a rule bank (braid_reduce, reduce_coreless), usable standalone"
heavy_processes: [braid_reduce, cent_enum]
mcp: none
local_checkouts:
  maumayma: /Users/maumayma/Desktop/reps/algo_mixing
  asetlearning: /media/psf/algo-mixer
docs: "[[mixer-core-overview]]"
used_by: ["[[project-mixer-core]]", "[[project-b25]]"]
tags: [meta, type/reference]
---

# algo-mixer (mixer-core)

## What it is
Our repository for the **Mixer** approach: several algorithm processes ("mixer Agents") run in parallel on the same problem, and a Rust engine (`mixer-core`) periodically moves items between them under a scheduler/transform policy. The engine lives in `mixer-core/src/` (Rust) and is exposed to Python via pyo3 (`mixer-core/python/mixer_core/`). Architecture docs: `Architecture/Mixer/` (start at [[mixer-core-overview]]).

The repo also holds a lot of **non-Mixer** experiment code that simply lives here for historical reasons. Examples: `experiments/burnside/burnside_bidirectional/` (the `braid_reduce` Rust binary), `experiments/b25_reduce_core/`, GAP scripts (`check_word.g`, `verify_confluence.g`), and the vendored kbmag trees ([[dep-kbmag]]). When one of these is used, the Mixer engine is **not** in the path. Record the component actually used, not "the Mixer".

## How we use it
- Mixer runs: `mixer_core.Mixer` + `StdioAgent`s + a scheduler. See [[project-mixer-core]].
- Standalone tools used by [[project-b25]] and the Burnside projects: `braid_reduce`, `reduce_coreless.py`, the GAP verifiers.
- Output goes to `runs/<project>/<experiment>/<timestamp>/` inside this repo.

## Protected surfaces
The list, with the reason for each, is in [[project-mixer-core]] § Protected interfaces. In short: the `mixer_core.Agent` ABC, the JSON-lines protocol, the pyo3 ABI, the `Scheduler`/`Transform` API, and the `runs/` layout.

## Known pitfalls
- Python ≥3.14 and a Rust toolchain are required. Forgetting `uv sync` after a Rust change leaves stale bindings.
- Vault notes must never be written into this repo; see the recorded failure in [[experimenter-b25]].

## Related material
- [[projects-and-dependencies-convention]]
- [[project-mixer-core]]
- [[project-b25]]
- [[mixer-core-overview]]
