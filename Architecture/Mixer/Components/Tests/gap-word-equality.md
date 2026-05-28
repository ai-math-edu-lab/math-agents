---
title: gap-word-equality
path: check_word.g
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "check_word.g — GAP script; edit lhs/rhs variables then run: gap -q check_word.g"
invariants:
  - id: presentation-completeness
    summary: "The GAP script constructs B(4,3) from all w^3=1 relations for |w|<=3. It does NOT use a convergent rewriting system; equality is decided by GAP's coset enumeration."
    why: "GAP's IsomorphismFpGroup and quotient operations make equality in the presented group decidable by coset table methods. This is sound for B(4,3) (finite group) but would diverge or fail for infinite groups. The script is correct only for the specific group it encodes."
  - id: alphabet-b43
    summary: "The script uses generators a,b,c,d for B(4,3), not a,b for B(2,5). Using it for B(2,5) words requires rewriting the presentation."
    why: "B(4,3) and B(2,5) have different generator sets and relations. The current script hardcodes 4 generators and B(4,3) relations. A user testing a B(2,5) word would get wrong results (they'd be testing equality in B(4,3), not B(2,5))."
related:
  - gap-confluence-verification
  - traced-braid-reduction
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# GAP word-equality check

## What it is

A GAP script that loads the KBMag package, constructs B(4,3) from scratch by enumerating all `w^3 = 1` relations for words of length ≤ 3, and tests whether two specific group words are equal in that group. The current words in the script test `abaCBAdcb = cABA` in B(4,3). The output is either `YES: …` or `NO: …`.

## Why it exists

Computational rewriting systems (like the rule banks produced by kbprog) can in principle reduce a word to a form that is *shorter* but not actually *equal* in the group — if the rules were unsound, incorrectly oriented, or applied to the wrong group. The GAP word-equality check provides an independent, ground-truth oracle: it constructs the group independently of any rewriting system and tests equality by coset enumeration. It is the final sanity check before trusting a reduction chain.

## How it fits

Used as a spot check after a significant reduction result, outside the automated pipeline:

```
(after finding a candidate reduction chain for B(4,3))
→ edit check_word.g lhs/rhs to your words
→ gap -q check_word.g
→ YES: reduction is valid in B(4,3)   NO: something is wrong
```

## Critical invariants — why each one exists

### presentation-completeness

The script constructs B(4,3) using all `(gh)^3 = 1` and `(ghk)^3 = 1` relations for generators `a,b,c,d` and their inverses. This is a complete presentation of B(4,3) in the sense that the quotient `F / rels` is exactly B(4,3). GAP decides equality by Todd-Coxeter coset enumeration, which is complete (terminates and gives the right answer) for any finite group. The method is independent of any ordering choice or rewriting system — it directly tests group equality.

### alphabet-b43

The generator set `{a,b,c,d}` and the exponent 3 are hardcoded for B(4,3). The script is not parameterised. To test B(2,5) equality, one would need to replace all relations with `w^5 = 1` for |w| ≤ 5 or equivalent, change the generators to `{a,b}`, and provide the two words to compare.

## Public surface — script interface

Edit `check_word.g` directly to set the words to compare:
```gap
lhs := ga*gb*gA*gC*gB*gA*gd*gc*gb;   -- left-hand side word
rhs := gc*gA*gB*gA;                   -- right-hand side word
```
Then run: `gap -q check_word.g`

Output: `YES: <lhs_str> = <rhs_str> in B(4,3)` or `NO: <lhs_str> != <rhs_str> in B(4,3)`

## Related

- [[gap-confluence-verification]] — tests a whole rewriting system, not individual words
- [[traced-braid-reduction]] — Python-side step-by-step chain verification for B(2,5)

## Known issues

- Hardcoded to B(4,3); not parameterised. Editing the script is required for every new word pair.
- No command-line interface. The words must be edited inside the script.
- Script is at repo root (`check_word.g`), not in `tests/`. Its location is informal.
