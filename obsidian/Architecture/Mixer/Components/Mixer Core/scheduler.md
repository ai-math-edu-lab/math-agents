---
title: scheduler
path: mixer-core/src/scheduler/
domain: infra
hot_path: true
status: draft
author: maumayma
project: mixer-core
public_api:
  - "trait Scheduler: tick(agents, elapsed) -> Vec<InjectDirective>"
  - "InjectDirective { from: AgentId, to: AgentId, max_items: usize }"
  - "ThresholdScheduler::new(ThresholdSchedulerConfig) — fires once when target item_count >= threshold"
  - "PeriodicScheduler::new(PeriodicSchedulerConfig) — threshold trigger + periodic re-injection"
  - "CompositeScheduler::new() + .add(scheduler) — composes multiple schedulers"
invariants:
  - id: tick-on-every-poll
    summary: "scheduler.tick() is called on every poll cycle — every poll_interval milliseconds (typically 5 ms). Implementations must return in microseconds."
    why: "The mixer's poll loop calls tick() before sleeping again. A blocking or slow tick() adds latency to every injection decision. All current implementations hold only in-memory state and do no I/O; new implementations must follow this constraint."
  - id: threshold-fires-once
    summary: "ThresholdScheduler sets a `fired: bool` flag after first firing and returns empty Vec on all subsequent ticks."
    why: "The B(4,3) injection pattern (inject once at 20k RPO rules) requires exactly one injection. Re-firing would inject the same source rules multiple times, causing rule bank instability (confirmed empirically: multiple injections are HARMFUL, introduce instability — see memory: v10c near-miss catastrophe)."
  - id: composite-union
    summary: "CompositeScheduler calls tick() on all inner schedulers and returns the union of their directives."
    why: "Multiple schedulers may fire on the same tick (e.g., two threshold schedulers for different agent pairs). The composite must not short-circuit after the first non-empty result; all inner schedulers see the same state snapshot."
related:
  - mixer-core-engine
  - transport
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# scheduler — injection scheduling for Mixer Core

## What it is

The `scheduler/` subsystem defines the `Scheduler` trait and three built-in implementations: `ThresholdScheduler`, `PeriodicScheduler`, and `CompositeScheduler`. The scheduler is the policy engine of the mixer: it observes agent states on each tick and returns `InjectDirective`s that tell the mixer what to transfer from which agent to which.

## Why it exists

Different experiments need different injection strategies:
- B(4,3): inject once when RPO reaches 20k rules (threshold)
- B(5,3)/B(2,5): inject periodically throughout the run
- Complex experiments: multiple thresholds for different agent pairs simultaneously

By making `Scheduler` a trait, experiments select the appropriate strategy by composing one or more scheduler instances. The mixer engine is agnostic about timing.

## How it fits in the system

```
Mixer::run() poll loop:
  → scheduler.tick(agent_states, elapsed)
  → Vec<InjectDirective>  ←  one per (from, to) pair that should fire now
  → execute_directive(directive): get_items(from) → transform → inject(to)
```

The scheduler sees `AgentState` (item_count, iteration, is_complete, metadata) but never sees the items themselves. It only decides whether to inject, not what to inject — that is the transform's job.

## Critical invariants — why each one exists

### tick-on-every-poll

`tick()` is a hot path: it runs every 5 ms for the lifetime of a multi-hour experiment. The implementations do only hash-map lookups and integer comparisons. Adding network I/O, disk I/O, or substantial computation would block the poll loop. New implementations should hold this contract.

### threshold-fires-once

The `ThresholdScheduler` pattern is the B(4,3) mixing pattern. The near-miss catastrophe (batch 200 at 20k caused full confluence check ~100s extra in 2/3 trials) showed that re-injecting at the same threshold point is harmful. The `fired` flag is set on first fire and never unset — the only way to get another injection is to create a new `ThresholdScheduler`. This is documented in the Python `ThresholdScheduler` docstring.

### composite-union

`CompositeScheduler` iterates all inner schedulers and extends a result vector:
```rust
fn tick(&mut self, agents, elapsed) -> Vec<InjectDirective> {
    self.schedulers.iter_mut()
        .flat_map(|s| s.tick(agents, elapsed))
        .collect()
}
```
The order of directives matters if multiple directives target the same agent — the mixer executes them in order. Callers composing multiple schedulers should be aware of this.

## Implementations

### ThresholdScheduler

Fires a single injection when `target.item_count >= threshold` AND `source.item_count >= min_source_items`. The B(4,3) optimal parameters: `threshold=20000, max_items=80, min_source_items=50`.

Config fields:
```rust
ThresholdSchedulerConfig {
    from: AgentId,  // source agent (rules come from here)
    to: AgentId,    // target agent (rules injected here)
    threshold: u64, // fire when target.item_count >= this
    max_items: usize,
    min_source_items: u64,
}
```

### PeriodicScheduler

Initial trigger: same threshold logic as ThresholdScheduler. After that, re-injects every `period` seconds. Batch size is `batch_fraction * target.item_count`, clamped to `[min_batch, max_batch]`.

The B(5,3)/B(2,5) pattern: threshold-trigger first injection, then sustained injection at `period=600s`.

### CompositeScheduler

Holds a `Vec<Box<dyn Scheduler>>`. Use when multiple (from, to) pairs or multiple strategies apply simultaneously. In Python: `CompositeScheduler.add_threshold(sched)` / `.add_periodic(sched)`.

## Public surface — Python API

```python
from mixer_core import ThresholdScheduler, PeriodicScheduler, CompositeScheduler

# Single threshold:
mixer.set_threshold_scheduler(
    ThresholdScheduler(from_agent="slex", to_agent="rpo",
                       threshold=20000, max_items=80, min_source_items=50)
)

# Composite:
cs = CompositeScheduler()
cs.add_threshold(ThresholdScheduler("slex", "rpo", threshold=20000, max_items=80))
cs.add_periodic(PeriodicScheduler("rpo2", "slex", threshold=10000, period_secs=300.0))
mixer.set_scheduler(cs)
```

## Related

- [[mixer-core-engine]] — calls `scheduler.tick()` in its poll loop
- [[transport]] — provides `AgentState` that scheduler observes
- [[pyo3-bindings]] — exposes Python scheduler classes
