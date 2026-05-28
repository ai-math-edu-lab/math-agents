---
title: "Comparative analysis of the Burnside groups B(2,5) and B₀(2,5)"
authors:
  - A. A. Kuznetsov
  - A. K. Shlepkin
year: 2009
venue: "Trudy Instituta Matematiki i Mekhaniki UrO RAN, vol. 15, no. 2, pp. 125–132"
url: ""
source_path: "Downloads/ketnesov_2009 (1).pdf"
language: ru
domain: group-theory
methodology_type: empirical
relevance: 1
citation_count: null
citation_count_date: null
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
  - "[[Concepts/verification-methods-for-group-equality]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
cited_by:
  - "[[kuznetsov-shlepkin-2010]]"
  - "[[_synthesis-kuznetsov-b25-algorithmic-line]]"
  - "[[kuznetsov-2019]]"
  - "[[kuznetsov-2020]]"
  - "[[kuznetsov-kuznetsova-2025]]"
  - "[[kuznetsov-2011]]"
  - "[[kuznetsov-filippov-2010-sjim]]"
  - "[[kuznetsov-filippov-2010-vmj]]"
quality_notes: "Russian-language paper from the Krasnoyarsk school (Krasnoyarsk State Agrarian University). The algorithm described here is a custom computational scheme distinct from KB completion and from coset enumeration, with a clean finiteness criterion (K_s = K_{s+1}). The {0, 1, 2, ... 27}-table of |C_27(2,5)| and |P_27(2,5)| is the verifiable contribution; citation count not located as of write time."
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

# Comparative analysis of the Burnside groups B(2,5) and B₀(2,5)

> **Translation note**: vault language is English. Source is Russian; the Abstract below is translated; quotes are translated and tagged `[trans.]`. Original Russian is not preserved here — `language: ru` records the source language; the source PDF is the canonical reference.

## Abstract

An algorithm for computing elements and relations in Burnside groups is described. Then a comparative analysis of the groups B(2,5) and B₀(2,5) is carried out. [trans.]

## TL;DR

Introduces a computer-algebra algorithm — distinct from KB completion and coset enumeration — that computes the elements and relations of a Burnside group $B(m,n)$ by iteratively growing the minimal-word set $P_s$ and updating a Cayley table $T_s$ whose row collisions force new relations. Applied to $B(2,5)$, the authors compute $K_{27}(2,5)$, tabulate $|C_{27}(2,5)| = 3995$ and $|P_{27}(2,5)| = 92\,228\,348$, and prove via a homomorphism $\psi: B(2,5) \to B_0(2,5)$ that the minimal-word structures of $B(2,5)$ and the restricted $B_0(2,5)$ coincide up to length 27. This sets up the divergence search continued in [[kuznetsov-shlepkin-2010]].

## Problem

The 1902 Burnside problem asks: is every $m$-generated group with the identity relation $x^n = 1$ finite? In general, no (Adyan 1975). For $B(2,5)$ specifically — the two-generator group of exponent 5 — finiteness is **open** (Kourovka Problem 11.48, see [[kourovka-11.48-kostrikin-1990]]). Kostrikin (1955) and Havas-Wall-Wamsley (1974, see [[havas-wall-wamsley-1974]]) settled the **restricted** version: the largest finite quotient $B_0(2,5)$ has order $5^{34}$. If $B(2,5)$ is finite, then $B(2,5) \cong B_0(2,5)$. This paper builds machinery to detect computationally whether the two groups differ.

## Approach

**Custom algorithm (Algorithm I).** For a free Burnside group $B(m,n) = \langle x_1, \ldots, x_m \mid g^n = e\rangle$, define a total order $<$ on words by length-then-lex, where $x_1 < x_2 < \cdots < x_m$ (§1.1). A word is **minimal** if it is the smallest representative of its group element. The algorithm computes a sequence of objects

$$K_s(m,n) = (P_s, A_s, T_s, C_s), \quad s = 1, 2, \ldots$$

where $P_s$ is the ordered set of minimal words of length $\le s$, $A_s$ is a reduction algorithm, $T_s$ is the Cayley multiplication table on $P_s$, and $C_s$ is the list of relations discovered so far.

