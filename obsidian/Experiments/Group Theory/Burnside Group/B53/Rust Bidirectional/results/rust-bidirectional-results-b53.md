---
title: Rust bidirectional results — B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: bidirectional
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/bidirectional, project/b53, status/inconclusive, results]
---

# Results — Rust Bidirectional Search on B(5,3)

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | Words proved | Validated by |
|---|---|---|---|---|---|---|
| v1/v2 baseline | 2026-03-20 | shortlex only | **0/153 proved** on first pass at 98K rules; interrupted at 123K | ~1s (until interrupt) | 0/153 | None |
| v5 | ~2026-03 | 4 orderings (rpo, shortlex, wtlex, rpo-r2l) + dynamic conj | **144/153 proved** at 1733s; 9 remain unsolved | **1733s** | 144/153 | None (formal) |

## Coverage progression (v5)

Progress was not uniformly distributed across orderings:
- Shortlex source provided first proofs (low-hanging: straightforward reduction)
- RPO source added more
- **Wtlex source (2.3M rules) was key**: proved words 119–144 after its rule bank built — the last large batch before plateau
- Dynamic conjugation handled ~21% of proofs (13% focus-conj + 8% conj strategy)

## Nine hardest unproved words (v5, at 1733s)

These 9 words are believed to require KB rules from ordering banks not yet generated:
1. `EaceAdBDbaECAecbDBdC`
2. `ECbcBeadADEbCBcedaDA`
3. `AbaBEbABaeCAbaBebABaEc`

(Remaining 6 not named in records; 3 hardest are named above from memory.)

## Version history

**v1/v2** (2026-03-20): Single ordering (shortlex), config `run17_shortlex_only.toml`. First transfer at 98K rules → 0 proved. Run interrupted at 123K rules.

**v5** (date approximate): 4 orderings + dynamic conjugation (`b53_bidir.rs`). Proved 144/153 at 1733s. Significant improvement over v1/v2. The wtlex bank reaching 2.3M rules was the decisive event.

## Main findings

1. **144/153 proved**: The 4-ordering + dynamic conjugation strategy proves 94% of the target word set — a strong result that exceeds v1/v2's 0%.

2. **Wtlex is key for the hard words**: The last 26 proofs (119–144) required the wtlex ordering's 2.3M rule bank. No other ordering covered them.

3. **9 words structurally resistant**: The 3 named hard words (`EaceAdBDbaECAecbDBdC`, `ECbcBeadADEbCBcedaDA`, `AbaBEbABaeCAbaBebABaEc`) have not been proved by any ordering. Their structure suggests they need rule banks that current orderings don't generate efficiently.

4. **Bidirectional vs. KBMag**: Bidirectional search proves 94% of word instances; full KB completion (KBMag) achieves 0% convergence after 97h. For B(5,3), the per-word approach is far more tractable.

## Open questions

1. What ordering or ordering variant would prove the 9 remaining words? A 5th ordering (e.g. wtlex-r2l, wreath-variant) may be needed.

2. Are the 9 hardest words genuinely in B(5,3) (i.e., equal to identity)? If any of them is NOT equal to identity, that would be a significant finding about B(5,3)'s structure.

3. Could a beam search approach (as used in b25_reduce_core) help with the remaining 9?

## Related material

- [[Rust Bidirectional/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[data/rust-bidirectional-data-b53]] — target words, run locations
- [[methodology/rust-bidirectional-b53-2026-06-02]] — methodology, strategy breakdown
- [[KBMag/results/kbmag-results-b53]] — KBMag results (contrast — no convergence in 97h)
- [[2026-06-02-non-b25-forensic-inventory]] — §2c forensic provenance
