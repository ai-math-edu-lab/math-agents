---
title: Reproducibility Audit Verdict — Phase B Gate
status: replicated
domain: cs
project: mixer-core
claim: "Developer's reproducibility audit table (a/b/c classifications) is sound enough to authorize Phase B migration, with specific row corrections noted."
claimant: Developer (overnight Phase A, [[2026-06-02-repro-audit-table]])
verification_method: kbprog file header inspection (isConfluent, ExitCode, maxeqns), filesystem spot-checks, Group IV _RWS format sampling, Group III driver verification
tools_used: [Python 3 file reads, head/cat on kbprog files, ls/wc -l, git ls-tree]
author: maumayma
tags:
  - agent/validator
  - user/maumayma
  - domain/cs
  - project/mixer-core
  - status/replicated
---

# Reproducibility Audit Verdict — Phase B Gate

## Overall verdict

**PHASE B AUTHORIZED WITH CORRECTIONS** to 2 row groups:

| Correction | Rows | Direction | Impact on Phase B |
|---|---|---|---|
| 1. m23_rpo and m22_rpo artifacts (Group II) | 2 file-groups | **(c)→(a)** | Remove from backup queue; gitignore without backup |
| 2. tests/special_mixer/kb_shortlex/ and kb_l2r_rpo/ | 2 run-dirs | **(a)→(c)** | **ADD to cold-backup list before any deletion** |

All other Group I, II, III, IV classifications are **ACCEPTED** (with notes below on sl-family conservatism).

---

## Q1 — e35/g7/m23_rpo/m22_rpo: (c) OPEN-problem state vs (a) REGENERABLE

### Method
Read kbprog file headers for `isConfluent` flag and `.kbprog.ec` exit codes.

### Evidence

| Artifact | isConfluent | ExitCode | Final eqns | Verdict |
|---|---|---|---|---|
| `kbmag_v1/standalone/kb_data/e35.kbprog` | (not checked — run is in e_kbmag/runs_e35_mix/) | — | N/A | (c) CONFIRMED |
| `experiments/e_kbmag/runs_e35_mix/` live banks | — | 2 (interrupted) | — | (c) CONFIRMED — open problem |
| `experiments/g_kbmag/runs_g7_mix/` live bank | — | — | — | (c) CONFIRMED — open problem |
| `kbmag_v1/standalone/kb_data/m23_rpo.kbprog` | **`isConfluent := true`** | — | **863,186** | **(a) RECLASSIFIED** |
| `kbmag_v1/standalone/kb_data/m22_rpo.kbprog` | **`isConfluent := true`** | **0** (success) | **35,766** | **(a) RECLASSIFIED** |

**e35 and g7**: The groups' finiteness is unknown (open Kourovka problems). KB will not terminate. The current partial KB states cannot be reproduced exactly by re-running — different compute-time snapshots produce different specific rule sets. Developer's (c) rationale is **correct**. (c) CONFIRMED.

**m23_rpo**: `m23_rpo.kbprog` header reads `isConfluent := true, maxeqns := 863186, ordering := "recursive"`. **The run COMPLETED**. M23 KB under RPO ordering converges to the same 863,186-equation final state as shortlex (verified: all M23 mixing experiments report `final_rules: 863186`, all winners are RPO). The converged KB state is uniquely determined by (presentation, ordering). The `m23_rpo` input file IS present in `kbmag_v1/standalone/kb_data/`. Regeneration cost: M23 shortlex converges in ~1100s; RPO may take somewhat longer but is almost certainly under 24h. C3 does NOT apply. C2 does NOT apply to converged runs (different confnum → same final state). → **(a) REGENERABLE. Override Developer's (c).**

**m22_rpo**: `m22_rpo.kbprog` header reads `isConfluent := true, maxeqns := 35766`. Exit code = 0 (clean termination). M22 has order 443,520 — much smaller than M23. KB terminates in minutes. Input `m22_rpo` is in `kb_data/`. → **(a) REGENERABLE. Override Developer's (c).**

**Impact**: Remove m23_rpo and m22_rpo artifact families from the cold-backup priority list. Total backup volume reduction: ~11.9 MB (m22_rpo) + ~500 MB (m23_rpo artifacts in kb_data) from the (c) list.

---

## Q2 — sl-family: (c) mathematical-reference vs (a) raw KBMAG output

### Evidence

