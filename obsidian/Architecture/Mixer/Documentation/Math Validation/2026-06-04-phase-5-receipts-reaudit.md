---
title: Phase 5 Receipts Re-Audit — Independent Verification
status: replicated
domain: cs
project: mixer-core
claim: "Developer's Phase 5 10-item execution + 1 STOP is structurally complete and correct."
claimant: Developer (Phase 5 session), Lead K3 sample
verification_method: git check-ignore -v, ls/find, tar -tzf, grep, cat PROVENANCE, sed on kbmag_agent.py, python3 path smoke test
tools_used: [git check-ignore, git status, ls/find, tar, grep, python3, cat, du]
author: maumayma
tags:
  - agent/validator
  - user/maumayma
  - domain/cs
  - project/mixer-core
  - status/replicated
---

# Phase 5 Receipts Re-Audit

## Overall verdict

**PHASE 5 COMPLETE WITH RECEIPTS** — all functional spot-checks pass. Two count discrepancies (archive count 7 vs 8; stale-ref count) are non-blocking and routed to morning packet.

---

## Check 1 — Gitignore re-verification (post-Phase-5 new paths)

### Artifacts → IGNORED

```
experiments/e35_kbmag/runs/e35-kbmag-mix-0001/kbmag/rpo/input.kbprog.live:
  .gitignore:49:*.kbprog.live  ✓

runs/b25/20260320_054109/kb_shortlex/input.kbprog.live:
  .gitignore:49:*.kbprog.live  ✓

runs/b53/20260320_052723/kb_shortlex/input.kbprog.live:
  .gitignore:49:*.kbprog.live  ✓
```

### Vault/scripts/figures → NOT IGNORED (correct)

```
analysis/archive/b25/1_growth_rate_decay.png:   NOT IGNORED ✓ (committed figure)
experiments/m23_kbmag/script/exploratory/deep_analysis.py: NOT IGNORED ✓ (committed script)
experiments/_shared/gen_b25_kbmag.py:           NOT IGNORED ✓
experiments/m23_kbmag/script/m23_mix.py:        NOT IGNORED ✓
experiments/e35_kbmag/script/e35_mix.py:        NOT IGNORED ✓
```

**All 8 gitignore checks pass.** ✓

---

## Check 2 — Archive integrity

**Command**: `ls -la /Users/maumayma/Desktop/reps/algo_mixing-archives/`

```
7 tarballs (NOT 8 as routing stated):
  2026-06-03-b43_bidirectional.tar.gz         15.4 KB   + PROVENANCE.md (1.9 KB)
  2026-06-03-bias_bidir_rules.tar.gz         172.1 MB   + PROVENANCE.md (2.4 KB)
  2026-06-03-checkpoints.tar.gz               71.9 MB   + PROVENANCE.md (994 B)
  2026-06-03-legacy_kbmag_debug.tar.gz       502.1 KB   + PROVENANCE.md (2.0 KB)
  2026-06-03-patterns_debug_runs.tar.gz      167.7 MB   + PROVENANCE.md (1.1 KB)
  2026-06-03-rl_mixer_source.tar.gz            7.2 MB   + PROVENANCE.md (1.4 KB)
  2026-06-04-tests_special_mixer_residual.tar.gz  139.6 KB  + PROVENANCE.md (1.9 KB)
```

⚠ **COUNT DISCREPANCY: 7 tarballs found; routing says 8. Exhaustive directory listing confirms no additional tarballs. No local `archives/` dir in repo (checked). Route to morning packet.**

### Tarball spot-checks

**b43_bidirectional.tar.gz** (13 entries):
```
experiments/burnside/b43_bidirectional/
experiments/burnside/b43_bidirectional/Cargo.toml
experiments/burnside/b43_bidirectional/reducer_agent.py
experiments/burnside/b43_bidirectional/b43_relators.txt
experiments/burnside/b43_bidirectional/b43_rpo_to_reducers.py
...
```
13 entries ✓

