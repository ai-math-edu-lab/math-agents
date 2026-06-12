---
title: "Post-mortem: word_3705 contamination (braid_reduce_fast bug)"
domain: group-theory
project: b25
instance: B(2,5)
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/b25, status/disproven, data]
created: 2026-06-12
---

# Post-mortem: word_3705 contamination

**Status: INVALID artifact. Do not use word_3705.txt or word_best.txt as reduction targets.**

---

## What happened

The Python function `braid_reduce_fast` in the pre-correction B(2,5) pipeline contained a non-abelian inverse-order error. For the reduction of `(gh)^k`, it computed the replacement using `(G+H)*k_mod` where `G = g⁻¹`, `H = h⁻¹`. But since B(2,5) is non-abelian, `(gh)⁻¹ = h⁻¹g⁻¹ = HG`, not `GH`. Each wrong application shifts the abelianization of the output word by `(3,3) mod 5` relative to the input.

See full bug analysis: `experiments/b25_reduce_core/corrected/README.md`.

---

## How word_3705 was produced

The buggy pipeline ran on `comm_12_9 = [c12, c9]` (28,652 chars, abelianization `(0,0) mod 5`). The chain:

| Stage | Length | Abel | Validity |
|-------|--------|------|----------|
| Original `[c12, c9]` | 28,652 | (0,0) | ✓ |
| Lifted `{a,b,m}` | 544 | (0,0) | ✓ |
| Coreless `{a,b}` | 15,328 | (0,0) | ✓ |
| After power reduction | 10,624 | (0,0) | ✓ |
| After **BUGGY** braid | 8,402 → **4,882** | **(4,4)** | ✗ FIRST POISONING |
| After Python KB rules | ~3,732 | (4,4) | ✗ |
| After Rust `braid_reduce` (correct, but poisoned input) | ~3,707 | (4,4) | ✗ |
| word_3705.txt (further reduction from same buggy run) | **3,705** | **(4,4)** | ✗ |

From the point where buggy braid fires (producing 4,882 chars with abelianization `(4,4)`), every subsequent word is a representative of the **wrong coset** — a different group element from `[c12,c9]`. The "reductions" after that point are real (the words do get shorter), but they converge to the identity of the **wrong** coset.

---

## Why 3,705 chars is an invalid result

- **Abelianization check fails**: `word_3705.txt` has abelianization `(4,4) mod 5`. Any valid representative of `[c12,c9]` must have abelianization `(0,0) mod 5` (the original commutator has this).
- **Wrong group element**: the word does not equal `[c12,c9]` in B(2,5). It cannot serve as a reduced form, a beam-search seed, or a target for biased rule generation.
- **Over-reduction as tell-tale**: the corrected pipeline achieves only 7,245 chars for `[c12,c9]`. Any result substantially below that (without a new verified chain) is suspect.

---

## Verified identity of contaminated files

Both files in `experiments/burnside/b25_bias_bidir/targets/` are byte-identical:

```
word_3705.txt  SHA256: ca6b305081c14c156cc2f03bb74b187b56f1c80e4db00a604360341a3ded0808  (3,705 bytes)
word_best.txt  SHA256: ca6b305081c14c156cc2f03bb74b187b56f1c80e4db00a604360341a3ded0808  (3,705 bytes)
```

`word_best.txt` was an alias for "best known result" at the time — now known to be invalid.

---

## What is valid

The correct reduction of `[c12,c9]` is:

```
28,652 → 544 (lift) → 15,328 (coreless) → 10,624 (power) → 8,402 (fixed braid)
→ 8,394 (KB rules) → 8,388 (Rust no-beam) → 7,245 (Rust beam)
```

All stages preserve abelianization `(0,0) mod 5`. Chain documented in `experiments/b25_reduce_core/corrected/README.md`. Corrected result: `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars). Validator verdict: `#status/conjectured` (2026-05-22). See [[2026-05-22-comm-12-9-7245-final]].

---

## Downstream contamination

The biased KB rule banks generated using `word_3705` as the kbprog seed were specialised toward the wrong coset. The rules themselves are mathematically valid B(2,5) Knuth-Bendix rules, but their coverage is biased toward a group element that is not `[c12,c9]`. These rule banks are **not useful** for reducing `[c12,c9]` or related target words.

**Contaminated rule banks** (12 subdirs, ~1.3 GB total):
- `experiments/burnside/b25_bias_bidir/rules/3705_run4_*/`
- `experiments/burnside/b25_bias_bidir/rules/3705_run5_*/`
- `experiments/burnside/b25_bias_bidir/rules/weq_sl/`, `weq_rpo/` (validity unclear — may be biased on same wrong target)

**Archive status**: rule banks already moved to `algo_mixing-archives/2026-06-03-bias_bidir_rules.tar.gz` (archived 2026-06-03; provenance sidecar labels them "biased for wrong coset, not reusable as-is for intended target").

**Remaining on disk (pending quarantine)**:
- `experiments/burnside/b25_bias_bidir/targets/word_3705.txt`
- `experiments/burnside/b25_bias_bidir/targets/word_best.txt`

---

## Action items

1. **Quarantine** (proposed, awaiting Maria sign-off): move `word_3705.txt` and `word_best.txt` to `algo_mixing-archives/b25/contaminated/braid-bug-3705/`.
2. **README fix** (proposed): update `experiments/burnside/b25_bias_bidir/README.md` to mark these files INVALID and fix the `scripts/` → `script/` directory name error.
3. **Restart biased KB**: biased kbprog runs should restart from `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars, abelianization (0,0)).

---

## Related notes

- [[reduce-core-results]] — results table for the Reduce Core pipeline
- [[reduce-core-pipeline-b25-2026-05-22]] — corrected pipeline methodology note
- [[_progress|B(2,5) Progress Note]] — "Critical bug (RESOLVED 2026-05-22)" section
- [[2026-05-22-comm-12-9-7245-final]] — Validator note for the 7,245-char result
