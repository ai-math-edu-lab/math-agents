---
title: "On the difference of the Burnside groups B(2,5) and B₀(2,5)"
authors:
  - A. A. Kuznetsov
  - A. K. Shlepkin
year: 2010
venue: "Trudy Instituta Matematiki i Mekhaniki UrO RAN, vol. 16, no. 2, pp. 133–138"
url: ""
source_path: "Downloads/ketnesov_2010 (1).pdf"
language: ru
domain: group-theory
status: draft
methodology_type: empirical
relevance: 1
citation_count: null
citation_count_date: null
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
  - "[[Concepts/verification-methods-for-group-equality]]"
extends:
  - "[[kuznetsov-shlepkin-2009]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[havas-wall-wamsley-1974]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
cited_by:
  - "[[_synthesis-kuznetsov-b25-algorithmic-line]]"
  - "[[kuznetsov-2019]]"
  - "[[kuznetsov-kuznetsova-2025]]"
  - "[[kuznetsov-2011]]"
quality_notes: "Russian-language paper. Headline empirical contribution: 125-node MATLAB cluster computation of K_35(2,5) at ~104 hours; |C_35(2,5)| = 104,409 and |P_35(2,5)| ≈ 5^14. Theorems 3 and 4 are the operationally important results: coincidence of B(2,5) and B_0(2,5) on minimal words up to length 29 is proved, and a table of explicit candidate-divergence relations at lengths 30–35 is provided — failure of any one of these in B(2,5) implies B(2,5) is infinite. The new theoretical content in §1 (replacing the row-collision detection with associativity-test detection) is a real algorithmic refinement and worth understanding in its own right."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/word-problem
  - topic/cayley-table-closure
  - topic/finite-group-enumeration
  - topic/computer-algebra
  - paper
  - status/draft
project: b25
---

# On the difference of the Burnside groups B(2,5) and B₀(2,5)

> **Translation note**: vault language is English. Source is Russian; the Abstract below is translated; quotes are translated and tagged `[trans.]`. Original Russian is not preserved here — `language: ru` records the source language.

## Abstract

An algorithm for calculating elements and relations in Burnside groups is described. A comparative analysis of the groups B(2,5) and B₀(2,5) is carried out. It is shown that these groups coincide in the minimal-word format up to words of length 29. For lengths 30–35, relations are found in the group B₀(2,5) such that a violation of at least one of them in B(2,5) would mean the infiniteness of this group. [trans.]

## TL;DR

Extends [[kuznetsov-shlepkin-2009]] in three ways: (1) presents a refined version of the Cayley-table-closure algorithm that uses **associativity-test collisions** $A_s(v_i A_s(v_j v_k)) \neq A_s(A_s(v_i v_j) v_k)$ rather than direct row collisions to detect new relations, with separate finite/infinite limit theorems; (2) using a 125-node MATLAB cluster (~104 hours wall-clock), computes $K_{35}(2,5)$ with $|C_{35}(2,5)| = 104{,}409$ relations and $|P_{35}(2,5)| \approx 5^{14}$ minimal words; (3) confirms that $B(2,5)$ and $B_0(2,5)$ coincide on minimal-word relations up to length 29, and exhibits explicit candidate relations at lengths 30 (2 relations), 31 (10), 32 (47), 33 (70), 34 (259), 35 (585) in $B_0(2,5)$ — **failure of any one of these in $B(2,5)$ would prove $B(2,5)$ infinite**.

## Problem

Building on [[kuznetsov-shlepkin-2009]]: that paper showed $B(2,5)$ and $B_0(2,5)$ coincide on minimal-word relations up to length 27. **Where do the two groups first differ?** Kourovka Problem 11.48 ([[kourovka-11.48-kostrikin-1990]]) asks whether $B(2,5)$ is finite (equivalently, whether $B(2,5) \cong B_0(2,5)$). If a relation that holds in $B_0(2,5)$ can be exhibited and shown to fail in $B(2,5)$, the infiniteness is proved. This paper attempts to push the comparison from length 27 up as high as computational resources allow, and to produce explicit candidate-divergence relations as targets for refutation.

## Approach

**Algorithm refinement (§1).** A new variant of Algorithm I uses the group's **associativity** as the row-collision detector. The construction parallels [[kuznetsov-shlepkin-2009]] but replaces the table-row-collision detection step. For a candidate triple $(v_i, v_j, v_k) \in P_s^{(1)} \times P_s^{(1)} \times P_s^{(1)}$, check

$$A_s^{(0)}\bigl(v_i \cdot A_s^{(0)}(v_j v_k)\bigr) \stackrel{?}{=} A_s^{(0)}\bigl(A_s^{(0)}(v_i v_j) \cdot v_k\bigr).$$

