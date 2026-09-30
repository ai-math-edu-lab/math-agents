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

### Project profile
- `[[project-<name>]]` — plus any extra pre-registration fields it requires (listed in its § Experiment template fields)

### Components / algorithms under test
- <each implementation: repo path + version/commit/build hash>

### Configuration
- <full parameter dict; for orchestration approaches include policy/scheduler type and params>

### Termination criteria
- <e.g. "first agent reports is_complete", "timeout 600s", "iteration count 10^6">

### Baselines (mandatory)
- <each component run alone, or the documented reference method — same seeds, same problems>

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
- Runner: `<repo>/experiments/<...>/run.py` (or tool / MCP service + job id)
- Command: `<exact command, incl. timeout>`

### Provenance record
- Code SHA(s): `<repo>@<sha>` (dirty: yes/no)
- Environment lock hash(es): `<lockfile or manifest> <hash>` for each
- Dependencies exercised: `<dep>@<version/sha>` (+ patches applied)
- Tool/binary versions: `<tool> <version/build hash>` for each
- Project-specific fields: `<per profile's provenance_fields>`

### Compute
- Where: <local host / MCP service / cloud backend>
- Resources: <CPU cores, RAM peak, GPU, wall-clock>

## Results — Baselines
| Problem | Agent (single) | Seed | Metric | |
|---|---|---|---|---|

## Results — Treatment
| Problem | Config | Seed | Metric | |
|---|---|---|---|---|

## Statistical analysis
- Test: <name>
- Statistic: <value>
- p-value: <value>
- Effect size: <Cliff's delta / Cohen's d / etc.>
- Conclusion: <...>

## Cross-verification (if applicable)
- Method: <independent tool from the dependency registry / hand calc>
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
- Treatment runs: `[[<output-note>]]`
