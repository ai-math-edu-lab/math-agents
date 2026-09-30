---
title: Project profile — b25
project: b25
owner: maumayma
repos:
  - "[[dep-algo-mixer]] — experiment code under experiments/burnside/ and experiments/b25_reduce_core/, output under runs/b25/"
dependencies:
  - "[[dep-kbmag]] — accepted-patch-only"
  - "[[dep-gap]] — read-only oracle"
  - "[[dep-algo-mixer]] mixer-core — read-only (changes go to Developer via Lead)"
build: uv sync; cargo build --release inside the relevant experiments/burnside/* crate when a Rust tool changes
test: the touched tool's own tests + the mixer-core suite if mixer-core is exercised (see [[project-mixer-core]])
smoke: a small-word reduction / verification on a known-good input for the tool being changed
lint: cargo clippy --all-targets for Rust tools; ruff for Python if configured
languages: [Rust, Python, GAP]
run_pattern: "timeout <cap> uv run python experiments/burnside/<exp>/<script>.py … | or the Rust/GAP binary directly"
runs_dir: runs/b25/<experiment-type>/<timestamp>/
provenance_fields: [algo-mixer git SHA, uv.lock hash, tool build hash (braid_reduce / kbprog / …), GAP version if used, mixer-core build hash only if the Mixer engine was in the path, host]
heavy_processes: [braid_reduce, kbprog, gap, nq, cent_enum]
protected_interfaces:
  - "runs/b25/ layout"
  - "rule-bank and corpus file formats consumed by braid_reduce / reduce_coreless"
hot_paths:
  - "braid_reduce Aho-Corasick + beam search over the 2.5 GB rule bank"
  - "kbprog inner loop"
vault_docs:
  components: Architecture/Mixer/Components/
  code_reviews: Architecture/Mixer/Documentation/Code Review/
  math_validation: Architecture/Mixer/Documentation/Math Validation/
  experiments: Experiments/Group Theory/Burnside Group/B25/
  progress: Experiments/Group Theory/Burnside Group/B25/_progress.md
tags: [meta, convention, project/b25]
---

# Project profile — b25

## Goal
Progress on **B(2,5)**, the free Burnside group on two generators of exponent 5. Whether it is finite is open (Kourovka 11.48). The standing state is in the progress note `Experiments/Group Theory/Burnside Group/B25/_progress.md`. [[experimenter-b25]] owns the vault subtree, `runs/b25/**`, and the `feat|fix|chore/b25-*` branches.

## Components under test
Most B25 compute is **not** the Mixer engine. It uses:
- `braid_reduce` (`experiments/burnside/burnside_bidirectional/src/bin/braid_reduce.rs`): Aho-Corasick + beam-search reducer over a large rule bank;
- `reduce_coreless.py` (`experiments/b25_reduce_core/`);
- standalone `kbprog` ([[dep-kbmag]]);
- GAP p-quotient and word-problem scripts ([[dep-gap]]);
- Mixer runs (e.g. the RL Mixer), only when the experiment type says so. When it does, [[project-mixer-core]] applies too.

Record the component actually used. "Mixer" is not a synonym for "our code".

## Test matrix
| Change kind | Required |
|---|---|
| Change to a reducer / search tool | regression on a known input (same output before/after unless the change is intended) + Validator check if reduction semantics change |
| New reduction rule source / rule bank | Validator soundness check of the rules before any experiment builds on them |
| mixer-core touched | see [[project-mixer-core]] |

## Protected interfaces — why each one exists
- **`runs/b25/` layout.** The results tables and `_progress.md` link into it, and expensive artifacts (rule banks, BFS tables, PcGroups) are reused from it.
- **Rule-bank and corpus formats.** Multiple tools and months of results depend on them.

## Experiment template fields
In [[experiment]], also fill:
- **Target words / properties**: exactly what is being proven or refuted.
- **Group computed in**: free B(2,5), restricted B₀(2,5), or a named finite quotient. This field is mandatory.
- **B25-specific modifications**: ordering, compression, custom transform.

## Related material
- [[projects-and-dependencies-convention]]
- [[project-mixer-core]]
- [[dep-algo-mixer]]
- [[experimenter-b25]]
