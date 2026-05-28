---
title: "GAP package: kbmag"
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

# GAP package: kbmag

The `kbmag` GAP package wraps the standalone KBMAG tools, allowing Knuth-Bendix completion directly from a GAP session.

**See also:** `Tools/GAP/examples/05-kbmag-package.md` for a complete runnable example (S3).

## Setup

```gap
gap> LoadPackage("kbmag", false);;   # false suppresses verbose loading output
```

## Create a rewriting system

From any GAP group (finitely presented):

```gap
gap> F := FreeGroup("a", "b");;
gap> a := F.1;; b := F.2;;
gap> G := F / [a^2, b^3, (a*b)^2];;   # S3
gap> R := KBMAGRewritingSystem(G);
```

`KBMAGRewritingSystem(G)` creates a rewriting system object R. The initial equations are derived from the group's relators.

## Run Knuth-Bendix

```gap
gap> KnuthBendix(R);;
gap> IsConfluent(R);
true
```

Returns `true` if the system converged to a confluent rewriting system. Returns `false` (or runs indefinitely) if KB doesn't terminate.

## Query the system

```gap
gap> Size(R);     # = |G| once confluent
6
gap> Length(R!.equations);   # number of rewriting rules
7
gap> EnumerateReducedWords(R, 0, 20);   # all elements as reduced words, length ≤ 20
```

## Word reduction

```gap
gap> ReducedForm(R, a*b*a);   # reduce a word to normal form
b^-1
```

Requires the system to be confluent. The normal form of a word w is the unique irreducible word equal to w in G.

## Test word equality

```gap
gap> ReducedForm(R, a*b*a) = ReducedForm(R, b^(-1));
true
```

Two words are equal in G iff their reduced forms match (when R is confluent).

## Ordering

Default ordering is shortlex. To change:

```gap
gap> R := KBMAGRewritingSystem(G, rec(ordering := "recursive"));;
```

## Relationship to standalone kbprog

The GAP package calls the standalone `kbprog` binary internally. For large groups (like B(2,5)), using standalone `kbprog` directly with custom flags is more flexible. See `Tools/KBMAG/` for standalone usage.

## Verified example

See `Tools/GAP/examples/05-kbmag-package.md` — the S3 example produces: `Confluent: true`, `Size: 6`, `Rules: 7`.

## Related material

- [[gap-overview]] — parent: GAP tool overview and key function reference
- [[group-theory-tools-overview]] — decision tree: which tool for which task
- [[kbmag-tools-overview]] — standalone kbprog alternative to the GAP package
- [[_moc-knuth-bendix]] — MOC covering KB completion, tooling, and the Mixer extension
- [[knuth-bendix]] — the technique conceptual note (what KB does and why)
- [[05-kbmag-package]] — verified GAP kbmag session on S3 (uses this package)