**Per-step construction** (§1.3): given $K_{s-1}$, extend $P_{s-1}$ by prepending each generator $x_i$ to each length-$(s-1)$ word, sort, apply $A_{s-1}$ to filter $A_{s-1}$-invariant words, yielding $P_s^{(1)}$. Build $T_s^{(0)} = \|v_i v_j\|$, apply $A^{(0)}_s$ to every cell. **Row collision** $A^{(0)}_s(v_{i_0} v_j) = A^{(0)}_s(v_{i_0} v_k)$ with $v_j < v_k$ implies the new relation $c_r = \{v_j = v_k\}$, which is added to $C_s$ and folds into the algorithm as $A^{(1)}_s = A^{(0)}_s * A_{c_r}$. Iterate until the table is invariant: $K_s = (P_s, A_s, T_s, C_s)$.

**Finiteness criterion (Theorem 1):** if $s$ is least with $K_s(m,n) = K_{s+1}(m,n)$, then $|B(m,n)| \le |P_s(m,n)|$. The authors verify $|B(2,3)| = |P_6(2,3)| = 3^3$, $|B(3,3)| = |P_{13}(3,3)| = 3^7$, $|B(2,4)| = |P_{20}(2,4)| = 2^{12}$ — known finite Burnside groups all hit the criterion with equality (§1.4).

**Comparison machinery (§2).** Using the consistent commutator presentation of $B_0(2,5)$ from [[havas-wall-wamsley-1974]] (generators $1, 2, 3, \ldots, 34$ with $1, 2$ the free generators and $3, \ldots, 34$ recursively defined as nested commutators), define the homomorphism $\psi: B(2,5) \to B_0(2,5)$ by $\psi(g_v) \mapsto k(h_v)$ where $k(h_v)$ is the **normal word** $1^{\alpha_1} \cdot 2^{\alpha_2} \cdots 34^{\alpha_{34}}$ representing $h_v \in B_0(2,5)$. Compute, in $B_0(2,5)$, the maximal possible list of $\{1,2\}$-word relations of each length; verify by computer that this matches the relations Algorithm I finds for $B(2,5)$ up to length 27.

## Key result

**Theorem 2 (§2):** Let $v, w$ be two words in the generator alphabet $\{1, 2\}$ with $L(v) \le 27$ and $L(w) \le 27$. Then $v = w$ is a relation in $B_0(2,5)$ if and only if $v = w$ is a relation in $B(2,5)$.

**Computational data (§3, Tables 1 and 2):**

Number of relations in $C_{27}(2,5)$, by length of the relation's longer side:

| Length | Count | Length | Count | Length | Count | Length | Count |
|---|---|---|---|---|---|---|---|
| 0–7 | 0 | 8 | 2 | 14 | 8 | 21 | 115 |
| | | 9 | 0 | 15 | 4 | 22 | 136 |
| | | 10 | 2 | 16 | 10 | 23 | 224 |
| | | 11 | 4 | 17 | 22 | 24 | 372 |
| | | 12 | 7 | 18 | 29 | 25 | 569 |
| | | 13 | 5 | 19 | 67 | 26 | 973 |
| | | | | 20 | 93 | 27 | 1353 |

Total $|C_{27}(2,5)| = 3995$.

Number of minimal words of each length in $P_{27}(2,5)$:

| Length | Count | Length | Count |
|---|---|---|---|
| 0 | 1 | 14 | 10,303 |
| 1 | 2 | 15 | 19,604 |
| 2 | 4 | 16 | 37,290 |
| 3 | 8 | 17 | 70,914 |
| 4 | 16 | 18 | 134,856 |
| 5 | 30 | 19 | 256,394 |
| 6 | 58 | 20 | 487,422 |
| 7 | 112 | 21 | 926,592 |
| 8 | 214 | 22 | 1,761,409 |
| 9 | 410 | 23 | 3,348,267 |
| 10 | 784 | 24 | 6,364,536 |
| 11 | 1,495 | 25 | 12,097,646 |
| 12 | 2,847 | 26 | 22,994,736 |
| 13 | 5,417 | 27 | 43,706,981 |

