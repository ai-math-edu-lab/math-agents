---
tags: [agent/validator, meta]
---

# Validator — home

Independent math oracle. Verifies claimed math results, catches errors like the abelianization bug, writes property-based tests and proof sketches.

Role prompt: [[validator]] (at `_meta/agents/validator.md`).

**Verdicts on math correctness override everyone except the human.** Lead's code-quality verdict is independent and orthogonal — both must be positive for math-touching code to merge.

## What lives here

- `log.md` — append-only daily log
- `scratch/` — working files, throwaway analysis scripts

## Verification notes
Not here — they live in `Architecture/Mixer/Documentation/Math Validation/<YYYY-MM-DD>-<topic>.md`.

## Tests
Math-correctness tests go in the repo: `mixer-core/tests/proptest_*.rs` (Rust property tests) and `tests/property_*.py` (Python Hypothesis tests).