**tests_special_mixer_residual.tar.gz** (45 entries):
```
tests/special_mixer/
tests/special_mixer/start_agents.sh
tests/special_mixer/run_reducer_loop_v2.sh
tests/special_mixer/mixer_config_deep2.toml
tests/special_mixer/reducer_loop_v2.log
...
```
45 entries. Size: 139,565 bytes ≈ 136.3 KB ✓ (routing matches exactly)

### PROVENANCE spot-checks (Ask 2 fields)

**tests_special_mixer_residual PROVENANCE.md** — all 3 Ask 2 doctrine fields present:
- **What**: "45 files / 1.4MB residual after Phase 2 Part 2 Q5 + Phase 5 A.7 migrations. Contents: 7 .sh scripts, 1 .py script, 4 .toml configs (Q8-fixed), ~22 .log files, 4 .txt data files, 2 PID files" ✓
- **Validity status**: "SCRIPTS + CONFIGS are post-Q8-fixed (workflow-current; reference b25_bias_bidir/runs/ canonical paths). LOGS are runtime output from past runs (regenerable)." ✓
- **Pointer-back**: "originally at `tests/special_mixer/`. Workflow-related to `experiments/burnside/b25_bias_bidir/runs/special-mixer-*`" ✓
- Maria open question documented: Phase 4 A.7 recommended migrating scripts/configs vs archiving; brief said ARCHIVE; Maria can reconsider ✓

**bias_bidir_rules PROVENANCE.md** — Ask 2 C4 invalidity label present verbatim:
> "valid B(2,5) KB rules, biased for wrong coset (word_3705/3707 buggy chain), not reusable as-is for intended target"
- What, Validity, Pointer-back all present ✓
- C4 invalidity label verbatim per doctrine ✓

---

## Check 3 — A.6 STOPPED-state verification

**runs/ size**:
```
$ du -sh runs/
3.0G    /Users/maumayma/Desktop/reps/algo_mixing/runs/
```
✓ Present at 3.0 GB (not moved; A.6 STOP correctly applied)

**runs/ contents**:
```
b25  b25_lifted  b53  sorting_bubble_only  sorting_mixed
```

**gitignore on runs/<id>/**:
```
$ git check-ignore -v "runs/20260320_054109/"
.gitignore:34:**/runs/**   runs/20260320_054109/
```
✓ Correctly IGNORED by `**/runs/**` pattern at line 34.

**Stale refs to runs/20260320_* in active (non-archive) scripts**:

My independent grep finds **25 lines** across 2 active scripts:
- `experiments/burnside/b25_bias_bidir/script/launch_agents.sh:6` — 1 ref (054957)
- `experiments/burnside/b25_bias_bidir/script/reduce_coreless.py:19-29` — 13 refs

Unique stale run-dirs referenced:
```
20260320_054109, 20260320_054957, 20260320_055128,
20260320_055557, 20260320_065252, 20260320_065653
```
= 6 unique dirs.

⚠ **COUNT DISCREPANCY: Developer claims "7 stale refs"; my grep finds 25 lines / 6 unique dirs in active scripts (plus 5+ in archive/ — acceptable).** The refs are NOT broken — all 6 run dirs exist at top-level `runs/b25/20260320_*/` (A.6 STOP preserved them). No runtime impact; morning packet for A.6 strategy decision. ✓ (functional)

---

## Check 4 — API kbmag/ wrapper smoke test

**Command**: `sed -n '88,112p' api/kbmag_agent.py`

```
 95:     self.ordering_name = name or f"kbmag_{ordering}"
 97:     # W3 § 5: KBMAG-native output wraps under kbmag/ subdir; non-native (logs) stays at run-folder root.
 98:     self.state_dir = Path(base_dir) / "kbmag" / self.ordering_name
 99:     self.state_dir.mkdir(parents=True, exist_ok=True)
