---
title: kbmag-source
path: kbmag_source/standalone/
domain: infra
hot_path: false
status: draft
author: maumayma
project: b25
public_api:
  - "kbprog (kbmag_source/standalone/bin/kbprog) — Knuth-Bendix completion engine, run as subprocess"
  - "b25_lifted (kbmag_source/standalone/kb_data/b25_lifted) — B(2,5) group presentation with lifted generator m"
invariants:
  - id: kbprog-live-readable
    summary: "kbprog writes rules incrementally to input.kbprog.live while still running; callers must not wait for termination."
    why: "kbprog runs for hours or indefinitely. b25_reduce_core scripts read rules live from input.kbprog.live; polling for process exit would block rule injection."
  - id: b25-lifted-ordering
    summary: "The b25_lifted presentation file uses shortlex ordering by default; RPO runs replace the ordering line via sed, not by editing the file."
    why: "run_biased_agents.sh creates per-agent copies in $BASE/runs/$name/ and uses sed to swap the ordering field. The canonical kb_data/b25_lifted is read-only source."
  - id: target-word-kgrams
    summary: "The -sk parameter must match the k-gram size used in the modified kbmag C source (default k=8). Mismatch silently changes which rules get marked special."
    why: "The biasing mechanism compares k-grams of candidate rules against k-grams of the target word. If -sk differs from the compiled-in k, the priority queue behaves differently from what the Python analysis scripts expect."
related:
  - kgram-overlap-verification
  - special-rule-overlap-verification
  - braid-reduce
  - b25-reduce-core-deps-2026-05-22
tests:
  unit: tests/verify_kgram_special.py
  integration: tests/verify_special_rules.py
known_issues:
  - "kbmag_source/ has no build system tracked in CI. The precompiled binary is committed; a clean rebuild requires running ./configure && make inside kbmag_source/."
  - "For RPO ordering, run_biased_agents.sh uses sed to swap the ordering field in a per-agent copy of b25_lifted — any other presentation fields that differ between shortlex and RPO (e.g. confnum defaults) are not adjusted."
tags: [agent/dev, user/maumayma, domain/infra, project/b25, status/draft]
---

# kbmag-source — KBMag Knuth-Bendix completion engine (b25_reduce_core only)

> **Scope:** `kbmag_source/` is the **narrow, secondary** KBMag installation. It serves one workflow: `experiments/b25_reduce_core/run_biased_agents.sh`. The project-wide main KBMag is `kbmag_v1/`; see [[kbmag-overview]] for the full picture. Do not use `kbmag_source/` as the starting point for new experiments.

## What it is

`kbmag_source/standalone/` provides the compiled `kbprog` binary used by `experiments/b25_reduce_core/run_biased_agents.sh` to generate rewrite rules for B(2,5). Given a group presentation file and a target word, `kbprog` runs indefinite Knuth-Bendix completion and writes discovered rules to a `.kbprog.live` file in its working directory while still running. The `b25_lifted` presentation file in `kb_data/` defines B(2,5) extended with a lifted generator `m = X⁻¹bX` where X is the 35-char core of the commutator `[c₁₂, c₉]`.

## Why it exists

The B(2,5) word-reduction problem requires rule banks that specifically cover the structural patterns of the target commutator words. Generic (unbiased) Knuth-Bendix generates a large but broadly distributed rule set; the biased variant, triggered by `-sw target.txt -sp prob -sk k`, prioritises equations whose k-grams overlap with the target word's k-grams. This dramatically increases the density of applicable rules for the specific target, at the cost of less overall convergence progress. The `b25_lifted` presentation extends B(2,5) with the compressed generator `m`, allowing kbprog to discover rules in a smaller alphabet space and reduce the 544-char lifted form directly.

## How it fits in the system

`run_biased_agents.sh` launches 6 kbprog processes in parallel, each with a different target word (core_a, core_b, boundary, prefix, etc.) and ordering (shortlex or RPO). Each writes to its own `experiments/b25_reduce_core/runs/<name>/input.kbprog.live`. These live rule files are then consumed by `reduce_coreless.py` (which scans them for rules whose LHS appears in the current word) and, after aggregation, feed the 2.5 GB `mega_ab_rules.live` bank used by the Rust beam-search scripts.

