---
title: KBMag results — B(5,3)
domain: group-theory
project: b53
instance: B(5,3)
experiment_type: kbmag
status: inconclusive
reconstructed_on: 2026-06-02
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/knuth-bendix, topic/kbmag, topic/mixer, project/b53, status/inconclusive, results]
---

# Results — KBMag on B(5,3)

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | RPO at capture | Shortlex at capture | Validated by |
|---|---|---|---|---|---|---|---|
| b53-server-v2 | ~2026-04 | threshold=100k, batch_frac=0.001, periodic=600s, cn=5000 | **In-progress / PLATEAU** | 97h+ (349,540s at last confirmed capture) | **11,714,026 rules** | **41,846,556 rules** | None — not converged |

## Trajectory

| Time | RPO rules | Shortlex rules | RPO phase | Events |
|---|---|---|---|---|
| t=10s | 101,550 | 360,577 | — | First injection (101 rules) |
| t=908s | 858,420 | 1,601,251 | — | Event #2 (8,584 rules) |
| t≈45h | ~8,000,000 | ~8,000,000 | — | (45h log capture) |
| t=97h (349,540s) | 11,714,026 | 41,846,556 | **PLATEAU** | Event #500 (11,712 rules; 92.9s scoring) |
| t≈144h (501,400s) | ~14,450,000 | — | PLATEAU | Event (14,444 rules injected) |

**PLATEAU definition**: EMA-smoothed net growth rate sustained near-zero (±0.03%) for 2800+ consecutive measurements.

## Phase trajectory

- **0–45h**: EXPLORATION — RPO grows monotonically from 0 to ~8M rules. Mixing injections continue every ~600s but do not change the growth trajectory.
- **45–97h+**: PLATEAU — RPO growth rate decays to +0.02–0.03% per period. Neither EXPLOITATION (net negative growth) nor any cascade observed.

**Contrast with B(4,3)**: B(4,3) RPO reaches ~21k rules in ~3s, then cascades to 2333. B(5,3) RPO passes 11.7M rules after 97h with no cascade. The rule count ratio at PLATEAU is ~5000× larger. Whether a cascade threshold exists for B(5,3) under this mixing strategy is unknown.

## Version history

**v7/v8** (archived in `old/v7_v8.zip`): Earlier strategies, details inside archive.

**v10 scored**: Overlap-scored injection, threshold=100k, batch proportional. Ran on server for 97h+ with no convergence.

**v10 scored v2**: Same as v10 but with `CachedPreparer` for incremental scoring. Confirmed PLATEAU at 97h. This is the primary result.

## Main findings

1. **No convergence in 97h**: B(5,3) does not converge under overlap-scored mixing at these parameters in 97h of server time. This is the primary result.

2. **PLATEAU, not divergence**: The rule bank does not explode — it stabilizes at ~+0.02% growth rate. Mixing is suppressing runaway growth but not triggering a cascade.

3. **Injection rate grew with bank size**: By event #500 at 97h, each injection was injecting ~11,712 rules (vs. 101 at event #1), and scoring time was 92.9s. The injection machinery scales poorly with bank size.

4. **B(5,3) vs B(4,3) scale**: B(4,3) converges at 2333 rules. B(5,3) at 97h has 11.7M RPO rules — no convergence in sight. The problem size may require a fundamentally different strategy (see [[Rust Bidirectional/_type]]).

## Open questions

1. Is there a cascade threshold for B(5,3) under RPO? Reached >14.5M rules at 144h with no cascade. If a threshold exists, it is at >14.5M RPO rules.

2. Would a larger cn value (cn=100k, as used for B43) change the trajectory? The B53 run used cn=5000. The cn=100k optimization was instrumental for B43; its effect on B53 is unknown.

3. The Rust Bidirectional approach (4 orderings, dynamic conjugation) proves 144/153 words — does it scale to full KB closure? See [[Rust Bidirectional/results/rust-bidirectional-results-b53]].

## Related material

- [[KBMag/_type]] — parent experiment-type
- [[B53/_progress]] — B(5,3) umbrella
- [[data/kbmag-data-b53]] — parameter details, run locations
- [[methodology/kbmag-overlap-scoring-b53-2026-06-02]] — methodology, hypothesis
- [[B43/KBMag/results/kbmag-results-b43]] — B(4,3) convergent contrast
- [[2026-06-02-non-b25-forensic-inventory]] — §2 B53 forensic provenance
