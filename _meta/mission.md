---
tags: [meta, mission]
---

# Math vault — Mission

> The North Star. Every agent reads this each session. If the mission changes, edit here first; everything else follows.

## What this vault is

**A multi-domain research wiki** for the algorithmic-mixing research circle. Contributors come from different fields (group theory, biology, SAT, Gröbner bases, AI, more) and share:

1. **The `algo_mixing` codebase** — the Mixer framework + per-domain experiments.
2. **This Obsidian vault** — durable knowledge across all those domains, organized for both humans and AI agents.

Repo: `/Users/maumayma/Desktop/reps/algo_mixing`
Stack: **Python 3.14+** (orchestration, agent subprocesses) + **Rust** (mixer-core engine, pyo3 bindings, maturin build). `uv` for Python.

## The Mixer research program — three layers

### Layer 1 — General Mixer framework
The **Algo Mixer** runs multiple algorithms on the same problem and shares intermediate results between them. Generalizes the TimSort insight (merge sort + insertion sort cooperate) to **arbitrary algorithm combinations with configurable sharing policies**.

Research questions at the framework layer:
- Does mixing accelerate convergence in general?
- What scheduling policies (threshold vs periodic vs adaptive) help most, for which algorithm pairs?
- Can mixing produce qualitative behavior no single algorithm exhibits (basin-hopping, escape from local optima)?
- What's the cost model? When does coordination overhead exceed cooperation benefit?

### Layer 2 — B(2,5) flagship hard problem
**B(2,5)** — the free Burnside group on 2 generators of exponent 5 — is our hardest open problem and the workload that drives framework evolution. A dedicated **`Experimenter-B25`** agent obsesses over it: knows the literature deeply, runs modified Mixer code with B(2,5)-specific tweaks (custom schedulers, custom transforms tuned for word-problem search), tracks progress in a standing note.

If a feature exists in the Mixer that helps B(2,5), B(2,5) usually finds it first.

### Layer 3 — Cross-domain Mixer applications
The Mixer's value scales with the number of domains it fits. **Researcher** scans literature across many domains looking for Mixer-shaped problems. When a candidate looks viable, a per-domain **Experimenter** spawns to stress-test the framework on that domain. Confirmed candidates so far: Gröbner bases, SAT solvers, biology (protein folding sampling, sequence analysis).

Cross-domain work both validates the framework and exposes gaps in it.

## Terminology disambiguation

The word **"agent"** is overloaded:

- **`algo_mixer.Agent`** — a *subprocess* implementing the mixer protocol (an algorithm instance: a sorter, a KB engine, a SAT solver). Code-level concept.
- **AI agent** — an LLM on the Maestri canvas (Lead, Researcher, Developer, Experimenter, Experimenter-B25, Validator). Six roles.

Throughout this vault, **"agent" with no qualifier means the AI agent on the canvas**. When referring to the code-level concept, write **`mixer Agent`** or **algorithm subprocess**.

## Engineering invariants

- **`uv sync` must succeed** on a clean clone. If a change breaks `uv sync`, that's a regression.
- **`uv run python examples/sorting/run.py` must pass** as the smoke test.
- **mixer-core Rust ABI**: don't break the pyo3 bindings without a Lead-approved migration plan.
- **JSON-lines protocol** between mixer and `mixer Agents` (subprocesses): backwards-compatible additions OK, breaking changes are userspace breaks.

## What "good" looks like

Across all three layers:

- **Pre-registered** experiments with falsifiable hypotheses and termination criteria, *before* runs.
- **Provenance triple** on every `runs/` output (git SHA + `uv.lock` hash + experiment script version).
- **Single-algorithm baselines** for every cooperation-gain claim. No baseline → no claim.
- **n ≥ 5 seeds** for any quantitative claim about cooperation gain.
- **Independent verification** of math results: GAP/Sage for symbolic, kbmag_v1 standalone for KBMag comparisons, property tests for code that implements math, hand proofs where rigor is needed. **Validator owns this layer.**

## Hot paths

CPU-bound, latency-sensitive parts of mixer-core:
- `mixer-core/src/` Rust engine (Knuth-Bendix runners can run for hours; constant factors matter)
- Transport layer (stdin/stdout JSON-lines + file I/O for KBMAG)
- Scheduler tick loop (`mixer-core/src/scheduler/`)

Not hot (clean readable code wins): Python orchestration, experiment harnesses, analytics, one-shot scripts.

## Roles on the canvas

Six AI agents. [[lead|Lead]] is your interface and the only agent that commits code. See `_meta/agents/` for each role's prompt and `_meta/canvas-setup.md` for canvas assembly.

- **[[lead|Lead Dev]]** — orchestrator, validator (code quality), only agent that commits code.
- **[[researcher|Researcher]]** — literature scan across domains, paper summaries, OCR of old papers (via `nuextract-cli` when image-only), restructure-authority over `Research/` and `Concepts/`.
- **[[developer|Developer]]** — Python + Rust + frameworks. Knows pyo3, async, performance tools. Ships mixer-core changes, mixer Agents, schedulers, transforms.
- **[[experimenter|Experimenter]]** — general experimenter for non-B(2,5) work and cross-domain explorations. Owns autoresearch.
- **[[experimenter-b25|Experimenter-B25]]** — B(2,5) specialist. Standing focus. Owns `Experiments/Group Theory/Burnside Group/B25/**`.
- **[[validator|Validator]]** — independent math oracle. Proves theorems, catches math bugs (like the abelianization bug), writes property tests and proof sketches. Verdict on math correctness overrides everyone except the human.

## Decision-making

The **human** is the final authority on:
- Research direction
- Algorithm choices (which mixer Agents to combine)
- Commits to `main`
- Dependency additions
- Public API / mixer protocol / on-disk-format changes

**Lead Dev** is the final authority on:
- Code quality (`MERGE` / `NEEDS WORK` / `REJECT`)
- Routing work between peers

**Validator** is the final authority on:
- Whether a math result is sound (`#status/proven`, `#status/conjectured`, `#status/disproven`)
- Even Lead defers to Validator on math correctness. Only the human can override Validator.

## Multi-user, multi-domain norms

This vault is shared. Norms:

- **Every note carries `#user/<handle>` + `author: <handle>`** (the human who owns it, even if AI-written). See [[tags]].
- **`#domain/*` and `#project/*` are orthogonal**: a single note can be `#domain/group-theory + #project/b25` (group-theory note about B(2,5) Mixer work) or `#domain/group-theory + #project/none` (general group-theory knowledge unrelated to any Mixer subproject).
- **Cross-domain shared knowledge lives in `Concepts/`**: methodology, scheduler theory, reusable patterns. Don't duplicate it into each domain.
- **People** get a `People/<handle>.md` note: who they are, what they work on, key contributions. The wiki has a human index.
- **Researcher may retag/move any note in `Research/` or `Concepts/`** when a better organization emerges. Logs every restructure. This authority is unique to Researcher; other agents only touch their own home dirs.
