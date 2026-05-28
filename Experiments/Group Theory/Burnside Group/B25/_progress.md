---
title: B(2,5) Progress Note
domain: group-theory
project: b25
instance: B(2,5)
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/kbmag, topic/proof-search, project/b25, status/inconclusive, experiment]
last_updated: 2026-05-22 (Validator verdict added)
---

# B(2,5) Standing Progress Note

Last updated: 2026-05-22 by B25 Experimenter (documentation backfill session).

---

## Current question

Can we reduce the word `comm_12_9 = [c12, c9]` (current best: 7,245 chars in {a,b,A,B}) further using:
- larger / more targeted KB rule banks, or
- the X-core lifting trick (compressed {a,b,m} alphabet), or
- beam search with wider width or more time?

The deeper question: can comm_12_9 be reduced to the empty word (i.e., proved equal to identity in B(2,5))?

---

## What's been tried

| Experiment type | Status | Top-line outcome | Vault note |
|----------------|--------|-----------------|-----------|
| **KBMag** (RPO+shortlex mixing) | #status/inconclusive | Both agents stayed in EXPLORATION; no cascade at 30min; 3 injections (2,263 rules total). v2 (bisect) is 10x more memory-efficient and 15x faster injections. | [[KBMag/methodology/kbmag-overlap-scoring-b25-2026-05-22]] |
| **Rust Bidirectional** (dual-RPO, beam) | #status/inconclusive | 9 surviving runs across 3 passes (2026-03-20 through 2026-03-30). Targets: comm_22_3, comm_11_1_kyr, comm_13_10, lifted comm_12_9. Best reductions: comm_22_3 4162→4156, comm_13_10 2500→2494, lifted comm_12_9 1772→544 (gen_braid only). No words proved. Code deleted from disk; configs at git bc3cba2. | [[Rust Bidirectional/methodology/rust-bidirectional-b25-2026-05-22]] |
| **Reduce Core** (pipeline: power→braid→rules→beam) | #status/inconclusive | comm_12_9: **7,245 chars** (74.7% reduction, abelianization (0,0) ✓). Previous "3,707" result INVALIDATED (braid_reduce_fast bug). | [[Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]] |

---

## What's worked

- **X-core compression**: the 35-char pattern X = `ABabAbabABaBAbabABABabAbaBABaBAbabb` appears ~34× in comm_13_10 (2,500 chars) and allows lifting comm_12_9 from 28,652 to 544 chars. The compression is ~98% before re-expansion. This dramatically reduces the search space.
- **Pipeline reduction**: power + braid + greedy rules + Rust beam achieves 74.7% reduction of comm_12_9 (28,652 → 7,245). This is the best validated result.
- **Large rule bank**: merging 12+ KB runs (multiple orderings, multiple sessions) into a 25.7M rule master bank. Biased runs (kbprog seeded on target word) add domain-specific rules.
- **v2 mixing (bisect)**: 10x less memory than Aho-Corasick at 13M rules, enabling sustained long runs on B(2,5) that were previously memory-limited.

---

## What's stuck

| Problem | What would unblock it |
|---------|----------------------|
| comm_12_9 plateaus at 7,245 chars | (1) Wider beam / longer beam time; (2) biased KB runs on valid 7,245-char target (not the invalid 3,707); (3) X-core KB rules in {a,b,m} alphabet |
| KBMag: no cascade observed | Longer runs with v2 (bisect); Researcher input on whether B(2,5) KB cascade is theoretically possible |
| Rust Bidirectional: no surviving outputs | Need to recover from git + re-run; 7,245-char starting word is a much better target than 28,652 |
| All biased KB runs were on INVALID targets (word_3705/3707) | Restart biased KB on word_7245 = `corrected/final_beam.txt` |
| comm_12_9 identity proof | No path yet — 7,245 chars is still far from trivial |

---

## Critical bug (RESOLVED 2026-05-22)

`braid_reduce_fast` in Python had non-abelian inverse order error. All words derived from this function before the fix are INVALID (wrong group element). The 3,707-char "record" was invalidated. The corrected chain is documented in `experiments/b25_reduce_core/corrected/README.md`.

