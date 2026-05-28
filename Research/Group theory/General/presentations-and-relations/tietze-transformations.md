---
title: "Tietze Transformations"
author: maumayma
language: en
source: "Lyndon & Schupp, Combinatorial Group Theory (1977), §I.4"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - status/validated
related:
  - "[[presentations]]"
  - "[[coset-enumeration]]"
---

# Tietze Transformations

## Definition

**Tietze transformations** are elementary operations on group presentations that preserve the presented group (up to isomorphism). There are four:

**T1 (Add relator):** If w is a consequence of the existing relators (i.e., w ∈ ⟪R⟫), add w to R.
$$\langle X \mid R \rangle \Rightarrow \langle X \mid R \cup \{w\} \rangle$$

**T2 (Remove relator):** If w ∈ R is a consequence of R\{w}, remove w from R.
$$\langle X \mid R \rangle \Rightarrow \langle X \mid R \setminus \{w\} \rangle$$

**T3 (Add generator):** If φ is a new symbol and w is a word in F(X), add generator φ with relator φw⁻¹.
$$\langle X \mid R \rangle \Rightarrow \langle X \cup \{\phi\} \mid R \cup \{\phi w^{-1}\} \rangle$$

**T4 (Remove generator):** If x ∈ X appears in a relator xw⁻¹ ∈ R (where w is a word in F(X)\{x}), eliminate x by substituting w throughout.
$$\langle X \mid R \cup \{xw^{-1}\} \rangle \Rightarrow \langle X \setminus \{x\} \mid R' \rangle$$
where R' is R with x replaced by w everywhere.

**Tietze's Theorem:** Two finite presentations present the same group iff one can be transformed to the other by finitely many Tietze transformations.

*Source: Lyndon-Schupp §I.4, Theorem 1.*

## Why it matters

Tietze transformations give a decision procedure for presentation equivalence in principle (though not in practice — testing presentation isomorphism is in general undecidable for infinite groups). In practice, they are used to:

1. **Simplify presentations:** Add redundant generators to express relators more simply; then eliminate the original generators that now appear in simple relators.
2. **Reidemeister-Schreier:** Derive a presentation for a subgroup H of G from a presentation of G. The resulting presentation is often highly redundant; Tietze T2 and T4 are applied to simplify.
3. **KB completion output:** The rules produced by Knuth-Bendix can be viewed as a systematic application of T1 (adding relators that are consequences of the original ones) — building up to a confluent system.

## Example

Presentation of S₃:

Starting: ⟨a, b | a², b³, (ab)²⟩.

Apply T3: introduce c = ab. Apply T4: c = ab so a = cb⁻¹ = cB. Substitute into relators:
- a² = e: (cB)² = cBcB = e → cBcB = e
- b³ = e: unchanged
- (ab)² = e: c² = e (directly, since ab = c and (ab)² = c² = e)
- New: cB (the relator expressing a = cB)

Result: ⟨b, c | b³, c², cBcB, cB⟩ — simplify further by T4 using cB to eliminate B...

In practice, GAP's `SimplifiedFpGroup` function applies Tietze transformations automatically.

## Related concepts

- [[presentations]] — the input/output of Tietze transformations.
- [[coset-enumeration]] — produces a presentation for a subgroup (Reidemeister-Schreier), which is then simplified by Tietze.