A mismatch — call the two sides $v$ and $w$ with $v \prec w$ — yields a new relation $c_r = \{v = w\}$, which is added to $C_s$ exactly as in [[kuznetsov-shlepkin-2009]]. Iterate until associativity holds on all triples in $P_s^{(z)}$.

**Lemma 1 (§1.1):** A monoid in which every element has finite order is a group. (Sketch: $g^{n_g - 1}$ is the unique inverse of $g$.) This is the technical bridge from the algorithm's structural output (a finite monoid presentation) to a group structure.

**Two limit theorems (§§1.4–1.5):**

- **Theorem 1 (finite case):** If $s$ is the least natural number with $K_s(m,n) = K_{s+1}(m,n)$, define $K(m,n) = (P_s, A_s, C_s, *)$ where $a * b = A_s(ab)$. Then $K(m,n) \simeq B(m,n)$ and $|B(m,n)| = |P_s|$. The proof uses Lemma 1 (the operation $*$ is associative on $P_s$, so $K(m,n)$ is a monoid; every element has finite order, so it is a group; isomorphic to $B(m,n)$ by construction).
- **Theorem 2 (infinite case):** If $|P_s| < |P_{s+1}|$ for all $s$, define $\lim_{s \to \infty} K_s(m,n) = (P, A, C, *)$ with $P = \bigcup_s P_s$ stably and similarly for $A, C$. Then $\lim_s K_s(m,n) \simeq B(m,n)$ and in particular $B(m,n)$ is infinite.

Together these give a **finite/infinite dichotomy from $K_s$**: either $K_s$ stabilizes (finite) or $|P_s|$ grows strictly forever (infinite). The algorithm provides a witness in either case.

**Cluster computation (§3).** $K_{35}(2,5)$ was computed on a 125-node cluster at the Institute of Space and Information Technologies, Siberian Federal University (Krasnoyarsk). Each node: 3 GHz CPU, 4 GB RAM. Software: MATLAB 7.7.0 + Distributed Computing Server + Parallel Computing Toolbox. Total wall-clock: $\approx 104$ hours.

**Output (§3 numerical summary):**
- $|C_{35}(2,5)| = 104{,}409$ relations
- $|P_{35}(2,5)| \approx 5^{14}$ minimal words

**Comparison machinery (§2).** Same $\psi: B(2,5) \to B_0(2,5)$ homomorphism as [[kuznetsov-shlepkin-2009]] (using the [[havas-wall-wamsley-1974]] generator basis 1–34). For each length $s \le 35$, the maximal possible $\{1,2\}$-word relation list for $B_0(2,5)$ is computed via $\psi$, and compared against the relations $K_s(2,5)$ finds in $B(2,5)$. Where the lists disagree, the $B_0$-only relations are candidate divergence witnesses.

## Key result

**Theorem 3 (§2).** Let $v, w$ be two words in the generator alphabet $\{1, 2\}$ with $L(v) \le 29$ and $L(w) \le 29$. Then $v = w$ is a relation in $B_0(2,5)$ if and only if $v = w$ is a relation in $B(2,5)$. **Proof:** direct computation.

This extends [[kuznetsov-shlepkin-2009]]'s length-27 coincidence theorem to length 29.

**Theorem 4 (§2 — the operationally important result).** If at least one of the relations from the table below fails to hold in $B(2,5)$, then $B(2,5)$ is infinite.

The table (called Table 1 / **Some relations in the group $B_0(2,5)$** in §2) lists explicit candidate-divergence relations by length:

| Length | Number of candidate relations | Sample relation (first listed) |
|---|---|---|
| 30 | 2 | `122121121221121212211212212112 = 212121122112212121122112212121` |
| 31 | 10 | `1221122121211221122121212222111 = 2121122121121221121212211212212` |
| 32 | 47 | `12211222121111211222212222121112 = 21211112121221122112112121112111` |
| 33 | 70 | `122212221112212211221122122112211 = 221111221122212211221112211221222` |
| 34 | 259 | `1112121221122112112121112111222211 = 2121211221122212111121122221222212` |
| 35 | 585 | `11212122112211212121111222121121121 = 22211122221212211212212112212121122` |

**Total candidate-divergence relations across lengths 30–35:** $2 + 10 + 47 + 70 + 259 + 585 = 973$. (The paper reproduces only a few representatives per length, not all 973.)

**Proof of Theorem 4 (§2).** The relations are all derived as $\psi(v) = \psi(w)$ via the Havas-Wall-Wamsley commutator basis — they hold in $B_0(2,5)$ by construction. If even one fails in $B(2,5)$, then $B(2,5) \not\cong B_0(2,5)$, which by [[kuznetsov-shlepkin-2009]]'s opening observation (and the structural fact that $B_0(2,5)$ is the maximal finite quotient of $B(2,5)$) implies $B(2,5)$ is infinite. The paper's example computation: $\psi(122121121221121212211212212112) = \psi(212121122112212121122112212121) = $ a specific normal word in the commutator basis (a long product of base commutators $1, 2, 3, \ldots, 34$ to powers).

