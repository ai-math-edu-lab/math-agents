---
title: "Synthesis — The Kuznetsov computational program on B₀(2,5): twenty years of structural data"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/cayley-table-closure
  - topic/growth-functions
  - topic/cayley-graphs
  - topic/finite-group-enumeration
  - topic/rewriting-systems
  - synthesis
  - status/draft
papers_synthesized:
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-tarasov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
  - "[[kuznetsov-2019]]"
  - "[[kuznetsov-2020]]"
  - "[[kuznetsov-kuznetsova-2025]]"
  - "[[kuznetsov-kuznetsova-2021]]"
  - "[[kuznetsov-safonov-2018]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-kuznetsova-2017]]"
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-karchevsky-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
  - "[[kuznetsov-2011]]"
  - "[[kuznetsov-filippov-2010-sjim]]"
  - "[[kuznetsov-filippov-2010-vmj]]"
  - "[[kuznetsov-safonov-2014]]"
  - "[[kuznetsov-safonov-2015]]"
  - "[[kuznetsov-2015-cayley-exp3]]"
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
  - "[[Concepts/growth-functions-burnside]]"
  - "[[Concepts/cayley-graphs-of-burnside-groups]]"
  - "[[Concepts/verification-methods-for-group-equality]]"
date_range: 2009-01 to 2025-12
project: b25
---

# Synthesis — The Kuznetsov computational program on B₀(2,5): twenty years of structural data

> **Synthesis note.** This covers 20 publications (2009–2025) by Alexander A. Kuznetsov and collaborators at the Reshetnev Siberian State University, forming a cohesive computational program on the largest two-generator Burnside group of exponent five $B_0(2,5)$. This synthesis supersedes the earlier 3-paper synthesis [[_synthesis-kuznetsov-b25-algorithmic-line]], which is retained as a focused deep-dive on the Cayley-table-closure algorithm specifically.

## The question

What does Kuznetsov's twenty-year computational program on $B_0(2,5)$ reveal about the structure of the group, and which of its results most directly enable or constrain the Mixer B(2,5) attack on Problem 11.48?

## Sources reviewed

**Cayley-table-closure line (2009–2010):**
1. [[kuznetsov-shlepkin-2009]] — Algorithm I on $B_0(2,5)$; $|P_{27}(2,5)| = 92{,}228{,}348$; $B(2,5) \cong B_0(2,5)$ on minimal words up to length 27.
2. [[kuznetsov-tarasov-shlepkin-2009]] — Algorithm I generalized to arbitrary finitely-presented periodic groups.
3. [[kuznetsov-shlepkin-2010]] — Refined detection (associativity-test); cluster computation to $s = 35$; $|P_{35}| \approx 5^{14}$; $|C_{35}| = 104{,}409$; 973 candidate-divergence relations at lengths 30–35.

**Computational foundations (2013):**
4. [[kuznetsov-kuznetsova-2013]] — Fast Hall polynomial multiplication for exponent-5 groups. The computational core for all subsequent work.
5. [[kuznetsova-kuznetsov-safonov-2013]] — Parallel variant of the growth function BFS algorithm.

**Cross-exponent Hall polynomial validation (2014–2015):**
6. [[kuznetsov-safonov-2014]] — Hall polynomials for exponent-7 two-generator groups ($k \le 4$).
7. [[kuznetsov-safonov-2015]] — Hall polynomials for exponent-3 Burnside groups (conference note).
8. [[kuznetsov-2015-cayley-exp3]] — Hall polynomials + Cayley graph diameters for exponent-3 groups ($k \le 4$); graphs beat hypercubes.

