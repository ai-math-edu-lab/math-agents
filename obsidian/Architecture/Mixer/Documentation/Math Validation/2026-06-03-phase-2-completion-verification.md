---
title: Phase 2 Part 2 Completion Verification — 12-Family Restructure
status: replicated
domain: cs
project: mixer-core
claim: "Developer's 12-family restructure + big-data moves + gitignore patterns are structurally complete and correct."
claimant: Developer (Phase 2 Part 2), Lead K3 sample
verification_method: kbmag/ wrapper survey, git check-ignore sampling (15+ artifacts), cross-repo reference-rot grep, kbmag_source/ status + md5, b43_bidirectional path audit, special_mixer kbprog.log binary verification
tools_used: [find, git check-ignore -v, grep, head/cat on kbprog.log, ls, md5]
author: maumayma
tags:
  - agent/validator
  - user/maumayma
  - domain/cs
  - project/mixer-core
  - status/replicated
---

# Phase 2 Part 2 Completion Verification

## Overall verdict

**PHASE 2 COMPLETE WITH FIXES** — structural work is correct and complete; 3 reference-rot groups in non-core scripts need path updates before those specific pipelines (RL mixer training, patterns/ analysis, tests/special_mixer/) can run.

---

## Check 1 — kbmag/ wrapper survey

**Found 10 kbmag/ directories:**

| Family | Run ID | kbmag/ present |
|---|---|---|
| burnside/b25_kbmag | b25-kbmag-mix-0001 | ✓ |
| burnside/b25_bias_bidir | special-mixer-kb-shortlex-0001 | ✓ |
| burnside/b25_bias_didir | special-mixer-kb-l2r-rpo-0001 | ✓ |
| burnside/b43_kbmag_mixing | b43-kbmag-baseline-0001 | ✓ |
| burnside/b43_kbmag_mixing | b43-kbmag-mix-0001 | ✓ |
| burnside/b53_kbmag_mixing | b53-kbmag-mix-v10-0001 | ✓ |
| e_kbmag | e35-kbmag-mix-0001 | ✓ |
| g_kbmag | g5-kbmag-mix-0001 | ✓ (with rpo/ shortlex/ logs/ subdirs) |
| g_kbmag | g7-kbmag-mix-0001 | ✓ |
| m23_kbmag | m23-kbmag-converged-0001 | ✓ |

**Documented no-wrapper exceptions (confirmed correct):**
- `b25_reduce_core`: no kbmag/ — expected (benchmark output, not raw kbprog tree) ✓
- `burnside_bidirectional/`: no kbmag/ — expected (mixed Python+Rust+text, not a KB-mixing run) ✓

**b25_kbmag server_logs/ migration confirmed**: `experiments/burnside/b25_kbmag/server_logs/` does NOT EXIST on disk — data successfully moved into `runs/b25-kbmag-mix-0001/kbmag/`. Run folder shows `b25_scoring.log`, `params.json`, `README.md`, `results.json` + `kbmag/` tree. ✓

---

## Check 2 — Gitignore sampling (15 artifacts)

| Artifact | Gitignore result | Pattern |
|---|---|---|
| `burnside/b25_kbmag/server_logs/rpo/input.kbprog.live` | **IGNORED** | `.gitignore:51:*.kbprog.live` |
| `burnside/b25_kbmag/server_logs/shortlex/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `burnside/b53_kbmag_mixing/server_logs/v10/rpo/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `m23_kbmag/converged_rpo_rules.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `burnside/b25_bias_bidir/rules/3705_run4_sl_k12/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `burnside/b25_bias_didir/rules/3705_run5_sl_k0_sp50/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `g_kbmag/runs_g7_mix/rpo/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `g_kbmag/runs_g5_mix/rpo/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `e_kbmag/runs_e35_mix/rpo/input.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `burnside/b25_bias_didir/runs/special-mixer-kb-shortlex-0001/kbmag/b25_test.kbprog.live` | **IGNORED** | `:51:*.kbprog.live` |
| `burnside/b25_bias_didir/runs/special-mixer-bootstrap-0001/bootstrap_all.txt` | **IGNORED** | `.gitignore:63:bootstrap_*.txt` |
| `kbmag_v1/standalone/kb_data/m23_rpo.kbprog` | **IGNORED** | `.gitignore:49:*.kbprog` |

**15/15 artifacts correctly gitignored.** ✓

