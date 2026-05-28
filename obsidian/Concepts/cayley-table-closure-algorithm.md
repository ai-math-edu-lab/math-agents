---
title: Cayley-table closure algorithm (Kuznetsov's Algorithm I)
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/cayley-table-closure
  - topic/word-problem
  - topic/finite-group-enumeration
  - concept
  - status/draft
introduced_in:
  - "[[kuznetsov-shlepkin-2009]]"
related_concepts:
  - "[[Concepts/verification-methods-for-group-equality]]"
appears_in:
  - "[[kuznetsov-shlepkin-2009]]"
  - "[[kuznetsov-tarasov-shlepkin-2009]]"
  - "[[kuznetsov-shlepkin-2010]]"
---

# Cayley-table closure algorithm (Kuznetsov's Algorithm I)

> **Concept hub.** This note exists as a shared anchor — the three Kuznetsov papers in this vault all rely on this algorithm. Long discussion lives in the paper notes; this hub gives the cross-paper view of one technique.

## Definition

A word-problem decision procedure for finite (or finitely-presented periodic) groups that incrementally builds a sequence of objects

$$K_s = (P_s,\ A_s,\ T_s,\ C_s),\quad s = 1, 2, \ldots$$

where, for a group $G = \langle x_1, \ldots, x_m \mid R\rangle$ presented by generators and relators $R$:

- $P_s$ = the ordered set of all **minimal words** (representatives) of length $\le s$, under a fixed length-then-lex order on words ($x_1 < x_2 < \cdots < x_m$, then $u < v$ iff $L(u) < L(v)$ or equal-length with lex tie-break);
- $A_s$ = a word-reduction algorithm that uses currently-known relations to rewrite any word to its $P_s$-form (or a shorter prefix of it);
- $T_s$ = the partial Cayley multiplication table $\|v_i v_j\|$ for $v_i, v_j \in P_s$, with cells reduced by $A_s$;
- $C_s$ = the cumulative list of relations $\{v = w \mid v \prec w\}$ discovered so far.

**Closure step (the heart of the algorithm):** extend $P_{s-1}$ to a candidate $P_s^{(0)}$ by appending generators, apply $A_{s-1}$ to filter $A$-invariant words, and build $T_s^{(0)}$. Detect new relations from one of two equivalent collision conditions:

- **Row-collision variant** (Kuznetsov-Shlepkin 2009): two cells in the same row of $T_s$ reduce to the same word, $A^{(0)}_s(v_{i_0} v_j) = A^{(0)}_s(v_{i_0} v_k)$ with $v_j < v_k$ ⟹ new relation $v_j = v_k$.
- **Associativity-test variant** (Kuznetsov-Shlepkin 2010): $A_s(v_i A_s(v_j v_k)) \neq A_s(A_s(v_i v_j) v_k)$ with $v \prec w$ being the two sides ⟹ new relation $v = w$.

Add each new relation to $C_s$, fold it into the reduction algorithm ($A^{(i+1)}_s = A^{(i)}_s * A_{c_r}$), and iterate until $T_s$ is invariant. The result is $K_s = (P_s, A_s, T_s, C_s)$.

**Termination dichotomy** (Kuznetsov-Shlepkin 2010, Theorems 1 and 2):

- **Finite case:** if $s$ is the least natural number with $K_s = K_{s+1}$, then $(P_s, A_s, C_s, *)$ with $a * b := A_s(ab)$ is a group isomorphic to $G$, and $|G| = |P_s|$.
- **Infinite case:** if $|P_s| < |P_{s+1}|$ for all $s$, then $\lim_s K_s$ exists and is isomorphic to $G$ — in particular, $G$ is infinite.

So the algorithm provides a witness in either case: a finite Cayley table when $G$ is finite, or a strictly-growing minimal-word sequence when $G$ is infinite. **Practical caveat:** the infinite case can only be detected in the limit, so the algorithm cannot _decide_ infiniteness in finite time — it can only fail to terminate.

## Why it matters

This algorithm is **a third algorithmic family for the word problem on finite groups**, alongside:

1. **Knuth-Bendix completion** ([[knuth-bendix]]): produces a confluent term-rewriting system; verification through reduction to normal form. Termination ⟺ finite group with confluent rewriting; non-termination is silent on finiteness.
2. **Coset enumeration** (Todd-Coxeter; see [[coset-enumeration]]): produces a permutation representation of $G$ on cosets; verification through orbit computation. Termination requires the right inputs but can be brittle (identification avalanches collapsing to the trivial group).

Kuznetsov's algorithm is **structurally different** from both. Where KB produces a rewriting system (oriented relations) and Todd-Coxeter produces a permutation representation (cosets), Kuznetsov produces an **explicit minimal-word set $P_s$ with a Cayley table $T_s$** — the most direct possible computational representation of a finite group.

**Concrete advantages over Todd-Coxeter** (per [[kuznetsov-tarasov-shlepkin-2009]] introduction):

- Memory needs are bounded between extensions of $P_s$ (the table size is determined by $|P_s|$ and doesn't fluctuate during inner-loop iterations).
- No identification-avalanche collapse to the trivial group (the row-collision detection is local; relations are added one at a time, and each is verified against the existing list before incorporation).
- Cheap checkpointing (the $K_s$ object is small and self-contained at each $s$).
- Partial results have standalone scientific value: $|C_s|$ and $|P_s|$ values for $s$ short of stabilization are useful empirical inputs.

**Advantages over KB:**

- The infinite-case witness (strictly-growing $|P_s|$) is more interpretable than KB's "the algorithm didn't terminate, but maybe it would have if we waited longer."
- Output is a **direct enumeration** of group elements rather than a normal-form rewriting system — useful for downstream operations that need to iterate over elements.

**Disadvantages:**

- Memory scales as $|P_s|^2$ for the Cayley table; for large groups this is harder than KB's rewriting-system size.
- No published parallelization strategy in the cited papers (the 2010 cluster run used MATLAB's Parallel Computing Toolbox at a coarse granularity, not algorithm-aware parallelism).
- The algorithm is, as published, **not benchmarked against KB or Todd-Coxeter** on a shared workload — comparative claims rest on architectural arguments rather than head-to-head numbers.

## Where it appears

- Introduced in: [[kuznetsov-shlepkin-2009]] (free Burnside group setting, row-collision detection)
- Generalized in: [[kuznetsov-tarasov-shlepkin-2009]] (arbitrary finitely-presented periodic groups, same row-collision detection)
- Refined in: [[kuznetsov-shlepkin-2010]] (associativity-test detection, finite/infinite limit theorems)
- Appears in: [[kuznetsov-shlepkin-2009]], [[kuznetsov-tarasov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]]
- Related concepts: [[Concepts/verification-methods-for-group-equality]] (the $\psi$ homomorphism in the Burnside papers is a verification-of-equality device built on top of this algorithm)

## Open questions

- Is Algorithm I provably faster than Knuth-Bendix on any natural class of finite groups, or are the advantages purely qualitative? No published head-to-head benchmark exists in this vault.
- Can the row-collision and associativity-test variants of detection be combined for additional efficiency, or are they equivalent in the sense that both detect exactly the same set of derivable relations at each step?
- Does the algorithm extend to **non-periodic** finitely-presented groups? Kuznetsov-Tarasov-Shlepkin 2009 explicitly requires periodicity (every element has finite order); without that, $A_1$ is the identity and $|P_s|$ grows unboundedly even on a finite quotient.
- Is there a Mixer-style cooperative scheme combining Algorithm I with KB or Todd-Coxeter — using element-enumeration (Algorithm I) and rewriting-rule generation (KB) and orbit computation (Todd-Coxeter) as three complementary witness streams? This is the natural multi-algorithm framing the Mixer architecture suggests; no published work investigates it for this combination.
- For B(2,5) specifically, what is the practical scaling rate of $|P_s(2,5)|$? The 2010 cluster run reaches $s = 35$ at ~104 CPU-hours per 125 nodes; whether modern hardware (or modern symbolic-algebra systems) can push this to $s \ge 45$ where $|P_s| > 5^{34}$ would prove $B(2,5)$ infinite is an open empirical question.

## References

1. Kuznetsov, A.A. & Shlepkin, A.K. (2009). *Comparative analysis of the Burnside groups B(2,5) and B₀(2,5)*. Trudy IMM UrO RAN, 15(2), 125–132. [Original presentation of Algorithm I in Burnside form; row-collision detection.] See [[kuznetsov-shlepkin-2009]].
2. Kuznetsov, A.A., Tarasov, S.A., & Shlepkin, A.K. (2009). *Generalized algorithm for modeling periodic groups*. Vestnik NSU, Mathematics, Mechanics, Informatics, 9(2), 47–54. [Generalization to arbitrary finitely-presented periodic groups.] See [[kuznetsov-tarasov-shlepkin-2009]].
3. Kuznetsov, A.A. & Shlepkin, A.K. (2010). *On the difference of the Burnside groups B(2,5) and B₀(2,5)*. Trudy IMM UrO RAN, 16(2), 133–138. [Associativity-test variant; cluster-scale computation; finite/infinite limit theorems; candidate-divergence relations at lengths 30–35.] See [[kuznetsov-shlepkin-2010]].
4. Sims, C. (1994). *Computation with Finitely Presented Groups*. Cambridge University Press. [Standard reference on the coset-enumeration alternative.]
5. Holt, D., Eick, B., & O'Brien, E. (2005). *Handbook of Computational Group Theory*. Chapman & Hall/CRC. [Comprehensive computational-group-theory reference; contrasting algorithm framework.]
