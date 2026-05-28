---
title: mixer-core-engine
path: mixer-core/src/mixer/
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "Mixer::run() -> Result<MixerResult> — start the orchestration loop; can only be called once"
  - "MixerBuilder — fluent builder: .agent(), .edge(), .scheduler(), .terminate_when(), .build()"
  - "MixerResult — { elapsed: Duration, reason: FinishReason, agent_states, events }"
  - "AgentId = String, Item = serde_json::Value"
  - "AgentState { iteration: u64, item_count: u64, is_complete: bool, metadata: Value }"
invariants:
  - id: run-once
    summary: "Mixer::run() takes ownership of the agent factories via Option::take() and panics (returns Err) if called a second time."
    why: "Agent factories are consumed when spawning processes — each factory closure moves data into the spawned transport. After run(), the agents map holds the live transports. Calling run() again would find factories = None and return a Config error. A Mixer is a single-use object."
  - id: per-agent-run-dir
    summary: "Agents receive a timestamped per-run directory path when spawned. The directory is created by experiment::make_run_dir() if not set via with_run_dir()."
    why: "Each kbprog agent writes its .kbprog.live rule file into this directory. Without a unique per-run directory, successive runs would clobber each other's outputs. The directory path is passed to each AgentFactory closure, which creates the per-agent subdirectory within it."
  - id: sigint-clean-shutdown
    summary: "Mixer::run() installs a SIGINT handler that sets SIGINT_RECEIVED and breaks the poll loop, then restores the previous handler on exit."
    why: "Ctrl-C during a multi-hour run should shut down agents cleanly rather than leaving kbprog processes running as orphans. The handler is installed per-run and always restored, even on error paths."
  - id: transform-required-for-edge
    summary: "Every edge registered via .edge() must have a corresponding transform registered. A missing transform causes execute_directive() to return MixerError::Config."
    why: "The mixer routes items through transforms, not directly. If an edge has no transform, the directive cannot be executed. The error surfaces at runtime rather than build time, so callers must ensure every edge has a transform."
related:
  - scheduler
  - transport
  - pyo3-bindings
  - mixer-core-engine
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# mixer-core-engine — the Mixer orchestrator

## What it is

The `mixer/` subsystem provides `Mixer` (the orchestration loop), `MixerBuilder` (fluent construction), and `MixerResult` (the run output). It is the central coordinator: it owns agent transports, drives the scheduler on each tick, executes injection directives by calling transforms, and maintains an event log.

## Why it exists

Multi-agent KB experiments require a control loop that polls agent states at regular intervals, decides when to inject (via a scheduler), retrieves items from source agents, transforms them, and injects them into target agents. Without this loop, experiment scripts wrote their own poll-sleep-inject loops — duplicated across every experiment with subtle differences in shutdown, error handling, and SIGINT behavior. `Mixer` standardises this loop.

## How it fits in the system

```
Experiment script (Python or Rust)
  → MixerBuilder: register agents (factories), edges (transforms), scheduler, termination
  → Mixer::run():
      1. Create run dir; spawn agent transports
      2. Install SIGINT handler
      3. Poll loop (every poll_interval):
           a. transport.get_state() for each agent → AgentState
           b. termination predicate? → break if yes
           c. all agents dead? → break
           d. scheduler.tick(states, elapsed) → Vec<InjectDirective>
           e. execute_directive: get_items from source → transform → inject to target
           f. emit MixerEvent::Tick
      4. Shut down all transports (idempotent)
      5. Return MixerResult { elapsed, reason, agent_states, events }
```

## Critical invariants — why each one exists

### run-once

`agent_factories` is stored as `Option<Vec<...>>` in `Mixer`. `run()` calls `self.agent_factories.take()`, consuming it. A second call gets `None` and returns `MixerError::Config("Mixer::run() can only be called once")`. This is by design: factories are closure-based and may capture mutable external state. Re-using them would be incorrect.

### per-agent-run-dir

`experiment::make_run_dir(&self.root_dir)` creates a timestamped directory like `runs/2026-05-22T13:00:00/`. Each agent factory receives this path and creates `run_dir/<agent_id>/` for its working files. The `KbmagLegacyTransport` places `<agent_id>.kbprog.live` there. The path is also recorded in the experiment log to stderr.

### sigint-clean-shutdown

The mixer uses `nix::sys::signal::sigaction` to install a handler that sets `SIGINT_RECEIVED: AtomicBool`. The poll loop checks this flag at the top of every iteration. On break, the shutdown code calls `transport.shutdown()` for all agents, which drops stdin (sending EOF to kbprog) and waits up to 5 seconds for exit. The old signal action is restored with a `sigaction` call in the same cleanup block.

### transform-required-for-edge

`execute_directive` looks up `self.edges.get_mut(&(from, to))` and returns `MixerError::Config` if absent. There is no default pass-through transform. This is intentional: the mixer is unopinionated about what "transfer items" means — callers must supply a domain-specific transform (overlap scoring, filtering, etc.).

## Public surface

From Rust:
```rust
let mixer = MixerBuilder::new(root_dir, poll_interval, timeout)
    .agent("rpo", |run_dir| Ok(Box::new(KbmagLegacyTransport::spawn(config)?)))
    .edge("slex", "rpo", make_kb_burnside_transform(expansion_map))
    .scheduler(Box::new(ThresholdScheduler::new(config)))
    .terminate_when(Box::new(|states, elapsed| { ... }))
    .build()?;
let result = mixer.run()?;
```

From Python: see [[pyo3-bindings]] — the Python `Mixer` class wraps `MixerBuilder` directly.

## Types

- `AgentId = String` — agent name string, used as key everywhere
- `Item = serde_json::Value` — opaque JSON; the mixer never inspects it
- `AgentState` — `{ iteration, item_count, is_complete, metadata: Value }` — the state poll contract
- `MixerResult` — `{ elapsed, reason: FinishReason, agent_states: HashMap<AgentId, AgentState>, events: Vec<MixerEvent> }`
- `FinishReason` — `AllComplete | Timeout | Predicate { reason: String } | Error`
- `MixerEvent` — `Started | Tick | Injection | AgentComplete | Finished | Error`

## Related

- [[scheduler]] — the `Scheduler` trait consumed by `Mixer::run()`; provides `InjectDirective`s each tick
- [[transport]] — the `Transport` trait; one instance per agent, wraps the subprocess I/O
- [[pyo3-bindings]] — Python `Mixer` class that constructs `MixerBuilder` and calls `run()`
