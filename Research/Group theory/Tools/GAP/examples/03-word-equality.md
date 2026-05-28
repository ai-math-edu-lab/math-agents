---
title: "GAP: Test word equality in a finitely presented group"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - topic/finitely-presented-groups
  - content-type/code-example
  - status/validated
---

# GAP: Test word equality in a finitely presented group

**Task:** Given two words w₁, w₂ in a finitely presented group G, decide if w₁ = w₂ in G.

**Verified on:** GAP 4.15.1 at `/opt/homebrew/bin/gap`, 2026-05-28.

## Example: Equality in Z/6Z

```gap
gap> F := FreeGroup("a", "b");;
gap> a := F.1;; b := F.2;;
gap> # Z/6Z = <a | a^6 = 1, b trivial>
gap> G := F / [a^6, b, a*b*a^(-1)*b^(-1)];;
gap> ga := G.1;; gb := G.2;;
gap> w1 := ga^3;; w2 := ga^3;;
gap> w1 = w2;
true
gap> w3 := ga^6;; e := Identity(G);;
gap> w3 = e;
true
gap> w4 := ga^2 * ga^4;; w4 = e;
true
```

**Output (verbatim):**
```
ga^3 = ga^3: true
ga^6 = e: true
ga^2 * ga^4 = e: true
```

## How it works

GAP uses coset enumeration internally for equality testing in FPGs. For equality testing:
- `w1 = w2` is equivalent to `w1 * w2^-1 = Identity(G)`.
- GAP reduces both sides to a canonical form (if the group is finite and small enough).

## Limitation

For large or infinite groups, `=` may not terminate. In that case:
- Use KBMAG to produce a confluent rewriting system, then reduce both words to normal form.
- If the normal forms are equal, the words are equal.
- See `Tools/KBMAG/examples/` for word reduction via kbprog.

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree: use GAP for small groups, KBMAG for large
- [[_moc-word-problem]] — the word-problem MOC (word equality is the core decision problem)
- [[target-words]] — what target words are and how to verify them (this example shows the verification step)
- [[01-s3-shortlex]] — sibling in KBMAG: the same equality check via a confluent system
