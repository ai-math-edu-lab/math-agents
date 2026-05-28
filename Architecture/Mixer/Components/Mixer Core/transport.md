---
title: transport
path: mixer-core/src/transport/
domain: infra
hot_path: false
status: draft
author: maumayma
project: mixer-core
public_api:
  - "trait Transport: get_state, get_items, inject, is_alive, shutdown"
  - "StdioTransport::spawn(command, args) — JSON-lines over child stdin/stdout"
  - "KbmagLegacyTransport::spawn(KbmagConfig) — file I/O + SIGUSR1 for kbprog processes"
invariants:
  - id: shutdown-idempotent
    summary: "transport.shutdown() must be safe to call multiple times and must not panic even if the child process is already dead."
    why: "Mixer::run() calls shutdown() on all agents unconditionally at the end of the loop, regardless of whether the agent died on its own or was still running. An idempotent shutdown prevents double-kill panics and ensures clean teardown even on error paths."
  - id: json-lines-protocol
    summary: "StdioTransport sends one JSON object per line on stdin, reads one JSON response per line on stdout. No framing bytes, no length prefix. Agents must not write partial lines."
    why: "serde_json::from_str() parses a complete line. A partial write (e.g., a Python agent that uses print() without flush, or writes a multi-part message) leaves a dangling read_line() call. The transport has no timeout on read_line(); a hung agent silently blocks the mixer."
  - id: kbmag-legacy-file-io
    summary: "KbmagLegacyTransport communicates with kbprog via the file system and SIGUSR1, not via stdin/stdout. get_items() reads the .kbprog.live file; inject() writes rules to a file and sends SIGUSR1."
    why: "kbprog predates the JSON-lines protocol and does not speak it. The legacy transport is an adapter that makes kbprog look like a Transport to the mixer. It shares no code path with StdioTransport."
related:
  - mixer-core-engine
  - scheduler
  - kbmag-source
tags: [agent/dev, user/maumayma, domain/infra, project/mixer-core, status/draft]
---

# transport — agent I/O abstraction

## What it is

The `transport/` subsystem defines the `Transport` trait and two implementations: `StdioTransport` (JSON-lines over child process stdin/stdout) and `KbmagLegacyTransport` (file I/O + SIGUSR1 for kbprog processes). The Transport trait is the boundary between the mixer's orchestration logic and the agent processes.

## Why it exists

The mixer needs to communicate with two fundamentally different kinds of agents: custom Python agents that speak the JSON-lines protocol, and legacy `kbprog` processes that use their own file-based interface. By hiding both behind a single `Transport` trait, the mixer engine is agnostic about the underlying communication mechanism. New agent types can be supported by implementing Transport without touching the orchestration loop.

## How it fits in the system

```
Mixer::run()
  → transport.get_state()   ← called every poll_interval for each agent
  → transport.get_items()   ← called when a directive fires
  → transport.inject(items) ← called when a directive fires, after transform
  → transport.shutdown()    ← called unconditionally at end of run
```

Each agent in the mixer has exactly one transport. The transport owns the child process (or its handle) for the duration of the run.

## Critical invariants — why each one exists

### shutdown-idempotent

`StdioTransport::shutdown()` drops `self.writer` (sending EOF to child stdin) and polls `child.try_wait()` with a 5-second timeout before calling `child.kill()`. If the child already exited, `try_wait()` returns `Ok(Some(_))` immediately and the function returns `Ok(())` without attempting a second kill. The `Drop` impl also calls `child.kill()` as a safety net for panic unwind. The two-level shutdown is safe because POSIX kill() on an already-dead process returns ESRCH, not a panic.

### json-lines-protocol

`StdioTransport::request()` serializes a `Request` to a single line (`writeln!`), flushes, then calls `reader.read_line()`. The mixer and agent must both follow the convention that each message fits on one line with no embedded newlines. Python agents using `json.dumps()` + `print()` with `flush=True` satisfy this. The transport does not validate that the response matches the request type beyond pattern matching on the enum variant.

### kbmag-legacy-file-io

`KbmagLegacyTransport` spawns kbprog and starts a background thread that reads kbprog's stdout to extract iteration/state information (rule count, confluence status). `get_items()` reads the `.kbprog.live` file from disk. `inject()` appends rules to an injection file and sends SIGUSR1 to the kbprog process to trigger a reload. This is a port of `api/kbmag_agent.py:KBMAGAgentV2`. The mechanism is specific to kbprog's injection protocol and is not reusable for other agent types.

## Transport trait

```rust
pub trait Transport: Send {
    fn get_state(&mut self)             -> Result<AgentState>;
    fn get_items(&mut self)             -> Result<Vec<Item>>;
    fn inject(&mut self, items: &[Item]) -> Result<usize>;
    fn is_alive(&self)                  -> bool;
    fn shutdown(&mut self)              -> Result<()>;
}
```

`is_alive()` is `&self` (non-mutating) because the mixer calls it while also holding mutable references elsewhere. In `StdioTransport`, aliveness is approximated by `self.writer.is_some()` — a heuristic that may lag the actual process state by one poll cycle.

## StdioTransport

Spawns a child with `Command::new(command).args(args).stdin(Stdio::piped()).stdout(Stdio::piped())`. On Unix, sets `process_group(0)` so the child is in its own process group — SIGINT from Ctrl-C goes to the mixer only, not directly to the child. The child is expected to react to EOF on stdin as its shutdown signal.

The JSON-lines wire protocol is defined in `protocol/messages.rs`:
- Requests: `GetState`, `GetItems`, `Inject { items }`
- Responses: `State { iteration, item_count, is_complete, metadata }`, `Items { items }`, `InjectAck { accepted, rejected }`, `Complete { success, metadata }`

## KbmagLegacyTransport

Config: `KbmagConfig { ordering, binary, input_file, state_dir, tidyint, maxeqns, maxstates, confnum, extra_flags, name }`.

Ordering flags supported: `shortlex`/`lex` → `-lex`; `recursive`/`rec` → `-rec`; `rtrec` → `-rtrec`; `wtlex` → `-wtlex`; `wreath` → `-wreath`.

Internal state tracked from kbprog stdout: `iteration`, `item_count` (rule count), `states_count`, `elapsed_secs`, `is_complete`, `is_confluent`, `is_checking_confluence`. This state is updated by a background reader thread and exposed via `get_state()`.

## Related

- [[mixer-core-engine]] — owns and calls transports; defines the poll loop
- [[kbmag-source]] / [[kbmag-v1]] — the kbprog processes that KbmagLegacyTransport wraps
- [[pyo3-bindings]] — Python agent types (KbmagAgent, StdioAgent) configure the transport at build time