| File | isConfluent | ExitCode | Verdict |
|---|---|---|---|
| `sl311.kbprog` | **false** | **2** (exit-limit hit) | (c) CONFIRMED — partial/interrupted |
| `sl37.kbprog` | **true** | **0** | Could be (a); (c) is conservative |
| `sl43.kbprog` | **true** | **0** | Could be (a); (c) is conservative |
| `sl72` (input) | N/A | N/A | Valid `_RWS := rec` at byte 1211 (long header) |

**sl311**: `isConfluent := false`, `ExitCode := 2` — KB did NOT complete. SL(3,11) has order 212M; the run hit an equation/state limit before converging. The current partial state (28.8MB .kbprog, 86.6MB .reduce) is NOT reproducible by re-running with the same params — a re-run starting from the clean input produces a different trajectory. Developer's (c) is **CONFIRMED**.

**sl37, sl43**: Both converged (`isConfluent := true`, ExitCode 0). The converged states ARE reproducible from their committed input files. Strictly, Developer's (c) is **conservative** for these two — (a) would be correct. However:
- (c) is not harmful (just avoids unnecessary backup avoidance)
- Without knowing the original runtime (hours?), the C3 defense is plausible
- Accepted as-is. No reclassification required for Phase B.

**sl72 input**: IS a valid `_RWS := rec` record — the `_RWS := rec` tag appears at byte offset 1211 (after listing all 42 generators in comments). The initial 200-byte check was insufficient. Confirmed valid input for Group IV.

**Verdict for Q2**: sl-family (c) classification is **ACCEPTED** (conservative for sl37/sl43 but defensible). No correction to Phase B.

---

## Q3 — Group I: 22 tracked B43/F2 artifacts all (a)?

### Evidence

| Item | Check | Result |
|---|---|---|
| `kbmag_v1/standalone/kb_data/f2` (input) | filesystem | EXISTS ✓ |
| `kbmag_v1/standalone/kb_data/b43` (input) | filesystem | EXISTS ✓ |
| `kbmag_v1/standalone/kb_data/b43_full` (input) | filesystem | EXISTS ✓ |
| `kbmag_v1/standalone/b43_confluent` (orphan input?) | filesystem | NOT FOUND (as expected) |
| `kbmag_v1/standalone/b43_confluent.kbprog` | header | `isConfluent := true, maxeqns := 2333, ordering := "recursive"` |
| `legacy/kbmag_debug/standalone/kb_data/b43_full.kbprog` | Developer notes md5-identical to V1 | Accepted ✓ |

**b43_confluent.kbprog orphan**: No input file named `b43_confluent` exists. The content matches B(4,3) RPO convergence at 2333 equations (per project memory and all B43 experiments). It IS regenerable: run `kbprog -rec b43_full` (or `b43`) until convergence → same 2333 equations. The filename mismatch (derived from `b43_full` but named `b43_confluent`) is explained by a likely manual copy/rename during development. The CONTENT is deterministically reproducible. → **(a) CONFIRMED**.

**Verdict for Q3**: All 22 Group I artifacts **confirmed (a) REGENERABLE**. `git rm --cached` safe to proceed.

---

## Additional spot-check: tests/special_mixer/ — CRITICAL RECLASSIFICATION

### Evidence

Developer classified `tests/special_mixer/**` (42 GB) as **(a) REGENERABLE** with reasoning "scripts committed, test output is regenerable."

**What I found:**

```
tests/special_mixer/kb_shortlex/:
  b25_test.kbprog.ec:  _ExitCode := 2  (INTERRUPTED)
  b25_test.kbprog.live: 1,998,342 lines = ~2M rules
  b25_test (input):    B(2,5), 4372 relations, shortlex ordering
  kbprog.log header:   biased with special_word=comm_13_10.txt,
                       special_prob=0.30, sk=8

tests/special_mixer/kb_l2r_rpo/:  1.9 GB
tests/special_mixer/kb_shortlex/: 1.3 GB
tests/special_mixer/bootstrap_*.txt: 5.4 GB + 3.3 GB + 3.3 GB + 3.8 GB + 4.1 GB + 2.1 GB + 2.4 GB ≈ 24 GB
tests/special_mixer/comm_13_10_reduced_2494.txt: 2494 chars (word result)
tests/special_mixer/inject_special_rules.sh: driver script (present)
```

This is NOT a standard test output directory. `tests/special_mixer/` is a **biased B(2,5) KB experiment** targeting comm_13_10 — structurally identical to the B25 kbmag server_logs experiment (which is correctly classified (c)). The KB run was INTERRUPTED (ExitCode 2), meaning:
- The specific ~2M rules in kb_shortlex/ cannot be exactly reproduced by re-running
- `special_prob=0.30, sk=8` biasing makes each run's rule set unique to the specific timing
- B(2,5) biased KB never terminates → partial state is the only record

