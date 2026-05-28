---
title: 2026-05-22-stale-component-inventory
author: maumayma
status: draft
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft, review]
---

# Stale-Component Inventory — 2026-05-22

Scope: every meaningful subsystem NOT in the Phase 1 dependency trace from `experiments/b25_reduce_core/`. Source: [[b25-reduce-core-deps-2026-05-22]].

"Not in the trace" means: not touched by b25_reduce_core directly or transitively. It does NOT mean globally dead; several subsystems listed here are load-bearing for other experiments.

Four categories below. For each entry: path, one-line description (from code), evidence of non-use by b25_reduce_core, recommendation.

---

## 0. Active project infrastructure (outside b25_reduce_core scope — not stale)

Components that are not in the b25_reduce_core dependency tree but are actively load-bearing for the broader project. Listed here only to account for them; no remediation needed.

---

### `kbmag_v1/`

**Path:** `kbmag_v1/`

**Description:** The project-wide main KBMag installation. `kbmag_v1/standalone/bin/kbprog` is the compiled binary. Package directory contains `standalone/`, `gap/`, `doc/`, `tst/`.

**Evidence not used by b25_reduce_core:** No file in the b25_reduce_core dependency tree references this path. The installation referenced by `run_biased_agents.sh` is `kbmag_source/standalone/` (an older installation kept specifically for that biased-KB workflow).

**Globally active (confirmed by human 2026-05-22):** `kbmag_v1/` is the **current/latest KBMag version** — the project main. It is used in bidirectional search alongside Rust, B(4,3)/B(5,3) mixing, SL series, Gröbner experiments, and B(2,5) KBMag mixing scripts (`experiments/burnside/b25_kbmag/`, intentionally untracked in git — code is still dirty; do not commit). `kbmag_source/` is a secondary, older installation retained only for the narrow biased-KB B(2,5) path.

**Recommendation:** No action. `kbmag_v1/` is the project main; do not delete or treat as stale. For the full picture see [[kbmag-overview]] (KBMag directory overview).

---

## 1. Stale-but-might-revive

Components that were clearly used in earlier experiments or for related problems, are structurally sound, and could plausibly re-enter active use — but are not currently load-bearing for b25_reduce_core.

---

### `api/` — KBAgent wrappers

**Path:** `api/` (3 files: `agent.py`, `burnside_rules.py`, `kbmag_agent.py`)

**Description:** Python wrappers for running KBMag as a managed subprocess (`KBAgent`, `KBMAGAgent V2`) and initial Burnside group relation tables (`burnside_rules.py`). `kbmag_agent.py` docstring: "KBMAGAgent V2 - KBMAG C binary wrapping with live rule reading and injection."

**Evidence not used by b25_reduce_core:** b25_reduce_core scripts invoke kbprog directly via shell (not through these wrappers). No file in the trace imports from `api/`.

**Recommendation:** Stale-but-might-revive. These wrappers represent an earlier attempt at a managed agent interface for kbprog. If b25_reduce_core ever moves from direct shell invocation to a Python-orchestrated approach, these would be the natural starting point. Do not delete.

---

### `mixer-core/` — Rust mixer engine

**Path:** `mixer-core/` (Rust crate with pyo3 bindings, Python package)

**Subsystems:**
- `mixer-core/src/mixer/` — async_run, builder, config, run (the Mixer orchestrator)
- `mixer-core/src/scheduler/` — composite, periodic, threshold schedulers
- `mixer-core/src/protocol/` — wire protocol
- `mixer-core/src/transport/` — JSON-lines stdio transport
- `mixer-core/src/kbmag/` — kbmag integration layer
- `mixer-core/src/pyo3_bindings/` — Python bindings via pyo3
- `mixer-core/python/mixer_core/` — Python package

**Description:** The core mixer engine — manages Agent processes, schedules rule injection events, handles JSON-lines transport between processes.

**Evidence not used by b25_reduce_core:** None of the b25_reduce_core Python scripts import `mixer_core`; the pipeline is driven by direct subprocess calls and shell scripts.

