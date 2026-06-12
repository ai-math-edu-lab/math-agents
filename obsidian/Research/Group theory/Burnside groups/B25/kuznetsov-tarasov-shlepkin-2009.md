---
title: "Generalized algorithm for modeling periodic groups"
authors:
  - A. A. Kuznetsov
  - S. A. Tarasov
  - A. K. Shlepkin
year: 2009
venue: "Vestnik Novosibirskogo Gosudarstvennogo Universiteta (NSU Bulletin). Series: Mathematics, Mechanics, Informatics, vol. 9 iss. 2, pp. 47–54"
url: ""
source_path: "Downloads/ketnesov_2009_general_alg (1).pdf"
language: ru
domain: group-theory
status: draft
methodology_type: theoretical
relevance: 2
citation_count: null
citation_count_date: null
key_concepts:
  - "[[Concepts/cayley-table-closure-algorithm]]"
extends:
  - "[[kuznetsov-shlepkin-2009]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-shlepkin-2009]]"
cited_by:
  - "[[_synthesis-kuznetsov-b25-algorithmic-line]]"
  - "[[kuznetsov-2020]]"
quality_notes: "Russian-language paper. The generalization is genuine but not surprising — it follows the natural template 'take the n-aperiodicity restriction out of A_1, allow C_1 to be the input relations.' The worked example is the symmetric group S_3, which is too small to stress the algorithm. Useful as the standalone statement of Algorithm I for arbitrary finitely-presented periodic groups, independent of the Burnside-specific machinery in the parallel 2009 paper."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/cayley-table-closure
  - topic/word-problem
  - topic/finitely-presented-groups
  - topic/periodic-groups
  - topic/coset-enumeration
  - topic/finite-group-enumeration
  - paper
  - status/draft
---

# Generalized algorithm for modeling periodic groups

> **Translation note**: vault language is English. Source is Russian; the Abstract below is translated; quotes are translated and tagged `[trans.]`. Original Russian is not preserved here — `language: ru` records the source.

## Abstract

The paper proposes an algorithm for modeling arbitrary periodic groups defined by generators and relations, based on the computation of elements and relations in the given groups. [trans.]

## TL;DR

Generalizes the $K_s(m,n)$-iteration algorithm of [[kuznetsov-shlepkin-2009]] from free Burnside groups to **arbitrary finitely-presented periodic groups**. Two changes from the Burnside version: drop the $n$-aperiodicity block (take $n \to \infty$ in $A_1$) so orders need not be known, and initialize the relation list $C_1$ with the presentation's input relators rather than $\emptyset$. The construction, the finiteness criterion (Theorem 2: $K_s = K_{s+1} \implies |G| \le |P_s|$), and the worked example ($G = \langle a, b \mid a^3 = b^2 = (ab)^2 = 1\rangle = S_3$, computed by hand to $|G| = 6$) follow the Burnside template directly.

## Problem

The earlier paper [[kuznetsov-shlepkin-2009]] gave an algorithm — call it Algorithm I — for computing elements and relations in free Burnside groups $B(m,n)$. Applying that algorithm to an arbitrary finitely-presented periodic group

$$G = \langle x_1, x_2, \ldots, x_m \mid w_i(x_1, \ldots, x_m) = v_i(x_1, \ldots, x_m),\ i = 1, \ldots, n \rangle$$

raises a difficulty: the orders of group elements are not generally known in advance, so the $n$-aperiodicity reduction step is not directly applicable. Question: can the algorithm be modified to compute $G$'s elements, relations, and order purely from the presentation, with no $a$-priori knowledge of element orders?

## Approach

**Two modifications to the Burnside-version Algorithm I** (§2):

1. **Drop the $n$-aperiodicity block.** Take $n \to \infty$ in the algorithm $A_1$ from [[kuznetsov-shlepkin-2009]]'s §1.2 ($A_1$ originally reduces any $n$-periodic subword $x^n$ to $\epsilon$). With $n = \infty$, $A_1$ becomes the identity (no $x^\infty$ subword can occur), so the $n$-aperiodicity reduction is effectively neutralized.
2. **Seed $C_1$ with the input relators.** Where the Burnside version starts with $C_1 = \emptyset$ (the exponent relation $g^n = e$ is enforced implicitly by $A_1$), the general version starts with

$$C_1 = \{w_i(x_1, \ldots, x_m) = v_i(x_1, \ldots, x_m) \mid i = 1, 2, \ldots, n\}.$$

