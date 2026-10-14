---
title: "B(2,5) trivial words — 2.5-reduced fixed points, unique up to rotation, inversion and letter automorphisms (820, corrected)"
dataset_id: ds-b25-trivial-2-5reduced-aut8-20261014
date: 2026-10-14
domain: group-theory
project: challenge-gen
instance: B(2,5)
kind: trivial-words
format: "text, one word per line, letters a A b B (A = a⁻¹, B = b⁻¹); each line is a cyclic word; sorted by length, then lexicographically"
records: 820
files:
  - path: "math-agents-challenge-generation:data/b25_trivial_2_5reduced_unique_aut8_20261014.txt"
    sha256: e0eeb777200c3540a718295c2fc1da25e8b70595864b4c1bc537dcf13631dda1
    bytes: 59238
    role: data
  - path: "math-agents-challenge-generation:data/b25_trivial_2_5reduced_unique_aut8_20261014.sources.csv"
    sha256: ef39bb455983676fcad662d90d5c333457e43017781569badf7bc0efb8b54b82
    bytes: 99569
    role: sources
storage: "git — fork asetlearning/math-agents-challenge-generation, data/ (files prepared 2026-10-14; commit awaits owner approval, a human gate)"
derived_from:
  - "`[[ds-b25-trivial-2-5reduced-aut8-20261007]]` (sha256 62c6431c80cb0fa9b25476c5710eee1135c7f71deb130d8782c1750714f11e29). Identical except for two words: lines 14 and 15 of the parent are replaced, see § What changed."
produced_by: "b25_pyproject_agentic@2ea95a0:experiments/challenge_gen/hardness/make_fixed_point_dataset.py (branch 12-hardness-harness, PR #2), run locally 2026-10-14 against tcgraph_agentic@a0d5e92 (tcgraph_ext standalone build); T-012"
supersedes: "ds-b25-trivial-2-5reduced-aut8-20261007"
superseded_by: ""
property_claimed: "every word is trivial in free B(2,5) (Knuth–Bendix proof, see vetting; for the two replaced words also Validator's independent certificates for their orbit mates); every word is a fixed point of the 2.5 reducer in BOTH modes defined under 'Reducer'; no two words are related by rotation, inversion or a letter automorphism"
vetting:
  - check: trivial in free B(2,5), 818 unchanged words
    tool: "inherited from the parent note: kbmag kbprog + wordreduce on b25_full, recursive and shortlex systems"
    scope: "free B(2,5) — proof"
    result: "818/818 (parent run 2026-10-07; unchanged strings)"
    by: "agent/exp (asetlearning)"
  - check: trivial in free B(2,5), the 2 replaced words (lines 14, 15)
    tool: "kbmag wordreduce with the parent run's rec and slx systems (runs/kb-verify-20261007)"
    scope: "free B(2,5) — proof"
    result: "2/2 reduce to IdWord under both systems; over the whole file 819/820 per system, misses are line 431 (rec) and line 41 (slx) exactly as in the parent, so all 820 reduce under at least one and 818 under both"
    date: 2026-10-14
    by: agent/exp (asetlearning)
  - check: trivial in free B(2,5), orbit of the replaced words
    tool: Validator, own script (independent of tcgraph and kbprog), step-checked certificates of 12 and 13 steps
    scope: "free B(2,5) — proof, for the parent's words 13 and 14 (0-based); their images under the letter automorphisms are trivial too, since the automorphisms preserve the normal closure of all x^5"
    result: "#status/proven"
    date: 2026-10-14
    by: Validator, see [[2026-10-14-t001-l0-soundness-and-words-13-14]]
  - check: fixed point of the reducer in both modes (see 'Reducer'), all cyclic shifts
    tool: "tcgraph_agentic@a0d5e92 via tcgraph_ext (b25_pyproject_agentic@7e50fea bindings)"
    scope: syntactic (rewrites v^p → v^-(5-p), p ≥ 2.5, including the length-neutral p = 2.5 step)
    result: "820/820"
    date: 2026-10-14
    by: agent/exp (asetlearning)
  - check: abelianization trivial (exponent sums ≡ 0 mod 5)
    tool: Python
    scope: syntactic (necessary condition)
    result: "820/820"
    date: 2026-10-14
    by: agent/exp (asetlearning)
  - check: images under the 8 letter automorphisms × inversion are also fixed points
    tool: "harness images16 + the same reducer"
    scope: syntactic
    result: "818/820 words have all 16 images fixed points; lines 14 and 15 do not (and cannot: the orbit of each contains words the reducer shortens, and a word's 16 images are exactly its orbit's representatives), so for them the fixed-point property holds only for the stored representative"
    date: 2026-10-14
    by: agent/exp (asetlearning)
  - check: uniqueness up to rotation × inversion × Aut₈
    tool: "construction: each replacement is an image of the word it replaces (same class); 820 distinct strings"
    scope: syntactic
    result: "820 distinct classes"
    date: 2026-10-14
    by: agent/exp (asetlearning)
