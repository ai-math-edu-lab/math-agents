---
title: "The Use of Knuth-Bendix Methods to Solve the Word Problem in Automatic Groups"
authors: D.B.A. Epstein, D.F. Holt, S.E. Rees
year: 1991
venue: "Journal of Symbolic Computation 12 (1991) 397–414"
url: "https://www.sciencedirect.com/science/article/pii/S0747717108800934"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 59
citation_count_date: 2026-06-11
key_concepts:
  - "[[Concepts/complete-rewriting-systems]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[knuth-bendix-1970]]"
  - "[[le-chenadec-1986]]"
  - "[[gilman-1979]]"
cited_by:
  - "[[holt-1995-warwick-ags]]"
  - "[[epstein-sanders-2000]]"
  - "[[epstein-et-al-1992-word-processing]]"
quality_notes: "Precursor paper to Epstein et al. 1992 (Word Processing in Groups) — the journal article that operationalised the automatic-group / KB integration before the full monograph appeared. The approach described here is the algorithmic core of KBMAG's word-acceptor and multiplier-automaton construction."
author: ethan-k
tags:
  - agent/research
  - user/ethan-k
  - domain/group-theory
  - topic/automatic-groups
  - topic/knuth-bendix
  - topic/word-problem
  - topic/finite-state-automata
  - topic/rewriting-systems
  - topic/shortlex-ordering
  - paper
  - status/draft
---

# The Use of Knuth-Bendix Methods to Solve the Word Problem in Automatic Groups

## Abstract

Certain classes of infinite groups arising from geometry and topology are known to have solvable word problem. We describe the development of practical methods for the solution of the word problem based on the reduction of words in the generators to a normal form. The Knuth-Bendix completion procedure is the principal tool used but, in the case that this process does not halt, we use alternative methods involving the construction of finite-state automata. A computer implementation of these procedures together with some performance statistics on some simple examples are also described.

## TL;DR

This paper describes an implemented algorithm for solving the word problem in automatic groups by combining Knuth-Bendix completion with finite-state automaton construction. When KB completion generates an infinite (but regular) confluent rewriting system, the procedure constructs a finite **word-acceptor automaton** W and **multiplier automata** Ma that certify correctness — without ever needing the full infinite system. The paper is the computational precursor to the 1992 Epstein et al. monograph and the direct ancestor of KBMAG.

## Problem

For infinite finitely-presented groups (hyperbolic groups, surface groups, Euclidean groups), KB completion commonly diverges — producing an infinite confluent rewriting system rather than a finite one. Simply stopping KB early and hoping for the best yields no correctness guarantee. The challenge: can one extract a provably correct word-problem solver from partial KB output, without proving confluence of the infinite system (which is known to be undecidable in general)?

## Approach

The algorithm proceeds in three stages (Sections 3–5):

**Stage 1 — KB completion with interruption (Section 3).** Run the KB procedure under the **shortlex (length-plus-lexicographic) ordering** on a finite generating set A. Interrupt at regular intervals after every n new equations. At each interruption: (a) make the current equation set Er minimal (remove redundant rules); (b) compute the set D of **word differences** — the finite set of group elements arising from all equations in Er. When D appears stable across interruptions, halt and proceed.

**Stage 2 — Construct the word-acceptor automaton W (Section 4).** Using the **principal transition table** (a partial map $\varphi: A \times A^* \times D \to D$ derived from the equations), build W as a subset-construction automaton over subsets of $D \setminus \{e\}$. Only accessible states need be computed. W accepts precisely the shortlex-least representatives (normal forms) for group elements, provided the principal transition table is correct.

**Stage 3 — Construct multiplier automata and verify (Sections 4–5).** Extend the equation set to $E'_r$ to compute the larger word-difference set $D'$. Construct multiplier automata $M_a$ for each generator $a \in A$ via Corollary 2.4 (a product of two copies of W plus a finite automaton tracking word differences). Minimise all automata. Verify the key hypothesis (Theorem 2.5 (iv)): for each defining relator $r = a_1 a_2 \ldots a_n$, check that the composite automaton $M_{a_1} \circ M_{a_2} \circ \cdots \circ M_{a_n}$ equals the diagonal automaton $M_\$$ derived from W. This is done by file-comparison of minimised automata transition tables.

All programs were written in C and run on a Sun 3/60 workstation.

## Key result

**Theorem 2.5** (correctness condition): Let G = (A|R) be a finitely presented group. Suppose W and $M_a$ (for each $a \in A$) are finite-state automata satisfying four conditions (each accepted word has a prefix also accepted; multiplier automata certify generator actions; relation verification passes). Then G is automatic with respect to these automata and W accepts a unique word for each group element.

**Theorem 4.1**: The finite-state automaton W defined by the principal transition table construction is correct if the principal transition table is correct. — Section 4.

**Performance statistics (Section 6):**
- Trefoil knot group $G = \langle a,b \mid bab = aba \rangle$: D has 14 typed word differences, D' has 20. W minimises to 16 states; multiplier automata minimise to 37–43 states. Computation: a few seconds cpu-time.
- Von Dyck group $D(2,3,n)$ for $n = 7,8,9,10,11$: complexity increasing slowly (probably linearly) with n; sizes similar to Example 6.1.
- Genus-2 surface group (4 generators): W minimises to 48 states (or 25 with non-default generator ordering that yields a finite confluent system). Largest composite automaton: $M_{a a' b b' a b}$ with 304 states minimising to 143. Total: about 80 seconds cpu-time.
- 4-generator hyperbolic Coxeter group (Example 6.4): KB run for about 3200 seconds; Er had ~500 equations; D has 76 word differences, D' has 87. W minimises to 126; $M_a$ etc. minimise to ~550. Relation verification: ~1360 seconds. Largest composite: 11 738 states minimising to 957.

