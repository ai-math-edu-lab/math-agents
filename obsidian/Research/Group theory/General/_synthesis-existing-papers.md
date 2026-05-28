---
title: "Group Theory Papers — Cross-Paper Synthesis"
author: maumayma
language: en
last_updated: 2026-05-28
refresh_trigger: "Re-run on every new paper landing in Research/Group theory/**, or when Lead routes /research --reconnect group-theory. Update last_updated and the 'Papers covered' section."
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - synthesis
  - status/validated
---

# Group Theory Papers — Cross-Paper Synthesis

**Last updated:** 2026-05-28 by Researcher (F6.3 Phase 6).
**Refresh trigger:** Re-run this synthesis when a new paper lands in `Research/Group theory/**` or when Lead routes `/research --reconnect group-theory`.

## Papers covered (2026-05-28)

15 paper notes across Research/Group theory/ and Research/Algorithm Cooperation/. Synthesis below draws on all 15.

**Burnside groups / B25:**
- [[havas-wall-wamsley-1974]] — B(2,5) foundational paper (1974)
- [[havas-newman-1980]] — computational Burnside survey (1980)
- [[havas-robertson]] — FPG computational tools (1994)
- [[kourovka-2022]] — Kourovka Notebook No. 20 (2022)
- [[kourovka-11.48-kostrikin-1990]] — Problem 11.48 mathematical analysis
- [[problems-people]] — project scope and team (internal, 2025)

**Open problems:**
- [[b25-finiteness-11.48-kostrikin]] — Mixer attack rationale for 11.48
- [[b-exponent-5-adian-4.2b]] — exponent-5 groups (Adian, 1973)
- [[braid-b4-membership-6.24-makanin]] — B₄ membership (Makanin, 1980)
- [[burau4-faithfulness]] — Burau₄ faithfulness (open since 1936)
- [[2-relator-word-problem-9.29-merzlyakov]] — 2-relator word problem (Merzlyakov, 1984)
- [[andrews-curtis-conjecture]] — AC conjecture (1965)
- [[kaplansky-zero-divisors]] — Kaplansky zero-divisors (~1956)

**Algorithm Cooperation:**
- [[algo-mixing-burnside-slides]] — B(4,3) breakthrough + Mixer methodology (2025)
- [[grobner]] — Gröbner quotient test for FPGs (Kreuzer-Myasnikov-Rosenberger, 2025 draft)

---

## What's settled

**1. B(2,5) restricted group is finite, order 5^34, class 12.**

Established by [[havas-wall-wamsley-1974]] via two independent methods (Lie algebra + nilpotent quotient). The Lie-algebraic route (Kostrikin-Sanov-Wall) and the p-quotient route (Wamsley-Bayes-Kautsky) converge to the same answer. This is not contested in any of the 15 papers; subsequent sources ([[havas-newman-1980]], [[kourovka-2022]]) cite it without reservation.

**Implication:** The generator numbering 1–34 from this paper and the `comm_X_Y` naming convention are canonical input for all B(2,5) KB experiments.

---

**2. B(4,3) is finite, order 3^14 = 4,782,969; the Mixer KB approach works.**

Established by [[algo-mixing-burnside-slides]]: two KB orderings (r2l_rpo_loop + rpo_iter) cooperating via rule injection produced a confluent system in 2,333 rules in 33 minutes. Confluence verified (1,702,360 pairs, 0 failures); group order confirmed. No paper in this vault contradicts this.

**Implication:** The Mixer architecture is empirically validated for a hard Burnside instance. B(2,5) is the next target.

---

**3. Novikov-Adian covers odd exponents ≥ 665; exponent 5 is open.**

[[b-exponent-5-adian-4.2b]] and [[b25-finiteness-11.48-kostrikin]] agree: for odd n ≥ 665, B(m,n) is infinite for m ≥ 2. For n = 5 (and n = 7), neither finiteness nor infiniteness is known. The [[kourovka-2022]] notebook confirms Problem 11.48 (B(2,5) finiteness) is open as of 2022.

---

**4. The word problem for 1-relator groups is decidable (Magnus 1932).**

Stated in [[2-relator-word-problem-9.29-merzlyakov]] without dispute. The 2-relator case is open. This boundary is a settled fact in the background of all FPG work.

---

## What's contested / open

**A. B(2,5) unrestricted — finite or infinite? (Kourovka 11.48)**

The single most important open question across all 15 papers. [[kourovka-11.48-kostrikin-1990]], [[b25-finiteness-11.48-kostrikin]], [[b-exponent-5-adian-4.2b]], [[kourovka-2022]], [[algo-mixing-burnside-slides]], and [[problems-people]] all engage with this. No paper claims progress toward resolution. The mechanistic condition (Kostrikin): B(2,5) is infinite iff `[[[[[[x,y],y],y],y],y],y]` is not a product of 5th powers in F(x,y).