> `run_biased_agents.sh` → 6× kbprog (biased, parallel) → `runs/<name>/input.kbprog.live`
> → [[reduce-coreless]] scans live files → [[braid-reduce]] beam search uses `mega_ab_rules.live`

## Critical invariants — why each one exists

### kbprog-live-readable

kbprog writes rules to `input.kbprog.live` continuously as it finds them; the file is valid and parseable at any point during the run. `reduce_coreless.py`'s `scan_matching_rules()` opens the file, reads all current rules, and closes it — the kbprog process keeps running. This design lets the experiment harvest rules progressively without coordinating process termination. The invariant breaks if any caller opens the file exclusively or renames it while kbprog has it open.

### b25-lifted-ordering

The canonical `kb_data/b25_lifted` file has `ordering := "shortlex"`. For RPO agents, `run_biased_agents.sh` creates a per-agent directory copy and runs `sed 's/ordering := "shortlex"/ordering := "recursive"/'` on it before launching kbprog. The original file in `kb_data/` is never modified. If a caller forgets the sed step and runs RPO mode against the unmodified file, kbprog silently uses shortlex ordering — the resulting rules will look different but no error is reported.

### target-word-kgrams

The modified kbmag C source uses k=8 for the special-rule biasing mechanism. When `run_biased_agents.sh` passes `-sk 8` (for boundary/prefix agents) or `-sk 6` (for core agents), these values must align with whatever k the C code was compiled with. The test `tests/verify_kgram_special.py` independently replicates the k=8 criterion in Python; if a rebuilt kbprog changes k, the test will report a mismatch between the Python prediction and the observed "special" fraction in `input.kbprog.live`.

## Public surface — what other components touch

`run_biased_agents.sh` is the sole direct caller of `kbprog`. The flags it actually passes:

```
kbprog -v -me 50000000 -ms 500000000 -t 5000 -cn 5000 \
       -sw <target.txt> -sp <fraction> -sk <k> <input_dir>
```

- `-me 50000000` — max equations (50 M); prevents runaway memory use
- `-ms 500000000` — max states for FSA automata
- `-t 5000` / `-cn 5000` — tidy interval / confluence number: how often to run the critical-pair check
- `-sw <file>` — path to a file whose first non-comment line is the target word; kbprog extracts k-grams to bias rule priority
- `-sp <prob>` — probability of selecting a "special" equation per tidy cycle (0.5–0.7 in practice)
- `-sk <k>` — k-gram size: 6 for core agents, 8 for boundary/prefix agents

The output file `<input_dir>/input.kbprog.live` has one rule per line in `LHS -> RHS` format. Lines starting with `#` are comments. Empty RHS means the LHS equals the identity.

## Hot path?

Not a hot path. `kbprog` is an external process launched once per agent and runs for hours. The `.live` file scan in `reduce_coreless.py::scan_matching_rules()` is I/O-bound, not CPU-bound.

## Tests

- `tests/verify_kgram_special.py` — verifies that the k=8 criterion correctly identifies "special" rules: given a target word and a rules file, reports what fraction of rules have LHS/RHS k-gram overlap with the target. Cross-checks against the fraction kbprog itself marks special. See [[kgram-overlap-verification]].
- `tests/verify_special_rules.py` — checks four overlap types (RHS substring, LHS substring, prefix/suffix overlap, factor containment) for rules kbprog marked special. See [[special-rule-overlap-verification]].

## Related

- [[kbmag-source]] ← you are here
- [[kbmag-overview]] — two-way split between kbmag_source and kbmag_v1
- [[braid-reduce]] — consumes the rule banks produced by kbprog agents
- [[reduce-coreless]] — scans live rule files while agents run
- [[kgram-overlap-verification]] — test methodology validating the biasing criterion
- [[special-rule-overlap-verification]] — test methodology for rule–word overlap types

## Recent changes

- 2026-05-22 — initial component note, drafted from Phase 1 dependency trace ([[b25-reduce-core-deps-2026-05-22]])
