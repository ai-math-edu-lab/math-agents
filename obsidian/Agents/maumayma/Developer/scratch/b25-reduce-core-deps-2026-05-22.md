---
name: b25-reduce-core-deps-2026-05-22
description: Phase 1 dependency trace from experiments/b25_reduce_core/ — all external binaries, repo-internal imports, and data files touched
metadata:
  type: project
  agent: Developer
  date: 2026-05-22
tags: [agent/dev, user/maumayma, domain/infra, project/b25, status/draft]
---

# Phase 1 — Dependency Trace: `experiments/b25_reduce_core/`

Traced from: `README.md`, all Python files in `experiments/b25_reduce_core/` and `experiments/b25_reduce_core/benchmark_run/`, and all shell scripts in those directories. Archive contents were **not** traced (per scope: archive/ is not "directly used").

---

## A. External Binaries

### 1. `kbprog` — KBMag Knuth-Bendix prover

**Invoked by:** `run_biased_agents.sh` (only; no Python script calls kbprog directly)

**Path used:**
```
/Users/maumayma/Desktop/reps/algo_mixing/kbmag_source/standalone/bin/kbprog
```
Confirmed present at that path.

**Also exists at:** `kbmag_v1/standalone/bin/kbprog` — present but NOT referenced by any traced file.

**Command-line flags passed:**
```
kbprog -v -me <maxeqns> -ms 500000000 -t <tidyint> -cn <confnum> \
       -sw <target.txt> -sp <fraction> -sk <kgram_size> <input_dir>
```
- `-v` verbose
- `-me` max equations (50,000,000 in all agents)
- `-ms` max states (500,000,000)
- `-t` tidy interval (5000)
- `-cn` confluence number (5000)
- `-sw <file>` "search word": biases rule selection toward rules whose LHS matches k-grams of `target.txt`
- `-sp <prob>` probability of prioritising a "special" (target-overlapping) equation each tidy cycle
- `-sk <k>` k-gram size for special equation selection (6 or 8)

**Input format:** a KBMag presentation file (text); see `kbmag_source/standalone/kb_data/b25_lifted` for the specific file used.

**Output:** `input.kbprog.live` — a growing file of rewrite rules in `LHS -> RHS` format, written into the working directory. Readable while kbprog is still running.

---

### 2. `braid_reduce` — Rust word-reduction binary

**Invoked by:** `reduce_benchmark.py`, `reduce_benchmark_v2.py`, `run_full_logged.py`, `overnight_4pass_smallfirst.sh`, `overnight_6pass.sh`, `remaining_4pass.sh`, `retry_failed.sh`, `run_logged.sh`, `run_traced.sh`

**Actual binary path (confirmed present):**
```
experiments/burnside/burnside_bidirectional/target/release/braid_reduce
```

**Stale path (referenced in several scripts, confirmed MISSING):**
```
experiments/burnside_bidirectional/target/release/braid_reduce
```
Scripts using the stale path: `overnight_4pass_smallfirst.sh`, `overnight_6pass.sh`, `remaining_4pass.sh`, `reduce_benchmark.py`, `reduce_benchmark_v2.py`. These would fail unless the old path is restored by a build.

**Source:** `experiments/burnside/burnside_bidirectional/src/bin/braid_reduce.rs` (verified).

**Command-line flags observed:**
```
braid_reduce --word-file <file> --exponent 5 --rules-file <rules.live> \
             [--beam-width N] [--beam-secs N] [--no-beam] \
             [--num-passes N] [--output <file>] [--trace-file <file.json>]
```
- `--exponent 5` — Burnside group exponent (B(2,5))
- `--rules-file` — `.live` rule bank file
- `--beam-width` / `--beam-secs` — beam search parameters
- `--no-beam` — braid+power reduction only, no beam search
- `--num-passes` — run N passes (AC built once, reused)
- `--trace-file` — output per-step JSON trace
- `LOG_RULES=1`, `LOG_ALL_BEAM=1` env vars enable structured rule-application logging to stderr (parsed by `run_full_logged.py`)

---

## B. Python Modules Imported from the Repo

Only one repo-internal import found (everything else is stdlib or third-party):

| Import | Source file | Imported by |
|--------|-------------|-------------|
| `reduce_coreless` | `experiments/b25_reduce_core/reduce_coreless.py` | `reduce_benchmark.py`, `reduce_benchmark_v2.py`, `run_full_logged.py` |

Import mechanism: `sys.path.insert(0, '.../experiments/b25_reduce_core')` then `import reduce_coreless as rc`.

Functions used from `reduce_coreless`:
- `rc.free_reduce(w)` — stack-based free cancellation
- `rc.power_reduce(w)` — replaces `g^k` runs using B(2,5) identity `g^5 = e`
- `rc.braid_reduce_fast(w)` — replaces alternating runs of length ≥ 6 using `(gh)^5 = e` (FIXED version; see memory note on non-abelian inverse order bug)

**Third-party packages** (not repo-internal, recorded for completeness):
- `ahocorasick` (pyahocorasick) — used by `analyze_rules.py` and `trace_reduction.py` for Aho-Corasick pattern matching over rule banks

---

## C. Data Files Referenced from the Repo

### C1. Input presentation file (KBMag format)

| File | Path | Status | Used by |
|------|------|--------|---------|
| `b25_lifted` | `kbmag_source/standalone/kb_data/b25_lifted` | **Present** | `run_biased_agents.sh` |