stats: {min_len: 32, max_len: 123, mean_len: 71.2, median_len: 67}
used_by: []
author: asetlearning
status: draft
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/word-problem, project/challenge-gen, project/b25, status/draft, dataset]
---

# B(2,5) trivial words — 2.5-reduced fixed points (820, corrected)

> [!info] Plain English
> Same 820 words as [[ds-b25-trivial-2-5reduced-aut8-20261007]], with two of them replaced. In the parent note, two words (lines 14 and 15) were *not* stable under the 2.5-power reducer as stored: the reducer shortens them to the empty word. They are still trivial in free B(2,5) and still the same symmetry classes, but they were not "2.5-reduced". Each is replaced here by its one image under letter relabelling or inversion that the reducer leaves alone.

**Status: draft** (prepared 2026-10-14, task T-012; waits for the owner's approval and for the files to be committed to the fork).

## What changed (T-012)
- The parent's `property_claimed` said "every word is a fixed point of `greedy_reduce_cyclic_exhaustive2_5`". That was checked on the *parent spellings* (the rpo/shortlex strings). The stored strings are canonical forms, i.e. other images of the same class, and the reducer is not invariant under letter relabelling or inversion. For two of them the claim fails. Validator: `#status/disproven` for those two, trivial in free B(2,5) `#status/proven` ([[2026-10-14-t001-l0-soundness-and-words-13-14]]). Found by the T-001 baselines ([[hardness-baselines-results]]).
- Replaced words (parent line → this dataset, before re-sorting):

  | Parent line | Parent string | Replacement string | fixed-point images found |
  |---|---|---|---|
  | 14 | `AABABAbabaBBababABABAABABBABABaababAAbabaBAB` | `AABABBABABababAAbabaBABABBABAbabaBBababbABAB` | 1 |
  | 15 | `AABABBABABaababAAbabaBABAbababbabaBBababABAB` | `AABABBABABababAAbabaababaBABAbabaBBababbABAB` | 1 |

  Each replacement is the shortlex-least rotation of the single image that is a fixed point. The 818 other words are unchanged strings. The file is re-sorted by (length, word); the `.sources.csv` is re-indexed and gets a last column `replaced_from` (the parent string, empty for unchanged words).

## Reducer (what "2.5-reduced / fixed point" means here)
A word is a fixed point if both of these keep its cyclically reduced length, over all cyclic shifts:
- **(A)** `greedy_reduce_cyclic_exhaustive2_5(w, None)`;
- **(B)** `greedy_reduce_cyclic_exhaustive2_5(greedy_reduce2_5(w), None)`, the pipeline of [[challenge-gen-success-metrics]] (R₂.₅ = cyclic-exhaustive after greedy).

Code: `tcgraph_agentic@a0d5e92`, `greedy_reduction.cpp`. This reducer applies the length-neutral move p = 5/2 (rule `q ≥ 2.5`); a strict p > 2.5 rule finds no step on the two parent words (Validator's remark, which is also why the parent's "not shortened" check and the harness differ). Which tcgraph pin ran the parent check was not recorded and was not checked here.

**Not invariant under symmetry:** 818 words are fixed points in all 16 images (8 letter automorphisms × inversion). For lines 14 and 15 only the stored representative is. Any hardness claim uses ρ_min16 (owner decision 2026-10-14, [[challenge-gen-success-metrics]]), and for these two words ρ_min16 = 0.

## Everything else
Origin, derivation, the Knuth–Bendix and GAP procedures, caveats (9 decomposable words, redundancy) and loading instructions are unchanged from the parent note [[ds-b25-trivial-2-5reduced-aut8-20261007]]; read them there. The GAP B₀(2,5) check was not repeated for the two replacements (they are automorphic images of GAP-checked words, so it holds by symmetry, but this was not re-run).

## How to load
```python
import hashlib
from pathlib import Path

p = Path("<math-agents-challenge-generation checkout>/data/b25_trivial_2_5reduced_unique_aut8_20261014.txt")
assert hashlib.sha256(p.read_bytes()).hexdigest() == \
    "e0eeb777200c3540a718295c2fc1da25e8b70595864b4c1bc537dcf13631dda1"
words = p.read_text().split()          # 820 strings over {a, A, b, B}
```

## Used by
- (none yet; [[hardness-baselines-results]] used the parent)

## Related material
- [[ds-b25-trivial-2-5reduced-aut8-20261007]]: the superseded parent
- [[datasets-convention]] · [[challenge-gen-success-metrics]] · [[Experiments/Group Theory/Challenge Generation/_progress|Challenge Generation progress]]
- [[project-challenge-gen]]