## Assumptions

- The $\psi$ homomorphism construction from [[kuznetsov-shlepkin-2009]] is correct and computable for words of length up to 35.
- Lemma 1's argument (finite-order monoid is a group) is valid in the constructive limit setting of Theorem 2.
- MATLAB 7.7.0 floating-point and integer arithmetic on the cluster does not introduce errors in symbolic relation derivation — implicit; the paper does not discuss verification.
- The cluster computation reaches the length-35 relations completely (not just partially up to time budget) — implicit from the reported $|C_{35}|$ and $|P_{35}|$ values being given as exact rather than as lower bounds.
- The list of 973 candidate divergence relations at lengths 30–35 is exhaustive within those lengths — the paper says "in the minimal word format up to length 29 the groups coincide; on lengths 30–35 [these] relations are found," implying these are all the divergent ones in that range.

## Limitations / scope

- The candidate divergence relations are **candidates only**. The paper does not show that any one of them fails in $B(2,5)$. Verifying or refuting one of them in $B(2,5)$ is the next step, and is delegated to other methods.
- Length 35 is the empirical ceiling for this cluster computation; nothing is said about whether the candidate set continues to grow at $|P_{s+1}|/|P_s| \approx 1.9$ beyond length 35 or whether the rate changes.
- No formal verification of the algorithm's MATLAB implementation. The 5^14 value for $|P_{35}|$ is stated as $\approx$ — not exact — which is mildly concerning for what should be an exact count.
- The associativity-test refinement (§1) generalizes the prior algorithm but the paper does not benchmark it against the row-collision version of [[kuznetsov-shlepkin-2009]]. It is plausibly faster (fewer candidates to test per step) but this is not quantified.
- Within-paper sanity checks against known finite groups (e.g. $B(2,3), B(3,3), B(2,4)$ as in [[kuznetsov-shlepkin-2009]]) are not repeated; the reader is referred back.

## Replication evidence

Internal continuation of [[kuznetsov-shlepkin-2009]]: extends that paper's length-27 result to length 29 (Theorem 3) and provides cluster-scale data at lengths up to 35.

No independent external replication of the length-30–35 candidate relations has been located in this vault. The candidate relations themselves are **directly verifiable**: any other tool that can decide word equality in $B(2,5)$ at the relevant length can check them. This is precisely what a Mixer KB attack would do.

## Why this paper matters

This paper does **two distinct things** that matter for the B(2,5) program:

**1. Operational: produces explicit refutation targets for Problem 11.48.** Each of the 973 candidate-divergence relations at lengths 30–35 is a **falsifier**: if any one is shown to fail in $B(2,5)$, the open finiteness question is resolved in the negative. This is a much sharper output than KB-completion-based attacks, which check finiteness by termination (a global property) rather than by checking a specific finite list of identities. For the Mixer / KBMAG / Rust-bidirectional pipelines, this paper produces **concrete length-30+ test words** that should be added to the verification suite.

