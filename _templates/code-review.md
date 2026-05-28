---
title: <YYYY-MM-DD>-<topic>
branch: <feat|fix|chore>/<topic>
commit_sha: <short SHA — fill after commit>
tags: [agent/lead, user/<handle>, domain/<...>, topic/<one+>, status/<verdict>, review]
---

# Code Review — <topic>

## Patch summary
<2-3 sentences. What changed.>

## Files touched
<git diff --stat>

## Data model / protocol verdict
<sound / questionable / wrong — why. Check mixer protocol, pyo3 ABI, Python API stability.>

## Tests verdict
- Tests added: <yes/no — list>
- Coverage: <complete / partial>
- Re-run by Lead: <command, runtime, pass/fail>
- Smoke test ran (`uv run python examples/sorting/run.py`): <yes/no>

## Doctrine review
- [P1] Data structure / protocol: <...>
- [P2] Boring code: <...>
- [P3] Hardware truth: <...>
- [P4] Surgical changes: <...>
- [P5] Numbers cited: <...>
- [P6] Don't break userspace: <surfaces touched>
- [P7] Bogus-shit names: <...>

## Unverified claims demanding proof
- <...>

## Userspace impact
- Surfaces: <mixer protocol / pyo3 ABI / Python API / KBMAG format / none>
- Breaking: <yes/no — accepted by human?>

## Scope leakage
<...>

## Verdict
**MERGE | NEEDS WORK | REJECT**

## Required fixes
1. <...>

## Human approval log
- Asked: <YYYY-MM-DD HH:MM>
- Response: <commit & push / hold / edit-message>
- Commit SHA: <fill after>
- Pushed: <yes/no>