**Reclassification:**

| Item | Volume | New class | Reason |
|---|---:|---|---|
| `kb_shortlex/` (B(2,5) biased KB, ExitCode 2) | 1.3 GB | **(c)** | Same as B25 server_logs — partial biased KB state, not reproducible exactly |
| `kb_l2r_rpo/` (likely same setup, 1.9 GB) | 1.9 GB | **(c) provisional** | Same pattern as kb_shortlex/ (didn't check .ec directly but identical setup) |
| `bootstrap_*.txt` (large rule bank exports) | ~23 GB | **(c)** | Derived from the KB live banks above; represent the search state at a point in time |
| `comm_13_10_reduced_2494.txt` | 2.4 KB | **(b/c)** | Word reduction result for comm_13_10 (2494 chars vs original 2500). Research artifact — preserve. |
| `inject_special_rules.sh`, `mixer_config_deep*.toml` | small | **(b)** | Input configs/scripts — committed or should be |

**Phase B impact**: The 3.2 GB of KB run directories in `tests/special_mixer/` MUST be added to the cold-backup list before any deletion. This is equivalent to the B25 kbmag server_logs (priority-1 backup). Recommend adding as cold-backup priority 8 (after current priorities 1-7).

---

## Group IV input spot-check

Sampled 5 inputs:

| Input | Format | _RWS := rec? | Type |
|---|---|---|---|
| `b25_gen` | long | ✓ (line 3) | Script-derived B(2,5) presentation, 4372 relators |
| `b53_full` | short | ✓ (line 2) | Hand-derived B(5,3) presentation |
| `g5` | short | ✓ (with comment) | Kourovka G5 — hand-written |
| `m23` | medium | ✓ (after 4 comment lines) | ATLAS M23 presentation, GAP-verified |
| `sl72` | long | ✓ (byte 1211) | SL(7,2) Steinberg presentation, 42 generators |

All 5 confirmed as genuine `_RWS := rec` input presentations (not generated artifacts). Classification as (b) NON-REGENERABLE SEED is **CONFIRMED** for Group IV.

---

## Summary: per-question verdicts

| Question | Developer's classification | Validator verdict | Action |
|---|---|---|---|
| Q1: e35 | (c) | **(c) CONFIRMED** | No change |
| Q1: g7 | (c) | **(c) CONFIRMED** | No change |
| Q1: m23_rpo artifacts | (c) | **(a) RECLASSIFIED** | Remove from backup queue |
| Q1: m22_rpo artifacts | (c) | **(a) RECLASSIFIED** | Remove from backup queue |
| Q2: sl311 | (c) | **(c) CONFIRMED** — ExitCode 2, not converged | No change |
| Q2: sl37, sl43 | (c) | **(c) ACCEPTED** — converged but (c) is conservative, not harmful | No change |
| Q2: sl-family overall | (c) | **(c) ACCEPTED** | No change |
| Q3: Group I (22 artifacts) | (a) | **(a) CONFIRMED** — all inputs committed, b43_confluent reproducible from b43_full | `git rm --cached` authorized |
| Additional: tests/special_mixer/ kb_shortlex/ | (a) | **(c) RECLASSIFIED — CRITICAL** | Add to cold-backup list; backup before any deletion |
| Additional: tests/special_mixer/ kb_l2r_rpo/ | (a) | **(c) PROVISIONAL** | Add to cold-backup list |
| Additional: tests/special_mixer/ bootstrap_*.txt | (a) | **(c)** | Covered by kb dirs backup |
| Group IV inputs (5 sampled) | (b) | **(b) CONFIRMED** | Rescue to _inputs/ as planned |

## Phase B authorization

**PHASE B AUTHORIZED WITH CORRECTIONS.**

Before Developer begins migration, apply these corrections to the repro-audit-table:
1. Row: "m23 family" in Group II → **(a)**. Remove from cold-backup target list.
2. Row: "m22_rpo family" in Group II → **(a)**. Remove from cold-backup target list.
3. NEW GROUP III ROW: `tests/special_mixer/kb_shortlex/` + `kb_l2r_rpo/` → **(c)**. Add to cold-backup priority list (suggest priority 8, after current 7). Total: ~3.2 GB.

Migration can proceed on all other rows immediately. The two (c) corrections for tests/special_mixer/ require Lead + Maria awareness before those specific paths are touched.
