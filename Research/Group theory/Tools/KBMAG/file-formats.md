---
title: "KBMAG file formats — .kbprog input/output and kbprog flags"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/kbmag
  - convention
  - status/validated
---

# KBMAG file formats — .kbprog input/output and kbprog flags

**Verified on:** `kbmag_v1/standalone/bin/kbprog`, 2026-05-28.

## .kbprog file format

KBMAG uses the same file format for both **input** (group presentation) and **output** (completed rewriting system). The format is a GAP record structure:

```
_RWS := rec(
           isRWS := true,
  generatorOrder := [a,A,b,B,...],   # generators + their inverses, interleaved
        ordering := "shortlex",       # reduction ordering (see below)
        inverses := [A,a,B,b,...],    # inverses[i] = inverse of generatorOrder[i]
       equations := [
         [lhs, rhs],                  # rewriting rules: lhs -> rhs
         ...
       ]
);
```

**Key fields:**
- `isRWS := true` — required; marks this as a rewriting system file.
- `generatorOrder` — lists all symbols. Convention: alternate generator/inverse pairs `[g, G, h, H, ...]` where uppercase = inverse.
- `inverses` — inverses[i] is the inverse of generatorOrder[i]. For `[a,A,b,B]` → `[A,a,B,b]`.
- `ordering` — the reduction ordering (see below).
- `equations` — list of rules `[lhs, rhs]` with `lhs ≻ rhs`. `IdWord` = identity.

**Output-only fields** (added by kbprog to the output file):
- `isConfluent := true` — added when KB completion succeeds.
- `maxeqns := N` — number of rules in the completed system.

## Minimal input example

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

This is the input for S3 = ⟨a,b | a²=e, b³=e, (ab)²=e⟩. See `Tools/KBMAG/examples/01-s3-shortlex.md` for the verified output.

## Output file naming

kbprog writes the completed system to `<inputfile>.kbprog`. Example:
- Input: `s3.kbprog`
- Output: `s3.kbprog.kbprog`

## Ordering options

| Ordering string | Description |
|---|---|
| `"shortlex"` | Shortlex: shorter words first; ties broken lexicographically by `generatorOrder`. Standard, safe. |
| `"recursive"` | Recursive path ordering (RPO): based on lexicographic order of generators. Better for non-abelian groups. |
| `"wtlex"` | Weighted lex: generators have weights; prefer lower-weight words. |
| `"wreathprod"` | Wreath product ordering: groups generators into "levels". |

For experiments in this repo, `"shortlex"` and `"recursive"` are the two orderings used in the Mixer (see `experiments/b43_kbmag_mixing/`).

## kbprog flags (selected)

Run `kbprog -help` for the full list. Key flags:

| Flag | Description |
|---|---|
| (no flags) `kbprog <file>` | Run KB completion; output to `<file>.kbprog` |
| `-wr <file>` | "Word reduce" mode: complete system + print final rules verbosely |
| `-cn N` | Stop if number of rules exceeds N (default: 32768) |
| `-ml N` | Max LHS length (default: 10) |
| `-mr N` | Max RHS length |
| `-sk N` | Extract k-grams for bias-seeding (used in mixing experiments) |
| `-sp P` | Fraction of equations biased to special (used in mixing experiments) |
| `-sw` | Read only the first non-comment line as the word to reduce |

**In practice:** The experiments in this repo call kbprog programmatically via Python wrappers in `experiments/b43_kbmag_mixing/` — see `b43_mix.py` for examples.

## Related material

- [[kbmag-tools-overview]] — parent: KBMAG tool overview and binary locations
- [[group-theory-tools-overview]] — decision tree: when to use kbprog vs GAP
- [[_moc-knuth-bendix]] — the KB MOC (file formats are prerequisite tooling knowledge)
- [[01-s3-shortlex]] — verified kbprog run illustrating the format in practice
- [[knuth-bendix]] — the technique: what the .kbprog equations section means algebraically