The practical limit of the KB stage was approximately 10 000 equations.

## Assumptions

- The group G is **shortest-word automatic** with respect to the ordered generating set A: W accepts only the lexicographically least word of shortest length for each group element (shortlex normal form). The algorithm is stated only for this restricted class, not automatic groups in general (though the theory extends; the shortlex restriction simplifies the $M_a$ construction).
- The generating set A is **closed under inversion**: for each $a \in A$ there exists $a' \in A$ with $aa', a'a \in R$.
- The group is finitely presented.
- The user must make "an intelligent guess as to when all word differences of E have been found, and then stop the program" — the halting of the KB stage is heuristic, not automatic.

## Limitations / scope

- **No termination guarantee for the KB stage.** For groups that are not automatic (or whose word differences stabilise slowly), the procedure may never produce a usable D. The paper gives no criterion for detecting this.
- **Confluence of the infinite system is undecidable** (cited from Benninghofen et al. 1987): the paper explicitly avoids verifying confluence of the full infinite system E, relying instead on Theorem 2.5's correctness check via the multiplier automata.
- **Practical limits on composite automata.** The space required for composite automata (before minimisation) is the main obstacle for complex examples. A 5-generator hyperbolic Coxeter group failed: W minimised to 1190 states but the multiplier automata had ~250 000 states (minimised to ~28 000); even the first composite $M_{aa}$ could not be computed for lack of space.
- **Restricted to shortest-word automatic groups.** Extensions to other automatic groups (non-shortlex normal forms) require additional work.

## Replication evidence

The approach described is the direct computational predecessor of KBMAG (Knuth-Bendix on Monoids and Automatic Groups), implemented by Holt and distributed as a GAP package. The algorithm is reproduced and extended in Epstein et al., *Word Processing in Groups* (1992), Chapter 10. The correctness of the automaton-construction procedure is confirmed by the KBMAG implementation.

## Why this paper matters

This paper is the first published implementation account of the KB-plus-automata strategy for solving the word problem in automatic groups. It bridges the theoretical definition of automatic groups (due to Thurston and Cannon, cited as a preprint) and the practical computational tool (KBMAG). Three specific contributions make it vault-relevant:

1. **Word-difference finiteness as the computational handle.** Theorem 2.3 (that the set of word differences of $L(M_a)$ is finite for automatic groups) transforms an infinite rewriting system into a finite data structure. This is what makes the construction of W and the $M_a$ from partial KB output feasible in practice.

2. **The correctness verification pipeline.** By reducing correctness to the equivalence of composite automata (Theorem 2.5 (iv)), the paper gives a practical certificate of correctness without proving confluence of the infinite system E — solving the fundamental problem that confluence of infinite systems is undecidable.

3. **Empirical limits of single-strategy KB.** The performance data in Section 6 documents exactly where KB-plus-automata breaks down: space for composite automata before minimisation. This is the empirical motivation for multi-strategy approaches.

## Quotes

1. > "The purpose of this paper is to describe an implementation of an effective solution to this problem for certain automatic groups." — Section 1

2. > "It is shown in Benninghofen et al. (1987, chapter III.1.3) that the confluence of such a system is an undecidable property in general." — Section 1

## Open questions surfaced

- **Stopping criterion for KB stage.** The paper relies on the user's "intelligent guess" about when D has stabilised. Can the stabilisation of word differences be detected algorithmically (without running forever)?
- **Space explosion in composite automata.** The main practical bottleneck (documented in Section 6) is the size of composite automata before minimisation. Is there an incremental minimisation technique that avoids constructing the full composite before minimising?
- **Non-shortlex automatic groups.** The procedure is stated for shortest-word automatic groups. Does it extend to groups that are automatic but not shortest-word automatic? If so, what changes to the principal transition table are needed?
- **Complexity of the word-difference set.** For what families of groups does $|D|$ grow with the presentation complexity? The performance data show growth from 14 (knot group) to 76 (4-generator Coxeter group), but no general bound is given.
- **Infinite rules.** The paper explicitly raises the case of infinite KB (groups like the genus-2 surface group with the default ordering) and notes it "is certainly no systematic method of achieving" a finite system. What classes of presentations necessarily produce infinite KB? (Addressed later by Epstein-Sanders 2000 for specific families.)

## Related material in vault

- Parent overview: [[word-problem-overview]]
- MOC: [[Research/Group theory/_MOCs/_moc-knuth-bendix|_moc-knuth-bendix]]
- MOC: [[Research/Group theory/_MOCs/_moc-word-problem|_moc-word-problem]]
- Cited by: [[epstein-et-al-1992-word-processing]] (this 1991 paper is the precursor to the 1992 monograph, which reproduces and extends its algorithm in Chapter 10)
- Cites: [[knuth-bendix-1970]] (the foundational KB completion procedure this paper applies)
- Technique hub: [[Research/Group theory/Word Problem/techniques/automatic-groups|automatic-groups]]

---

*Author: [[People/ethan-k|ethan-k]]*