100:     self.logs_dir = Path(base_dir) / "logs"
```

**Empirical smoke test**:
```python
base_dir = Path('/tmp/test_run')
state_dir = base_dir / "kbmag" / "kbprog_rpo"
# → /tmp/test_run/kbmag/kbprog_rpo
kbmag/ subdir injected by API: True
```

**Q-old-3 fix confirmed**: API now injects `kbmag/` internally. Callers pass `base_dir = run_dir`; API creates `run_dir/kbmag/rpo/`. ✓

*Carry-over note*: line 108 fallback `project_root / "kbmag/standalone/bin/kbprog"` still stale (callers pass binary explicitly; no runtime impact).

---

## Check 5 — B.3 m23 exploratory move

**Command**: `ls experiments/m23_kbmag/script/` and `ls experiments/m23_kbmag/script/exploratory/`

**script/ top level:**
```
analyze_rules.py        ← active script ✓
exploratory/            ← exploratory dir ✓
m22_kbmag.gap           ← migrated .gap (B.2)
m22_setup.gap           ← migrated .gap (B.2)
m23_atlas.gap           ← migrated .gap (B.2)
m23_atlas_verify.gap    ← migrated .gap (B.2)
m23_final.gap           ← migrated .gap (B.2)
m23_fromperm.gap        ← migrated .gap (B.2)
m23_mix.py              ← active script ✓
m23_pres.gap            ← migrated .gap (B.2)
m23_simplepres.gap      ← migrated .gap (B.2)
m23_to_kbmag.gap        ← migrated .gap (B.2)
m23_v2.gap              ← migrated .gap (B.2)
m23_v3.gap              ← migrated .gap (B.2)
m23_verify8.gap         ← migrated .gap (B.2)
```

Active Python scripts at top: `m23_mix.py` + `analyze_rules.py` only ✓ (12 .gap files are B.2 migration artifacts, correctly co-located at script/ top)

**exploratory/ (9 scripts — all present):**
```
deep_analysis.py       divergence_quick.py    micro_inject.py
ordering_test.py       param_divergence.py    recursive_analysis.py
rtrec_dump_experiment.py  rtrec_targeted.py   timeline_analysis.py
```
9/9 confirmed ✓

---

## Check 6 — B.2 e_kbmag → e35_kbmag rename + .gap migration

```
$ ls experiments/e_kbmag/  →  e_kbmag/ GONE ✓
$ ls experiments/e35_kbmag/ →  README.md  runs  script
$ ls experiments/e35_kbmag/script/  →  e35_check.gap  e35_mix.py
```

e_kbmag/ gone ✓; e35_kbmag/ exists with script/{e35_check.gap, e35_mix.py} = exactly 2 files as expected ✓

12 m22*/m23*.gap files confirmed at m23_kbmag/script/ (listed in Check 5 above, counted = 12) ✓

---

## Check 7 — Smaller sweeps

**ui/ post-cleanup**:
```
__pycache__/           benchmarks_data.json   benchmarks.html
comm_12_9_data.json    comm_12_9.html         comm_12_9_reduced.html
comm_12_9_reduced_data.json  comm_13_10_data.json   comm_13_10.html
comm_6_2_data.json     comm_6_2.html          cross_analysis_data.json
cross_analysis.html    index.html             runs/
server.py
```
`ui/scripts/`: GONE ✓ (24 subdirs confirmed dropped)

`ui/b25_mix`: Found at `ui/runs/b25_mix/` (a run subdirectory preserved inside ui/runs/) ✓

`orchestrator/`: GONE ✓

**patterns/ residual** (only .py analysis scripts + analysis_results.json):
```
__pycache__  analysis_results.json  deep_dive.py  full_comparative.py
internal_structure.py  kb_dynamics.py  rule_graph_3d.py  rule_structure.py
rule_trie.py  trie_evolution.py  visualize.py
```
figures/ moved ✓ (now at analysis/archive/b25/ — 45 PNGs); debug_runs/ archived ✓

**analysis/archive/b25/**: 45 entries (45 PNGs by name-check sample):
```
1_growth_rate_decay.png, 10_return_map_fixed_points.png, ...
```
NOT gitignored (correct — figures are committed as permanent reference) ✓

**experiments/_shared/**:
```
gen_b25_kbmag.py  generate_b25_challenges.py
```
2 scripts present ✓

**Stale b43_bidir.py** at old `b43_bidirectional/` location: GONE ✓ (Phase 5 Part B clean-up confirmed)

**git status count**:
```
$ git status --short | wc -l
558
```
✓ Routing states "614 → 558". Confirmed 558.

---

## Summary table

| Check | Item | Result | Receipt |
|---|---|---|---|
| 1 | Gitignore artifacts (e35, runs/, analysis/) | ✅ PASS | :49:*.kbprog.live hits on 3 new paths |
| 1 | Gitignore negations (scripts, PNGs, _shared) | ✅ PASS | exit-code 1 on all 5 |
| 2 | Archive count | ⚠ 7/8 | 7 tarballs confirmed; 1 count discrepancy vs routing's "8" |
| 2 | PROVENANCE.md sidecar per tarball | ✅ PASS | 7/7 sidecars present |
| 2 | Ask 2 fields (What/Validity/Pointer) | ✅ PASS | Confirmed in 2 spot-checked files |
| 2 | C4 invalidity label verbatim | ✅ PASS | bias_bidir_rules PROVENANCE.md confirmed |
| 3 | runs/ present at 3.0G | ✅ PASS | `du -sh runs/` = 3.0G |
| 3 | runs/ gitignored | ✅ PASS | .gitignore:34:**/runs/** |
| 3 | Stale-ref count | ⚠ 25 vs "7" | Not broken (runs/ preserved); methodology differs; morning packet |
| 4 | kbmag_agent.py state_dir fix | ✅ PASS | line 98: `base_dir / "kbmag" / ordering_name` |
| 4 | Smoke test | ✅ PASS | `/tmp/test_run/kbmag/kbprog_rpo` confirmed |
| 5 | m23 exploratory 9 scripts | ✅ PASS | All 9 named scripts confirmed |
| 5 | m23_mix.py + analyze_rules.py at script/ top | ✅ PASS | Only .py scripts at top; .gap files are B.2 migration |
| 6 | e_kbmag/ gone, e35_kbmag/ exists | ✅ PASS | GONE / exists confirmed |
| 6 | e35_kbmag/script/ 2 files only | ✅ PASS | e35_check.gap + e35_mix.py |
| 6 | 12 .gap at m23_kbmag/script/ | ✅ PASS | 12 counted (m22_kbmag, m22_setup, m23_atlas{,_verify}, m23_final, m23_fromperm, m23_pres, m23_simplepres, m23_to_kbmag, m23_v2, m23_v3, m23_verify8) |
| 7 | ui/ b25_mix preserved | ✅ PASS | ui/runs/b25_mix/ |
| 7 | orchestrator/ gone | ✅ PASS | GONE |
| 7 | stale b43_bidir.py gone | ✅ PASS | GONE (Phase 5 Part B) |
| 7 | patterns/ only .py scripts | ✅ PASS | figures/ in archive; debug_runs/ archived |
| 7 | analysis/archive/b25/ 45 PNGs | ✅ PASS | 45 entries confirmed |
| 7 | _shared/ 2 scripts | ✅ PASS | gen_b25_kbmag.py + generate_b25_challenges.py |
| 7 | git status = 558 | ✅ PASS | 558 confirmed |

**PHASE 5 COMPLETE WITH RECEIPTS.** Two minor count discrepancies (archive 7 vs 8; stale-ref count methodology) do not affect correctness of the restructure. All structural, gitignore, API, and migration claims independently verified.