This file defines B(2,5) extended with lifted generator `m = X⁻¹bX` where X is the 35-char core. It specifies generator order `[a,A,b,B,m,M]`, inverses, and 4435 equations (all `w^5=1` for `|w|≤7`, plus 2 linking `m` to `a,b`, plus 61 power relations involving `m`).

For RPO runs, `run_biased_agents.sh` modifies it in-place via `sed` to change `ordering := "shortlex"` → `ordering := "recursive"`.

### C2. Rule banks (`.live` files)

| File | Path | Status | Used by |
|------|------|--------|---------|
| `mega_ab_rules.live` (2.5 GB) | `experiments/b25_reduce_core/benchmark_run/rule_banks/mega_ab_rules.live` | **Present** | `analyze_rules.py`, `trace_reduction.py`, all beam shell scripts |
| Per-run rule banks (17 files) | `runs/b25/<timestamp>/{kb_shortlex,kb_wtlex,kb_rpo}/input.kbprog.live` | At least `runs/b25/20260320_054109/kb_shortlex/input.kbprog.live` confirmed present | `reduce_coreless.py` |
| Biased-run rule banks (5 dirs) | `experiments/b25_reduce_core/runs/{rpo_core_a,sl_boundary,sl_core_a,sl_core_a_plus_a,sl_prefix}/input.kbprog.live` | Produced by `run_biased_agents.sh`; not verified present | `reduce_coreless.py` |
| `filtered_rules.live` | `experiments/b25_lifted_kb/filtered_rules.live` | **MISSING** from repo | `reduce_benchmark_v2.py` (lifted rules for `{a,b,m}` alphabet) |

### C3. Target word files

| File | Path | Status | Used by |
|------|------|--------|---------|
| `word_coreless.txt` | `experiments/b25_reduce_core/word_coreless.txt` | **MISSING** (not committed) | `reduce_coreless.py` (input), `verify_reduction.py` (verification) |
| `word_7264.txt` | `experiments/b25_reduce_core/word_7264.txt` | **MISSING** | `verify_reduction.py` |
| `word_544.txt` | `experiments/b25_lifted_kb/word_544.txt` | **MISSING** | `run_biased_agents.sh` (copied to `targets/`) |
| `comm_*.txt` (119 files) | `experiments/b25_reduce_core/benchmark_run/words/` | Present (directory exists) | `analyze_rules.py`, `trace_reduction.py`, all beam shell scripts |

### C4. Other data files

| File | Path | Status | Used by |
|------|------|--------|---------|
| `comm_12_9_reduced_data.json` | `ui/comm_12_9_reduced_data.json` | **Present** | `verify_reduction.py` (reads `lifted_word`, `core`, `core_alt`, `rpo_discovery.*`) |
| `benchmarks_data.json` | `ui/benchmarks_data.json` | **Present** | `collect_best.sh` (reads + updates benchmark scores) |
| `result_coreless_reduced.txt` | `experiments/b25_reduce_core/result_coreless_reduced.txt` | **MISSING** | `verify_reduction.py` (comparison target) |
| `result_combined.txt` | `experiments/b25_reduce_core/result_combined.txt` | **MISSING** | `reduce_coreless.py` (optional comparison) |

---

## D. Broken Path Summary

Two distinct issues found during trace:

**Issue 1 — Stale `braid_reduce` path in most scripts:**
- Expected: `experiments/burnside/burnside_bidirectional/target/release/braid_reduce`
- Broken reference in: `overnight_4pass_smallfirst.sh`, `overnight_6pass.sh`, `remaining_4pass.sh`, `reduce_benchmark.py`, `reduce_benchmark_v2.py`
- Working reference in: `retry_failed.sh`, `run_logged.sh`, `run_traced.sh`, `run_full_logged.py`
- Impact: those scripts would fail unless `experiments/burnside_bidirectional/` is rebuilt or symlinked

**Issue 2 — Missing data files (not committed):**
- `word_coreless.txt`, `word_7264.txt`, `result_coreless_reduced.txt`, `result_combined.txt` in `experiments/b25_reduce_core/`
- `experiments/b25_lifted_kb/filtered_rules.live` and `word_544.txt`
- These are large derived data files; their absence means `reduce_coreless.py` and `verify_reduction.py` cannot run from a clean checkout

---

## E. Component Summary (for Phase 2 scope)

Components confirmed **in-use** by this trace:

1. **`kbmag_source/standalone/bin/kbprog`** — the KBMag kbprog binary, called directly from shell
2. **`kbmag_source/standalone/kb_data/b25_lifted`** — KBMag input presentation for B(2,5) lifted
3. **`experiments/burnside/burnside_bidirectional/` (specifically `braid_reduce` binary)** — Rust word-reduction engine
4. **`ui/comm_12_9_reduced_data.json`** — source-of-truth for the comm_12_9 reduction chain
5. **`ui/benchmarks_data.json`** — benchmark scoreboard
6. **`runs/b25/`** — pre-generated rule banks consumed by `reduce_coreless.py`

Components **not touched** by this trace (Phase 3 candidates):
- `mixer-core/` (Rust engine, pyo3 bindings, schedulers, transports)
- `api/`
- `orchestrator/`
- `legacy/`
- `patterns/`
- `kbmag_v1/` (exists, not referenced by any traced file)
- `kbmag_source/` except `standalone/bin/kbprog` and `standalone/kb_data/b25_lifted`
- `checkpoints/`, `docs/`, `examples/`, `tests/` (repo-level)