**Recommendation:** Stale-but-might-revive. The mixer engine is the infrastructure the B(4,3) experiments (`experiments/b43_kbmag_mixing/`) use actively. For b25_reduce_core the experiments were built with direct shell + Python orchestration, bypassing mixer-core. Whether b25 experiments should be ported to use mixer-core is an open question. Do not archive.

---

### `orchestrator/`

**Path:** `orchestrator/v2/` and `orchestrator/old_rl/`

**Description:** Python orchestration layer. `v2/` appears to have no Python source files (only a `__pycache__` directory present). `old_rl/` is an older RL-based orchestrator.

**Evidence not used by b25_reduce_core:** No file in the trace imports from `orchestrator/`.

**Recommendation (confirmed by human 2026-05-22):** `v2/` is abandoned. Move to `legacy/` or delete when convenient. `old_rl/` — assumed abandoned alongside v2. No active work depends on either.

---

### `patterns/` — KB dynamics analysis scripts

**Path:** `patterns/` (`kb_dynamics.py`, `rule_graph_3d.py`, `deep_dive.py`, `rule_structure.py`, `rule_trie.py`, `internal_structure.py`, `full_comparative.py`, `analysis_results.json`)

**Description:** Standalone analysis scripts for studying Knuth-Bendix rule dynamics, rule graph structure, and comparative analysis across runs. Per brief scope: not documented as individual components; listed here as a path with description and recommendation.

**Evidence not used by b25_reduce_core:** No file in the trace imports from `patterns/`.

**Recommendation:** Stale-but-might-revive. These are analysis tools, not production components — running them when studying a new experiment's rule bank dynamics is reasonable. Do not delete; they contain substantial analysis logic. Not worth archiving.

---

### `checkpoints/` — RL model checkpoints

**Path:** `checkpoints/` (also `patterns/rl_mixer_*.pt` files)

**Description:** Saved PyTorch model weights for RL-based mixer agents.

**Evidence not used by b25_reduce_core:** No file in the trace references checkpoints or PyTorch.

**Recommendation:** Stale-but-might-revive if RL-based mixing is revisited. No action needed; `.pt` files are inert. Consider whether they are still reproducible (training code still present?).

---

### `runs/` (non-b25 content)

**Path:** `runs/` (contains `b25/` which IS in the trace, plus any other subdirectories)

**Description:** Top-level run output directory. `runs/b25/` holds the 6 timestamped rule bank directories consumed by `reduce_coreless.py` and IS in-use. Other potential subdirectories (if any) are outside the trace.

**Evidence:** `runs/b25/` is load-bearing; confirmed present. No other subdirectories were verified during the trace.

**Recommendation:** No action on `runs/b25/`. If other `runs/<group>/` directories exist, they are likely outputs of other experiments and should be left in place.

---

## 2. Genuinely Dead

Components that are explicitly superseded, renamed, or broken with no apparent plan to revive.

---

### `legacy/` (all subdirectories)

**Path:** `legacy/b43_kbmag_mixing_old/`, `legacy/b53_kbmag_mixing_old/`, `legacy/kbmag_debug/`, `legacy/old_kb/`, `legacy/_junk/`, `legacy/old/`, `legacy/orchestrator/`

**Description:** Archived old experiment code. `kbmag_debug/` was deleted from the main tree and moved here; `b43_kbmag_mixing_old` and `b53_kbmag_mixing_old` are superseded by current `experiments/b43_kbmag_mixing/` and `experiments/burnside/b53_bidir/`. `_junk/` is explicitly labelled.

**Evidence not used by b25_reduce_core:** No file in the trace references `legacy/`.

**Recommendation:** Genuinely Dead for active work. The value is historical reference. If the repo is cleaned up, these are safe to delete or move to a separate archive branch. Do not actively maintain.

---

### `kbmag_source/` non-standalone content

**Path:** `kbmag_source/gap/`, `kbmag_source/doc/`, `kbmag_source/tst/`, `kbmag_source/init.g`, etc.

