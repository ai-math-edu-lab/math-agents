---
title: <experiment-name>-<YYYY-MM-DD>
hypothesis: <falsifiable claim>
status: pending
tags: [agent/exp, user/<handle>, domain/<...>, topic/<one+>, project/<subproject>, status/pending, experiment]
---

# Experiment — <name>

## Hypothesis
<One falsifiable sentence: metric + threshold + problem set.>

## Pre-registration

### Problem set
- Problems: <e.g. "B(4,3) with presentation X, B(5,3) with presentation Y, sorting random arrays of size N">
- Sizes / instances: <list>

### mixer Agents involved
- <list with module path + version/commit>

### Scheduler config
- Type: <threshold / periodic / composite>
- Params: <full param dict>

### Termination criteria
- <e.g. "first agent reports is_complete", "timeout 600s", "iteration count 10^6">

### Baselines (mandatory)
- Single-algo run for each `mixer Agent` involved, same seeds, same problems.

### Seeds
- <list, n≥5 for quantitative claims>

### Metric
- What we're measuring: <wall-clock to first solution / iteration count / items shared / quality of result>
- Why this metric (vs alternatives): <...>

### Statistical test
- Test: <paired Wilcoxon / Bayesian comparison / etc.>
- Why: <distribution assumptions justified>
- Effect size measure: <...>

### Anti-pattern check
- Param tuning on test set: <no / yes — justify>
- Cherry-picked seeds: <no — list all seeds>
- Cross-verification plan (for math claims): <how>

## Setup
- Runner: `experiments/<...>/run.py`
- Command: `<exact uv run command>`
- Provenance triple: git SHA `<...>` + uv.lock hash `<...>` + mixer-core build hash `<...>`

## Results — Baselines
| Problem | Agent (single) | Seed | Metric | |
|---|---|---|---|---|

## Results — Mixed
| Problem | Config | Seed | Metric | |
|---|---|---|---|---|

## Statistical analysis
- Test: <name>
- Statistic: <value>
- p-value: <value>
- Effect size: <Cliff's delta / Cohen's d / etc.>
- Conclusion: <...>

## Cross-verification (if applicable)
- Method: <kbmag_v1 / hand calc / Sage>
- Result: <matches / does not match>

## Final verdict
**`#status/validated` | `#status/rejected` | `#status/inconclusive`**

### Why
<One paragraph postmortem.>

### What I'd do next
- <Promote / file negative result / add seeds / replicate>

### Lead notified
- Date:
- Message: <wikilink>

## Output captures
- Baseline runs: `[[<output-note>]]`
- Mixed runs: `[[<output-note>]]`
