---
title: "KBMAG: Knuth-Bendix on B(2,3) (shortlex, fuller presentation)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/kbmag
  - topic/burnside
  - content-type/code-example
  - status/validated
---

# KBMAG: Knuth-Bendix on B(2,3) (shortlex, fuller presentation)

**Task:** Run standalone `kbprog` on a finitely presented group to produce a confluent rewriting system, then verify the group has the expected order.

**Group:** A quotient of B(2,3) (2-generator group of exponent 3) presented with 4 key relators.

**Binary used:** `/Users/maumayma/Desktop/reps/algo_mixing/kbmag_v1/standalone/bin/kbprog`
**Verified on:** 2026-05-28.

## Why a "fuller" presentation?

The simple presentation ⟨a,b | a³, b³, (ab)³⟩ (3 relators) is insufficient to present B(2,3) — kbprog diverges on it because the system is underdetermined (the presentation presents a larger group). B(2,3) requires more relators. A standard finite presentation uses:

```
a³ = b³ = (ab)³ = (ab⁻¹)³ = e
```

or equivalently ⟨a,b | a³, b³, [a,b]³⟩ (the commutator cube). With 4 relators, kbprog converges.

## Input file (`b23_full.kbprog`)

```
_RWS := rec(
           isRWS := true,
  generatorOrder := [a,A,b,B],
        ordering := "shortlex",
        inverses := [A,a,B,b],
       equations := [
         [a*a*a, IdWord],
         [b*b*b, IdWord],
         [a*b*a*b*a*b, IdWord],
         [a*B*a*B*a*B, IdWord]
       ]
);
```

Note: `B` is b⁻¹; `a*B*a*B*a*B` encodes (ab⁻¹)³.

## Run command

```sh
kbprog b23_full.kbprog
```

**Terminal output (verbatim):**
```
#System is confluent.
#Halting with 26 equations.
```

## Output file (verbatim, first 20 rules)

```
_RWS := rec(
           isRWS := true,
     isConfluent := true,
         maxeqns := 26,
  generatorOrder := [a,A,b,B],
        ordering := "shortlex",
        inverses := [A,a,B,b],
       equations := [
         [a*A,IdWord],
         [A*a,IdWord],
         [b*B,IdWord],
         [B*b,IdWord],
         [a^2,A],
         [b^2,B],
         [A^2,a],
         [B^2,b],
         [b*a*b,A*B*A],
         [B*A*B,a*b*a],
         [B*a*B,A*b*A],
         [b*A*b,a*B*a],
         [a*b*a*B,B*A*b],
         [A*B*A*b,b*a*B],
         [a*B*a*b,b*A*B],
         [A*b*A*B,B*a*b],
         [b*A*B*A,B*a*b],
         [B*a*b*a,b*A*B],
         [b*a*B*A,a*B*A*b],
         [B*A*b*a,a*B*A*b],
         ... (26 rules total)
       ]
);
```

## Reading the output

- `a² → A` and `A² → a`: generators a, A = a⁻¹ have order 3.
- `b² → B` and `B² → b`: generators b, B = b⁻¹ have order 3.
- `b*a*b → A*B*A`: the non-trivial commutator rule. In the group: bab = a⁻¹b⁻¹a⁻¹.

The 26-rule confluent system certifies the group is finite. The number of irreducible words equals the group order.

## Important note on presentations

The number of relators needed for KB to converge depends strongly on which group you mean. For B(2,n) in general:
- B(2,3) = 27 (finite): needs ≥ 4 relators for a practical finite presentation; more are needed for larger B(m,n).
- B(2,5) = 5^34: the full presentation from [[Research/Group theory/Burnside groups/B25/havas-wall-wamsley-1974]] has all commutator power relations; kbprog has not yet terminated for B(2,5).

## Related material

- [[kbmag-tools-overview]] — parent: KBMAG tool overview and binary locations
- [[_moc-knuth-bendix]] — the KB MOC (Burnside group KB completion examples live here)
- [[_moc-burnside]] — B(2,3) is a Burnside group; relates to B(2,5) as a simpler validated instance
- [[01-s3-shortlex]] — sibling: simpler S3 example showing the .kbprog format
- [[file-formats]] — .kbprog format and kbprog flags used in this example
- [[havas-newman-1980]] — B(2,3) is related to the Burnside group survey (B(2,4) example therein)