**Description:** The KBMag GAP package files — the GAP (Groups, Algorithms, Programming) interface to KBMag. Only `kbmag_source/standalone/` is used by b25_reduce_core experiments.

**Evidence not used by b25_reduce_core:** No file in the trace references `kbmag_source/gap/` or the GAP package interface. GAP is invoked directly by `check_word.g` and `verify_confluence.g` at the repo root, not through `kbmag_source/gap/`.

**Recommendation:** Not dead globally — the GAP package is needed if using KBMag from within GAP. No action needed; it ships as part of the kbmag_source distribution. Document as "not touched by b25_reduce_core."

---

## 3. Unknown — Requires Human Input

Components where the code alone is insufficient to determine active vs. dormant status.

---

### `ui/` HTML dashboards

**Path:** `ui/` (`benchmarks.html`, `comm_12_9_reduced.html`, `comm_12_9.html`, `comm_13_10.html`, plus JSON data files)

**Description:** HTML visualization dashboards for benchmark results and commutator word analysis. The JSON data files `benchmarks_data.json` and `comm_12_9_reduced_data.json` ARE in-use (consumed by `collect_best.sh` and `verify_reduction.py` respectively). The HTML files themselves are not touched by the b25_reduce_core dependency tree.

**Evidence:** HTML files not referenced by any traced script. JSON files are in-use.

**Recommendation (confirmed by human 2026-05-22):** Most HTML dashboards are in active use. JSON data files (`benchmarks_data.json`, `comm_12_9_reduced_data.json`) are live and consumed by scripts. No action needed.

---

### `docs/`

**Path:** `docs/`

**Description:** Documentation directory. Contents not enumerated during trace.

**Evidence:** Not referenced by any file in the b25_reduce_core dependency tree.

**Recommendation:** Unknown. May contain project documentation that is still current or may be stale. Quick human review would resolve.

---

### `examples/`

**Path:** `examples/`

**Description:** Example scripts / experiment harnesses. `mixer-core/examples/b43_experiment.rs` appears to reference `kbmag_v1/`, suggesting at least one example drives the B(4,3) experiments.

**Evidence:** Not referenced by b25_reduce_core dependency tree.

**Recommendation (confirmed by human 2026-05-22):** `mixer-core/examples/b43_experiment.rs` is **not** the current entry point for B(4,3) experiments. Examples directory is not load-bearing for active work. Classify as Genuinely Dead until proven otherwise.

---

### `tests/` repo-level (non-b25-methodology)

**Path:** `tests/special_mixer/` (specifically `reduce_word.py`, `inject_special_rules.sh`, `run_special_mixer.sh`, etc.)

**Description:** `tests/special_mixer/` contains a mixer experiment for `comm_13_10` reduction — it shows signs of active recent use (many log files, bootstrap files, run directories). `reduce_word.py` is a standalone Aho-Corasick-based word reducer with depth-1 search.

**Evidence of non-use by b25_reduce_core:** Not imported or called by any file in the b25_reduce_core trace.

**Recommendation (confirmed by human 2026-05-22):** Archived. `tests/special_mixer/` is no longer active. Safe to move to `legacy/` if the repo is cleaned up.

---

## Open Questions for Human

All questions from initial draft resolved on 2026-05-22.

1. **kbmag_v1/ vs kbmag_source/**: `kbmag_v1/` is the current/latest version (bidir search + Rust). `kbmag_source/` is older, kept for b25_reduce_core biased agents. Both needed. ✓
2. **orchestrator/v2/**: Abandoned. ✓
3. **ui/*.html dashboards**: Most in active use. ✓
4. **tests/special_mixer/**: Archived. ✓
5. **tests/ ordering-sweep group ambiguity**: General-purpose tests, not B(4,3)-specific. ✓
6. **tests/containment-verification.py**: No active script depends on archived copies. ✓
7. **experiments/burnside/b25_kbmag/ untracked**: Intentional — code still dirty. Do not commit. ✓

All questions fully resolved. No open items.
