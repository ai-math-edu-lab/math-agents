---
title: braid-reduce
path: experiments/burnside/burnside_bidirectional/src/bin/braid_reduce.rs
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "braid_reduce binary (experiments/burnside/burnside_bidirectional/target/release/braid_reduce)"
invariants:
  - id: exponent-5
    summary: "All B(2,5) reduction runs must pass --exponent 5; changing the exponent changes the group axioms applied."
    why: "braid_reduce uses the exponent to apply power and braid identities. Passing the wrong exponent silently produces words that are reduced in a different group."
  - id: abelianization-invariant
    summary: "Every step must preserve abelianization (word.count('a') - word.count('A')) mod 5 = 0 and similarly for b. This is tracked by the Python benchmark scripts but NOT by braid_reduce itself."
    why: "The FIXED braid_reduce_fast bug (non-abelian inverse order) was undetected because the Python verifier had the same bug. Abelianization is an independent invariant: any rule rewrite that changes (a-A mod 5, b-B mod 5) away from (0,0) is incorrect. Tracking it in the benchmark harness catches future bugs at the boundary."
  - id: binary-path
    summary: "The correct binary path is experiments/burnside/burnside_bidirectional/target/release/braid_reduce. Several older scripts reference experiments/burnside_bidirectional/target/release/braid_reduce (path no longer exists) and will silently fail."
    why: "The braid_reduce source lives at experiments/burnside/burnside_bidirectional/. The top-level experiments/burnside_bidirectional/ directory has been removed (shown in git status as staged deletions). Shell scripts that still reference the old path get a non-zero exit and produce no output without an obvious error message."
related:
  - kbmag-source
  - reduce-coreless
  - traced-braid-reduction
  - b25-reduce-core-deps-2026-05-22
tests:
  unit: experiments/b25_reduce_core/verify_reduction.py
  integration: "none — correctness checked via abelianization invariant in benchmark harness"
known_issues:
  - "Path mismatch: overnight_4pass_smallfirst.sh, overnight_6pass.sh, remaining_4pass.sh, reduce_benchmark.py, reduce_benchmark_v2.py all reference the now-removed path experiments/burnside_bidirectional/target/release/braid_reduce. These scripts fail silently unless the path is updated."
  - "LOG_RULES=1 and LOG_ALL_BEAM=1 env vars enable verbose structured logging to stderr; this output is parsed by run_full_logged.py but not by the simpler shell scripts."
  - "Source is present on disk at experiments/burnside/burnside_bidirectional/src/bin/braid_reduce.rs. The old top-level experiments/burnside_bidirectional/ directory has been removed (git status shows staged deletions from commit bc3cba2's tree)."
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# braid-reduce — Rust word-reduction binary with beam search

## What it is

`braid_reduce` is a compiled Rust binary that reduces words in Burnside groups using a combination of braid identity rewriting, power-reduce (`g^n → g^(n mod exp)`), a loaded rule bank scanned via Aho-Corasick, and optional beam-search over rule applications. It takes a word from a file, a rule bank in `.live` format, and CLI parameters for the search budget, then writes the reduced word to an output file.

## Why it exists

Python-only reduction with sequential rule scanning is too slow on the 2.5 GB `mega_ab_rules.live` bank for iterative multi-pass work. The Rust binary builds the Aho-Corasick automaton once, can run multiple passes with `--num-passes`, and performs beam search in native code. The Python benchmark scripts use it for phases 2 and 3 of reduction, after the Python `braid_reduce_fast` pass handles the coarse structure.

## How it fits in the system

The benchmarking pipeline feeds into `braid_reduce` after Python preprocessing:

> [[reduce-coreless]] (Python: free + power + braid) → intermediate word file
> → `braid_reduce` (rule bank scan + beam search) → output word file
> → `collect_best.sh` → `ui/benchmarks_data.json`