**Growth functions and Cayley graph geometry (2016–2019):**
9. [[kuznetsov-2016]] — Growth function algorithm for $B_k$, $k = 15, 16, 17$.
10. [[kuznetsov-karchevsky-2016]] — Conference companion to the above.
11. [[kuznetsov-kuznetsova-2017]] — Cayley graph of centralizer of permutation automorphism: $|C| = 5^{17}$, diameter $D = 33$, $\bar{D} \approx 26.1$.
12. [[kuznetsov-kuznetsova-2018]] — Resource-efficient growth algorithm; **Cayley graph diameter of $B_0(2,5)$: ~105 (2-gen), ~69 (4-gen)**.
13. [[kuznetsov-safonov-2018]] — Cayley graph geometry of centralizer of inversion automorphism ($|C| = 5^{16}$).
14. [[kuznetsov-2019]] — Diameter hypothesis: $D_{A_4}(eN_k) = D_{A_4}(B_k)$; verified for $k \le 19$.

**Automorphism centralizers (2010):**
15. [[kuznetsov-filippov-2010-sjim]] — Centralizer of inversion automorphism $\varphi: a_i \mapsto a_i^{-1}$: generators, order ($5^{16}$), solvability, nilpotency.
16. [[kuznetsov-filippov-2010-vmj]] — Companion publication; adds explicit central series construction.

**Subgroup structure (2011, 2021):**
17. [[kuznetsov-2011]] — Subgroup $G = \langle xy, yx \rangle \le B_0(2,5)$: $|G| = 5^{14}$, class 6, derived length 3.
18. [[kuznetsov-kuznetsova-2021]] — Minimum word length for noncyclic abelian subgroup: 16; abelian subgroup of order 25 found.

**Rewriting systems and center (2020, 2025):**
19. [[kuznetsov-2020]] — Algorithm for confluent irreducible rewriting systems of finite groups; applied to exponent-5 quotients.
20. [[kuznetsov-kuznetsova-2025]] — Supercomputer computation of center of $B_0(2,5)$: central elements as minimal-length words.

## Convergence

**On computational infrastructure:**
All 20 papers share the power commutator representation of $B_0(2,5)$ from [[havas-wall-wamsley-1974]] — 34 generators $a_1, \ldots, a_{34}$ with $\alpha_i \in \mathbb{Z}_5$. Hall polynomial multiplication (introduced for exponent-5 in [[kuznetsov-kuznetsova-2013]], extended to exponents 3 and 7 in [[kuznetsov-safonov-2015]] and [[kuznetsov-safonov-2014]]) is the universal group oracle across all papers. This is not incidental: the Hall polynomial representation is the only structure that makes large-scale $B_0(2,5)$ computation tractable.

**On the Cayley graph diameter of $B_0(2,5)$:**
Papers [[kuznetsov-kuznetsova-2018]], [[kuznetsov-2019]], [[kuznetsov-kuznetsova-2017]], and [[kuznetsov-safonov-2018]] collectively build a consistent picture of Cayley graph geometry. The central empirical result — diameter ~105 under 2-generators, ~69 under the symmetric 4-generator set — is the best available estimate for $B_0(2,5)$'s word geometry.

**On the B(2,5) ≅ B₀(2,5) question:**
[[kuznetsov-shlepkin-2009]] and [[kuznetsov-shlepkin-2010]] together establish that $B(2,5)$ and $B_0(2,5)$ have identical minimal-word relations up to length 29 (proven, not estimated). Neither result resolves finiteness; they constrain where a difference could appear (lengths 30+).

**On methodology generality:**
Papers [[kuznetsov-safonov-2014]], [[kuznetsov-safonov-2015]], [[kuznetsov-2015-cayley-exp3]] establish that the Hall polynomial + Cayley graph methodology works across exponents 3, 5, and 7. This cross-exponent consistency validates the exponent-5 implementation.

## Disagreement

**No mathematical disagreements found.** The papers are internally consistent and do not contradict each other.

**Structural observations (not contradictions):**
- [[kuznetsov-filippov-2010-sjim]] and [[kuznetsov-filippov-2010-vmj]]: same result (centralizer structure), different venues and different co-author name spellings (Filippov vs. Philippov — same person). Likely a full-paper + companion-abstract split.
- [[kuznetsov-2016]] and [[kuznetsov-karchevsky-2016]]: same growth-function results (k=15,16,17) in journal and supplement respectively.
- [[kuznetsov-kuznetsova-2017]] ($|C| = 5^{17}$) vs. [[kuznetsov-safonov-2018]] ($|C| = 5^{16}$): different automorphisms, not the same computation. 2017 paper studies a permutation-type automorphism; 2018 paper studies the inversion automorphism $a_i \mapsto a_i^{-1}$.

