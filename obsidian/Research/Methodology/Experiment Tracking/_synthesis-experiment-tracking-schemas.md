---
title: "Synthesis — Experiment-tracking schema proposal for the Mixer repo (W1, June 2026)"
author: maumayma
language: en
domain: methodology
status: draft
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/experiment-tracking
  - topic/reproducibility
  - synthesis
  - status/draft
papers_synthesized:
  - "[[mlflow]]"
  - "[[wandb]]"
  - "[[hydra]]"
  - "[[dvc]]"
key_concepts: []
date_range: 2017 to 2024
project: mixer-core
---

# Synthesis — Experiment-tracking schema proposal for the Mixer repo (W1, June 2026)

> **Status: PROPOSAL — read-only.** No files in `experiments/` or `runs/` are moved or modified by this synthesis. Maria reviews before any adoption. Output is a written proposal only.
>
> **Seed**: extends the existing schema at `experiments/g_kbmag/runs_g5_mix/results.json`. **Does not reinvent** — adds provenance and namespacing on top of what's already there.
>
> **Cross-links**: B25 rule-mixing is a combinatorial-search-parameter problem — the params space is exactly what [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] describes. Tracking params is tracking the combinatorial search configuration.

## The question

What schemas for `params.json` and `results.json` should the Mixer repo adopt, and what vault frontmatter structure enables Obsidian Bases views to table params across runs?

## Sources reviewed

1. [[mlflow]] — MLflow (2018): Experiment/Run/Params/Metrics/Artifacts hierarchy; offline-first; flat params with dotted-key convention for namespacing.
2. [[wandb]] — W&B (2018): cloud-first with native nested config dicts; strongest sweep management; design inspiration for namespace blocks.
3. [[hydra]] — Hydra (2019): structured config composition via Python dataclasses; auto-saved config per run; `--multirun` for grid sweeps.
4. [[dvc]] — DVC (2017): git-native artifact versioning; `params.yaml` / `metrics.json` conventions; complementary to MLflow for large artifacts.

## Convergence from tools

All four tools converge on the same abstraction:
1. **Params** = what goes in (config, hyperparams). Captured before the run starts.
2. **Metrics/Results** = what comes out. Captured after the run finishes.
3. **Provenance** = linking a run to its code (git SHA) and inputs (param hash or run ID).

The tools differ on where they store params (flat vs. nested), how they compare runs (local UI vs. cloud dashboard), and how they version large artifacts.

---

## Section 1 — Proposed `params.json` schema

**Seeded from**: existing TOML configs (`experiments/burnside/burnside_bidirectional/configs/b43/rpo.toml`) + the proposed common keys from the brief.

**Design principles** (from Hydra and W&B):
- Namespaced blocks prevent collisions when engines share key names (both KBMAG and Mixer have a "timeout" concept).
- Common top-level keys are flat for easy Bases filtering.
- Per-engine blocks are nested dicts for extensibility.
- `git_sha_or_local` is the reproducibility anchor.

```json
{
  "experiment_id": "b43-kbmag-mixing-v10d-001",
  "engine": "mixer",
  "target": "b43",
  "git_sha_or_local": "abc123def456",
  "params": {
    "kbmag": {
      "cn": 100000,
      "me": null,
      "ms": null,
      "tidyint": 1000,
      "ordering_primary": "recursive",
      "ordering_secondary": "shortlex"
    },
    "mixer": {
      "injection_threshold_rules": 20000,
      "batch_size": 80,
      "scoring": "overlap-count",
      "cooldown_s": null,
      "max_injections": null
    },
    "beam": null
  }
}
```

**`params.beam` block** (populated — see W2 inventory Section 4b and `tests/special_mixer/mixer_config.toml`):

```json
{
  "experiment_id": "b25-reduce-core-beam-0001",
  "engine": "beam",
  "target": "b25",
  "git_sha_or_local": "local-2026-04-10T01:23:00",
  "params": {
    "kbmag": null,
    "mixer": null,
    "beam": {
      "beam_width": 1024,
      "beam_max_steps": 20000,
      "beam_fwd_overlapping": 256,
      "beam_inv_overlapping": 128,
      "beam_time_budget_secs": 60,
      "ordering": "shortlex",
      "input_rule_banks": [
        "runs/b25/20260320_054109/kb_shortlex/input.kbprog.live",
        "runs/b25/20260320_054109/kb_rpo/input.kbprog.live"
      ],
      "seed_word_file": "experiments/b25_reduce_core/word_coreless.txt"
    }
  }
}
```

