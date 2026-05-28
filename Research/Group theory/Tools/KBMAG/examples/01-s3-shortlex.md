---
title: "KBMAG: Knuth-Bendix on S3 (shortlex ordering)"
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

# KBMAG: Knuth-Bendix on S3 (shortlex ordering)

**Task:** Run standalone `kbprog` on the symmetric group S3 and read the confluent rewriting system output.

**Binary used:** `/Users/maumayma/Desktop/reps/algo_mixing/kbmag_v1/standalone/bin/kbprog`
**Verified on:** 2026-05-28.

## Input file (`s3.kbprog`)

```
_RWS := rec(
           isRWS := true,
  generatorOrder := [a,A,b,B],
        ordering := "shortlex",
        inverses := [A,a,B,b],
       equations := [
         [a*a, IdWord],
         [b*b*b, IdWord],
         [a*b*a*b, IdWord]
       ]
);
```

**Group:** S3 = ⟨a, b | a² = e, b³ = e, (ab)² = e⟩

**Notation:** Lowercase = generator; uppercase = inverse (A = a⁻¹, B = b⁻¹). `IdWord` = identity.

## Run command

```sh
kbprog s3.kbprog
```

**Terminal output (verbatim):**
```
#System is confluent.
#Halting with 8 equations.
```

## Output file (`s3.kbprog.kbprog`)

kbprog writes the completed rewriting system to `<input-file>.kbprog`:

```
_RWS := rec(
           isRWS := true,
     isConfluent := true,
         maxeqns := 8,
  generatorOrder := [a,A,b,B],
        ordering := "shortlex",
        inverses := [A,a,B,b],
       equations := [
         [b*B,IdWord],
         [B*b,IdWord],
         [a^2,IdWord],
         [b^2,B],
         [A,a],
         [B^2,b],
         [B*a,a*b],
         [b*a,a*B]
       ]
);
```

## Reading the output

- `isConfluent: true` — the system is complete (every word has a unique normal form).
- `maxeqns: 8` — 8 rewriting rules in the final system.
- `A → a`: a⁻¹ = a (a has order 2).
- `b² → B`: b² = b⁻¹ (b has order 3, so b³ = e → b² = b⁻¹).
- `B² → b`: consistent with b³ = e.
- `b*a → a*B`: ba = ab⁻¹ (the non-abelian rule for S3).
- `B*a → a*b`: b⁻¹a = ab.

**Normal forms** (irreducible words): {e, a, b, B, a*b, a*B} — 6 elements, correct for S3.

## Verifying word equality

To test if word w₁ = w₂, reduce both by the rules (by longest-match, left-to-right) to normal form. Equal normal forms ⟺ equal group elements.

Example: Does a*b*a = b⁻¹ in S3?
- a*b*a: apply `b*a → a*B` to get a*(a*B) = a²*B → B (since a² → e). So a*b*a reduces to B. ✓

## Related material

- [[kbmag-tools-overview]] — parent: KBMAG tool overview and binary locations
- [[group-theory-tools-overview]] — decision tree for GAP vs KBMAG
- [[_moc-knuth-bendix]] — the KB MOC (this is a primary verified KBMAG example)
- [[knuth-bendix]] — foundational technique note: what KB does and what confluence means
- [[file-formats]] — .kbprog input/output format reference (format used in this example)
- [[05-kbmag-package]] — sibling: the same S3 completion via the GAP kbmag package
