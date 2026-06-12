---
title: Phase 2 Regression Re-Audit — R1 + R2 Fix Verification
status: replicated
domain: cs
project: mixer-core
claim: "Developer's R1 (kbmag_source/ pristine restore) + R2 (b25_full reference sweep) + latent project_root depth fix are complete and the repo is clean for Phase 2 Part 2 (12-family restructure)."
claimant: Developer (overnight Phase 2), Lead K3 sample
verification_method: full-repo grep (stale path refs), git status + git ls-files (kbmag_source tracking), empirical project_root depth test, file content spot-checks
tools_used: [grep, git ls-files, git diff --cached, git status, python3 pathlib, md5]
author: aksimemor
tags:
  - agent/validator
  - user/aksimemor
  - domain/cs
  - project/mixer-core
  - status/replicated
---

# Phase 2 Regression Re-Audit Verdict

## Overall verdict

**PHASE 2 PART 2: AUTHORIZED WITH EXPLICIT EXCEPTION**

All primary regression checks pass. One kbmag_source/ tracking item outstanding — does not affect Part 2 execution but should be routed to Lead for a call (fix now or carry into restructure).

---

## Check 1 — Stale kb_data runtime references

**Grep command**: all `.py`, `.sh`, `.toml`, `.md` in repo, excluding `.git`, `.maestri`, `.venv`, `legacy/`.

**Pattern: `kbmag_v1/standalone/kb_data`**

```
experiments/_inputs/kbmag/README.md:5   — provenance note ("files copied from kbmag_v1/standalone/kb_data/")
experiments/burnside/b43_kbmag_mixing/README_LAYOUT.md:32 — historical note ("scripts previously referenced kbmag_v1/standalone/kb_data/b43 no longer find files there")
```

Both are README/documentation mentions. **Zero runtime refs (scripts/configs).** ✓

**Pattern: `kbmag_source/standalone/kb_data`**

```
experiments/_inputs/kbmag/README.md:6   — provenance breadcrumb ("one file b25_lifted from kbmag_source/standalone/kb_data/")
experiments/b25_reduce_core/README_LAYOUT.md:46 — historical note ("KB_DATA redirected from kbmag_source/standalone/kb_data")
```

Both are README documentation. **Zero runtime refs.** ✓

**Result**: All 4 hits are provenance breadcrumbs or historical notes in READMEs. No scripts or configs reference the old kb_data paths at runtime. R2 reference sweep: **PASS** ✓

---

## Check 2 — Project_root depth in 3 PR-3 scripts

**Empirical test** (`experiments/burnside/b25_kbmag/script/` depth = 5 levels from repo root):

```python
pathlib.Path(".../script/b25_mix.py").parent.parent.parent.parent.parent
  → /Users/maumayma/Desktop/reps/algo_mixing  ✓ (repo root)

experiments/_inputs/kbmag/b25_full exists at 5-parent path: True  ✓
experiments/_inputs/kbmag/b25_lifted exists at 5-parent path: True  ✓
```

**Per-file spot-check** (grep for `project_root` + `B25_INPUT`/`INPUT_FILE`):

| File | project_root line | depth | input path | result |
|---|---|---|---|---|
| `script/b25_mix.py:46` | `Path(__file__).parent.parent.parent.parent.parent` | **5** | line 54: `experiments/_inputs/kbmag/b25_full` | ✓ |
| `script/b25_mix_v2.py:45` | `Path(__file__).parent.parent.parent.parent.parent` | **5** | line 53: `experiments/_inputs/kbmag/b25_full` | ✓ |
| `script/standalone.py:25` | `Path(__file__).parent.parent.parent.parent.parent` | **5** | line 393: `experiments/_inputs/kbmag/b25_full` | ✓ |

No 3-parent project_root in the 3 PR-3 script files. Latent depth bug: **FIXED** ✓

**standalone.py INPUT_FILE**: comment at line 392 reads "stale fallbacks removed 2026-06-03" — confirms the fix was applied. Single canonical path. ✓

---

## Check 3 — kbmag_source/ pristine state

**git status `--short -- kbmag_source/`**: All entries show `??` (untracked from upstream). **No `M`, `D`, `R`, or staged modifications.** Criterion per routing: **PASS** ✓

**git diff `--cached -- kbmag_source/`**: Zero staged changes to kbmag_source/. ✓

**MD5 spot-checks:**

| File | MD5 | Result |
|---|---|---|
| `kbmag_source/standalone/kb_data/b25_lifted` | `8b0f3da95a3b5c87bd8f9974a35978d9` | matches `_inputs/kbmag/b25_lifted` ✓ (Lead K3 confirmed, I independently confirmed) |
| `experiments/_inputs/kbmag/b25_lifted` | `8b0f3da95a3b5c87bd8f9974a35978d9` | byte-identical ✓ |
| `kbmag_source/standalone/lib/fsa.c` | `d1f6f83f406d7a270db436c320a7d7da` | upstream file, unmodified ✓ |

Content check: **PASS** ✓

