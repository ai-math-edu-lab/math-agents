---
title: M23 Mixing — Negative Result (slower than baseline across all 18 variants)
status: replicated
domain: group-theory
project: m23-kbmag-mixing
claim: "All 18 M23 KB mixing strategy variants are slower than the single-agent RPO baseline; best mixing result (v10f7, 1409.2s) is +27.7% above baseline (1103.8s); worst (v10f6, 1937.7s) is +75.5% above baseline."
claimant: Experimenter (general) via [[2026-06-02-non-b25-forensic-inventory]] §4 M23
verification_method: direct JSON spot-check of 5 individual result files + full-coverage Python sweep across all 18 variants + presentation/binary consistency check
tools_used: [Python 3, json, glob; direct file reads of results_archive/*.json]
author: maumayma
tags:
  - agent/validator
  - user/maumayma
  - domain/group-theory
  - project/m23
  - status/replicated
  - proof
---

# Verification — M23 Mixing Negative Result

## The claim

Experimenter (general) §4 of the non-B25 forensic inventory: all 18 M23 mixing variants are slower than the baseline single-RPO-agent run. Best mixing result (v10f7) is 1409.2s = +27.7% above baseline (1103.8s). This is the opposite of the B(4,3) result, where mixing accelerates convergence ~50× (91s baseline → 16s mixed).

## Method

1. Read `runs_m23_baseline_results.json` directly for baseline number.
2. Read `runs_baseline_v2_results.json` for a second baseline measurement (baseline variance check).
3. Read individual JSON for 5 spot-checked variants: v10f7 (best), v10f6 (worst), v10a, v10c, v10h.
4. Python sweep across all 18 variants in `tests/results_archive/` for coverage.
5. Checked both `m23_mix.py` and `tests/m23_sweep.py` for presentation file path and kbprog binary path.
6. Verified convergence state (final equation count) is consistent.

## Evidence

### Baseline

```
runs_m23_baseline_results.json:
  elapsed:        1103.8s
  confluent:      true
  winner:         rpo
  final_rpo_rules: 863186
  total_injected:  0
```

```
runs_baseline_v2_results.json (second run, same params):
  elapsed:        1023.0s
  confluent:      true
  final_rpo_rules: 863186
  total_injected:  0
```

**Baseline variance: 1103.8s vs 1023.0s = 80.8s (7.9% timing variance), n=2.** KB convergence is structurally deterministic (final rule count is identical: 863186 in both runs) but wall-clock timing is subject to system noise. Both baseline runs converge to the same solution.

### Spot-checked variants (raw JSON)

| Variant | total_time | final_rules | confluent | desc |
|---|---|---|---|---|
| v10f7 | **1409.2s** | 863186 | ✓ | Strict same-len @50k+100k, batch=0.005 |
| v10f6 | **1937.7s** | 863186 | ✓ | Strict same-len @50k, batch=0.01, 600s source |
| v10a  | **1484.3s** | 863186 | ✓ | Same-len @10k, \|red\|≤1, batch=0.01 |
| v10c  | **1489.7s** | 863186 | ✓ | Same-len @200k, \|red\|≤1, batch=0.01 |
| v10h  | **1418.3s** | 863186 | ✓ | Same-len @50k, \|red\|≤2, batch=0.01 |

All five verified individually. All match Experimenter's claims.

### Full 18-variant sweep

```
All 18 variants in tests/results_archive/ vs primary baseline (1103.8s):

  v10f7       1409.2s   +27.7%   (best mixing)
  v10h        1418.3s   +28.5%
  v10f5       1461.2s   +32.4%
  v10b        1466.3s   +32.8%
  v10e        1469.0s   +33.1%
  v13         1468.7s   +33.1%
  v10a        1484.3s   +34.5%
  v10c        1489.7s   +35.0%
  v10f2       1501.5s   +36.0%
  v10f3       1509.2s   +36.7%
  v10f4       1509.5s   +36.8%
  v5          1526.4s   +38.3%
  v1          1529.1s   +38.5%
  v10f        1536.9s   +39.2%
  v2          1536.7s   +39.2%
  v10d        1542.3s   +39.7%
  v10i        1590.9s   +44.1%
  v10f6       1937.7s   +75.5%   (worst)

All final_rules: 863186 in every variant ✓ (same convergence state)
All > primary baseline: True ✓
All > baseline_v2 (1023.0s): True ✓
```

Range: 1409.2s – 1937.7s. Experimenter's "v10f7 best: 1409.2s; v10f6 worst: 1937.7s" confirmed.

**Effect vs baseline variance**: minimum overhead = 1409.2 − 1103.8 = 305.4s. Baseline timing variance = 80.8s. Effect is **3.8× the baseline variance**. The negative result is robust — it cannot be explained by system timing noise.

### Percentage arithmetic check

Experimenter/routing state "+27.6% slower" for v10f7.
Computed: (1409.2 − 1103.8) / 1103.8 × 100 = **+27.7%** (routing uses +27.6% — minor rounding).

### Presentation and flags consistency

```
m23_mix.py:
  M23_INPUT = str(KB_DATA / "m23")        ← kbmag_v1/standalone/kb_data/m23
  KBMAG_BIN = ...kbmag_v1/.../kbprog
  RPO_CONFNUM = 5000; SLEX_CONFNUM = 5000

tests/m23_sweep.py:
  M23_INPUT = str(KB_DATA / "m23")        ← same file
  KBMAG_BIN = same kbprog binary
  RPO_CONFNUM = 5000
```

Both scripts use `kbmag_v1/standalone/kb_data/m23` (MD5: `05b90894b5ce0a350979fb8f122cbafa`) and the same kbprog binary with the same confnum. Baseline and all 18 variants use the same presentation — scope is clean.

**Note on preseed variants**: `m23_sweep.py` has some strategies (v6-type) that modify the input file via "preseed" (adding rules before start). None of the 18 confirmed result JSON files correspond to a preseed variant — all 18 use the standard `m23` input unchanged. Confirmed by checking desc strings and injection_history structure.

### Comparison to B(4,3)

The B(4,3) baseline converges at ~91s (22s cascade + ~70s confluence check per vault memory). B(4,3) mixing (80 rules injected at 20k RPO) brings cascade to ~16s total (~50× speedup in effective convergence time, ~21% total improvement). M23 shows the exact opposite: all 18 mixing variants increase wall time by 27–76%.

M23 converges at 863186 equations (vs B(4,3)'s 2333). The much larger M23 rule count means injection overhead (scoring, index build, rule transfer) occupies a greater fraction of total convergence time, and the injected shortlex rules do not reduce the M23 RPO cascade the way B(4,3) does.

## Verdict

**#status/replicated** — the M23 mixing negative result is confirmed across all 18 variants.

### Why this verdict (and why not #status/conjectured)

The routing suggested `#status/conjectured` for this finding. Per the Validator role's definitions:
- `#status/conjectured` = claimed but not verified (default for new claims)
- `#status/replicated` = multiple independent runs agree; not theoretically proven but no counterexample

I'm promoting to `#status/replicated` because:
1. I independently read all 18 JSON files — this is verification, not mere restatement of a claim.
2. 18 qualitatively different injection strategies all produce the same direction of effect (slower). This is multiple-run agreement in the spirit of "replicated."
3. Effect is 3.8× baseline variance — robust to timing noise.
4. Both baseline measurements (n=2) are faster than every mixing variant.

This is NOT `#status/proven` because: (a) no mathematical explanation of *why* injection overhead dominates for M23 but not B(4,3); (b) n=1 per variant (no repeated trials per strategy).

### What remains open

- Why does M23 mixing slow convergence while B(4,3) mixing accelerates it? Hypothesis: M23 has a much longer convergence trajectory (863k equations vs 2333), so injection overhead is not amortized. The shortlex rules injected into the RPO agent may also not be structurally useful for M23's RPO cascade pattern. This is `#status/conjectured` and requires theoretical investigation.
- Could a fundamentally different strategy (e.g., pre-seeding rather than live injection) help M23? The v6 preseed variants were not run to completion in the archived results. Open.
- n=1 per strategy is the limiting factor for stronger claims. A second run of v10f7 (the best variant) would cost ~1409s and would meaningfully upgrade confidence.

## Notes for downstream agents

- **For Lead**: Experimenter's §4 M23 numbers are accurate. The negative result is genuine, not an inventory error. Safe to document as `#status/replicated` in the per-family M23 vault doc (Phase C).
- **Percentage correction**: The routing/inventory state "+27.6% slower" for v10f7 — correct computation is +27.7%. Trivial rounding; no action needed.
- **Baseline note**: Two baseline measurements exist (1103.8s and 1023.0s). The inventory mentions only 1103.8s. The Phase C M23 doc should mention both and note the 7.9% timing variance.
- **For Researcher**: This negative result is a clean entry for the algorithm-performance section: "overlap-scored rule injection consistently slows M23 KB convergence (18/18 strategies, +28% to +76% overhead, n=1 per variant)."
