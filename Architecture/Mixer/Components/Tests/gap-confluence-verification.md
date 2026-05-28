---
title: gap-confluence-verification
path: verify_confluence.g
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "verify_confluence.g — run: gap -q -c 'rules_file := \"path/to/rules.txt\";' verify_confluence.g"
invariants:
  - id: generator-count-matches
    summary: "The GAP free group is constructed with a fixed number of generators (currently up to 5: a,b,c,d,e). Rules referencing generators beyond this set are silently skipped."
    why: "StringToWord in verify_confluence.g maps characters 'a'–'e' to F.1–F.5. A rules file using generators outside this range (e.g. for a 6-generator group) would have those rules silently ignored, giving a false impression of confluence."
  - id: group-presentation-separate
    summary: "verify_confluence.g does NOT include the group relations. It only checks whether the given rules form a confluent rewriting system for the FREE GROUP on the generators."
    why: "The current script reads a rules file and checks local confluence (critical pair completion) in the free monoid, not in the quotient group. This means it verifies the formal rewriting system property, not group-theoretic confluence. A caller who wants to verify confluence of a Burnside group rewriting system must supply rules that already encode the group relations, or the verification is incomplete."
related:
  - gap-word-equality
  - kbmag-source
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# GAP confluence verification

## What it is

A GAP script that reads a rewriting rules file (text format, one `LHS->RHS` rule per line), constructs the rules as a KnuthBendixRewritingSystem in GAP's KBMag package, and checks whether the system is confluent. Returns a pass/fail result to stdout.

## Why it exists

A confluent rewriting system for a group has a unique normal form for every group element — a critical property for word-problem solvers. Before using a rule bank as an oracle ("reduce this word to its unique normal form"), you want evidence that the rules together form a confluent system rather than a partial/incomplete one. This script provides that check via GAP's KBMag package, which implements the Knuth-Bendix confluence criterion directly.

## How it fits

Used as a one-shot post-hoc check after a kbprog run appears to have converged:

```
kbprog run → candidate rule set (input.kbprog.live or extracted subset)
→ gap -q -c 'rules_file := "<path>";' verify_confluence.g
→ CONFLUENT / NOT CONFLUENT
```

## Critical invariants — why each one exists

### generator-count-matches

`StringToWord()` in the script recognises characters `a–e` (lowercase) and `A–E` (uppercase inverses), mapping them to `F.1–F.5` and their inverses. Rules containing any other characters are silently skipped. For a 2-generator group (B(2,5): generators a,b), this is fine. For a 4-generator group (B(4,3): generators a,b,c,d), also fine. A 6-generator group would fail silently. The number of generators in the free group `F` must also match: the script currently uses `FreeGroup("a","b","c","d","e")` (5 generators), and that must match the rules being checked.

### group-presentation-separate

The script checks whether the given set of rules is a confluent rewriting system in the abstract sense — local confluence on the free monoid. It does NOT encode the group axioms (Burnside relations, etc.) separately. To verify confluence of a Burnside group rewriting system, the rules file must include the group relations as rewrite rules, not just the KB-generated rules. Omitting the group presentation means the script verifies a weaker property than intended. This is a known limitation documented in the script's comment: "Uses KBMAG package to verify that a rewriting system is confluent."

## Public surface — script interface

```
gap -q -c 'rules_file := "/abs/path/to/rules.txt";' verify_confluence.g
```

Input: a plain-text file with rules in `LHS->RHS` format, one per line, comments starting with `#`.

Output: `CONFLUENT` or `NOT CONFLUENT` (or an error if the file cannot be read or GAP's KBMag package is not installed).

## Related

- [[gap-word-equality]] — tests individual word equality, orthogonal to confluence
- [[kbmag-source]] — produces the rule sets this tool verifies

## Known issues

- Group presentation not included — the verification is of the formal rewriting system, not the quotient group. See the `group-presentation-separate` invariant.
- Script is at repo root (`verify_confluence.g`), not in `tests/`. Its location is informal.
- Requires GAP with the KBMag package installed; no check for this precondition.
