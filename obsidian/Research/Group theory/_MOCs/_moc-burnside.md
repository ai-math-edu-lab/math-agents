---
title: "Burnside Groups — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/moc
  - status/validated
---

# Burnside Groups — Map of Content

**This MOC is a curated reading path for the Burnside group program** — from the foundational B(2,5) computation (1974) through the open B(2,5) finiteness question, to the B(4,3) Mixer breakthrough (2025). Navigate here when you want to understand where we are, what's settled, and what's open on Burnside groups.

---

## Foundational papers

- [[havas-wall-wamsley-1974]] — The 1974 paper that establishes |B(2,5)| = 5^34, class 12, via two independent methods; defines the generator numbering 1–34 that is the source of all `comm_X_Y` naming in B(2,5) experiments. Read this before anything else on B(2,5).

- [[havas-newman-1980]] — 1980 survey contextualizing B(2,5) within the broader Burnside program; gives |B(4,3)| = 2^69, class 7 — the 1977 baseline against which the Mixer's B(4,3) result must be compared. Source of the "apply several different techniques to the same problem" framing.

---

## The open problem

- [[kourovka-11.48-kostrikin-1990]] — Mathematical analysis of Kostrikin's Problem 11.48 (1990): B(2,5) is infinite iff the weight-7 commutator `[[[[[[x,y],y],y],y],y],y]` is not a product of 5th powers in F(x,y). The formal statement of what "success" means for all B(2,5) experiments.

- [[kourovka-2022]] — Source of Problem 11.48 in the Kourovka Notebook No. 20; confirms the problem is open as of 2022. Also contains Problem 4.2b (Adian) and the Gröbner-relevant problems 7.25 and 11.10b.

- [[b-exponent-5-adian-4.2b]] — Adian's equivalent framing (1973): do infinite finitely generated groups of exponent 5 exist? Equivalent to Problem 11.48 for m=2. Broader perspective when the B(2,5) result generalizes to B(m,5).

---

## Mixer attack

- [[b25-finiteness-11.48-kostrikin]] — Researcher's strategic note: why KB mixing is the right tool for Problem 11.48, what the B(4,3) precedent shows, and what we don't yet know about B(2,5). The Mixer-attack angle, distinct from the mathematical analysis in [[kourovka-11.48-kostrikin-1990]].

- [[algo-mixing-burnside-slides]] — The B(4,3) breakthrough (2025): two KB orderings cooperating via rule injection in 33 minutes, 2,333 rules, confluence verified. Verbatim run logs and B(4,3) relators. The proof-of-concept for all subsequent Burnside experiments.

---

## Cayley-table-closure attack (Kuznetsov line, Russian, 2009–2010)

A third algorithmic family for B(2,5): Cayley-table closure on a length-truncated minimal-word set. Distinct from KB completion and coset enumeration; provides a clean finite/infinite dichotomy and a list of 973 candidate-divergence relations at lengths 30–35 in $B_0(2,5)$ whose failure in $B(2,5)$ would prove infiniteness.

- [[kuznetsov-shlepkin-2009]] — Introduces Algorithm I (row-collision-based Cayley-table closure) on free Burnside groups. Computes $K_{27}(2,5)$ on a personal computer; $|P_{27}(2,5)| = 92{,}228{,}348$ exact minimal-word count, $|C_{27}| = 3{,}995$ relations. Proves $B(2,5)$ and $B_0(2,5)$ have identical minimal-word relations up to length 27.

- [[kuznetsov-tarasov-shlepkin-2009]] — Generalizes Algorithm I to arbitrary finitely-presented periodic groups. Useful for the algorithm's standalone statement; positions it against coset enumeration as a complementary technique.

- [[kuznetsov-shlepkin-2010]] — Refines detection (associativity-test variant); cluster-scale computation of $K_{35}(2,5)$ (~104 hours, 125 nodes, $|P_{35}| \approx 5^{14}$, $|C_{35}| = 104{,}409$). Theorem 3: $B(2,5) \sim B_0(2,5)$ coincide on minimal-word relations up to length 29. **Theorem 4: produces 973 explicit candidate-divergence relations at lengths 30–35; failure of any one in $B(2,5)$ would resolve Problem 11.48 in the negative (B(2,5) infinite).**

- [[_synthesis-kuznetsov-b25-algorithmic-line]] — Synthesis of the three Kuznetsov papers. Frames the Mixer / B(2,5) verification opportunities: $|P_s(2,5)|$ baseline check, direct test of the 2 length-30 candidate relations, pre-registration of a Kuznetsov-Algorithm-I Mixer Agent for multi-witness cross-checking.

---

## Background / project context

- [[problems-people]] — Internal project document listing algorithms and implementers for the B(2,5) effort; early Mixer architectural constraints (API boundary, memory limits, serialization).

---

## Synthesis

- [[_synthesis-existing-papers]] — cross-paper synthesis of all Research/Group theory/ papers, covering what's settled vs. open across the Burnside group literature; refreshed on each `/research --reconnect group-theory` pass.

## Related MOCs

- [[_moc-knuth-bendix]] — The algorithm used to attack Burnside groups; navigate there for KB ordering choices, stagnation handling, and the Gröbner alternative.
- [[_moc-word-problem]] — The word problem as a topic; navigate there for decidability landscape, target-word methodology, and algorithmic techniques.
