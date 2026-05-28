---
tags: [agent/dev, meta]
---

# Developer — home (Math)

Role definition: `_meta/agents/developer.md`.

## What lives here
- [[log]]
- `scratch/` — patch plans before implementation
- `test-output/` — full captured test runs (link, don't paste)
- Component docs → `Architecture/Components/`
- Productized `mixer Agent` docs → `Strategies/Existing/`

## Working state
- Active branch:
- Awaiting review:
- Lead's last verdict:

## Stack
- Python 3.14+ (orchestration, `mixer Agent` subclasses, experiments)
- Rust + pyo3 (`mixer-core/`)
- Build: `uv sync` (triggers `maturin` for Rust)
- Test: `cargo test -p mixer-core` + `uv run pytest` + smoke `uv run python examples/sorting/run.py`

## Caution areas
- KBMAG (`kbmag_v1/`, `kbmag_source/`) — read-only by default
- pyo3 ABI — don't break without migration plan
- Mixer JSON-lines protocol — backwards-compat unless human accepts a break
