---
title: "Mixable API — The mixer_core Agent Protocol (Rust specification)"
domain: methodology
project: mixer-core
status: validated
author: maumayma
related:
  - "[[algo-mixing-burnside-slides]]"
  - "[[kb-mixing-stagnation]]"
  - "[[grobner]]"
introduced_in:
  - "[[Research/Algorithm Cooperation/algo-mixing-burnside-slides]]"
appears_in:
  - "[[Research/Algorithm Cooperation/algo-mixing-burnside-slides]]"
  - "[[Research/Algorithm Cooperation/grobner]]"
related_concepts:
  - "[[kb-mixing-stagnation]]"
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/mixer
  - concept
  - status/validated
---

# Mixable API — The mixer_core Agent Protocol

Extracted from [[algo-mixing-burnside-slides]] (Stepanov & Matveeva). The formal interface specification that any algorithm must satisfy to participate in Mixer cooperation. This is the design contract, not the implementation — the Rust trait specifies what each algorithm must expose.

## The Trait (verbatim from deck)

```rust
trait Mixable {
    type State;           // Internal state
    type Artifact;        // Shareable knowledge (rules, polynomials, ...)

    fn step(&mut self) -> Metrics;        // Run one iteration
    fn export(&self) -> Vec<Artifact>;    // What can we share?
    fn inject(&mut self, artifacts: Vec<Artifact>);  // Accept external knowledge
    fn is_complete(&self) -> bool;        // Are we done?
}

struct Metrics {
    progress: f64,        // How much progress this step?
    stagnation: f64,      // Are we stuck?
    artifacts_count: usize,
}
```

## Key design properties

**Artifacts must be transformable across algorithms.** The deck specifies three cases:
- KB rules → reoriented for a different word ordering (e.g., shortlex rules → RPO-oriented)
- Gröbner basis polynomials → reduced w.r.t. a new monomial order
- Cross-algorithm: rules ↔ polynomials "when applicable" (see [[grobner]] for the theoretical basis)

**Metrics enable intelligent coordination:**
- `stagnation` high → request help from other agents (see [[kb-mixing-stagnation]] for how stagnation is computed)
- `progress` high + `artifacts_count` high → share artifacts with others
- Convergence (`is_complete()`) → other agents should adopt our artifacts

**The Mixer orchestrates; algorithms compute.** The Mixer calls `step()`, reads `Metrics`, decides when to call `export()` on one agent and `inject()` on another. Individual agents do not communicate directly.

## Invariants implied by the design

1. `export()` must be side-effect-free — it reads state, does not mutate it.
2. `inject()` may mutate State substantially (e.g., triggering a tidy pass in KB).
3. `is_complete()` returning `true` after an `inject()` call is valid — injected artifacts can cause immediate completion.
4. `step()` called on a complete agent is implementation-defined behavior (callers should check `is_complete()` first).

## Relationship to current implementation

The `mixer_core` Python/Rust codebase implements this protocol via the `mixer_core.Agent` pyo3 binding. The Rust trait above is the theoretical specification; the actual implementation may differ in names and signatures. Check `mixer-core/CLAUDE.md` for canonical current API surface.

## Cross-domain application

The deck explicitly lists Gröbner bases as a second algorithm type where the Mixable API applies:
- `Artifact` = polynomial over Q[T] (from the variety-of-representations ring Q_R in [[grobner]])
- `inject()` adds polynomials to the current ideal I_R and recomputes (or updates) the Gröbner basis
- `stagnation` = rate of new generator polynomials being added to the basis

This means the Mixer can in principle run KB completion and Gröbner basis computation simultaneously on the same group presentation, sharing discovered structure. The feasibility for B(2,5) is speculative — see [[grobner]] §known_issues.

## Cross-references

- [[algo-mixing-burnside-slides]] — source of this specification.
- [[kb-mixing-stagnation]] — the stagnation metric that drives coordination.
- [[grobner]] — the second algorithm family the deck proposes as a Mixable implementor.
