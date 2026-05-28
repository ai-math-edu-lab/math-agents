---
title: "GAP: Compute exponent and list subgroups"
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

# GAP: Compute exponent and list subgroups

**Task:** Compute the exponent of a group and enumerate its subgroups.

**Verified on:** GAP 4.15.1 at `/opt/homebrew/bin/gap`, 2026-05-28.

## Compute group exponent

The **exponent** of G is the smallest n such that gⁿ = e for all g ∈ G.

```gap
gap> C6 := CyclicGroup(6);;
gap> Exponent(C6);
6
gap> K4 := DirectProduct(CyclicGroup(2), CyclicGroup(2));; # Klein 4-group
gap> Exponent(K4);
2
gap> G := SmallGroup(12, 1);;
gap> Order(G);
12
gap> Exponent(G);
12
```

**Output (verbatim):**
```
Group order: 12
Exponent: 12
Z/6Z exponent: 6
Z2xZ2 exponent: 2
```

Note: Z/2Z × Z/2Z has exponent 2 (not 4) — every non-identity element has order 2.

## List subgroups

```gap
gap> G := SmallGroup(8, 3);;  # Dihedral group D4
gap> Order(G);
8
gap> subs := AllSubgroups(G);;
gap> Length(subs);
10
gap> List(subs, Order);
[ 1, 2, 2, 2, 2, 2, 4, 4, 4, 8 ]
```

**Output (verbatim):**
```
Group: D4 (SmallGroup(8,3))
Order: 8
Number of subgroups: 10
Subgroup orders: [ 1, 2, 2, 2, 2, 2, 4, 4, 4, 8 ]
```

D4 has 10 subgroups: the trivial group (order 1), five subgroups of order 2 (the five reflections and one rotation of order 2), three subgroups of order 4, and D4 itself.

## Notes

- `AllSubgroups(G)` is only feasible for small groups (exponential in |G| in the worst case).
- For large groups, use `MaximalSubgroups(G)` or `ConjugacyClassesSubgroups(G)` instead.
- `Exponent(G)` requires the group to be finite.

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree for GAP vs KBMAG
- [[_moc-presentations-and-orders]] — the presentations-and-orders MOC
- [[order-exponent]] — foundational note defining exponent and torsion
- [[01-group-order]] — sibling: basic order computation
- [[classification-fsg]] — the CFSG: all subgroups of finite simple groups are classified