Total $|P_{27}(2,5)| = 92,\!228,\!348$.

## Assumptions

- The free Burnside group $B(m,n)$ is well-defined and the exponent relation $g^n = e$ holds for all $g$.
- Algorithm I's correctness (Theorem 1) is established by the §1.4 argument: every $g \in B(m,n)$ has a length-$\le s$ minimal representative once $K_s$ stabilizes.
- The consistent commutator basis $\{1, 2, \ldots, 34\}$ of $B_0(2,5)$ from [[havas-wall-wamsley-1974]] is correct.
- The homomorphism $\psi$ is well-defined and computable on every $\{1,2\}$-word; in particular, all relations of $B(2,5)$ are preserved in $B_0(2,5)$ (the converse is what's being tested).
- Computational implementation correctness — implicit; this is a computer-algebra paper, no formal verification of the implementation is offered.

## Limitations / scope

- Length 27 only — coincidence of $B(2,5)$ and $B_0(2,5)$ on minimal-word structure beyond length 27 is **not** addressed in this paper (extended to length 29 in [[kuznetsov-shlepkin-2010]]).
- The criterion $K_s = K_{s+1}$ would detect finiteness if it ever triggers; the paper does not report it triggering for $B(2,5)$ — consistent with the open finiteness question, but provides no upper bound on |B(2,5)| beyond the known $|B_0(2,5)| = 5^{34}$.
- Algorithm I is implemented and run on a personal computer; no parallelization is discussed in this paper. The much larger run in [[kuznetsov-shlepkin-2010]] uses a 125-node cluster.
- All claims are within-paper computational results; no external replication is documented in the paper itself.

## Replication evidence

**Internal validation:** the algorithm reproduces the known orders $|B(2,3)| = 3^3$, $|B(3,3)| = 3^7$, $|B(2,4)| = 2^{12}$ — agreeing with the consensus values cited in [[havas-newman-1980]] and Vaughan-Lee 1993. This is meaningful within-paper sanity-checking.

**External replication not located in this vault.** The follow-up [[kuznetsov-shlepkin-2010]] (same authors, one year later) re-uses and extends the algorithm; that is continuation, not independent replication.

## Why this paper matters

This paper introduces a **third algorithmic family** for B(2,5) computation, complementing the Lie-algebra/p-quotient approach of [[havas-wall-wamsley-1974]] and the KB-completion approach used by the Mixer ([[algo-mixing-burnside-slides]]). The $K_s(m,n)$ object is **a different shape of partial knowledge**: KB produces a confluent rewriting system, coset enumeration produces a permutation representation, and Kuznetsov's algorithm produces an explicit minimal-word set $P_s$ plus its Cayley table $T_s$ truncated by length.

Two reasons this matters for the Mixer / B(2,5) program:

1. **Direct attack on Problem 11.48.** Algorithm I has a built-in finiteness criterion ($K_s = K_{s+1}$); if it ever triggers on $B(2,5)$, $B(2,5)$ is finite. If $|P_s|$ grows strictly forever, $B(2,5)$ is infinite (Theorem 2 of [[kuznetsov-shlepkin-2010]]). This is structurally analogous to "KB terminates → finite" but uses a different witness object.
2. **A verifiable length-27 baseline.** The explicit table $|P_s(2,5)|$ for $s = 1, \ldots, 27$ provides hard numerical targets. Any reduction pipeline that claims to enumerate $B(2,5)$ minimal words must reproduce these counts. The growth rate $|P_{s+1}| / |P_s| \approx 1.9$ at $s = 27$ is also a useful empirical input.

The contribution is concrete and verifiable. The limitation is that the algorithm — as run in 2009 — only reaches length 27 (the 2010 follow-up extends to 35 on a cluster). For comparison, the Mixer's B(4,3) breakthrough produces a **confluent** system in 2,333 rules; Kuznetsov's algorithm at $s = 27$ has produced 3,995 relations but is not confluent and the truncation provides no finiteness guarantee.

## Quotes

1. > "If the group B(2,5) is finite, then B₀(2,5) ≅ B(2,5)." — Introduction [trans.]
2. > "Theorem 2. Let v, w be two words in the generator alphabet {1, 2}, L(v) ≤ 27 and L(w) ≤ 27. Then v = w is a relation in B₀(2,5) if and only if v = w is a relation in B(2,5)." — Section 2 [trans.]

## Open questions surfaced

- What is the smallest length $L$ at which $B(2,5)$ and $B_0(2,5)$ first diverge in minimal-word structure (if they do)? This paper says $L > 27$; [[kuznetsov-shlepkin-2010]] reports $L \ge 30$ with candidate witnesses but no proof.
- Can Algorithm I be combined with KB-completion (the Mixer's approach) to attack $B(2,5)$? The two produce structurally different witnesses; a hybrid might detect divergence faster than either alone.
- What is the practical asymptotic complexity of building $K_s(2,5)$? The 2009 personal-computer run reaches $s = 27$; the 2010 cluster run reaches $s = 35$. Length per CPU-month?
- Does $|P_s(2,5)|$ have a closed-form growth rate at small $s$, or only asymptotically?

## Mixer / B(2,5) project framing

This paper is **highly relevant to the Mixer's B(2,5) attack** ([[b25-finiteness-11.48-kostrikin]]). Three connections:

**1. Alternative witness.** The Mixer's KB approach asks: does a confluent rewriting system exist? Kuznetsov's algorithm asks: does $K_s = K_{s+1}$ ever happen? Both detect finiteness. If KB stagnates indefinitely (as it currently does on B(2,5)) but Kuznetsov's algorithm is provably making progress (extending $P_s$ each step), the two are complementary debugging signals. A Mixer Agent running Kuznetsov's algorithm in parallel with KB Agents could serve as an **oracle-style sanity check** — e.g. "at length 30, Kuznetsov reports $|P_{30}(2,5)| = N$; does my KB-derived rewriting system reduce all length-30 words to exactly $N$ canonical forms?"

**2. Length-truncated comparison baseline.** The 2009 table gives exact $|C_s|$ and $|P_s|$ values for $s \le 27$ (extended to $s \le 35$ in the 2010 paper). Any Mixer experiment that produces a partial rewriting system on $B(2,5)$ can be validated against this baseline: the number of distinct length-$\le 27$ reduced forms should equal $|P_{27}(2,5)| = 92{,}228{,}348$. **This is a verifiable empirical check the current B(2,5) experiments are not using.**

**3. Convergence/divergence signal.** If Mixer's KB ever produces a rule that contradicts Kuznetsov's tables (e.g. forces two length-$\le 27$ minimal words to coincide that this paper says are distinct as elements of $B_0(2,5)$), that contradiction proves $B(2,5) \neq B_0(2,5)$, i.e. **resolves Problem 11.48 in the negative**. The 2010 paper's Theorem 4 is the explicit form of this argument at lengths 30–35.

The Mixer's current B(2,5) attack — KB-only — is missing this independent witness stream. Adding a Kuznetsov-style enumeration Agent is a natural Mixer extension and a candidate Experimenter pre-registration.

## Related material in vault

- Extends: (none — first paper in this vault from this author group)
- Contradicts: (none)
- Replicates: confirms known $|B(2,3)|, |B(3,3)|, |B(2,4)|$ (within-paper sanity-check, not external replication of HWW1974)
- Concepts introduced/used: [[Concepts/cayley-table-closure-algorithm]] (introduced here in its B(2,5)-specific form), [[Concepts/verification-methods-for-group-equality]] (the ψ-homomorphism is a verification technique)
- Cites (in vault): [[havas-wall-wamsley-1974]], [[kourovka-11.48-kostrikin-1990]]
- Cited by (in vault): [[kuznetsov-shlepkin-2010]], [[_synthesis-kuznetsov-b25-algorithmic-line]]
- Open problem this engages: [[b25-finiteness-11.48-kostrikin]] (Mixer attack rationale, separate framing)
- MOC: [[_moc-burnside]]
- Parent overview: [[group-theory-overview]]
