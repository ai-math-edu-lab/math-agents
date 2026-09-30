---
title: Project profile — mixer-core
project: mixer-core
owner: maumayma
repos:
  - "[[dep-algo-mixer]] — implementation + experiments (mixer-core crate, Python package, experiments/, runs/)"
dependencies:
  - "[[dep-kbmag]] — accepted-patch-only (see note)"
  - "[[dep-gap]] — read-only oracle"
build: uv sync   # rebuilds pyo3 bindings via maturin; mandatory after any mixer-core/src change
test: cargo test -p mixer-core && uv run pytest tests/
smoke: uv run python examples/sorting/run.py
lint: cargo clippy --all-targets && uv run ruff check
languages: [Rust, Python (uv, maturin/pyo3)]
run_pattern: uv run python experiments/<experiment>/run.py
runs_dir: runs/<project>/<experiment>/<timestamp>/
provenance_fields: [algo-mixer git SHA, uv.lock hash, mixer-core build hash, kbmag tree + build hash if used, GAP version if used, host]
heavy_processes: [braid_reduce, kbprog, gap, nq, cent_enum]
protected_interfaces:
  - "mixer_core.Agent Python ABC — subclasses in the wild depend on it"
  - "JSON-lines protocol between the mixer and mixer Agents (get_state / get_items / inject)"
  - "pyo3 bindings between Rust mixer-core and Python (ABI)"
  - "Scheduler / Transform Python API"
  - "on-disk layout of runs/<project>/<experiment>/<timestamp>/"
  - "KBMAG file formats"
hot_paths:
  - "Knuth-Bendix inner loop in any KB-running mixer Agent — runs for hours; constant factors and allocation patterns matter"
  - "scheduler tick (mixer-core/src/scheduler/) — called every poll cycle; avoid per-tick allocations"
  - "JSON-lines transport serialization (mixer-core/src/transport/) — every transfer goes through it"
vault_docs:
  components: Architecture/Mixer/Components/
  code_reviews: Architecture/Mixer/Documentation/Code Review/
  math_validation: Architecture/Mixer/Documentation/Math Validation/
  overview_and_adrs: Architecture/Mixer/Documentation/Overview/
  bases: Architecture/Mixer/Bases/
  experiments: Experiments/<Domain>/<Subject>/<Instance>/
tags: [meta, convention, project/mixer-core]
---

# Project profile — mixer-core

## Goal
Engineering of the **Mixer** framework: N algorithm processes cooperate on one problem, and a Rust engine moves items between them under a scheduler/transform policy. The hypothesis is that cooperation beats each algorithm alone. It generalizes the TimSort insight (merge sort and insertion sort cooperating) to arbitrary algorithm combinations with configurable sharing policies. Architecture: [[mixer-core-overview]].

Research questions:
- Does mixing accelerate convergence in general?
- Which scheduling policies (threshold, periodic, adaptive) help most, and for which algorithm pairs?
- Can mixing produce behaviour no single algorithm exhibits, such as basin-hopping or escaping local optima?
- What is the cost model? When does coordination overhead exceed the benefit of cooperation?

Other projects may reuse Mixer components standalone (e.g. a kbmag wrapper, a reducer) without adopting the framework.

## Components under test
- **mixer Agents**: subprocesses implementing the `mixer_core.Agent` protocol (`work()`, `get_items()`, `inject(items)`, `get_state()`; JSON-lines over stdio). Python subclasses, or native binaries via `StdioAgent` / `KbmagLegacyTransport`.
- **Orchestration**: `Mixer`, `StdioAgent`, schedulers (`ThresholdScheduler`, `PeriodicScheduler`, `CompositeScheduler`), transforms, `terminate_when(predicate)`.
- **Rust crate** `mixer-core/` (engine, scheduler trait in `mixer-core/src/scheduler/`, transports in `mixer-core/src/transport/`). Python package at `mixer-core/python/mixer_core/`.

Terminology: a **mixer Agent** (lowercase, qualified) is an algorithm subprocess. It is never an AI agent.

## Test matrix
| Change kind | Required |
|---|---|
| New mixer Agent subclass | subprocess launches, JSON protocol round-trips, agent terminates cleanly |
| New Scheduler | unit test (Rust if implementing the trait) + integration test showing it fires when expected |
| New Transform | unit test (Python) |
| mixer-core Rust internals | `cargo test -p mixer-core` + smoke test |
| pyo3 binding change | Rust test + Python import test + smoke test |
| Math-layer change (KB semantics, transforms, schedulers' math behaviour) | behaviour tests + Validator property tests and verdict |
| Performance claim | `criterion` (Rust) or `pytest-benchmark` (Python) |

Rust idioms: `Result<T, E>` everywhere; no `.unwrap()` outside tests/`main`; `cargo clippy --all-targets` is clean on touched code.
Validator's property tests go in `mixer-core/tests/proptest_*.rs` and `tests/property_*.py`.

## Protected interfaces — why each one exists
- **`mixer_core.Agent` ABC.** Every mixer Agent in `experiments/` subclasses it, so changing a method signature silently breaks them all.
- **JSON-lines protocol.** Native agents (kbmag wrappers, C++ agents) speak it over stdio with no shared types. The schema *is* the contract.
- **pyo3 ABI.** The Python package and the Rust crate are built together by maturin, and a mismatch shows up only at import time.
- **Scheduler / Transform API.** Experiment configs are written against it, and pre-registrations cite it.
- **`runs/` layout.** Analysis scripts and vault notes link into it by path.
- **KBMAG formats.** Shared with upstream tooling; see [[dep-kbmag]].

A change to any of these is a **human gate** (Lead asks the human before committing).

## Experiment template fields
In [[experiment]], under **Components under test**: list each mixer Agent with its module path and version. Under **Configuration**: the scheduler type (threshold / periodic / composite) with its full params, plus the transforms used. **Baselines**: each mixer Agent run alone on the same problems and seeds.

## Related material
- [[projects-and-dependencies-convention]]
- [[dep-algo-mixer]]
- [[mixer-core-overview]]
- [[project-b25]]
