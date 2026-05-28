---
tags: [meta, canvas-setup]
---

# Canvas Setup — Math (algo_mixing)

How to assemble the Maestri canvas for the Math / algo_mixing project. **Six persistent agents + on-demand spawns** for cross-domain experiments.

## Prerequisites (one-time)

Plus this vault adds:
- The `nuextract-cli` tool is **not yet installed**. Researcher knows to flag image-only PDFs to Lead until it exists. See [[ocr-tooling]].
- GAP (`/opt/homebrew/bin/gap` 4.15.1) and the `kbmag` GAP package are installed. Sage is **NOT** installed; if Validator needs Sage-specific tooling beyond what GAP provides, file the install through Lead → human.
- Note: agents must probe tool availability with `which <tool>` or equivalent before assuming a tool is missing. This vault's setup docs can drift.

## Step 1 — Create the canvas

1. Open Maestri.
2. New canvas → name it **`Math`** (or **`algo_mixing`** if you prefer the project name).
3. Save.

## Step 2 — Spawn six persistent agent terminals

For each:
1. Name and assign role (matching the role prompt at `<vault>/_meta/agents/<role>.md`).
2. Working directory: `/Users/maumayma/Desktop/reps/algo_mixing`.
3. Start `claude` in the terminal.
4. Model assignment:
   - **Lead** → Opus (reviewing across math + code + people needs the bigger model).
   - **Validator** → Sonnet (math claims require careful work but not opus-scale; upgrade if you see verdict quality slipping).
   - **Developer, Researcher, Experimenter, Experimenter-B25** → Sonnet.

Terminals:

| Terminal name | Role prompt | Notes |
|---|---|---|
| **Lead** | `math-lead` | Orchestrator + code-quality gate + commit ritual. Primary human interface. |
| **Researcher** | `math-researcher` | Multi-domain literature. Restructure authority over `Research/` and `Concepts/`. |
| **Developer** | `math-developer` | Rust + Python + framework/perf expertise. |
| **Experimenter** | `math-experimenter` | General + cross-domain Mixer applications (everything except B(2,5)). |
| **Experimenter-B25** | `math-experimenter-b25` | B(2,5) specialist. Always on. Owns `Experiments/Group Theory/Burnside Group/B25/**`. |
| **Validator** | `math-validator` | Independent math oracle. Math verdicts override all peers. |

## Step 3 — Load role prompts

### Approach A — Maestri Agent Roles (preferred)
For each role, create a Maestri Agent Role:
- `math-lead` ← `<vault>/_meta/agents/lead.md`
- `math-researcher` ← `<vault>/_meta/agents/researcher.md`
- `math-developer` ← `<vault>/_meta/agents/developer.md`
- `math-experimenter` ← `<vault>/_meta/agents/experimenter.md`
- `math-experimenter-b25` ← `<vault>/_meta/agents/experimenter-b25.md`
- `math-validator` ← `<vault>/_meta/agents/validator.md`

Assign each role to the matching terminal.

### Approach B — Per-session paste
On session start, tell each terminal:
```
Read the role definition at /Users/maumayma/Documents/Obsidian/Math/_meta/agents/<role>.md. This is your operating doctrine — adhere to it strictly.
```

## Step 4 — Sticky note: project context

Create a sticky note named **`math-context`** connected to **all six** terminals. Paste:

```
# Math (algo_mixing) canvas context

Vault: /Users/maumayma/Documents/Obsidian/Math
Repo:  /Users/maumayma/Desktop/reps/algo_mixing
Branch: main (working: feat/* fix/* chore/*)

Read on session start (your role + shared):
- Role: /Users/maumayma/Documents/Obsidian/Math/_meta/agents/<role>.md
- Shared: /Users/maumayma/Documents/Obsidian/Math/_meta/agents/_common.md
- Mission: /Users/maumayma/Documents/Obsidian/Math/_meta/mission.md
- Tags: /Users/maumayma/Documents/Obsidian/Math/_meta/tags.md (6-axis taxonomy)
- Experiment convention: /Users/maumayma/Documents/Obsidian/Math/_meta/experiment-folder-convention.md
- Repo README: /Users/maumayma/Desktop/reps/algo_mixing/README.md  ← extensive, read it

Terminology: "agent" without qualifier = AI agent (you, one of six). "mixer Agent" = algorithm subprocess. Don't conflate.

Six AI agents on canvas:
- Lead (orchestrator + code review + commit)
- Researcher (multi-domain literature + restructure authority)
- Developer (Rust + Python + framework + perf)
- Experimenter (everything except B(2,5))
- Experimenter-B25 (B(2,5) specialist, exclusive owner of that subtree)
- Validator (math oracle; verdicts override all peers except human)

Topology: hub-and-spoke through Lead. Exception: Validator's #status/disproven verdict overrides immediately without Lead routing.

Commit policy: ONLY Lead commits, ONLY after explicit per-action human approval (commit, push, dep add, mixer protocol change, on-disk format change, math-touching code requires Validator verdict too).

Maestri CLI:
- maestri list
- maestri ask "<Name>" "..."
- maestri check "<Name>"
- maestri note read/write/edit "<note>"
```

