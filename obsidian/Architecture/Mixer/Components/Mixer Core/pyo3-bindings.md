---
title: pyo3-bindings
path: mixer-core/src/pyo3_bindings/
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "mixer_core.Mixer — Python class, builder-style, wraps MixerBuilder + Mixer::run()"
  - "mixer_core.KbmagAgent(ordering, binary, input_file, tidyint, maxeqns, maxstates, confnum) — agent descriptor"
  - "mixer_core.StdioAgent(command, args) — agent descriptor for JSON-lines agents"
  - "mixer_core.ThresholdScheduler(from_agent, to_agent, threshold, max_items, min_source_items)"
  - "mixer_core.PeriodicScheduler(from_agent, to_agent, threshold, batch_fraction, min_batch, max_batch, min_source_items, period_secs)"
  - "mixer_core.CompositeScheduler() — .add_threshold(), .add_periodic()"
  - "mixer_core.AgentState — .iteration, .item_count, .is_complete, .metadata (dict), .is_confluent"
  - "mixer_core.MixerResult — .elapsed_secs, .reason, .agent_states, .events_json"
  - "mixer_core.log(msg) — timestamped stderr log"
  - "mixer_core.print_result(result) — human-readable run summary to stderr"
invariants:
  - id: py-allow-threads
    summary: "Mixer.run() calls py.allow_threads(|| mixer.run()) to release the GIL for the duration of the Rust run loop."
    why: "The mixer poll loop sleeps poll_interval_ms between ticks. Without releasing the GIL, those sleeps would block all other Python threads. More importantly, Python callable transforms (registered via on_transfer()) re-acquire the GIL for each call. GIL release + re-acquire on each transform call is the correct pattern; holding the GIL throughout would deadlock if the transform runs in a separate Python thread."
  - id: edge-drain
    summary: "Mixer.run() drains self.agents, self.edges, self.kb_edges, and self.scheduler via .drain() and .take() — the Mixer object cannot be reused after run()."
    why: "The Rust MixerBuilder takes ownership of factories (closures). Python cannot represent Rust ownership; instead, the Python Mixer stores entries in Vecs and drains them into the builder on run(). After run(), the Vecs are empty. Calling run() again would find no agents/edges/scheduler and raise PyValueError('No scheduler configured')."
  - id: metadata-flattened
    summary: "In Python termination predicates, agent state is a flat dict: metadata fields are merged into the state dict alongside iteration/item_count/is_complete."
    why: "Python callers access KB-specific fields like `states['rpo']['is_confluent']` or `states['rpo']['rules_count']` directly, without a nested .metadata dict. The binding code merges all metadata JSON fields into the state dict. Callers must not assume a .metadata sub-key exists."
related:
  - mixer-core-engine
  - scheduler
  - transport
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# pyo3-bindings — Python interface for Mixer Core

## What it is

`pyo3_bindings/` generates the `mixer_core` Python extension module via pyo3. It wraps the Rust `MixerBuilder`/`Mixer`, all scheduler types, agent descriptors, and result types into Python classes. The compiled `.so` plus a thin `__init__.py` and type stubs (`.pyi`) are installed as the `mixer_core` package at `mixer-core/python/mixer_core/`.

## Why it exists

Experiment scripts are written in Python. The mixer engine is in Rust for performance (the scheduler tick and transport I/O must be fast). pyo3 provides the bridge: Rust types are exposed as Python classes with Python-idiomatic APIs, and Python callables (transforms, termination predicates) are called from Rust via `Python::with_gil()`. This lets experiments stay in Python while the hot plumbing runs in Rust.

## How it fits in the system

```
Experiment script (Python)
  import mixer_core
  → Mixer.add_kbmag_agent() → stores PyKbmagAgent in Vec
  → Mixer.on_kb_burnside_transfer() → stores kb_edge tuple in Vec
  → Mixer.set_threshold_scheduler() → stores scheduler entry
  → Mixer.run():
      → drains all stored entries into MixerBuilder
      → py.allow_threads(|| rust_mixer.run())  ← GIL released here
      → returns PyMixerResult
```

## Critical invariants — why each one exists

### py-allow-threads

The GIL is released for the entire duration of `mixer.run()`. Python callable transforms (registered via `Mixer.on_transfer()`) call `Python::with_gil()` each time they're invoked from the execute_directive loop. This round-trip (release → re-acquire per transform call) is the correct pattern. If GIL were held throughout, any Python-side callback that tries to import a module or run a timer would deadlock. The `py.allow_threads` call is the one line that makes Python callable transforms and Rust concurrent transport threads safe simultaneously.

### edge-drain

The Python `Mixer` class holds all configuration in `Vec`s and `Option`s. `run()` calls `self.agents.drain(..)`, `self.edges.drain(..)`, etc. to move data into the Rust builder. After `run()`, these collections are empty. The `Mixer` object becomes unusable. This mirrors the single-use constraint of the Rust `Mixer::run()` (see [[mixer-core-engine]]). Users should create a new `Mixer` for each run.

### metadata-flattened

The termination predicate receives `states: dict[str, dict]` where each inner dict has keys: `iteration`, `item_count`, `is_complete`, plus all metadata fields flattened in. For KB agents this means `is_confluent`, `states_count`, `elapsed_secs` are top-level dict keys, not under `metadata`. The `PyAgentState.is_confluent` property also provides direct access for the common case.

## Python package layout

```
mixer-core/python/mixer_core/
├── __init__.py          — re-exports from mixer_core .so
├── __init__.pyi         — stub for type checkers
├── mixer_core.pyi       — generated stubs for Rust classes
├── mixer_core.cpython-314-darwin.so  — compiled extension
├── agent.py             — AgentBase ABC (for pure-Python agents)
└── py.typed             — PEP 561 marker
```

`agent.py` defines the `AgentBase` ABC for pure-Python agents that communicate with the mixer via the StdioTransport JSON-lines protocol. Agents subclass `AgentBase` and implement `work()`, `get_items()`, `inject()`, `get_state()`.

## Build

```bash
uv sync        # invokes maturin; recompiles .so if Rust source changed
# or directly:
cd mixer-core && maturin develop --uv
```

The ABI tag `cpython-314-darwin` is Python-version and OS specific. After a Python upgrade, `uv sync` must re-run to rebuild against the new interpreter.

## Related

- [[mixer-core-engine]] — the Rust Mixer that PyMixer wraps
- [[scheduler]] — Rust scheduler types exposed as Python classes
- [[transport]] — KbmagLegacyTransport and StdioTransport are the Rust backends for KbmagAgent and StdioAgent

## Known issues

- Changing the pyo3 ABI (adding/removing/renaming classes or method signatures) requires a `uv sync` on all development machines. There is no version guard in the `.so` that prevents using an old binary with new Python code.
- `agent.py`'s `AgentBase` ABC is not tested by the Rust test suite; it is exercised only by experiment-level integration tests.
