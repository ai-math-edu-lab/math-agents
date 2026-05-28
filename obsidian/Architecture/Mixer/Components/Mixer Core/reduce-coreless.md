---
title: reduce-coreless
path: experiments/b25_reduce_core/reduce_coreless.py
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "free_reduce(w: str) -> str — free group cancellation (stack-based)"
  - "power_reduce(w: str) -> str — apply g^5=e, g^4=g^-1, g^3=g^-2 identities"
  - "braid_reduce_fast(w: str) -> tuple[str, int] — alternating-run reduction using (gh)^5=e; returns (reduced_word, total_delta)"
invariants:
  - id: non-abelian-inverse
    summary: "braid_reduce_fast uses (HG)^(5-k_mod) for k_mod in {3,4}, NOT (GH)^(5-k_mod). B(2,5) is non-abelian: (gh)^-1 = h^-1 g^-1 = HG."
    why: "An earlier version used (inv[g]+inv[h])*k_mod for all k_mod > 2, which is correct for abelian groups but wrong for B(2,5). The bug shifted abelianization by (3,3) mod 5 per wrong braid step. It was undetected for a long time because the original verify_reduction.py had the same bug (self-certification). The corrected forms: k_mod∈{1,2}: (g+h)*k_mod; k_mod∈{3,4}: (inv[h]+inv[g])*(5-k_mod). See memory: CRITICAL BUG FIXED."
  - id: abelianization-preserved
    summary: "Every application of free_reduce, power_reduce, and braid_reduce_fast must keep (w.count('a')-w.count('A')) mod 5 = 0 and similarly for b."
    why: "These are the only three operations used in the Python reduction path. If any one of them breaks abelianization, all downstream results are silently wrong. The benchmark scripts track this invariant explicitly after every Python phase."
  - id: restart-on-match
    summary: "braid_reduce_fast restarts the scan from position 0 after each replacement. This is correct but O(n^2) worst-case."
    why: "A partial-overlap replacement can create a new alternating run at the replacement boundary that was not present before. Restarting from scratch guarantees no such run is missed. On typical B(2,5) words (10k–30k chars) this is fast enough; it would become a bottleneck on much longer words."
related:
  - braid-reduce
  - traced-braid-reduction
  - b25-reduce-core-deps-2026-05-22
tests:
  unit: experiments/b25_reduce_core/verify_reduction.py
  integration: experiments/b25_reduce_core/benchmark_run/reduce_benchmark.py
known_issues:
  - "reduce_coreless.py is imported by benchmark scripts via sys.path.insert(0, '.../b25_reduce_core') — not a proper package install. Moving the file breaks the import without updating all callers."
  - "verify_reduction.py depends on ui/comm_12_9_reduced_data.json (present) and word_coreless.txt (NOT committed) — cannot run from a clean checkout."
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# reduce-coreless — Python B(2,5) reduction utilities (FIXED)

## What it is

`reduce_coreless.py` is a Python module providing three reduction functions for words in B(2,5): free cancellation (`free_reduce`), single-generator power reduction (`power_reduce`), and two-generator alternating-run reduction (`braid_reduce_fast`). It is the first stage of the benchmark pipeline for reducing the 119 commutator words, and is imported by `reduce_benchmark.py`, `reduce_benchmark_v2.py`, and `run_full_logged.py`.

## Why it exists

The Rust `braid_reduce` binary is the heavy lifter (beam search over a 2.5 GB rule bank), but it benefits from clean input. The Python functions eliminate the gross structure first: free cancellation removes adjacent inverse pairs, power reduction collapses runs like `aaa → AA` (since `a^3 = a^{-2}` in B(2,5)), and braid reduction collapses long alternating runs like `ababababab → AB` (since `(ab)^5 = e`). These three passes together reduce typical commutator words from 10k–30k chars to a few thousand before the Rust beam search takes over.

## How it fits in the system

The module sits at the Python-side entry point of the two-stage pipeline:

> `reduce_coreless` (Python: free → power → braid) → intermediate word
> → [[braid-reduce]] (Rust: rule bank + beam search) → final word

The module also runs as a standalone script (`__main__`) to reduce `word_coreless.txt` and compare with stored results.

## Critical invariants — why each one exists

### non-abelian-inverse

The core issue: B(2,5) is non-abelian. The inverse of the element `(gh)^k` is `(gh)^{-k}`, and `(gh)^{-1} = h^{-1} g^{-1} = HG`, **not** `GH`. The corrected replacement logic for `(gh)^k` where `k_mod = k % 5`:
- `k_mod = 0`: replace with `''` (identity)
- `k_mod ∈ {1, 2}`: replace with `(g+h) * k_mod` (literal repetition)
- `k_mod ∈ {3, 4}`: replace with `(inv[h]+inv[g]) * (5-k_mod)` ← THIS is the fix

The previous code used `(inv[g]+inv[h]) * k_mod` for k_mod > 2 — swapping `g` and `h` in the inverse. This is correct in an abelian group (`GH = HG`) but wrong in B(2,5). The symptom: the pattern `babababababa` = `(ba)^6` got replaced with `BA` instead of `ba`, shifting abelianization by `(3,3) mod 5` per wrong step.

### abelianization-preserved

The abelianization `(Σa − ΣA mod 5, Σb − ΣB mod 5)` of a commutator word `[c, d]` is `(0, 0)`. All three functions in this module are identity-preserving rewrites — they must not change this invariant. `power_reduce` uses only `g^5 = e` and its consequences; `free_reduce` uses `g · g^{-1} = e`; `braid_reduce_fast` uses `(gh)^5 = e`. Each is a proven B(2,5) identity. The benchmark harness checks `(0,0)` after every call; any drift means this file has a new bug.

### restart-on-match

`braid_reduce_fast` breaks out of the inner scan loop after each replacement (`break`) and restarts the outer `while changed` loop. This is necessary because a replacement can create a new alternating run at the boundary with adjacent characters. The restart guarantees the scan is exhaustive. The `O(n^2)` worst-case is acceptable for current word lengths.

## Public surface — what other components touch

`reduce_benchmark.py`, `reduce_benchmark_v2.py`, and `run_full_logged.py` import this module via:
```python
sys.path.insert(0, '/Users/maumayma/Desktop/reps/algo_mixing/experiments/b25_reduce_core')
import reduce_coreless as rc
```
Then call: `rc.free_reduce(word)`, `rc.power_reduce(word)`, `rc.braid_reduce_fast(word)`.

## Tests

- `verify_reduction.py` — independently reproduces the corrected 7245-char chain using the same functions step-by-step with full identity logging. Requires `word_coreless.txt`. See [[traced-braid-reduction]].
- `reduce_benchmark.py::run_python_phase()` — exercises all three functions on each of the 119 benchmark words and checks abelianization after every call.

## Related

- [[braid-reduce]] — Rust binary that takes over after this module's output
- [[traced-braid-reduction]] — test methodology that validates each step of the Python reduction chain
- [[mixer-core-overview]] — Mixer Core family overview

## Recent changes

- 2026-05-22 — moved to Mixer Core/ from ReduceCoreless/; documents the FIXED version (non-abelian inverse order corrected)