The Python scripts `reduce_benchmark.py`, `reduce_benchmark_v2.py`, and `run_full_logged.py` all invoke `braid_reduce` via `subprocess.run()`. The shell scripts (`overnight_4pass_smallfirst.sh`, `overnight_6pass.sh`, `remaining_4pass.sh`, `retry_failed.sh`, `run_logged.sh`, `run_traced.sh`) invoke it directly in bash.

## Critical invariants — why each one exists

### exponent-5

B(2,5) has exponent 5: every element satisfies `g^5 = e`. `braid_reduce` applies both single-generator power reductions (`a^k → a^(k mod 5)`) and two-generator braid reductions (`(gh)^k → equivalent shorter form mod 5`). Running with `--exponent 3` would instead apply `g^3 = e`, producing words that are reduced in B(2,3) — a different (much smaller) group. Since no output format records which exponent was used, a mistakenly-produced result would be silently wrong.

### abelianization-invariant

The abelianization of a word `w` in B(2,5) is `(Σa − ΣA mod 5, Σb − ΣB mod 5)`. For a commutator `[c, d]`, this must be `(0, 0)`. The `braid_reduce` binary does not check this internally. The Python benchmark harness (`reduce_benchmark.py`, `reduce_benchmark_v2.py`) checks abelianization after every phase and aborts with an error if it drifts. This invariant caught the original `braid_reduce_fast` Python bug (non-abelian inverse order, which shifted abelianization by `(3,3) mod 5` per wrong braid step). See memory note: `CRITICAL BUG FIXED: braid_reduce_fast`.

### binary-path

The `experiments/burnside_bidirectional/` top-level directory has been removed from disk (git status shows staged deletions). The current source and binary live under `experiments/burnside/burnside_bidirectional/`. Five scripts were found during the Phase 1 trace to reference the old (now-missing) path: `overnight_4pass_smallfirst.sh`, `overnight_6pass.sh`, `remaining_4pass.sh`, `reduce_benchmark.py`, `reduce_benchmark_v2.py`. These scripts produce no output and exit with a non-zero status.

## Public surface — what other components touch

The CLI interface as used by b25_reduce_core scripts:

```
braid_reduce \
  --word-file <input.txt> \
  --exponent 5 \
  --rules-file <rules.live> \
  [--beam-width N]        # default 16384 in shell scripts
  [--beam-secs N]         # 60–600 depending on script
  [--no-beam]             # braid+power only, skip search
  [--num-passes N]        # build AC once, run N passes
  [--output <out.txt>]    # reduced word written here
  [--trace-file <t.json>] # per-step JSON trace (run_traced.sh)
```

Environment variables (parsed by `run_full_logged.py`):
- `LOG_RULES=1` — emit `RULE\t...` lines to stderr for each rule application
- `LOG_ALL_BEAM=1` — emit `BEAM_BEST\t...` and `BEAM_RULE\t...` lines

Input format: plain text file, one word per line (generator alphabet `{a,A,b,B}`).
Output format: plain text file, the reduced word on a single line.

## Hot path?

Not a hot path in the b25_reduce_core workflow — it runs once per word per benchmark pass, with budget 60–600 seconds. The internal beam search loop is the computational hot path inside the binary itself.

## Tests

- `experiments/b25_reduce_core/verify_reduction.py` independently reconstructs the corrected 7245-char chain using only Python identity rewrites, without invoking `braid_reduce`. See [[traced-braid-reduction]].
- Abelianization checks in `reduce_benchmark.py::reduce_one()` provide runtime correctness guards on every phase-2 and phase-3 output.

## Related

- [[kbmag-source]] — produces the rule banks (`.kbprog.live`) that braid_reduce consumes
- [[reduce-coreless]] — Python preprocessing stage before braid_reduce in the pipeline
- [[traced-braid-reduction]] — test methodology for verifying individual reduction steps
- [[mixer-core-overview]] — Mixer Core family overview

## Recent changes

- 2026-05-22 — moved to Mixer Core/ from BraidReduce/; updated binary-path known_issue to reflect removal of top-level experiments/burnside_bidirectional/ directory