## Step 5 — Connect terminals (full mesh)

Multi-Experimenter and Validator-as-oracle benefit from direct lines. Wire as a full mesh:

- Lead ↔ each of the other five
- Researcher ↔ each Experimenter (Researcher feeds them syntheses)
- Researcher ↔ Validator (literature checks during verification)
- Researcher ↔ Developer (read-only Q&A on framework grounding)
- Developer ↔ each Experimenter (when patches enable new experiments)
- Developer ↔ Validator (Validator can request tests Developer should add)
- Experimenter ↔ Experimenter-B25 (peer coordination when methodologies overlap)
- Experimenter ↔ Validator (every math claim routes here)
- Experimenter-B25 ↔ Validator (every B(2,5) math claim — heavy traffic)

Behavioral rules (in prompts) keep work-changing requests through Lead. Direct lines are for read-only Q&A and verdict routing.

## Step 6 — On-demand terminals

When Researcher identifies a viable new cross-domain Mixer application, spawn a per-domain Experimenter:

- Name: `Experimenter-<domain>` (e.g. `Experimenter-Grobner`, `Experimenter-Biology`).
- Role: use `math-experimenter` (the general role) — the per-domain focus comes from the brief Lead gives them.
- Working dir + model: same as the general Experimenter.
- Connect to Lead, Researcher, Validator (mesh).
- Shut down when the cross-domain exploration concludes (validated / rejected / paused).

These are temporary terminals. The persistent six handle the long-lived workflows.

## Step 7 — Per-user Agents dir

The `Agents/` tree is **per-user** to keep colleagues from colliding on log files. Before first canvas use, ensure `Agents/<your-handle>/` exists with the six role subdirs:

```bash
cd /Users/maumayma/Documents/Obsidian/Math/Agents
mkdir -p <your-handle>/{Lead,Researcher,Developer,Experimenter,Experimenter-B25,Validator}
# Each role dir gets its own log.md, scratch/, etc. as the agent uses them.
```

Maria's tree is at `Agents/maumayma/`. Each colleague gets their own subtree when they join the canvas. The role prompts in `_meta/agents/*.md` use `Agents/<your-user>/<role>/` paths — they auto-resolve to the correct subtree based on which user's session is active.

## Step 8 — Verify

In each terminal: `maestri list` should show 5 peers + the `math-context` note (plus on-demand terminals when present).

Then: *"Cold-start handshake."* Each terminal should respond with a single short message naming its role, listing peers, and saying it's standing by. **No other action.** If it tries to write logs, do experiments, or send unsolicited messages, the role prompt didn't load — re-paste.

## Step 9 — First flow

Your primary terminal is **Lead**. Talk to Lead in natural language:

- *"Ask Researcher to scan recent literature on Buchberger's algorithm with cooperation — looking for a Mixer fit in Gröbner."*
- *"Developer should add a `ShortlexAgent` mixer Agent for Burnside KB. Tests required, Validator will review the math layer."*
- *"Experimenter-B25, what's in `_progress.md` right now? Next experiment shortlist?"*
- *"Ask Validator to verify claim X from yesterday's experiment with GAP."*

Lead delegates, gates, and pings you when a decision is needed.

## Permissions reminder

Both vaults' Write/Edit allow rules in `~/.claude/settings.json`:
```
"Write(/Users/maumayma/Documents/Obsidian/Math/**)"
"Edit(/Users/maumayma/Documents/Obsidian/Math/**)"
```
Plus `additionalDirectories` includes the Math vault. Restart any active Claude Code session if you change settings.

## Troubleshooting

Same as BOTBOTBOT's canvas-setup. If you don't see a base file render in Obsidian, check the YAML quoting in the `.base` file (most common issue — strings with colons need quotes).
