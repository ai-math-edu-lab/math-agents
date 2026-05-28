---
title: traced-braid-reduction
path: experiments/b25_reduce_core/verify_reduction.py
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "verify_reduction.py — run standalone: python verify_reduction.py (requires ui/comm_12_9_reduced_data.json and word_coreless.txt)"
invariants:
  - id: identity-chain
    summary: "Every step in the reduction chain must use a named B(2,5) identity: free cancellation (xX=e), power reduction (g^5=e), or braid reduction ((gh)^5=e). Steps that cannot be attributed to one of these identities are not valid."
    why: "The point of the trace is to make the equality chain machine-checkable: if every step is a valid B(2,5) identity, the chain is a proof. If any step uses a rule whose validity is assumed rather than proven, the chain is only as trustworthy as that assumption."
  - id: abelianization-at-each-step
    summary: "After each step in the traced reduction, abelianization (a-A mod 5, b-B mod 5) must remain (0,0)."
    why: "The FIXED braid_reduce_fast bug was undetected for a long time because verify_reduction.py had the same bug (self-certification). Tracking abelianization at every step, independently of what the reduction function claims, is the mechanism that would have caught that bug. It is now the primary per-step sanity check."
  - id: independent-reconstruction
    summary: "verify_reduction.py must reconstruct the reduction independently — not by replaying a stored trace, but by applying the same functions fresh and comparing the output."
    why: "A test that only replays a stored trace certifies that the replay matches the trace, not that the original result was correct. By rerunning the functions from scratch and comparing outputs at each intermediate step, the test catches both bugs in the current functions and drift between the stored result and the current implementation."
related:
  - reduce-coreless
  - braid-reduce
  - gap-word-equality
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# Traced braid reduction verification

## What it is

An end-to-end verification script for the comm_12_9 reduction chain in B(2,5). It independently reconstructs the full chain — from the original 28,652-char commutator word, through the lifted (544-char), coreless (15,328-char), and reduced (4,882-char → corrected 7,245-char) forms — by applying only named B(2,5) identities (free cancellation, power reduction, braid reduction). At each intermediate step it compares the recomputed word against stored references and checks that abelianization is preserved.

## Why it exists

The `braid_reduce_fast` function in [[reduce-coreless]] had a subtle non-abelian bug (using `GH` instead of `HG` for the inverse of `(gh)^k`). The bug was undetected for a long time because the original `verify_reduction.py` contained the same bug — the verifier self-certified the wrong answer. The corrected script serves as the reference verification for the FIXED implementation: it independently applies `power_reduce_traced` and `braid_reduce_traced` (traced versions of the same functions) and produces a step-by-step log of every identity used, where in the word it was applied, and what the abelianization was before and after.

## How it fits

Run once after any change to the reduction functions in [[reduce-coreless]], and as the ground-truth certification of the comm_12_9 reduction chain:

```
ui/comm_12_9_reduced_data.json (source of truth for lifted_word, core, RPO rules)
→ verify_reduction.py
  → recomputes: standard expansion, coreless expansion
  → applies: power_reduce_traced + braid_reduce_traced step by step
  → compares against: word_coreless.txt, result_coreless_reduced.txt
  → reports: VERDICT: ✓ REDUCTION VERIFIED CORRECT / ✗ VERIFICATION FAILED
```

## Critical invariants — why each one exists

### identity-chain

Every replacement in `power_reduce_traced` is labelled with the specific B(2,5) identity it uses (`a^5 = e`, `a^4 = a^{-1} = A`, etc.). Every replacement in `braid_reduce_traced` is labelled with `(gh)^k = (gh)^{k_mod}` or `(gh)^k = (HG)^{5-k_mod}`. The output log includes these labels. An independent reviewer can verify each labelled step by checking the group axioms. This transforms "trust the code" into "trust the identities plus the enumerated steps."

### abelianization-at-each-step

The script checks abelianization `(a-A mod 5, b-B mod 5)` at the start, after free reduction, after power reduction, and after braid reduction. Any drift from `(0,0)` triggers a `VERDICT: ✗ VERIFICATION FAILED`. This is the invariant that the original bug violated: each wrong braid step shifted abelianization by `(3,3) mod 5`. The fix made the invariant hold again. The check is independent of the reduction function's internal logic — it just counts character frequencies.

### independent-reconstruction

The script does not load a pre-computed result and replay it; it calls the same functions (`power_reduce_traced`, `braid_reduce_traced`) on the freshly-expanded coreless word and compares the output to the stored `result_coreless_reduced.txt`. If the functions are changed in a way that produces a different output, the comparison will fail — even if the new output is also correct. This is by design: the stored result is the reference, and any change to it requires re-running and re-blessing.

## Public surface — script interface

```
python experiments/b25_reduce_core/verify_reduction.py
```

No arguments. Requires:
- `ui/comm_12_9_reduced_data.json` (present)
- `experiments/b25_reduce_core/word_coreless.txt` (NOT committed — not runnable from clean checkout)
- `experiments/b25_reduce_core/result_coreless_reduced.txt` (NOT committed)

Output: step-by-step log with identity labels, abelianization values at each step, and a final `VERDICT` line.

## Related

- [[reduce-coreless]] — the Python module whose functions this test validates
- [[braid-reduce]] — Rust binary whose output this test cross-validates
- [[gap-word-equality]] — independent oracle for spot-checking individual equalities

## Known issues

- `word_coreless.txt` and `result_coreless_reduced.txt` are not committed to the repo. The test cannot run from a clean checkout. This is a data hygiene issue: these files should either be committed (if small enough) or their derivation script should be runnable.
- verify_reduction.py was itself the source of the original false-positive certification (it had the same bug as reduce_coreless.py). The corrected version was manually verified to produce `(0,0)` abelianization. Future maintainers should be aware of this history.