**Unresolved approximation:** [[kuznetsov-shlepkin-2010]] reports $|P_{35}(2,5)| \approx 5^{14}$, not exact, despite the same run producing exact values for $|C_{35}| = 104{,}409$. The approximation has not been explained or independently verified (see [[_synthesis-kuznetsov-b25-algorithmic-line]] for detailed discussion).

## What's settled

1. **$|B_0(2,5)| = 5^{34}$, nilpotency class 12** (from [[havas-wall-wamsley-1974]]; all papers assume this).
2. **Hall polynomial multiplication** is a practical oracle for $B_0(2,5)$ computation (verified across 3 exponents).
3. **$B(2,5)$ and $B_0(2,5)$ agree on minimal-word relations up to length 29.** (proven, [[kuznetsov-shlepkin-2010]])
4. **973 candidate-divergence relations exist at lengths 30–35** in $B_0(2,5)$; failure of any one in $B(2,5)$ proves $B(2,5)$ infinite. ([[kuznetsov-shlepkin-2010]] Theorem 4)
5. **Cayley graph diameter of $B_0(2,5)$**: $\approx 105$ (2-gen), $\approx 69$ (4-gen). Estimated from $B_{18}, B_{19}$ computations. ([[kuznetsov-kuznetsova-2018]])
6. **Center of $B_0(2,5)$ is computed** and expressed as minimal-length words. ([[kuznetsov-kuznetsova-2025]])
7. **Subgroup $\langle xy, yx \rangle \le B_0(2,5)$**: order $5^{14}$, class 6, derived length 3. ([[kuznetsov-2011]])
8. **Minimum noncyclic abelian subgroup length**: 16; abelian subgroup of order 25 exists. ([[kuznetsov-kuznetsova-2021]])
9. **Centralizer of inversion automorphism** $\varphi: a_i \mapsto a_i^{-1}$ has order $5^{16}$. ([[kuznetsov-filippov-2010-sjim]])

## What's contested

- **The $|P_{35}| \approx 5^{14}$ approximation.** See [[_synthesis-kuznetsov-b25-algorithmic-line]] for the detailed analysis. Unresolved; no external replication.
- **Exact diameter of $B_0(2,5)$.** The ~105 and ~69 estimates are extrapolated from $k = 18, 19$; the true diameter at $k = 34$ is unknown.
- **Completeness of the center computation.** [[kuznetsov-kuznetsova-2025]] reports the center as computed but does not quote its size in the abstract. Whether the full list of central elements is publicly available is unknown.

## What's open

1. **The 973 candidate-divergence relations** (lengths 30–35). Has any one of them been verified to fail in $B(2,5)$? If yes, Problem 11.48 is resolved. Vault has no evidence of follow-up since 2010.
2. **Growth functions for $k > 19$.** The 2018 resource-efficient algorithm could extend to $k > 19$ on modern hardware. At $k = 34$ (full $B_0(2,5)$), the exact growth function would confirm the ~105 diameter estimate.
3. **Confluent rewriting system sizes.** [[kuznetsov-2020]] computes rewriting systems for finite $B_k$ groups but does not quote rule counts. These rule counts would bound what the Mixer's KB system must produce for $B(2,5)$.
4. **The B(2,5) center question.** Do the central elements of $B_0(2,5)$ (from [[kuznetsov-kuznetsova-2025]]) all reduce to identity in $B(2,5)$? If $B(2,5) \cong B_0(2,5)$, they must. Testing this is a concrete experiment.
5. **The 2019 diameter hypothesis.** Does $D_{A_4}(eN_k) = D_{A_4}(B_k)$ hold for $k > 19$? Unproved for all 34 layers.

## Methodology notes

**All papers are abstract-only in this vault**: 20 papers, zero full-text access via mathnet.ru (paywall + Russian journals not indexed in English). All key results are from abstracts + the 3 papers where PDFs were available from earlier work. Quality of individual note summaries is bounded by this.