**Invalidated artifacts** (do not use):
- word_4882, word_3732, word_3707 (all in b25_bias_bidir/archive and b25_reduce_core/archive)
- Rule banks: `b25_bias_bidir/rules/3705_run4_*/`, `3705_run5_*/`, `weq_*/`
- `ui/comm_12_9_reduced_data.json#final_word` (contains 3707)
- Any beam/bidir run outputs derived from these

**Valid current best**: `experiments/b25_reduce_core/corrected/final_beam.txt` — 7,245 chars, abelianization (0,0).

---

## Next (prioritized)

1. ~~Route `corrected/final_beam.txt` (7,245 chars) to Validator~~ — **DONE. `#status/conjectured` 2026-05-22.** See [[Architecture/Mixer/Documentation/Math Validation/2026-05-22-comm-12-9-7245-final]].
2. **HIGHEST**: Run biased kbprog on word_7245 (now Validator-confirmed target) to generate new specialized rule banks; then re-apply pipeline. Previous biased runs were on INVALID targets (word_3707) — restart from scratch.
3. Run overnight benchmark with corrected pipeline on all 119 words to fill `benchmark_run/best_words/`.
4. Run b25_mix_v2.py for 10h+ to investigate whether cascade is possible at larger rule counts; compare against RPO-only baseline at same runtime.
5. Restore B(2,5) Rust Bidirectional configs from git (`bc3cba2`), re-run dual-RPO targeting 7,245-char word. File requirement to Lead if mixer-core changes needed.
6. Investigate: does the X-core KB in {a,b,m} alphabet reduce word_7245 further?

---

## Open literature questions for Researcher

- Is there published theory on whether KB with RPO must cascade (eventually) for finite Burnside groups? References beyond Adian-Novikov?
- What is known about the complexity of the word problem in B(2,5) as a function of word length?
- Are there papers on the "depth" of Burnside group commutators (i.e., do higher-weight commutators have structurally longer normal forms)?
- Kyr's construction for B(2,5) words (referenced in `b25_comm_11_1_kyr.txt`): what is this and is it published?

---

## Open math claims for Validator

- **CLAIM (`#status/conjectured` — 2026-05-22)**: the word `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars, abelianization (0,0)) represents the same element of B(2,5) as `[c12, c9]`. See [[Architecture/Mixer/Documentation/Math Validation/2026-05-22-comm-12-9-7245-final]].
  - Sub-claim A (input is a B(2,5) identity): VERIFIED by Havas relator byte match. Sub-claim B (chain soundness): PARTIALLY VERIFIED — abelianization (0,0) at all stages, lifted-KB rule m→m_pure evidences the expansion step. Sub-claim C (element equality): NOT VERIFIED — GAP kbmag does not complete KB on B(2,5); tooling limit reached.
  - Downstream work may proceed with `#status/conjectured` status. Do not cite as proven.

Verified by [[2026-05-22-comm-12-9-7245-final]]

---

## Literature

- [[havas-wall-wamsley-1974]] — establishes |B(2,5)| = 5^34 and class 12; provides the generator numbering (generators 1–34) that defines every target word in these experiments (comm_12_9, comm_13_10, comm_11_1_kyr, etc.).
- [[havas-newman-1980]] — survey of computer-assisted Burnside results; contextualizes the p-quotient algorithm that generated the B(2,5) presentation and establishes that applying multiple independent computational techniques to the same group is the right strategy.
- [[havas-robertson]] — computational framework for finitely presented groups: coset enumeration (§2.1), KB completion (§2.9), and Tietze transformation (§2.3); the technique classes used across all three B(2,5) experiment types.
- [[kourovka-2022]] — Kourovka Notebook No. 20 (2022); houses problem 11.48 (Kostrikin 1990) asking whether B(2,5) is infinite; no resolution note as of 2022.
- [[kourovka-11.48-kostrikin-1990]] — dedicated note on problem 11.48: the open theoretical question all B(2,5) word-reduction and KB work is ultimately in service of.
- [[problems-people]] — project planning document listing all B(2,5) algorithms and named implementers in the algo_mixing effort; confirms KB, coset enumeration, Cayley-graph search, and bidirectional KB as the full portfolio of approaches.