**2. Architectural: clean dichotomy theorem from a Cayley-table algorithm.** Theorems 1 and 2 together give a clean finite/infinite split: either $|P_s|$ stabilizes (then $B(m,n)$ is finite and we know its presentation) or $|P_s|$ grows strictly (then $B(m,n)$ is infinite). This is **structurally simpler** than the KB termination criterion (KB termination implies finite; KB non-termination doesn't imply infinite). For B(2,5) specifically, the cluster run shows $|P_{27}| < |P_{28}| < \ldots < |P_{35}|$ — consistent with infiniteness, but the rate of growth is bounded by $|P_s| \le |B_0(2,5)| = 5^{34}$ as long as $B(2,5) \cong B_0(2,5)$, so it is **not yet a proof of infiniteness**. Pushing the cluster computation farther — into lengths where $|P_s| > 5^{34}$ would be required if $B(2,5)$ were not isomorphic to $B_0(2,5)$ — is one direction. Verifying or refuting the 973 candidate relations is the other.

The paper's combination — a clean infiniteness theorem + an explicit refutation set — makes it **the most operationally relevant Russian-language paper on B(2,5) in this vault**.

## Quotes

1. > "If at least one of the relations from the table does not hold in B(2,5), then the group B(2,5) is infinite." — Theorem 4 [trans.]
2. > "On lengths 30–35, relations are found in the group B₀(2,5) such that a violation of at least one of them in B(2,5) would mean the infiniteness of this group." — Abstract [trans.]

## Open questions surfaced

- Has any of the 973 candidate-divergence relations been verified or refuted in $B(2,5)$ since 2010? Either result resolves Problem 11.48. (Vault check: nothing in `Research/` or `Experiments/` references these specific relations as of this write.)
- At what length does $|P_s(2,5)|$ first exceed $|B_0(2,5)| = 5^{34}$? Reaching that length computationally would prove $B(2,5) \neq B_0(2,5)$, equivalently $B(2,5)$ is infinite. (Rough estimate: extrapolating the $\approx 1.9$ growth ratio from the 2009 tables, this requires $s \approx 45$–55.)
- Could the candidate relations at length 30 be tested directly with KBMAG starting from the B(2,5) presentation? If KBMAG produces a confluent system that rewrites both sides of, say, the first relation to **distinct** canonical forms, that's a refutation.
- Is the §1 associativity-test variant of the algorithm genuinely faster than the §1 row-collision variant from [[kuznetsov-shlepkin-2009]]? The change reduces the number of triples to test per step but introduces a 3-way product per check; the net effect on wall-clock is not benchmarked.
- Have the original 2010 cluster outputs (the specific list of 973 relations, the full $P_{35}$ word list) been preserved or are they only summarized in this paper? The relations table in §2 lists only one or two per length; recovering the full set may require contacting the authors.

## Mixer / B(2,5) project framing

This paper is **the highest-leverage external paper on B(2,5) in the vault for the Mixer attack** ([[b25-finiteness-11.48-kostrikin]]), for one reason: it gives **concrete, length-30 to length-35 test words** that the Mixer's rewriting system must handle correctly. Specifically:

**Verification asks for the Mixer's B(2,5) pipeline (recommended actions for Experimenter-B25):**

1. **Take the first length-30 relation** `122121121221121212211212212112 = 212121122112212121122112212121` and run both sides through whatever partial rewriting system the Mixer has accumulated for B(2,5). If both sides reduce to the same canonical form (or are provably equal modulo currently-known relations), the Mixer is consistent with $B(2,5) \cong B_0(2,5)$ at length 30. If they reduce to distinct canonical forms, **Problem 11.48 is resolved**: $B(2,5)$ is infinite.
2. **Repeat for the length-31 relations** (10 of them) and so on up to the available cluster output.
3. **Reproduce $|P_{27}(2,5)|$ and $|P_{35}(2,5)|$** as ground-truth counts: any reduction Agent claiming to enumerate B(2,5) elements up to length 35 must produce $\approx 5^{14}$ distinct canonical forms. (Note: this paper says $\approx$ not exact, suggesting some implementation precision concern in the original; treat as a benchmark with error bars rather than a hard target.)
4. **Add the 973 relations to the bidirectional search test set.** The `experiments/burnside_bidirectional/` pipeline (which proves specific word identities in restricted $B(2,5)$) is the natural home for these — each relation is a specific identity claim, and any failure becomes a Mixer-level argument for infiniteness.

This paper does not, by itself, resolve Problem 11.48 — but it converts the open question from "does KB ever terminate?" (a hard-to-detect property) to "does any of these 973 specific identities fail?" (a finite, verifiable check). **That conversion is exactly the kind of empirical handle the Mixer architecture needs.**

For Lead: this paper should feed into the next pre-registered B(2,5) experiment. Suggest Experimenter-B25 attempts at least the 2 length-30 relations through the Rust bidirectional and KBMAG pipelines, with results recorded as `experiments/burnside_bidirectional/` data files cross-linked back here.

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]] (length-27 coincidence theorem → length-29 coincidence; row-collision-based algorithm → associativity-test-based algorithm)
- Contradicts: (none)
- Replicates: continues [[kuznetsov-shlepkin-2009]]'s implementation work at cluster scale
- Concepts introduced/used: [[Concepts/cayley-table-closure-algorithm]] (the refined associativity-test variant), [[Concepts/verification-methods-for-group-equality]] (the ψ-homomorphism comparison)
- Cites (in vault): [[kuznetsov-shlepkin-2009]], [[havas-wall-wamsley-1974]] (the commutator basis 1–34 used to define ψ), [[kourovka-11.48-kostrikin-1990]] (the problem this attacks)
- Cited by (in vault): [[_synthesis-kuznetsov-b25-algorithmic-line]]
- Open problem this engages: [[b25-finiteness-11.48-kostrikin]] (Mixer attack rationale, separate framing)
- MOC: [[_moc-burnside]]
- Parent overview: [[group-theory-overview]]
- Related Mixer artifact: [[algo-mixing-burnside-slides]] (the B(4,3) breakthrough that gives the proof-of-concept; B(2,5) is the next harder target where this paper's candidate relations become relevant)