**Status:** Open. No computational evidence of either finiteness or infiniteness from KB experiments yet.

---

**B. The B₄ frontier — two open problems about the 4-string braid group**

[[braid-b4-membership-6.24-makanin]] (Kourovka 6.24) and [[burau4-faithfulness]] are distinct but related open problems:
- Membership problem: decidable for B₃, undecidable for B₅+, open for B₄.
- Burau₄ faithfulness: faithful for n≤3, unfaithful for n≥5, open for n=4.

No source in this vault shows progress on either. They share the "B₄ is the exceptional case" structure, making them natural twin problems.

---

**C. Gröbner approach for FPG word problem (grobner draft)**

[[grobner]] proposes a new approach: SL(n, Q_R) quotient test via Gröbner bases. The approach is new (2025 draft) and Section 7.5 (B(2,5) application) is incomplete ("TODO"). The claim that this approach works is demonstrated only for small Kourovka examples. No independent verification or follow-up.

**Status:** Promising but unverified for the B(2,5) scale. The [[algo-mixing-burnside-slides]] does not cite this paper; the connection between Gröbner and KB in a Mixer architecture is conceptual (from [[grobner]] itself), not experimentally validated.

---

**D. Witness words count for B(2,5) finiteness**

[[algo-mixing-burnside-slides]] claims "~50 witness words wᵢ such that if wᵢ = e for all i, then B(2,5) is finite." This claim is not sourced to any paper. No other paper in the vault verifies or contradicts it. **Flagged for Validator** in the note.

---

## Cross-cutting themes

**Multi-algorithm cooperation as the dominant strategy:**

Every major computational result cited across these papers used multiple algorithmic approaches cooperating:
- [[havas-wall-wamsley-1974]]: two independent methods (Lie algebra + nilpotent quotient).
- [[havas-newman-1980]]: "the basic approach is to apply several different computational techniques to the same problem."
- [[havas-robertson]]: KB + coset enumeration + Reidemeister-Schreier in a pipeline.
- [[algo-mixing-burnside-slides]]: two KB orderings cooperating via rule injection.
- [[grobner]]: Gröbner filter + KB in a hybrid Mixer architecture (proposed).

This convergence is the strongest cross-paper signal: **algorithm mixing is not a novel technique but the natural, historically validated approach to hard FPG problems.**

---

**Relevance gradient for current experiments:**

| Paper | Relevance to B(2,5) experiments | Direct use |
|---|---|---|
| havas-wall-wamsley-1974 | High — defines the input presentation | Generator table for KBMAG input |
| algo-mixing-burnside-slides | High — defines the architecture | B(4,3) parameters as B(2,5) starting template |
| kourovka-11.48-kostrikin-1990 | High — defines the question | Confirms what "success" means |
| havas-newman-1980 | Medium — historical context | B(4,3) baseline (1977 era) |
| grobner | Medium — future Mixer agent | Section 7.5 (incomplete) |
| burau4-faithfulness | Low — different problem | Architecture analogy only |
| kaplansky-zero-divisors | Low — torsion-free groups only | No direct B(2,5) connection |

---

## Open empirical questions for Experimenter

1. **Can the Mixer complete KB for B(2,5)?** The B(4,3) injection strategy (80 rules at 20k-rule trigger, shortlex + RPO) is the template. Which modifications help for the deeper (class 12) case?

2. **What injection parameters are optimal for B(2,5)?** The B(4,3) sweep found a "death zone" at batch-size 200. Is there a similar death zone for B(2,5)?

3. **Does the Gröbner approach (Section 7.5 of [[grobner]]) produce a fast "No" oracle for B(2,5) words?** What is the computational cost of the Gröbner basis for I_R at n=2?

4. **Do the bidirectional search experiments ([[b53_bidir]]) generalize to B(2,5)? What is the bottleneck — rule bank size, word difficulty, or proof strategy?**

---

## Refresh notes (for next Researcher)

On next `/research --reconnect group-theory`:
1. Update `last_updated`.
2. Check `Papers covered` section against actual files in `Research/Group theory/**`.
3. Re-assess "What's settled" if any new paper contradicts a settled claim.
4. Add new open questions if new papers surface them.
5. Flag any contradiction with `#risk/high` on the relevant paper note.

## About this synthesis

- [[group-theory-overview]] — parent: Research/Group theory/ directory map (links here as the synthesis resource)
- [[general-group-theory-overview]] — parent: Research/Group theory/General/ scope definition
- [[_moc-burnside]] — the burnside MOC that relies on this synthesis for its "what's settled" section
