---
title: "KB Mixing — Stagnation Metric and Rule Injection Protocol"
domain: methodology
project: mixer-core
status: validated
author: maumayma
related:
  - "[[algo-mixing-burnside-slides]]"
  - "[[mixable-api]]"
introduced_in:
  - "[[Research/Algorithm Cooperation/algo-mixing-burnside-slides]]"
appears_in:
  - "[[Research/Algorithm Cooperation/algo-mixing-burnside-slides]]"
  - "[[Research/Group theory/Burnside groups/B25/kalika-2026]]"
related_concepts:
  - "[[mixable-api]]"
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/knuth-bendix
  - topic/mixer
  - concept
  - status/validated
---

# KB Mixing — Stagnation Metric and Rule Injection Protocol

Extracted from [[algo-mixing-burnside-slides]] (Stepanov & Matveeva). The operational protocol for KB-based Mixer agents: how stagnation is measured, when injection fires, and how rules are transferred between orderings.

## Stagnation metric (verbatim)

$$\text{stagnation}(t) = \frac{\Delta\text{rules}_{\text{after tidy}}(t)}{\text{total\_rules}(t)}$$

**Critical implementation note:** Measure **after tidying**, not before. Raw rule count can grow (rules added from critical pairs) while making no real progress (most are immediately subsumed by existing rules). A bloated rule set without post-tidy growth is not progress.

**Threshold:** If stagnation(t) < ε for k consecutive iterations, trigger injection from the other agent.

## The mixing recipe (verbatim from deck)

```
1. Run RPO and Shortlex in parallel
2. Apply tidying
3. On stagnation:
   - Pass rules from the other ordering to a stagnating one
   - Tidy the new rules
   - Continue
4. Repeat until confluent
```

## Rule injection (cross-pollination)

When switching, inject rules from the other agent's current rule set:

$$R_{\text{new}} = R_{\text{current}} \cup \text{reorient}(R_{\text{other}}, \text{ordering}_{\text{current}})$$

**reorient()** flips the direction of rules that the new ordering would orient differently. A rule `l → r` under shortlex (where `l` is shortlex-larger) becomes `r → l` under RPO (if RPO orients it the other way), then is retidied.

**Why injection works:**
- Shortlex finds rules RPO misses (and vice versa).
- Injected rules "unstick" the completion by introducing new critical pairs in the stagnating agent's search space.
- Both orderings contribute to the final system.

## Observed dynamics in B(4,3) overnight run

From the breakthrough experiment log (see [[algo-mixing-burnside-slides]] § Breakthrough):

| Time | r2l_rpo_loop | rpo_iter | Event |
|---|---|---|---|
| 5m | 160,060 rules, stag=0.03 | 4,088 rules, stag=0.14 | r2l exploding, rpo stagnating |
| 10m | 221,061 rules, stag=0.23 | 2,949 rules, stag=0.04 | rpo received rules from r2l, shrinking |
| 15m | 60,035 rules, stag=0.08 | 2,543 rules, stag=0.04 | r2l received rules from rpo, contracting |
| 20m | 4,415 rules, stag=0.03 | 2,432 rules, stag=0.03 | both converging |
| 25m | 2,562 rules, stag=0.03 | **2,333 rules, complete=True** | rpo first to complete |

Both agents converged to the **same** 2,333 rules. 54 rule-sharing events over 33 minutes.

The "explosion then contraction" pattern in r2l is characteristic: a large intermediate rule set is pruned by tidying after rpo's rules are injected.

## Ordering choices

The deck describes two orderings used:
- **Shortlex (length-lexicographic):** shorter < longer, then left-to-right on tied lengths. Tends to produce more rules (822 for B(2,4) vs 159 for RPO) but explores different regions.
- **RPO (Recursive Path Ordering):** right-to-left, based on term structure. Tends to produce fewer rules, faster convergence when it works.
- **r2l_rpo_loop:** a variant of RPO. The "r2l" indicates right-to-left orientation; "loop" may indicate a specific iteration strategy. (Exact semantics: check `mixer-core/CLAUDE.md`.)
- **rpo_iter:** the standard RPO iterative completion.

## Tidying: why it must precede stagnation measurement

The deck emphases this explicitly:

> "**This must happen before stagnation checking!** A bloated rule set looks like progress but isn't."

The tidy step:
1. **Interreduce:** apply rules to each other's RHS (eliminate redundant RHS structure)
2. **Remove redundant:** delete rules whose LHS is reducible by other rules
3. **Reorient:** some rules may now orient differently under the current ordering

Post-tidy rule count is the authoritative measure of completion progress.

## Connection to v10 experiments (B(4,3))

The MEMORY.md records a later, more refined version of this approach: v10d "live 2-agent batch size sweep" with specific injection trigger at RPO reaching 20,000 rules and a batch size of 80 (13.7s ±0.1s cascade). That experiment refines the "share every 10 iters" schedule from the overnight run into a threshold-based trigger. The overnight run protocol and the v10 protocol are both instances of this general injection framework.

## Cross-references

- [[algo-mixing-burnside-slides]] — source of this protocol description; also contains the complete overnight run log.
- [[mixable-api]] — the API that formalizes `inject()` and `export()` as first-class operations.
