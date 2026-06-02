---
title: "Synthesis — Burau₄ faithfulness: status, approaches, and combinatorial-search framing"
author: maumayma
language: en
domain: group-theory
status: draft
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/braid-groups
  - topic/braid-representations
  - topic/word-problem
  - synthesis
  - status/draft
papers_synthesized:
  - "[[bigelow-1999]]"
  - "[[long-paton-1993]]"
  - "[[datta-2022]]"
key_concepts:
  - "[[Concepts/burau4-faithfulness]]"
date_range: 1993 to 2022
project:
---

# Synthesis — Burau₄ faithfulness: status, approaches, and combinatorial-search framing

> **Synthesis note.** Covers the current state of the Burau₄ faithfulness question: which cases are settled, what the remaining n=4 case requires, and how it frames as a combinatorial-search problem (connecting to Part A's methodology catalog). Corpus is thin — three acquired papers + bibliographic references. The thinness is honest; surface it plainly.
>
> **Bibliographic references (no standalone notes)**: Burau (1936, German, Abh. Math. Sem. Univ. Hamburg 11:179-186) — original definition, unacquirable; Birman (1974) "Braids, Links, and Mapping Class Groups" (Ann. of Math. Studies 82, Princeton UP) — textbook survey; Kassel & Turaev (2010) "Braid Groups" (Springer GTM 247) — modern reference for Burau rep definition.

## The question

Is the Burau representation $\beta_4 : B_4 \to \mathrm{GL}_3(\mathbb{Z}[q^{\pm 1}])$ injective (faithful)? This is the last unresolved case of the Burau faithfulness problem, open since 1936.

## Sources reviewed

1. [[long-paton-1993]] — Long & Paton (1993, Topology 32(2)): proves $\beta_n$ unfaithful for $n \geq 6$ via a simple closed curve on the 6-punctured disc. Source paywalled; content from authoritative knowledge.

2. [[bigelow-1999]] — Bigelow (1999, Geometry & Topology 3:397-404, arXiv math/9904100): improves Long-Paton to $n = 5$ (i.e., $n > 4$) via a 5-punctured disc curve. Abstract retrieved verbatim.

3. [[datta-2022]] — Datta (2022, arXiv 2209.10826): establishes strong entry constraints on $\ker(\beta_4)$ via Garside normal form analysis; proves $\beta_4$ is "faithful almost everywhere." Abstract retrieved verbatim. Most significant post-2020 progress.

**Bibliographic only** (no notes): Burau 1936 (original definition), Birman 1974 (textbook survey), Kassel-Turaev 2010 (modern reference).

## Convergence

**Settled cases** (all sources agree):
- $\beta_n$ is faithful for $n \leq 3$ — classical result, not contested.
- $\beta_n$ is NOT faithful for $n \geq 5$: Long-Paton ($n \geq 6$) + Bigelow ($n=5$) together give this.
- **$n=4$ is open**: all sources agree this is the unique unsettled case.

**Methodological convergence**: both Long-Paton and Bigelow use the same geometric framework — simple closed curves on $n$-punctured discs with homological properties. Datta 2022 uses a completely different algebraic approach (Garside matrix entry analysis). The geometric and algebraic approaches converge on the same conclusion (strong constraints) without resolving the question.

## Disagreement

No mathematical disagreement in the literature — the settled cases are universally accepted. The divergence is methodological: the geometric curve approach (Bigelow, Long-Paton) is unlikely to extend to $n=4$ (the 4-punctured disc has fewer topological degrees of freedom than the 5-punctured disc), which is why Datta's algebraic approach represents a different line of attack.

## What's settled

1. **Faithfulness/unfaithfulness chain**: faithful for $n \leq 3$; unfaithful for $n \geq 5$. Proof chain: Long-Paton → Bigelow (as published in peer-reviewed journals; Bigelow's arXiv version is open access).
2. **$n=4$ is the unique remaining case**: every subsequent reference to the "Burau faithfulness problem" means $n=4$ specifically.
3. **$\beta_4$ is faithful "almost everywhere"** (Datta 2022): any kernel element, if one exists, must satisfy strong algebraic constraints. This is the most current partial result.
4. **No Kourovka Notebook number**: Burau₄ faithfulness does not appear in the 2022 Kourovka Notebook (confirmed from vault note `open-problems-catalog.md`). The open problem lives in the braid group / mapping class group community, not the general algebra Kourovka tradition.

## What's contested

**Nothing in the settled cases is contested.** The following are genuinely open:

- **$\ker(\beta_4) = \{e\}$?** — The question itself.
- **Minimal kernel element length** — If $\ker(\beta_4)$ is non-trivial, what is the shortest braid word in it? Short-braid enumeration can put a lower bound.
- **Whether the geometric approach can extend to $n=4$** — Bigelow's geometric construction doesn't obviously adapt (4-punctured disc has fewer free parameters). Not formally proved impossible.

## What's open

1. **Primary question**: is $\beta_4$ faithful?
2. **Constructive approach**: can a kernel element be found via computational search? Datta's constraints bound the search: only braids satisfying specific matrix-entry conditions need to be checked.
3. **Geometric approach**: is there an analogue of Bigelow's 5-punctured disc construction for the 4-punctured disc? (If such a curve exists, $\beta_4$ is unfaithful.)
4. **Consequences for B₄ word problem**: if $\beta_4$ is faithful, $\beta_4(b) = I \iff b = e$ in $B_4$, giving a structural proof of decidability. The word problem is already decidable (Garside), but faithfulness would give a linear-algebra certificate.
5. **Consequences for B₄ membership** ([[braid-b4-membership-6.24-makanin]]): if $\beta_4$ is faithful, it directly assists the membership problem — $b \in H$ iff $\beta_4(b) \in \beta_4(H)$.

## Methodology notes

**Corpus thinness**: only 3 papers directly acquired (Long-Paton, Bigelow, Datta). The field moves slowly — major results are decades apart. Birman and Kassel-Turaev provide background but are textbooks (not acquired as notes). The post-2020 search found only one result (Datta 2022) beyond the classic papers.

**Bigelow's venue error in prior vault**: the stub note listed Bigelow's paper as J. Amer. Math. Soc. This is incorrect. The correct venue is **Geometry & Topology** 3 (1999) 397-404. This note corrects the record.

---

## Combinatorial-search framing (the Part A / Part B bridge)

> This section makes the connection explicit between the Burau₄ problem and the general combinatorial-search methodology from [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]].

The Burau₄ faithfulness question is a **kernel-element search problem** over the braid group $B_4$. Its search structure maps directly onto the "partial-No oracle alongside complete search" pattern (Area 5 of the methodology catalog):

**The search problem stated algorithmically:**
> Given: the Burau representation $\beta_4 : B_4 \to \mathrm{GL}_3(\mathbb{Z}[q^{\pm 1}])$ and the Garside normal-form enumeration of $B_4$ by length.  
> Find: a braid word $b \in B_4$ with $b \neq e$ and $\beta_4(b) = I_3$ (or prove no such word exists).

**The partial-No oracle pattern:**

| Search component | Burau₄ instantiation |
|---|---|
| Complete oracle | Matrix equality check: $\beta_4(b) = I_3$ over $\mathbb{Z}[q^{\pm 1}]$. Decidable but $O(\ell^2)$ in braid length. |
| Partial-No oracle | Datta's entry constraints: for any kernel element, its Burau matrix entries must satisfy specific algebraic conditions. For most short braids, these fail instantly — fast "No." |
| Search space | Garside normal form enumeration of $B_4$ by length: canonical short-form for each braid class. |
| Information sharing | Datta's constraints filter the search space before the complete oracle is invoked — exactly the "clause sharing" or "counterexample" pattern from ManySAT / CEGAR. |

**Connection to ManySAT** ([[Research/Algorithm Cooperation/hamadi-et-al-2009-manysat]]): the Datta filter is analogous to ManySAT's short-clause sharing — both prune the search space globally using lightweight constraints derived from structural analysis, before the expensive complete check.

**Connection to CEGAR** ([[Research/Algorithm Cooperation/clarke-et-al-2000-cegar]]): the Datta constraints play the role of CEGAR's abstract model checker. A braid that fails Datta's constraints is "certainly not in the kernel" (like a spurious counterexample that the concrete system doesn't admit). A braid that passes Datta's constraints needs the full matrix check (like a counterexample that must be simulated in the concrete system).

**Mixer relevance**: the Burau₄ kernel-search problem is a natural domain for Mixer-style cooperation:
- One agent: Garside normal-form reduction (complete, slow)
- Second agent: Datta filter (partial-No, fast)
- Cooperation: Garside agent enumerates braid classes; Datta agent immediately filters most as non-kernel; remaining candidates go to full matrix equality check.

This is not currently implemented — Borys Nolikov is listed as the implementer in [[problems-people]] — but the architecture is direct.

## Recommendation

1. **The short-braid search is tractable**: systematically check all $B_4$ braids of Garside word length $\leq L$ for kernel elements, using Datta's constraints as the fast filter. Computationally feasible for moderate $L$ (the existing literature mentions bounds up to 2000 intersections for arc-pairs in a related approach). This would put an explicit lower bound on kernel-element length, which is publishable even without a full resolution.

2. **Datta 2022 should be checked for publication status**: the arXiv preprint (September 2022) may now have a journal home as of June 2026.

3. **The combinatorial-search frame is the correct Mixer framing**: the Burau₄ problem is NOT about KB completion or Burnside groups. Its Mixer relevance is as a **braid-word kernel search** — the Datta filter as partial-No oracle, Garside as complete search. See [[Concepts/burau4-faithfulness]] for the concept hub.

## Related vault material

- Papers: [[bigelow-1999]], [[long-paton-1993]], [[datta-2022]]
- Concept hub: [[Concepts/burau4-faithfulness]]
- Related problem: [[braid-b4-membership-6.24-makanin]] (B₄ membership — harder problem; Burau faithfulness assists it)
- Algorithm Cooperation cross-link: [[Research/Algorithm Cooperation/_synthesis-combinatorial-search-methods]] (Section 7: Mixer-shaped methods — the partial-No oracle pattern)
- Specific Mixer-shaped analogs: [[Research/Algorithm Cooperation/hamadi-et-al-2009-manysat]] (ManySAT), [[Research/Algorithm Cooperation/clarke-et-al-2000-cegar]] (CEGAR)