**Otherwise identical** to [[kuznetsov-shlepkin-2009]]: build the sequence $K_1, K_2, \ldots, K_s, \ldots$ where each $K_s = (P_s, A_s, T_s, C_s)$ is a quadruple of (minimal-word set $\le$ length $s$, reduction algorithm, Cayley multiplication table, relation list). Iterate the Cayley-table-closure construction: row collisions in $T_s$ force new relations, which fold into $A_s$ and refine $P_s$. Continue until $K_s = K_{s+1}$.

**Finiteness criterion (Theorem 2).** If $s$ is the least natural number such that $K_s = K_{s+1}$, then $|G| \le |P_s|$. Proof: from $P_s = P_{s+1} = P_{s+2} = \cdots$, every $g \in G$ has some representative word $v_1 = \alpha_1 \cdots \alpha_r$, and $A_s(v_1) = v \in P_s$ with $r_1 \le s$; the lemma from [[kuznetsov-shlepkin-2009]] gives uniqueness, so distinct group elements map to distinct $P_s$ words.

**Comparison with coset enumeration (Introduction).** The authors note that the standard alternative — Todd-Coxeter coset enumeration ([Sims 1994], [Holt-Eick-O'Brien 2005]) — operates in the **opposite direction**: it specifies trailing subwords in defining relators (introducing new symbols for unspecified ones, then iterating), while Algorithm I **excludes** words from an ordered sequence using existing and newly derived relations. The authors argue Algorithm I is more technologically stable: memory needs are bounded between extensions of $P_s$; identification avalanches that collapse partial results to the trivial group (a known coset-enumeration failure mode) do not occur; checkpointing is cheap; partial results have standalone scientific value (the relations and minimal-word counts computed at each $s$).

**Worked example (§3).** $G = \langle a, b \mid a^3 = b^2 = (ab)^2 = 1\rangle$ (the symmetric group $S_3$). The authors walk through the construction step by step:

- $P_1 = \{a, b\}$, $C_1 = \{aaa = e,\ bb = e,\ abab = e\}$, $T_1$ shown explicitly.
- $K_2$ obtained with $P_2^{(1)} = \{a, b, aa, ab, ba\}$ (the word $bb$ reduces to $e$).
- $K_3$ requires four iterations: row collisions force successive new relations $bab = aa$, $baa = ab$, $aab = ba$, $aba = b$.
- After the fifth iteration, $P_3^{(5)} = \{a, b, aa, ab, ba\}$ stabilizes; $C_3$ contains 7 relations.
- $P_4 = P_3 \cup \{e\}$ — no new minimal words at length 4; algorithm terminates with $|G| = 6$, $G = \{e, a, b, aa, ab, ba\}$. Matches the known $|S_3| = 6$.

## Key result

**Theorem 2 (§2).** Let $s$ be the least natural number such that $K_s(m,n) = K_{s+1}(m,n)$, where $K_s = (P_s, A_s, T_s, C_s)$ is constructed from the generalized algorithm starting with $C_1 = \{w_i = v_i\}$. Then $|G| \le |P_s|$. Moreover (implicit from the worked example), when $G$ is finite the inequality is an equality.

**The algorithm fully specifies a decision procedure for the word problem on any finite finitely-presented periodic group** — given a word $u$ in the generators, compute $K_s$ until stabilization, then $A_s(u) \in P_s$ is the unique minimal representative.

**Worked example result:** for $G = \langle a, b \mid a^3 = b^2 = (ab)^2 = 1\rangle$, the algorithm computes $|G| = 6$ explicitly, in 5 iterations on $K_3$.

## Assumptions

- The presentation $\langle x_1, \ldots, x_m \mid w_i = v_i\rangle$ defines a periodic group (every element has finite order). If $G$ is not periodic, the algorithm's behaviour is undefined — there is no $A_1$ reduction at $s = 1$ to bound word lengths, so $|P_s|$ may grow unboundedly even on a finite quotient.
- The length-then-lex order on words is well-defined and total — standard.
- The lemma carried over from [[kuznetsov-shlepkin-2009]]: distinct group elements always have distinct minimal-word representatives.
- Cayley-table-row collision detection is a sound implication: $A_s(v_{i_0} v_j) = A_s(v_{i_0} v_k)$ in $G$ implies $v_j = v_k$ in $G$ (cancellation of $v_{i_0}$ on the left, which holds in any group).
- Computational implementation correctness — implicit.

## Limitations / scope

- The algorithm **only terminates when $G$ is finite**. For infinite $G$ (or for $G$ whose finiteness is unknown), the algorithm produces an unbounded sequence $K_1, K_2, \ldots$ with $|P_s| < |P_{s+1}|$ strictly. This is the same fundamental limitation as KB completion on infinite groups — Algorithm I is not an oracle for infiniteness.
- Periodicity is required. The "general" in the title refers to **arbitrary finitely-presented periodic groups**, not arbitrary finitely-presented groups. Non-periodic infinite groups break the algorithm's foundations.
- The worked example ($S_3$, order 6) is too small to stress the algorithm or to demonstrate scaling. No timings, memory profiles, or comparisons to Knuth-Bendix or Todd-Coxeter are reported.
- No upper-bound theorem on $|P_s|$ as a function of $s$ or of the presentation — the algorithm's complexity is empirical only.

## Replication evidence

The worked $S_3$ example is verifiable by hand or by any group-theory CAS. The 6-element output matches the known $|S_3| = 6$. No further computational examples are reported in this paper. External replication outside the authors' Krasnoyarsk group has not been located in this vault.

## Why this paper matters

This paper **decouples Algorithm I from the Burnside setting**, giving it standalone status as a word-problem decision procedure for finitely-presented periodic groups. That generalization is necessary if Algorithm I is to be used on **groups that are presented with explicit non-trivial relators** — i.e. quotients of free groups by more than just an exponent relation. Anything but a free Burnside group falls under this category.

The two-line modification (drop $n$-aperiodicity, seed $C_1$ with input relators) is genuine but unsurprising — the underlying machinery from [[kuznetsov-shlepkin-2009]] does the work. The paper's main contribution is **positioning Algorithm I as a method for general computational group theory**, not just for Burnside computation.

The comparison-with-coset-enumeration argument is the paper's most useful editorial content: Algorithm I has structural advantages (bounded memory between $P$-extensions, no identification-avalanche collapse, cheap checkpointing, partial-result scientific value) that the authors argue make it complementary to Todd-Coxeter rather than competitive. This positioning is worth keeping in mind when considering algorithm-cooperation framings for general FPG word-problem attacks — exactly the Mixer architectural pattern.

## Quotes

1. > "The element-exclusion process in Algorithm I is the opposite of the new-symbol-inclusion process in the coset enumeration algorithm; consequently, this algorithm is more suited to enumerating groups universal in some class." — Introduction [trans.]
2. > "Theorem 2. Let s be the least natural number with the property $K_s = K_{s+1}$. Then $|G| \le |P_s|$." — Section 2 [trans.]

## Open questions surfaced

- For which finitely-presented periodic groups does Algorithm I terminate in a tractable number of iterations? The $S_3$ example is too small to characterize this empirically; what is the algorithm's behaviour on, say, the alternating groups $A_n$, or on small Coxeter quotients?
- Can Algorithm I be coupled with a coset-enumeration Agent in a cooperative scheme — using element-exclusion (Algorithm I) and symbol-inclusion (Todd-Coxeter) as complementary search strategies? The authors hint at this in the introduction but do not pursue it.
- For an unknown-finiteness group, what tractable upper bounds can be placed on the rate of $|P_s|$ growth that would constitute computational evidence (not proof) for infiniteness?
- Does the algorithm extend naturally to **non-periodic** finitely-presented groups by introducing a length-bounded variant — e.g. compute $K_s$ for fixed $s$ and report the partial Cayley structure as a finite-quotient approximation?

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]] (Algorithm I, originally for free Burnside groups, here lifted to arbitrary finitely-presented periodic groups)
- Contradicts: (none)
- Replicates: (none — different setting from any prior vault note)
- Concepts introduced/used: [[Concepts/cayley-table-closure-algorithm]] (this paper is the natural location of the algorithm's general statement, independent of Burnside specifics)
- Cites (in vault): [[kuznetsov-shlepkin-2009]]
- Cites (outside vault): Sims 1994 "Computation with Finitely Presented Groups"; Holt-Eick-O'Brien 2005 "Handbook of Computational Group Theory" — neither is in vault as of write time; both are standard references on coset enumeration; Kostrikin 1986 "Around Burnside" (Russian) — also not in vault.
- Cited by (in vault): [[_synthesis-kuznetsov-b25-algorithmic-line]]
- MOC: [[_moc-burnside]] (despite being the general-FPG paper, lands here because of its lineage with the B(2,5)-specific [[kuznetsov-shlepkin-2009]] and [[kuznetsov-shlepkin-2010]])
- Related techniques: [[knuth-bendix]] (alternative word-problem algorithm; this paper does not use it but the comparison is implicit), [[coset-enumeration]] (the alternative the authors explicitly position against)
- Parent overview: [[group-theory-overview]]