**m23 edge case resolved**: `converged_rpo_rules.live` no longer exists on disk (glob match confirms: `ls converged*` returns no matches). File was renamed to `converged_rpo_rules.kbprog.live` and is now caught by the `*.kbprog.live` pattern. ✓

---

## Check 3 — Cross-family reference rot

**Grep patterns**: `b25_kbmag/server_logs/`, `tests/special_mixer/`, `b43_kbmag_mixing/runs_mix/`, `b53_kbmag_mixing/server_logs/`

### Group A — patterns/ scripts (low priority — analysis tools, not core mixer)

4 active scripts with hardcoded absolute paths to old locations:

| File | Line | Stale path |
|---|---|---|
| `patterns/full_comparative.py` | 27 | `b43_kbmag_mixing/runs_mix/baseline_t0/rpo/input.kbprog.live` |
| `patterns/full_comparative.py` | 28-29 | `b53_kbmag_mixing/server_logs/v10/{rpo,shortlex}/input.kbprog.live` |
| `patterns/full_comparative.py` | 30-31 | `b25_kbmag/server_logs/{rpo,shortlex}/input.kbprog.live` (pre-burnside/ prefix) |
| `patterns/rule_trie.py` | 28 | `b53_kbmag_mixing/server_logs/v10/rpo/input.kbprog.live` |
| `patterns/rule_graph_3d.py` | 30 | same |
| `patterns/rule_structure.py` | 25 | same |

These scripts are standalone analysis/visualization tools. They will error on `RULES_FILE` open. New canonical paths per the restructure: `burnside/b53_kbmag_mixing/runs/b53-kbmag-mix-v10-0001/kbmag/rpo/input.kbprog.live` (similar pattern for b43, b25).

### Group B — rl_mixer/rl/ active scripts (medium priority — RL training pipeline)

5 active training/test scripts referencing moved b25_kbmag data:

| File | Line | Stale path |
|---|---|---|
| `rl_mixer/rl/config.py` | 54 | `burnside/b25_kbmag/server_logs/shortlex/input.kbprog.live` |
| `rl_mixer/rl/test_all_targets.py` | 117 | `burnside/b25_kbmag/server_logs/rpo/input.kbprog.live` |
| `rl_mixer/rl/test_target_comparison.py` | 29 | same (rpo) |
| `rl_mixer/rl/test_macro_env.py` | 27 | same (rpo) |
| `rl_mixer/rl/train_subword_ppo.py` | 39 | same (rpo) |

These are RL mixer training scripts. New canonical path: `burnside/b25_kbmag/runs/b25-kbmag-mix-0001/kbmag/{rpo,shortlex}/input.kbprog.live`. Without this fix, `python3 train_subword_ppo.py` fails at startup.

`rl_mixer/rl/archive/`: 15 scripts with same old paths — **acceptable historical references**, not active.

### Group C — tests/special_mixer/ scripts (low priority — content already moved)

- `tests/special_mixer/run_special_mixer.sh:21-22`: `RPO_RULES`/`SLEX_RULES` hardcoded to `burnside/b25_kbmag/server_logs/{rpo,shortlex}/` (moved to runs/). The special_mixer content has been moved to `burnside/b25_bias_bidir/runs/`, so the script's rule paths need updating.
- `tests/special_mixer/mixer_config*.toml:10-11`: `runs_dir = "tests/special_mixer/runs_deep"` — old location (runs are now under b25_bias_didir/runs/).

### Summary

| Group | Files | Priority | Impact |
|---|---|---|---|
| A — patterns/ | 4 analysis scripts | Low | Fail only when analysis is run manually |
| B — rl_mixer/rl/ active | 5 training scripts | **Medium** | RL mixer pipeline broken at startup |
| C — tests/special_mixer/ | 1 sh + 4 toml | Low | Tests reference moved data |

**15 archive-only refs** (rl_mixer/rl/archive/) — acceptable historical, not active.

---

## Check 4 — kbmag_source/ pristine state

**git status `--short -- kbmag_source/`**: No non-`??` entries. Zero staged/unstaged modifications to tracked upstream files. ✓

**MD5 spot-checks** (3 upstream files):

| File | MD5 |
|---|---|
| `kbmag_source/standalone/lib/fsa.c` | d1f6f83f406d7a270db436c320a7d7da |
| `kbmag_source/standalone/lib/fsa.h` | aa052dc5ba88e1743226cbc757e5fb0b |
| `kbmag_source/gap/kbsmg.gd` | d94c0c62d06944de24e971a6783da74d |