**⚠ EXCEPTION — kbmag_source/ git tracking not cleaned up:**

`git ls-files kbmag_source/` on origin/main still shows:
```
kbmag_source/README_biased_agents.md        ← project file ADDED to upstream, still tracked
kbmag_source/standalone/kb_data/b25_lifted  ← project input ADDED to upstream, still tracked
```

Lead's K3 verified `b25_lifted` content is byte-identical (no data risk). But **neither file has been `git rm --cached`'d**. The PR-1 violation is verified-safe but not git-removed.

- `kbmag_source/README_biased_agents.md`: Lead's K3 did NOT check this file — it was missed. It exists on disk and is still tracked. This was the core "NEVER TOUCH kbmag_source/" violation (project-written README inside upstream package).
- `kbmag_source/standalone/kb_data/b25_lifted`: Lead K3 checked content only. Still tracked.

**Does this block Part 2?** Part 2 is the 12-family restructure — it does NOT touch `kbmag_source/`. The tracking violation doesn't affect the restructure execution. Fix is a 30-second two-line git rm. Recommend: fix before Part 2 starts to avoid carrying the violation through the 6-10 hour window.

---

## Check 4 — kbmag_source/ context and staged changes

The staged index shows `R100` renames of kbmag_v1/standalone/kb_data → experiments/_inputs/kbmag (Group IV input rescue) and `D` deletions of kbmag_v1 generated artifacts (Group I git rm --cached). No staged changes involving kbmag_source/. The Phase B restructure is progressing correctly; kbmag_source is out of scope.

---

## Additional findings (non-blocking, morning packet items)

**A. standalone.py KBMAG_BINARY fallback — stale paths still present**

Lines 381-390 contain a 5-path fallback for the KBMAG binary discovery:
```python
Path("/Users/maumayma/Desktop/reps/algo_mixing/kbmag_detailed/standalone/bin/kbprog"),
project_root / "kbmag_detailed/standalone/bin/kbprog",
project_root / "kbmag/standalone/bin/kbprog",
project_root / "api/kbmag/standalone/bin/kbprog",
Path(__file__).parent.parent / "kbmag/standalone/bin/kbprog",  ← also wrong depth
```

None of these paths exist. `kbmag_detailed/`, `kbmag/`, `api/kbmag/` are not in the repo. The script will set `KBMAG_BINARY = None` and exit with "Error: KBMAG binary not found." **Note**: this is the BINARY discovery fallback, NOT the INPUT_FILE fallback (which was correctly fixed to canonical single-path). b25_mix.py and b25_mix_v2.py define `KBMAG_BIN = str(project_root / "kbmag_v1" / "standalone" / "bin" / "kbprog")` directly and are unaffected. standalone.py binary fix is a separate task.

**B. b43_mix.py pre-existing depth bug**

`experiments/burnside/b43_kbmag_mixing/b43_mix.py:25`:
```python
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
```
3-parent from `experiments/burnside/b43_kbmag_mixing/b43_mix.py` → `experiments/burnside/` → `experiments/` → `experiments/` (3-parent = `experiments/`, NOT repo root; needs 4-parent).

Pre-existing, not introduced by R1/R2/R3. Same bug in `b43_bidirectional/`, `burnside_bidirectional/` scripts (all at `experiments/burnside/<X>/` depth, using 3-parent). Not blocking Part 2.

---

## Authorization summary

| Check | Result | Notes |
|---|---|---|
| Stale kbmag_v1/kb_data runtime refs | ✅ PASS | 0 runtime hits; docs-only |
| Stale kbmag_source/kb_data runtime refs | ✅ PASS | 0 runtime hits; docs-only |
| 3-parent depth in PR-3 scripts | ✅ PASS | All 3 now 5-parent |
| INPUT_FILE canonical path (3 scripts) | ✅ PASS | All 3: experiments/_inputs/kbmag/b25_full |
| Empirical 5-parent test | ✅ PASS | Resolves to repo root; _inputs paths exist |
| kbmag_source/ git status (no M/D/R) | ✅ PASS | Only `??` untracked entries |
| b25_lifted md5 (byte-identical) | ✅ PASS | 8b0f3da9... = _inputs/ md5 |
| kbmag_source README_biased_agents.md removed | ⚠ EXCEPTION | Still tracked; Lead K3 missed this file |
| kbmag_source b25_lifted git rm'd | ⚠ EXCEPTION | Content verified; git tracking not cleaned |
| standalone.py KBMAG_BINARY paths | ℹ NOTE | Stale paths in binary discovery; separate fix needed |
| b43_mix.py 3-parent depth | ℹ NOTE | Pre-existing bug, not R1/R2 regression |

**PHASE 2 PART 2: AUTHORIZED.** The kbmag_source tracking exception does not block the 12-family restructure (Part 2 doesn't touch kbmag_source/). Route exception to Lead: fix is `git rm --cached kbmag_source/README_biased_agents.md kbmag_source/standalone/kb_data/b25_lifted` (30 seconds) — recommend doing it before Part 2 commits rather than after.
