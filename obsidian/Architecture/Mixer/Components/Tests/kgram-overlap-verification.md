---
title: kgram-overlap-verification
path: tests/verify_kgram_special.py
domain: methodology
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "verify_kgram_special.py <special_word_file> <rules_file> [--sample N] — k-gram overlap analysis"
invariants:
  - id: k-matches-kbmag
    summary: "k must equal the k-gram size compiled into the modified kbmag C source (default 8). The script hardcodes K=8."
    why: "kbmag marks a rule as 'special' if any k-gram of its LHS or RHS appears in the target word's k-gram set. If the script uses k=8 but kbmag was compiled with k=6, the script's predictions will not match what kbmag actually marks special."
  - id: short-rule-fallback
    summary: "Rules shorter than k are tested with full-substring membership rather than k-gram overlap."
    why: "A rule whose LHS has length < k produces zero k-grams by definition. The script uses `rhs in special_word` for these, mirroring what kbmag must do for short patterns."
related:
  - special-rule-overlap-verification
  - kbmag-source
tags: [agent/dev, user/maumayma, domain/methodology, project/mixer-core, status/draft, convention]
---

# k-gram overlap verification

## What it is

A static analysis tool that reads a rule bank (`.live` format) and a target word, and reports what fraction of rules have any k-gram (default k=8) from their LHS or RHS appearing in the target word's k-gram set. It independently replicates the criterion kbmag uses to classify rules as "special" — eligible for priority scheduling in the biased KB completion run.

## Why it exists

The biased kbmag completion (`-sw target -sp prob -sk k`) marks rules as special based on k-gram overlap. If the biasing is working correctly, special rules should be concentrated on patterns that structurally relate to the target word. This test answers: "are the rules kbmag is prioritising actually related to our target?" It was developed to validate that the `-sk 8` flag in `run_biased_agents.sh` was producing the expected behaviour — and to catch situations where a recompile of kbmag changed k without an obvious failure mode.

## How it fits

Run after kbprog has been running for some time on a biased agent, to validate that the emerging rule bank is biased as expected:

```
run_biased_agents.sh → input.kbprog.live (growing)
→ verify_kgram_special.py <target_word> <input.kbprog.live>
  → reports: % rules with LHS/RHS k-gram overlap, directly applicable rules
```

## Critical invariants — why each one exists

### k-matches-kbmag

The hardcoded `K = 8` in `verify_kgram_special.py` must match the value compiled into the kbmag C source. There is no runtime way to query what k kbmag is using. If someone recompiles kbmag with a different k and forgets to update the script, the script will report that many fewer rules are "special" than kbmag actually marks — the apparent drop in biasing effectiveness is a false alarm. Conversely, if the script uses a larger k than kbmag, it will undercount special rules and the biasing will look weaker than it is.

### short-rule-fallback

Rules whose LHS or RHS is shorter than k cannot have any k-gram; the k-gram set is empty. The script handles these separately: a short RHS is considered special if it appears as a full substring of the target word (`rhs in special_word`). This mirrors the only meaningful overlap test for short strings.

## Public surface — script interface

```
python tests/verify_kgram_special.py <special_word_file> <rules_file> [--sample N]
```

- `special_word_file` — path to a text file; first non-comment line is the target word
- `rules_file` — path to a `.kbprog.live` file
- `--sample N` — limit to the first N rules (for quick checks on large banks)

**Output:** prints k-gram match statistics (% special by type), directly applicable rules (LHS is full substring of target), k-gram match count distribution, and a sample of applicable special rules with position context.

## Related

- [[special-rule-overlap-verification]] — complementary test: checks 4 overlap types for rules kbmag *already* marked special
- [[kbmag-source]] — the component whose output this test validates

## Known issues

- `K = 8` is hardcoded; no CLI flag to change it. If kbmag is rebuilt with a different k, both the script and the documentation must be updated.
- Does not verify that kbmag's internal marking agrees with the script's prediction — it only replicates the expected criterion. A live comparison would require parsing kbmag's internal debug output.
