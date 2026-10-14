---
tags: [meta, canvas-setup]
---

# Canvas Setup — Math

How to assemble the Maestri canvas for the Math vault's research program. **Seven persistent agents + on-demand spawns** for cross-domain experiments. The roles are architecture-neutral: per-project repos, commands and conventions come from project profiles (`_meta/projects/`) and the dependency registry (`_meta/dependencies/`) — see [[projects-and-dependencies-convention]].

## Prerequisites (one-time)

Plus this vault adds:
- The `nuextract-cli` tool is **not yet installed**. Researcher knows to flag image-only PDFs to Lead until it exists. See [[ocr-tooling]].
- Tool state per machine is recorded in the dependency notes (e.g. [[dep-gap]]: GAP 4.15.1 + `kbmag` package on maumayma's machine; [[dep-sage]]: Sage **NOT** installed there); if Validator needs Sage-specific tooling beyond what GAP provides, file the install through Lead → human.
- Each human records their local checkouts (vault, code repos) under `## Math vault — local checkouts` in their own `~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` — see [[projects-and-dependencies-convention]] § Local checkouts.
- Note: agents must probe tool availability with `which <tool>` or equivalent before assuming a tool is missing. This vault's setup docs can drift.

## Step 1 — Create the canvas

1. Open Maestri.
2. New canvas → name it **`Math`**.
3. Save.

## Step 2 — Spawn seven persistent agent terminals

For each:
1. Name and assign role (matching the role prompt at `<vault>/_meta/agents/<role>.md`).
2. Working directory: the code workspace you use most (e.g. your checkout of the experiments repo). Agents switch repos per the project profile named in each brief.
3. Start `claude` in the terminal.
4. Model assignment (owner, 2026-10-14). The advisor is Claude Code's `advisorModel` setting, a stronger reviewer the agent consults before and after substantive work.

   | Terminal | Model | Advisor |
   |---|---|---|
   | **Lead** | Opus 5.5 (`claude-opus-5-5`) | Fable |
   | **Experimenter**, **Experimenter-B25** | Opus 5.5 | Fable |
   | **Validator** | Opus 5.5 | Fable |
   | **Developer** | Sonnet 5.5 (`claude-sonnet-5-5`) | Fable |
   | **Researcher** | Sonnet 5.5 | none |
   | **Math Expert** | Fable (`fable`) | default |

   **How to apply.** Claude Code reads project settings from the **git root**, not from the folder a terminal starts in, so a settings file in a role folder is ignored unless passed explicitly. Maestri starts each role's terminal in its role folder `<repo>/.maestri/roles/<role-id>/` (gitignored; `role.json` there names the role). Put the role's settings in `.claude/settings.local.json` in that folder, e.g. `{ "model": "claude-opus-5-5", "advisorModel": "fable" }` (no advisor: `"advisorModel": ""`; `null` is rejected), and start the agent with `claude --settings .claude/settings.local.json`. Lead's file is `<repo>/.maestri/lead/settings.json` (`claude --settings .maestri/lead/settings.json` from the repo root). **Do not** put a `settings.local.json` in `<repo>/.claude/`: every agent inherits it.
   - **Restart** (to apply): `/exit`, then `claude --settings <file>` for a fresh session; the agent re-orients from the vault. `claude --continue` keeps the conversation but also keeps the old session's **model** (the advisor does follow the file).
   - **Don't** fix a running agent's model with `/model`: it also overwrites `"model"` in the user-wide `~/.claude/settings.json`. Likewise `/advisor off` changes the user-wide advisor. Check with `/status`.

Terminals:

| Terminal name | Role prompt | Notes |
|---|---|---|
| **Lead** | `math-lead` | Orchestrator + code-quality gate + commit ritual. Primary human interface. |
| **Researcher** | `math-researcher` | Multi-domain literature. Restructure authority over `Research/` and `Concepts/`. |
| **Developer** | `math-developer` | Implementation in each project's stack + framework/perf expertise. |
| **Experimenter** | `math-experimenter` | General + cross-domain experiments: everything except the B(2,5) program owned by Experimenter-B25. `#project/challenge-gen` work, B(2,5) challenge generation included, belongs here or to a spawned `Experimenter-ChallengeGen` (Step 6). |
| **Experimenter-B25** | `math-experimenter-b25` | B(2,5) specialist. Always on. Owns `Experiments/Group Theory/Burnside Group/B25/**`. |
| **Validator** | `math-validator` | Independent math oracle. Math verdicts override all peers. |
| **Math Expert** | `math-expert` | Idea-generator / advisor. Proposes, never certifies. |

## Step 3 — Load role prompts

### Approach A — Maestri Agent Roles (preferred)
For each role, create a Maestri Agent Role:
- `math-lead` ← `<vault>/_meta/agents/lead.md`
- `math-researcher` ← `<vault>/_meta/agents/researcher.md`
- `math-developer` ← `<vault>/_meta/agents/developer.md`
- `math-experimenter` ← `<vault>/_meta/agents/experimenter.md`
- `math-experimenter-b25` ← `<vault>/_meta/agents/experimenter-b25.md`
- `math-validator` ← `<vault>/_meta/agents/validator.md`
- `math-expert` ← `<vault>/_meta/agents/math-expert.md`

Assign each role to the matching terminal.

### Approach B — Per-session paste
On session start, tell each terminal:
```
Read the role definition at <vault>/_meta/agents/<role>.md. This is your operating doctrine — adhere to it strictly.
```

## Step 4 — Sticky note: project context

Create a sticky note named **`math-context`** connected to **all seven** terminals. Paste:

```
# Math canvas context

Vault: <your vault path>
Local checkouts: see `## Math vault — local checkouts` in your ~/.claude/CLAUDE.md
Branch: main (working: feat/* fix/* chore/*)

Read on session start (your role + shared):
- Role: <vault>/_meta/agents/<role>.md
- Shared: <vault>/_meta/agents/_common.md
- Mission: <vault>/_meta/mission.md
- Tags: <vault>/_meta/tags.md (6-axis taxonomy)
- Experiment convention: <vault>/_meta/experiment-folder-convention.md
- Projects & dependencies: <vault>/_meta/projects-and-dependencies-convention.md
- Project TODO lists: <vault>/_meta/project-todo-convention.md (private queue per project; Lead owns, others read)

Per task: Lead's brief names a project profile (<vault>/_meta/projects/project-<name>.md). Read it + the
dependency notes it lists + that repo's README before touching code.

Terminology: "agent" without qualifier = AI agent (you, one of seven). Algorithm processes are "components"
(or the project's qualified term, from its profile). Don't conflate.

Seven AI agents on canvas:
- Lead (orchestrator + code review + commit)
- Researcher (multi-domain literature + restructure authority)
- Developer (implementation in the project's stack + framework + perf)
- Experimenter (everything except B(2,5))
- Experimenter-B25 (B(2,5) specialist, exclusive owner of that subtree)
- Validator (math oracle; verdicts override all peers except human)
- Math Expert (idea-generator / advisor; proposes, never certifies)

Topology: hub-and-spoke through Lead. Exception: Validator's #status/disproven verdict overrides immediately without Lead routing.

Commit policy: ONLY Lead commits, ONLY after explicit per-action human approval (commit, push, dep add, protected-interface change, on-disk format change, math-touching code requires Validator verdict too).

Maestri CLI:
- maestri list
- maestri ask "<Name>" "..."
- maestri check "<Name>"
- maestri note read/write/edit "<note>"
```

## Step 5 — Connect terminals (full mesh)

Multi-Experimenter and Validator-as-oracle benefit from direct lines. Wire as a full mesh:

- Lead ↔ each of the other six
- Math Expert ↔ Researcher, Validator (literature grounding; soundness checks of proposed ideas)
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

When Researcher identifies a viable new cross-domain application, spawn a per-domain Experimenter (Lead writes a project profile for the new domain first):

- Name: `Experimenter-<domain>` (e.g. `Experimenter-Grobner`, `Experimenter-Biology`, `Experimenter-ChallengeGen` for [[project-challenge-gen]]).
- Role: use `math-experimenter` (the general role) — the per-domain focus comes from the brief Lead gives them.
- Working dir + model + advisor: same as the general Experimenter (Opus 5.5, Fable advisor).
- Connect to Lead, Researcher, Validator (mesh).
- Shut down when the cross-domain exploration concludes (validated / rejected / paused).

These are temporary terminals. The persistent seven handle the long-lived workflows.

## Step 7 — Per-user Agents dir

The `Agents/` tree is **per-user** to keep colleagues from colliding on log files. Before first canvas use, ensure `Agents/<your-handle>/` exists with the seven role subdirs:

```bash
cd <vault>/Agents
mkdir -p <your-handle>/{Lead,Researcher,Developer,Experimenter,Experimenter-B25,Validator,MathExpert,_shared}
# Each role dir gets its own log.md, scratch/, etc. as the agent uses them.
# _shared/ holds data all roles share, e.g. the monthly message-log-YYYY-MM.md.
```

Every `maestri ask` is logged to `Agents/<your-handle>/_shared/message-log-YYYY-MM.md` by Claude Code hooks (rules: [[_common]] § Message log). Install them once per machine — canvas agents run outside this repo, so the hooks go in your **user** settings, `~/.claude/settings.json`, under `"hooks"`:

```json
"PreToolUse":       [{"matcher": "Bash", "hooks": [{"type": "command", "timeout": 10, "command": "python3 \"<repo>/claude/hooks/maestri_message_log.py\" sent --vault \"<vault>\" --handle <your-handle>"}]}],
"PostToolUse":      [{"matcher": "Bash", "hooks": [{"type": "command", "timeout": 10, "command": "python3 \"<repo>/claude/hooks/maestri_message_log.py\" reply --vault \"<vault>\" --handle <your-handle>"}]}],
"UserPromptSubmit": [{"hooks": [{"type": "command", "timeout": 10, "command": "python3 \"<repo>/claude/hooks/maestri_message_log.py\" recv --vault \"<vault>\" --handle <your-handle>"}]}]
```

Append these entries to any existing lists for the same events. The script does nothing outside Maestri terminals and always exits 0, so it never blocks an agent. Restart running Claude Code sessions after installing.

**Lead ↔ human transcript (optional).** `claude/hooks/lead_human_transcript.py` keeps a readable record of the human's conversation with Lead in `Agents/<your-handle>/Lead/transcripts/lead-human-YYYY-MM.md` (private, gitignored): one heading per day, every human message and Lead reply in full, agent messages as collapsed callouts, no tool output. Put it in Lead's own settings file (`<repo>/.maestri/lead/settings.json`, see Step 2) so only Lead runs it, and start Lead with `claude --settings .maestri/lead/settings.json`:

```json
"Stop": [{"hooks": [{"type": "command", "timeout": 15, "command": "python3 \"<repo>/claude/hooks/lead_human_transcript.py\" stop --vault \"<vault>\" --handle <your-handle>"}]}]
```

`... lead_human_transcript.py backfill <session>.jsonl --handle <your-handle>` fills it from an earlier session transcript (`~/.claude/projects/<project>/<session>.jsonl`). Agent messages are recognised by their `TYPE:`/`FROM:` header, so agents must always send it. Limitation: a short text Lead writes just before a tool call is sometimes not stored by Claude Code and then missing from the transcript; turn-final replies are always captured.

Maria's tree is at `Agents/maumayma/`. Each colleague gets their own subtree when they join the canvas. The role prompts in `_meta/agents/*.md` use `Agents/<your-user>/<role>/` paths — they auto-resolve to the correct subtree based on which user's session is active.

## Step 8 — Verify

In each terminal: `maestri list` should show 6 peers + the `math-context` note (plus on-demand terminals when present).

Then: *"Cold-start handshake."* Each terminal should respond with a single short message naming its role, listing peers, and saying it's standing by. **No other action.** If it tries to write logs, do experiments, or send unsolicited messages, the role prompt didn't load — re-paste.

## Step 9 — First flow

Your primary terminal is **Lead**. Talk to Lead in natural language:

- *"Ask Researcher to scan recent literature on Buchberger's algorithm with cooperation — looking for an approach that fits Gröbner."*
- *"Start a new project for <problem>; have Researcher survey candidate approaches and tools first, then write the profile."*
- *"Developer should implement <component> for project <name>. Tests required, Validator will review the math layer."*
- *"Experimenter-B25, what's in `_progress.md` right now? Next experiment shortlist?"*
- *"Ask Validator to verify claim X from yesterday's experiment with an independent oracle."*

Lead delegates, gates, and pings you when a decision is needed.

## Permissions reminder

Both vaults' Write/Edit allow rules in `~/.claude/settings.json`:
```
"Write(<vault>/**)"
"Edit(<vault>/**)"
```
Plus `additionalDirectories` includes the Math vault. Restart any active Claude Code session if you change settings.

## Troubleshooting

Same as BOTBOTBOT's canvas-setup. If you don't see a base file render in Obsidian, check the YAML quoting in the `.base` file (most common issue — strings with colons need quotes).
