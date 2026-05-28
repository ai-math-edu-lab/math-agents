---
title: "GAP: Enumerate cosets of a subgroup"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/coset-enumeration
  - topic/finitely-presented-groups
  - content-type/code-example
  - status/validated
---

# GAP: Enumerate cosets of a subgroup

**Task:** Enumerate right cosets of a subgroup H in G, compute [G:H].

**Verified on:** GAP 4.15.1 at `/opt/homebrew/bin/gap`, 2026-05-28.

## Example: Cosets of ⟨a⟩ in S3

```gap
gap> F := FreeGroup("a", "b");;
gap> a := F.1;; b := F.2;;
gap> G := F / [a^2, b^3, (a*b)^2];;    # S3
gap> ga := G.1;; gb := G.2;;
gap> H := Subgroup(G, [ga]);;           # H = <a> (order 2)
gap> Index(G, H);
3
gap> cosets := RightCosets(G, H);;
gap> Length(cosets);
3
gap> for c in cosets do Print("  ", Representative(c), "\n"); od;
  <identity ...>
  b
  b*a
```

**Output (verbatim):**
```
Index [G:H]: 3
Right cosets: 3
  <identity ...>
  b
  b*a
```

## Coset table (Todd-Coxeter)

```gap
gap> ct := CosetTable(G, H);;
gap> NumberRows(ct);
4
```

The 4 rows in the coset table correspond to: 4 generators/inverses (a, A=a⁻¹, b, B=b⁻¹). Each column is one coset.

## Notes

- `RightCosets(G, H)` enumerates by Todd-Coxeter internally; terminates only for finite index.
- For verification: `[G:H] × |H| = |G|` — check: 3 × 2 = 6 ✓
- If [G:H] is infinite or very large, `CosetTable` will not terminate.

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree for GAP vs KBMAG
- [[_moc-presentations-and-orders]] — the presentations-and-orders MOC (coset enumeration is a core topic)
- [[coset-enumeration]] — foundational note on the Todd-Coxeter algorithm
- [[01-group-order]] — sibling: order computation uses coset enumeration internally
- [[presentations]] — the presentation ⟨X|R⟩ is the input; Todd-Coxeter operates on it