**Publication duplication pattern**: Kuznetsov consistently publishes results in both a full journal (Prikl. Diskr. Mat. or Trudy IMM) and a conference supplement (Prikl. Diskr. Mat. Suppl.) in the same year. This means the 20 papers represent roughly 12–14 distinct scientific contributions, not 20.

**All in Russian**: these papers are not discoverable via standard English-language academic searches. The vault now holds the only English-language synthesis of this 20-year program. Implications: (1) no external replication via the literature; (2) potential for missed advances if Kuznetsov published in Russian venues not indexed.

**Cross-exponent validation**: Hall polynomial multiplication is verified for exponents 3, 5, 7. Since the software is the same for all three, a bug in the polynomial implementation would likely manifest across exponents — making the cross-exponent agreement (independently checkable against known finite group orders) the strongest validation available.

## Recommendation

For Lead and the Mixer B(2,5) workstream:

1. **Immediate verification target**: take the 2 length-30 candidate-divergence relations from [[kuznetsov-shlepkin-2010]] (quoted verbatim in that note's Key result table) and run them through the Mixer's current KB and bidirectional pipelines. If either pair reduces to distinct normal forms, Problem 11.48 is resolved. This is the highest-leverage experiment derivable from this entire body of work.

2. **Center as a cross-ordering test**: extract the central elements of $B_0(2,5)$ from [[kuznetsov-kuznetsova-2025]] (requires contacting Kuznetsov or reading the full paper). Central elements must reduce to identity under ANY ordering's KB system if $B(2,5) \cong B_0(2,5)$ — they are the cheapest consistency checks for the Mixer.

3. **Growth function benchmarks for Mixer calibration**: use [[kuznetsov-kuznetsova-2018]]'s $B_{18}$ and $B_{19}$ growth function results as calibration targets. Any B(2,5) pipeline that can enumerate $B_{18}$ (order $5^{18}$) should reproduce these values. If it doesn't, there's a bug.

4. **Rewriting system rule count from [[kuznetsov-2020]]**: contact the authors or read the full paper to obtain rule counts for confluent irreducible rewriting systems of $B_k$ ($k \le 34$). These counts would tell the Mixer team how large a confluent KB system for $B_0(2,5)$ must be, bounding the exploration space.

5. **Subgroup benchmark**: the subgroup $\langle xy, yx \rangle$ of order $5^{14}$ and nilpotency class 6 ([[kuznetsov-2011]]) should appear in the Mixer's B(2,5) rule system at the correct layer. Add this as a structural sanity check to the B(2,5) validation suite.

## Related vault material

- Papers: [[kuznetsov-shlepkin-2009]], [[kuznetsov-tarasov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]], [[kuznetsov-kuznetsova-2013]], [[kuznetsova-kuznetsov-safonov-2013]], [[kuznetsov-safonov-2014]], [[kuznetsov-safonov-2015]], [[kuznetsov-2015-cayley-exp3]], [[kuznetsov-2016]], [[kuznetsov-karchevsky-2016]], [[kuznetsov-kuznetsova-2017]], [[kuznetsov-kuznetsova-2018]], [[kuznetsov-safonov-2018]], [[kuznetsov-2019]], [[kuznetsov-2020]], [[kuznetsov-filippov-2010-sjim]], [[kuznetsov-filippov-2010-vmj]], [[kuznetsov-2011]], [[kuznetsov-kuznetsova-2021]], [[kuznetsov-kuznetsova-2025]]
- Concepts: [[Concepts/cayley-table-closure-algorithm]], [[Concepts/growth-functions-burnside]], [[Concepts/cayley-graphs-of-burnside-groups]], [[Concepts/verification-methods-for-group-equality]]
- Prior syntheses: [[_synthesis-kuznetsov-b25-algorithmic-line]] (focused deep-dive on the Cayley-table-closure algorithm; 3-paper treatment; retained as companion)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]], [[kourovka-11.48-kostrikin-1990]]
- Foundational paper: [[havas-wall-wamsley-1974]]
