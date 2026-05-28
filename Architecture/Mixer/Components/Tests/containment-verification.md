---
title: containment-verification
path: experiments/b25_reduce_core/archive/scripts/verify_containment.py
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "verify_containment.py — run standalone: python verify_containment.py (hardcoded words; edit source)"
invariants:
  - id: hardcoded-words
    summary: "The script tests a fixed set of hardcoded LHS/RHS pairs against hardcoded CORE_A and CORE_B strings. It is not a general-purpose containment checker."
    why: "The script was written as a one-off verification for specific rules being investigated at a point in time. It is not parameterised for general use. Any new containment question requires editing the source."
related:
  - reduce-coreless
  - traced-braid-reduction
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# Containment verification

## What it is

A static analysis script that checks whether specific LHS/RHS substrings of candidate rules contain, or partially overlap with, `CORE_A` and `CORE_B` — the two 35-char repeating cores of the comm_12_9 reduced word. It checks full containment (is CORE_A/B a substring of the rule's LHS?) and partial overlap (does a prefix of CORE_A/B match a suffix of the LHS, or vice versa?). The current script tests four hardcoded rule pairs.

## Why it exists

Understanding how reduction rules interact with the core structure of the target word is a key analysis step in the B(2,5) reduction program. When a candidate rule is long and opaque, manually checking "does it contain the core?" or "does it overlap the core boundary?" is tedious and error-prone. This script automates that check for a specific set of rules under investigation.

## How it fits

Used as a one-off analysis tool, not in any automated pipeline:

```
(investigating whether a specific rule relates to CORE_A/B)
→ edit verify_containment.py to add the rule pair
→ python verify_containment.py
→ reports: "Core B in LHS at offset: N" or "NO" for each pair, plus partial overlap lengths
```

## Critical invariants — why each one exists

### hardcoded-words

`CORE_A = "ABabAbabABaBAbabABABabAbaBABaBAbabb"` and `CORE_B = "BBABabAbabABaBAbabaBABabAbaBABaBAba"` are hardcoded. These are the defining structural constants of the comm_12_9 experiment (CORE_B is the free inverse of CORE_A). Any script derived from or analogous to this one must use the same CORE_A/B values — using incorrect cores would produce false containment verdicts.

## Public surface — script interface

```
python experiments/b25_reduce_core/archive/scripts/verify_containment.py
```

Hardcoded inputs; edit `lhs_46`, `lhs_43`, etc. to add new pairs. Output: for each pair, prints offset of CORE_A/B in LHS, offset in RHS, and partial overlap lengths at LHS boundaries.

An identical copy also exists at:
```
experiments/burnside/b25_bias_bidir/archive/verify_containment.py
```

Both are in archived locations.

## Related

- [[reduce-coreless]] — uses CORE_A/B for core-counting in the output report
- [[traced-braid-reduction]] — the step-by-step verification that tracks core structure through the chain

## Known issues

- Both copies are in archived directories. The methodology still matters (checking core containment in rules remains a valid analysis technique) but the specific files are not maintained.
- The script is hardcoded to specific rules from a specific investigation. It is not a reusable tool without editing.
- Confirmed by human (2026-05-22): no active script depends on these archived copies. They are purely historical.
