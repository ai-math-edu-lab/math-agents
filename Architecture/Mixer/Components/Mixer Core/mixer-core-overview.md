---
title: Mixer Core — component family overview
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "mixer_core Python package (mixer-core/python/mixer_core/) — primary user-facing API"
  - "mixer_core.Mixer — builder-style Python class for constructing and running a mixer"
  - "mixer_core.KbmagAgent, StdioAgent — agent descriptors"
  - "mixer_core.ThresholdScheduler, PeriodicScheduler, CompositeScheduler — scheduler descriptors"
  - "mixer_core.AgentState, MixerResult — result types"
  - "Rust crate (mixer-core/) — internal; also used by Rust experiment binaries directly"
related:
  - mixer-core-engine
  - scheduler
  - transport
  - pyo3-bindings
  - braid-reduce
  - reduce-coreless
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# Mixer Core — component family overview

## What it is

`mixer-core/` is a Rust crate with pyo3 Python bindings that provides the orchestration engine for multi-agent Knuth-Bendix experiments. It manages agent processes, mediates item (rule) transfers between them, drives schedulers that decide when to inject, and provides a structured event log of the run. The Python package `mixer_core` is the primary interface for experiment scripts.

## Why it exists

Experiment scripts for B(4,3), B(5,3), and other groups need to coordinate multiple `kbprog` processes running different orderings and inject rules from one into another at the right moment. Without a shared engine, each experiment script reimplements subprocess management, scheduling logic, and file I/O. `mixer-core` factored this out into a reusable Rust core with Python bindings so experiments can focus on the domain logic (what to inject, when) rather than the plumbing.

## Directory structure

```
mixer-core/
├── src/
│   ├── mixer/         ← the orchestration engine (Mixer, MixerBuilder, MixerResult)
│   ├── scheduler/     ← scheduler trait + ThresholdScheduler, PeriodicScheduler, CompositeScheduler
│   ├── transport/     ← Transport trait + StdioTransport, KbmagLegacyTransport
│   ├── protocol/      ← JSON-lines wire protocol (Request/Response message types)
│   ├── kbmag/         ← KB-specific utilities: overlap scoring, inverse expansion, transform builder
│   ├── pyo3_bindings/ ← Python bindings (the mixer_core module)
│   ├── types.rs       ← AgentId, Item, AgentState
│   ├── event.rs       ← MixerEvent (Started, Tick, Injection, AgentComplete, Finished, Error)
│   ├── transform.rs   ← TransformFn type alias, TransformResult
│   ├── error.rs       ← MixerError enum
│   └── experiment.rs  ← logging helpers (timestamped stderr)
├── python/
│   └── mixer_core/    ← Python package (mixer_core.cpython-*.so + __init__.py + stubs)
└── examples/          ← Example Rust binaries (b43_experiment.rs, etc.) — not entry points for active experiments
```

## How to use from Python

```python
from mixer_core import (
    Mixer, KbmagAgent, StdioAgent,
    ThresholdScheduler, PeriodicScheduler, CompositeScheduler,
)

mixer = Mixer(run_dir="runs/", poll_interval_ms=5, timeout_secs=120)
mixer.add_kbmag_agent("rpo", KbmagAgent(ordering="recursive", binary="...", input_file="..."))
mixer.add_kbmag_agent("slex", KbmagAgent(ordering="shortlex", binary="...", input_file="..."))
mixer.on_kb_burnside_transfer("slex", "rpo", num_generators=4, exponent=3)
mixer.set_threshold_scheduler(ThresholdScheduler("slex", "rpo", threshold=20000, max_items=80))
mixer.terminate_when(lambda states, elapsed: "done" if states["rpo"].get("is_confluent") else None)
result = mixer.run()
```

## Build

```bash
uv sync          # triggers maturin to recompile mixer-core Rust crate and install Python package
cargo test -p mixer-core   # run Rust unit tests
cargo clippy --all-targets # lint
```

The Python package is installed into the `uv` virtualenv as an editable extension via `[tool.uv.sources]` in the workspace `pyproject.toml`. After `uv sync`, `import mixer_core` works from any script in the workspace.

## Subsystem notes

- [[mixer-core-engine]] — the `Mixer` orchestrator: agent lifecycle, tick loop, `execute_directive`
- [[scheduler]] — `Scheduler` trait, `ThresholdScheduler`, `PeriodicScheduler`, `CompositeScheduler`
- [[transport]] — `Transport` trait, `StdioTransport`, `KbmagLegacyTransport`
- [[pyo3-bindings]] — how the Python API surface is generated from the Rust types

## Also in Mixer Core

- [[braid-reduce]] — Rust binary for B(2,5) word reduction with beam search; lives in `experiments/burnside/burnside_bidirectional/` but is logically a Mixer Core deliverable
- [[reduce-coreless]] — Python word-reduction utility layer (pre-processing stage before braid-reduce)
