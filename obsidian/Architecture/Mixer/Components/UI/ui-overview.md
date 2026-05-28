---
title: UI — HTML dashboards and data artifacts
path: ui/
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "ui/benchmarks_data.json — consumed by collect_best.sh (written) and benchmarks.html (read)"
  - "ui/comm_12_9_reduced_data.json — consumed by verify_reduction.py (read) and comm_12_9_reduced.html (read)"
invariants:
  - id: json-data-files-live
    summary: "The JSON data files (benchmarks_data.json, comm_12_9_reduced_data.json, and others) are live artifacts consumed and written by scripts. Do not delete or replace them without understanding the downstream consumers."
    why: "verify_reduction.py reads comm_12_9_reduced_data.json to extract the lifted_word, core, and RPO rules for the b25_reduce_core verification chain. collect_best.sh writes benchmarks_data.json as the authoritative benchmark summary. These are not static assets — they are the integration point between script outputs and the dashboards."
  - id: comm_12_9_reduced_stale-final-word
    summary: "ui/comm_12_9_reduced_data.json currently contains the old (invalidated) final_word: the 3,707-char word produced by the buggy braid_reduce_fast (non-abelian inverse order). It is NOT equal to the original commutator [c12, c9]."
    why: "The braid_reduce_fast bug (fixed 2026-05-22) produced word_3707 with abelianization (4,4) mod 5, not (0,0). The corrected chain produces word_7245 instead. comm_12_9_reduced_data.json has not been updated with the corrected final_word. Any script that reads this file's final_word field will get the wrong word. The lifted_word, core, and RPO rules fields in the same file are unaffected by the bug and are still correct."
related:
  - reduce-coreless
  - braid-reduce
  - traced-braid-reduction
known_issues:
  - "comm_12_9_reduced_data.json#final_word is stale: contains the 3,707-char invalidated word. Correct value is 7,245 chars. Update requires regenerating the file from the corrected reduction chain."
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# UI — HTML dashboards and data artifacts

## What it is

`ui/` contains static HTML dashboards for visualising benchmark results and commutator word analysis, JSON data files consumed by those dashboards and by experiment scripts, and a `server.py` for serving the dashboards locally. The directory also has `runs/` (run output subdirectories) and `scripts/` (support scripts including `b43_mix.py`).

## Why it exists

Visualising rule bank benchmark results (which rule sets reduce which words, by how much) and exploring commutator word structure requires human-readable interfaces that go beyond terminal output. The HTML dashboards allow the human and agents to inspect the current reduction state interactively, compare rule bank runs, and verify the structural properties of reduced words. The JSON data files serve as the bridge between experiment script outputs and the dashboards.

## How it fits in the system

```
collect_best.sh (writes) → benchmarks_data.json ← benchmarks.html (reads)
verify_reduction.py (reads) ← comm_12_9_reduced_data.json → comm_12_9_reduced.html (reads)
braid_reduce output → [manual update step] → comm_12_9_data.json → comm_12_9.html
```

The HTML files are static (no server-side logic); they fetch their corresponding `_data.json` file via JavaScript. `server.py` provides a local HTTP server for viewing them. The dashboards are not deployed anywhere; they are for local analysis only.

## Contents

| File | Description |
|---|---|
| `benchmarks.html` + `benchmarks_data.json` | Rule bank benchmark results — which rule banks reduce which of the 119 words |
| `comm_12_9_reduced.html` + `comm_12_9_reduced_data.json` | Detailed analysis of the comm_12_9 reduction chain; contains lifted_word, core, RPO rules, final_word |
| `comm_12_9.html` + `comm_12_9_data.json` | Full comm_12_9 commutator word analysis |
| `comm_13_10.html` + `comm_13_10_data.json` | comm_13_10 word analysis |
| `comm_6_2.html` + `comm_6_2_data.json` | comm_6_2 analysis |
| `cross_analysis.html` + `cross_analysis_data.json` | Cross-group comparison |
| `index.html` | Dashboard index |
| `server.py` | Local HTTP server for dashboard viewing |
| `scripts/b43_mix.py` | B(4,3) mixing script; references `kbmag_v1/` |
| `runs/` | Run output subdirectories |

## Critical invariants — why each one exists

### json-data-files-live

`benchmarks_data.json` is written by `collect_best.sh` as the authoritative record of which beam-search runs produced the best reductions. `comm_12_9_reduced_data.json` is read by `verify_reduction.py` on every invocation to get `lifted_word`, `core`, and the RPO rule set used in the reduction chain. These files must not be treated as static assets. Overwriting them with an older version would silently break verification runs.

### comm_12_9_reduced_stale-final-word

The `final_word` field in `comm_12_9_reduced_data.json` was set when the buggy `braid_reduce_fast` was the production code (pre-2026-05-22 fix). The 3,707-char word it contains has abelianization `(4,4) mod 5` — it is NOT equal to the original commutator `[c12, c9]`. The corrected reduction chain produces word_7245 (7,245 chars, abelianization `(0,0)`). Until `comm_12_9_reduced_data.json` is regenerated from the corrected chain, callers must not use the `final_word` field. The `lifted_word`, `core`, and rule-bank fields in the same file are derived independently of the buggy code and remain correct.

## Classification note

In the Phase 3 stale-component inventory ([[2026-05-22-stale-component-inventory]]), `ui/` was classified as "Unknown — Requires Human Input" because the HTML files were not in the b25_reduce_core dependency trace. Human confirmed (2026-05-22) that most dashboards are in active use. This note reclassifies `ui/` as active UI infrastructure. The `comm_12_9_reduced_data.json#final_word` stale data issue is documented above as a known issue, not a reason to classify the component as dead.

## Related

- [[reduce-coreless]] — braid_reduce_fast fix affects comm_12_9_reduced_data.json's final_word
- [[braid-reduce]] — produces the word files that feed into the data files
- [[traced-braid-reduction]] — reads comm_12_9_reduced_data.json as source of truth for verification