Field origins (from codebase + W2 inventory):
- `beam_width` / `beam_max_steps` / `beam_fwd_overlapping` / `beam_inv_overlapping` / `beam_time_budget_secs`: directly from `[reducer]` section of TOML config (e.g., `tests/special_mixer/mixer_config.toml`). `beam_max_steps` is the search depth.
- `ordering`: from the `[[kb_agent]].ordering` field (which ordering the beam reducer uses to produce candidates).
- `input_rule_banks`: list of `.live` rule bank paths consumed by the beam search. From `reduce_coreless.py`'s `RULE_FILES` list. For b25 reduce-core runs these are the KB rule banks from `runs/b25/*/kb_*/` directories + `b25_lifted_kb/filtered_rules.live` (~25.7M rules per W2 inventory).
- `seed_word_file`: path to the word being reduced (e.g., `word_coreless.txt` = the 28,652-char `[c12,c9]` word).

**Notes on other fields**:
- `engine`: `"mixer"` | `"kbmag"` | `"beam"` | `"reduce-core"` | `"bidirectional"`. Determines which `params.*` block is populated.
- `target`: `"b43"` | `"b25"` | `"b53"` | `"m23"` | `"g5"` | `"comm_12_9"` | etc. Maps to a relators file.
- `git_sha_or_local`: git SHA (full 40-char hex) for committed runs; `"local-<ISO8601>"` (e.g., `"local-2026-06-02T14:30:00"`) for uncommitted/development runs. ISO8601 is human-readable and lexicographic sort = chronological. *(Decision Q2: ISO8601 format confirmed.)*
- `experiment_id`: manual slug + 4-digit run counter (e.g., `"b43-mixing-v10d-0001"`). Grep-able, git-branchable, human-meaningful. *(Decision Q3: slug-plus-counter confirmed.)*
- `params.kbmag.cn`: the `-cn` flag in kbprog (confnum; tidy interval for the KB completion loop). Null means "use kbprog default." Field name uses CLI spelling per Phase C ratification.
- `params.mixer.scoring`: currently always `"overlap-count"` (per the Phase 9 discovery); the field is explicit so future scoring variants are tracked.

---

## Section 2 — Proposed `results.json` schema

**Extends** `experiments/g_kbmag/runs_g5_mix/results.json` directly — every existing field is preserved, common fields are added at the top.

```json
{
  "experiment_id": "b43-kbmag-mixing-v10d-001",
  "engine": "mixer",
  "target": "b43",
  "git_sha_or_local": "abc123def456",
  "wall_time_s": 13.7,
  "confluent": true,
  "winner": "rpo",
  "final_rpo_rules": 2333,
  "peak_rpo_rules": 21000,
  "final_slex_rules": 72000,
  "total_injected": 80,
  "injection_history": [
    {
      "time": 2.5,
      "reason": "THRESHOLD (20000 >= 20000)",
      "n_injected": 80,
      "batch_target": 80,
      "slex_rules": 72000,
      "rpo_rules": 20000,
      "candidates_scored": 1600,
      "index_time": 0.03,
      "prep_time": 0.12,
      "score_time": 0.25,
      "total_time": 0.40,
      "prep_new": 71800,
      "prep_cache_size": 71800
    }
  ]
}
```

**Changes from the seed** (additions only, no removals):
- Added: `experiment_id`, `engine`, `target`, `git_sha_or_local` — the four common provenance fields.
- `elapsed` → renamed to `wall_time_s` for clarity (seconds-unit explicit in the key name). **Rename confirmed (Decision Q1).** Backward-compat adapter in the runner reads either key during transition so existing `results.json` files remain parseable. W3 storage spec records the migration note.
- All existing injection_history fields preserved verbatim.

**For non-mixer engines**: the mixer-specific fields (`final_slex_rules`, `total_injected`, `injection_history`) are set to `null` or `[]` when engine ≠ "mixer". Engine-specific result fields go in an `"engine_results"` block:

```json
{
  "experiment_id": "b43-kbmag-baseline-001",
  "engine": "kbmag",
  "target": "b43",
  "git_sha_or_local": "abc123def456",
  "wall_time_s": 1103.8,
  "confluent": true,
  "winner": "rpo",
  "final_rpo_rules": 863186,
  "peak_rpo_rules": 863212,
  "final_slex_rules": 0,
  "total_injected": 0,
  "injection_history": []
}
```

*(Single-agent KBMAG runs already match this format — no changes needed for existing baseline results.)*

---

## Section 3 — Vault experiment-note frontmatter

**Problem**: Obsidian Bases can group/filter on YAML frontmatter properties, but NOT on nested objects (Bases quirk: groupBy on a nested dict shows the whole dict as a string key). Solution: flatten namespaced params to `_`-separated keys.

**Proposed frontmatter for a Mixer run note**:

```yaml
---
experiment_id: b43-kbmag-mixing-v10d-001
engine: mixer
target: b43
git_sha_or_local: local-2026-06-02T14:30:00
wall_time_s: 13.7
confluent: true
winner: rpo
final_rpo_rules: 2333
total_injected: 80
params_kbmag_cn: 100000
params_mixer_batch_size: 80
params_mixer_threshold: 20000
params_mixer_scoring: overlap-count
tags:
  - experiment
  - status/results
---
```

**Note on KBMAG field naming**: param keys use KBMAG CLI flag spelling (`-cn`, `-me`, `-ms`, `-t`) for unambiguous mapping from kbprog documentation to vault frontmatter. *(Ratified 2026-06-03: Phase C data notes used `cn`; schema updated to match.)* Use `params_kbmag_cn`, not `params_kbmag_confnum`.

**Why flat keys**: `params_kbmag_cn` vs. `params.kbmag.cn` — Bases parses dots as property access in some contexts, making dotted keys ambiguous. Underscore-separated flat keys are unambiguous in YAML frontmatter.

**Bases view recipe** (once these fields are populated):
1. Filter: `engine = "mixer"` AND `target = "b43"`
2. Group by: `params_mixer_batch_size`
3. Columns: `wall_time_s`, `confluent`, `total_injected`, `final_rpo_rules`

This gives a table of all mixer B43 runs grouped by batch size — directly the v10d sweep view Maria needs.

**Not in frontmatter** (too verbose):
- `injection_history` (per-event array — in `results.json` only)
- All `peak_*` fields (intermediate state, not run-level summary)

---

## Section 4 — Tool recommendation summary

| Need | Tool | Reasoning |
|---|---|---|
| Run tracking (params + metrics) | MLflow | Offline-first, simple, wraps existing results.json |
| Config schema design | Hydra pattern | Typed dataclasses; auto-save config per run |
| Large artifact versioning | DVC | Git-native; rule banks need this |
| Sweep orchestration | Python `--multirun` or Hydra | Current scale doesn't need W&B |
| Cloud sync / team dashboard | Skip for now | Small academic group; local MLflow UI sufficient |

**Minimum viable adoption** (Phase 1, ~1 day effort):
1. Add `experiment_id`, `engine`, `target`, `git_sha_or_local` to every run's `results.json` (4-line code change in the Python runner).
2. Write `params.json` at run start with the namespaced blocks (Hydra-style serialization or hand-rolled).
3. Populate vault experiment-note frontmatter with the flat keys above.

**Phase 2** (optional, ~1 week effort): Wrap with MLflow (`mlflow.log_params()`, `mlflow.log_artifact()`) for the comparison UI. Point DVC metrics at `results.json`.

---

## Section 5 — Decisions (2026-06-02)

All five questions answered by Maria (2026-06-02); no overrides. Schema is now fully decided.

1. **`elapsed` → `wall_time_s` rename** — **CONFIRMED.** Backward-compat adapter in the runner reads either key. W3 storage spec records the migration note.

2. **`git_sha_or_local` format** — **CONFIRMED: `"local-<ISO8601>"`** e.g. `"local-2026-06-02T14:30:00"`. Lexicographic sort = chronological; human-readable.

3. **`experiment_id` format** — **CONFIRMED: manual slug + 4-digit run counter**, e.g. `"b43-mixing-v10d-0001"`. Grep-able, git-branchable, human-meaningful.

4. **`params_beam` block** — **POPULATED from W2 inventory** (see Section 1 above). Fields: `beam_width`, `beam_max_steps`, `beam_fwd_overlapping`, `beam_inv_overlapping`, `beam_time_budget_secs`, `ordering`, `input_rule_banks`, `seed_word_file`. Source: `tests/special_mixer/mixer_config.toml` `[reducer]` section + W2 Section 4b reduce-core pipeline.

5. **TOML vs. JSON for params** — **CONFIRMED: TOML as human-authored source of truth**, JSON auto-generated at run start. Preserves existing `rpo.toml` / `mixer_config.toml` configs; no breaking change to the B43 v10d sweep workflow.

## Related vault material

- Tool notes: [[mlflow]], [[wandb]], [[hydra]], [[dvc]]
- Cross-vault: [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] (the params space being tracked IS the combinatorial-search-param problem)
- W2 feed: `Agents/maumayma/Experimenter-B25/scratch/2026-06-02-b25-forensic-inventory.md` § Section 4b provides beam-run param examples for the populated `params.beam` block
- W3 feed: Developer's storage spec (`Agents/maumayma/Developer/scratch/2026-06-02-storage-spec.md`) references this schema in the target run layout