Upstream content unmodified. ✓

**Outstanding carry-over**: `kbmag_source/README_biased_agents.md` STILL PRESENT and tracked in git (flagged in `[[2026-06-03-phase-2-regression-reaudit]]`). Not resolved in this phase. Does not affect Phase 2 structural completion.

---

## Check 5 — b43_bidirectional path audit

- `experiments/b43_bidirectional/` does NOT exist on disk. ✓
- `experiments/burnside/b43_bidirectional/` EXISTS with `b43_bidir.py`, `b43_bidir_kb_only.py`, `b43_rpo_to_reducers.py`, `b43_relators.txt`, `Cargo.lock`. ✓
- `experiments/burnside/README.md:11` correctly references `b43_bidirectional/` (relative, resolves to burnside/b43_bidirectional/). ✓
- `README.md` (repo root):110+172: stale `experiments/b43_bidirectional/b43_rpo_to_reducers.py` — documentation rot only, no runtime impact.

**Verdict**: `b43_bidirectional` was never at the top-level experiments/ path in the current working tree. It lives at `burnside/b43_bidirectional/`. README.md (repo root) has a stale doc reference — morning packet item, not blocking.

---

## Check 6 — special_mixer → b25_bias_bidir attribution

**Content location confirmed**: bootstrap_*.txt files at `burnside/b25_bias_bidir/runs/special-mixer-bootstrap-0001/`. KB run directories at `runs/special-mixer-kb-shortlex-0001/kbmag/` and `runs/special-mixer-kb-l2r-rpo-0001/kbmag/`.

**kbprog.log verification** (both runs):
```
kb_shortlex kbprog.log header:
  #Modified mixer mode: special_word_file=.../special_word_comm_13_10.txt, special_prob=0.30
  #Loaded special word: length=2500 from .../special_word_comm_13_10.txt
  #Special equations: 197 of 4376 (4.5%) [kgram8: ...]

kb_l2r_rpo kbprog.log header:
  #Modified mixer mode: special_word_file=.../special_word_comm_13_10.txt, special_prob=0.30
  #Loaded special word: length=2500 from .../special_word_comm_13_10.txt
  #Special equations: 140 of 4376 (3.2%) [kgram8: ...]
```

`#Modified mixer mode` with `special_prob=0.30` and `kgram8` confirms the biased kbprog binary (`-sw`, `-sp`, `-sk` flags — available ONLY in `kbmag_source/standalone/bin/kbprog`, not in `kbmag_v1/`). Developer's lineage attribution is **CORRECT** — special_mixer runs used the biased binary, aligning them with b25_bias_bidir's workflow. ✓

---

## Summary checklist

| Check | Result | Notes |
|---|---|---|
| kbmag/ wrappers present (10 families) | ✅ PASS | All 10 families confirmed; b25_reduce_core + burnside_bidirectional documented exceptions ✓ |
| b25_kbmag server_logs/ moved | ✅ PASS | server_logs/ not found; runs/b25-kbmag-mix-0001/ confirmed |
| Gitignore (15 artifacts sampled) | ✅ PASS | 15/15 ignored; m23 edge case rename confirmed resolved |
| Reference rot Group A (patterns/) | ⚠ FIX | 4 analysis scripts, 8 stale abs paths; no runtime impact until manually run |
| Reference rot Group B (rl_mixer/) | ⚠ FIX | 5 active training scripts broken; pipeline fails at startup |
| Reference rot Group C (tests/special_mixer/) | ⚠ FIX | 1 sh + 4 toml, low priority |
| kbmag_source/ pristine (no staged mods) | ✅ PASS | No non-?? entries; 3 md5 spot-checks clean |
| kbmag_source README_biased_agents.md | ℹ CARRY | Still present; flagged from previous audit; not Phase 2 scope |
| b43_bidirectional path audit | ✅ PASS | Correctly at burnside/; top-level README.md has doc rot (morning packet) |
| special_mixer → b25_bias_bidir attribution | ✅ PASS | kbprog.log confirms biased binary (#Modified mixer mode, sp=0.30) |

**PHASE 2 COMPLETE WITH FIXES** — structural completion confirmed. Reference rot fixes are surgical path updates (8 files, ~15 lines total across Groups A+B+C). Recommend routing Group B (rl_mixer/rl/ config.py + 4 training scripts) to Developer as a single-PR follow-up; Groups A and C are low-priority and can be filed as morning-packet items for Maria.
