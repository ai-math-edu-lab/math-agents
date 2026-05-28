---
title: kbmag-ordering-sweep
path: tests/
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "tests/{l2r_rpo_*,r2l_rpo_*,shortlex_*,*_kgram*,*_30min}/ — KBMag run output directories, not scripts"
invariants:
  - id: runs-not-scripts
    summary: "The tests/ ordering-sweep directories contain KBMag run OUTPUTS (b25_test.kbprog.live, b25_test.reduce, etc.), not executable test scripts. The scripts that launched these runs are not present in tests/."
    why: "The sweep was run with external scripts (likely a precursor to run_biased_agents.sh or a manual loop). The results were committed as data. To re-run the sweep, the launch scripts must be recovered or reconstructed."
  - id: b43-not-b25
    summary: "The naming convention (b25_test.*) and the README description ('B(4,3) mixing experiments') appear inconsistent. The actual group tested in each run must be verified from the kbprog input file, not from the directory name."
    why: "The README.md in tests/ says 'Historical test runs for B(4,3) mixing experiments' while the output files are named b25_test.*. Whether these runs were on B(2,5) or B(4,3) cannot be determined from the file names alone — the kbprog input file (b25_test, inside each run directory) would need to be inspected."
related:
  - kbmag-source
  - kgram-overlap-verification
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# KBMag ordering-sweep runs

## What it is

A collection of KBMag completion runs stored under `tests/` with different ordering and biasing configurations, used as a methodology for comparing which ordering produces the smallest or most useful rule set. Subdirectories follow the naming scheme: `l2r_rpo_*` (left-to-right RPO), `r2l_rpo_*` (right-to-left RPO), `shortlex_*` (shortlex), with suffixes `_kgram*` (k-gram biasing enabled) and `_30min` (30-minute run). Each directory contains kbprog output files: the presentation file (`b25_test`), the live rule bank (`b25_test.kbprog.live`), the reduction automaton (`b25_test.reduce`), and an equivalence class file (`.ec`).

## Why it exists

The choice of ordering (shortlex vs. RPO, left-to-right vs. right-to-left) dramatically affects which rules kbprog generates and how quickly it converges. For a new problem (new group, new target word), a systematic ordering sweep — run each ordering for a fixed time budget, compare the resulting rule sets by size, density of applicable rules, and reduction power — is the standard first step. The `tests/` directories preserve the results of such a sweep so that conclusions about ordering choice can be revisited without re-running.

## How it fits

The sweep is a one-time analysis that informs the choice of ordering for ongoing biased-agent runs:

```
(new problem setup)
→ launch kbprog with each ordering × biasing configuration
→ let each run for 30 min or until rule count stabilises
→ store outputs in tests/<ordering>_<variant>/
→ compare: tests/verify_kgram_special.py on each output vs. target word
→ pick ordering(s) with best applicable-rule density
→ use chosen ordering in run_biased_agents.sh
```

## Critical invariants — why each one exists

### runs-not-scripts

The `tests/` subdirectories are data stores, not executable tests. They contain the outputs of completed kbprog runs. There is no `run_sweep.sh` or equivalent in `tests/`. To re-run the sweep, one would need to recover the launch parameters from the kbprog input files in each directory (which encode ordering and biasing settings) and invoke kbprog manually or write a new sweep script.

### b43-not-b25

The README.md in `tests/` says "Historical test runs for B(4,3) mixing experiments." The output files inside each directory are named `b25_test.*`. This inconsistency is not resolved by file names alone. The actual group is determined by the content of the `b25_test` kbprog input file (which defines generators, inverses, and relations). A reader interested in which specific group was tested must inspect that file. This note documents the ambiguity rather than resolving it, as resolving it requires human confirmation.

## Public surface — script interface

There is no script to invoke. The runs are data. To use them:
- Read `<dir>/b25_test.kbprog.live` as a rule bank
- Feed to `tests/verify_kgram_special.py` or `tests/verify_special_rules.py`
- Or feed to `braid_reduce` as `--rules-file`

Special-word files for biasing comparison:
- `tests/special_word_comm_13_10.txt` — comm_13_10 target
- `tests/special_word_comm_13_10_rpo.txt` — RPO variant of the same word

## Related

- [[kbmag-source]] — the component that produces these run outputs
- [[kgram-overlap-verification]] — test to run on each ordering's output to compare biasing quality

## Known issues

- README says "B(4,3) mixing experiments" but the methodology is general: these runs were probably used for multiple groups. The `b25_test.*` naming reflects the input filename (which could be any group's presentation), not a specific group. Human confirmed: "probably for all of them, more general tests."
- Launch scripts that produced these runs are not preserved in `tests/`. Re-running the sweep requires reconstructing the kbprog invocation from the input files.
- `tests/special_mixer/` is a separate ongoing experiment directory (comm_13_10 reduction work), not part of this ordering-sweep methodology. See the stale-component inventory for its status.
