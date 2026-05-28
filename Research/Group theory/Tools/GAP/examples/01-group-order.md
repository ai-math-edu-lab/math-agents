---
title: "GAP: Compute group order"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/finitely-presented-groups
  - content-type/code-example
  - status/validated
---

# GAP: Compute group order

**Task:** Given a finitely presented group, compute |G|.

**Verified on:** GAP 4.15.1 at `/opt/homebrew/bin/gap`, 2026-05-28.

## Method 1: SmallGroups library (for groups of small order)

```gap
gap> G := SmallGroup(6, 1);
<pc group of size 6 with 2 generators>
gap> Order(G);
6
gap> IdGroup(G);
[ 6, 1 ]
```

**Output (verbatim):**
```
<pc group of size 6 with 2 generators>
6
[ 6, 1 ]
```

## Method 2: Finitely presented group

```gap
gap> F := FreeGroup("a", "b");;
gap> a := F.1;; b := F.2;;
gap> # S3 = <a,b | a^2 = b^3 = (ab)^2 = e>
gap> G := F / [a^2, b^3, (a*b)^2];;
gap> Order(G);
6
```

**Output (verbatim):**
```
6
```

**Note:** `Order(G)` on a finitely presented group uses coset enumeration internally. It will not terminate if G is infinite (or too large). For very large finite groups, use KBMAG to get a confluent rewriting system first, then enumerate.

## When to use

- Use `SmallGroup(n, k)` when you know the order and want one specific group.
- Use FPG presentation + `Order(G)` when you have a presentation and want to verify finiteness.
- If `Order(G)` hangs: the group may be infinite, or the order is too large for coset enumeration. Switch to KBMAG or the nilpotent quotient algorithm.

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree for GAP vs KBMAG
- [[_moc-presentations-and-orders]] — the presentations-and-orders MOC (order computation is a core topic)
- [[02-coset-enumeration]] — sibling: coset enumeration is how GAP computes order internally
- [[04-exponent-subgroups]] — sibling: related group-structure queries
- [[order-exponent]] — foundational note defining |G|, exponent, and torsion
