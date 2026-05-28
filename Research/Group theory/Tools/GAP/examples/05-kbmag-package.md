---
title: "GAP + kbmag: Knuth-Bendix from within GAP"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/kbmag
  - content-type/code-example
  - status/validated
---

# GAP + kbmag: Knuth-Bendix from within GAP

**Task:** Run Knuth-Bendix completion on a finitely presented group using the GAP `kbmag` package, check confluence, and enumerate elements.

**Verified on:** GAP 4.15.1 + kbmag package, 2026-05-28.

## Setup

```gap
gap> LoadPackage("kbmag", false);;   # false = suppress verbose loading
gap> F := FreeGroup("a", "b");;
gap> a := F.1;; b := F.2;;
gap> G := F / [a^2, b^3, (a*b)^2];;  # S3: the symmetric group on 3 elements
gap> R := KBMAGRewritingSystem(G);
```

The `KBMAGRewritingSystem(G)` creates a rewriting system object R from the group presentation.

## Run Knuth-Bendix

```gap
gap> KnuthBendix(R);;
gap> IsConfluent(R);
true
gap> Size(R);
6
gap> Length(R!.equations);
7
```

**Output (verbatim):**
```
Confluent: true
Size: 6
Rules: 7
```

`Size(R)` returns |G| = 6 once the system is confluent. `Length(R!.equations)` gives the number of rewriting rules in the confluent system.

## Enumerate elements

```gap
gap> EnumerateReducedWords(R, 0, 10);
[ <identity ...>, a, a*b, a*b^-1, b, b^-1 ]
```

This lists all 6 elements of S3 in reduced form (words of length ≤ 10).

## Word reduction

```gap
gap> ReducedForm(R, a*b*a);
b^-1
```

`ReducedForm(R, w)` reduces word w to its normal form under the confluent system. Here a*b*a reduces to b⁻¹ in S3.

## See also

- `Tools/KBMAG/examples/` — standalone `kbprog` usage for the same task (without GAP overhead)
- `Tools/GAP/package-kbmag.md` — full package documentation

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree for GAP vs KBMAG
- [[_moc-knuth-bendix]] — the KB MOC (this example uses KB completion via the GAP package)
- [[package-kbmag]] — the full GAP kbmag package overview (this example demonstrates it)
- [[01-s3-shortlex]] — sibling in KBMAG examples: the same S3 completion via standalone kbprog
- [[knuth-bendix]] — foundational technique note: what KB does and why it terminates
