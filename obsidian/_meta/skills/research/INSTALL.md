# Installing the `/research` skill

This skill ingests papers into the shared Obsidian Math vault as structured summaries with a connection graph. Once installed, you can invoke it from any Claude Code session by typing `/research`.

## Prerequisites

1. **Claude Code installed.** See https://docs.claude.com/en/docs/claude-code/overview.
2. **Access to the shared Obsidian vault.** Default path: `~/Documents/Obsidian/Math/`. If your local copy lives somewhere else, you'll need to tell the skill the local path on first invocation.
3. **A handle registered in the vault.** Edit `<vault>/_meta/tags.md` and add `#user/<your-handle>`, plus add yourself to `<vault>/People/<your-handle>.md` (use the existing `People/maumayma.md` as a template). Without this, the skill will ask you for your handle every session.

## Install

Skills in Claude Code live at `~/.claude/skills/<skill-name>/`. The simplest setup is a symlink from your local Claude config to the vault — that way, any updates Maria makes to the skill propagate to you without re-installing.

### macOS / Linux

```bash
mkdir -p ~/.claude/skills
ln -s /Users/maumayma/Documents/Obsidian/Math/_meta/skills/research ~/.claude/skills/research
```

Adjust the source path if your vault is somewhere else.

### Windows

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\research" -Target "C:\path\to\Obsidian\Math\_meta\skills\research"
```

### Verify

Start a new Claude Code session in any project. Type `/research`. The skill should respond with the prompt for a paper URL or topic.

If it doesn't appear, check:
- `ls ~/.claude/skills/research/SKILL.md` returns the file (symlink resolved)
- You restarted Claude Code after installing
- The skill name in `SKILL.md` frontmatter is `research`

## Usage

Once installed, invoke from natural-language prompts in any project:

```
/research https://arxiv.org/abs/2410.12345
```

```
/research https://arxiv.org/abs/2410.12345 https://link.springer.com/article/...
```

```
"Summarize this paper for the vault: <url>"
```

```
"Do a literature pass on Buchberger algorithms with cooperation"
```

```
"Re-link all the Burnside papers using the current taxonomy"
```

See `SKILL.md` for the four supported modes and `workflows/` for what happens under each.

## What the skill writes to

The skill **only writes to the Obsidian vault.** It does not modify any files in your current working directory. Specifically:

- New paper summaries → `<vault>/Research/<domain>/<topic-path>/<paper-id>.md`
- Concept hubs → `<vault>/Concepts/<concept-name>.md`
- Syntheses → `<vault>/Research/<domain>/_synthesis-<topic>.md`
- Your log → `<vault>/Agents/<your-handle>/Researcher/log.md` (created on first use)

It does not touch:
- Other users' `Agents/<other-user>/` directories
- The vault's git state (the vault is not under git)
- Your local repo's `.git/`

## Updating the skill

Since the skill is a symlink to the vault, any updates Maria pushes to `<vault>/_meta/skills/research/` propagate automatically to your install. To verify you're on a recent version, check the SKILL.md modification date:

```bash
ls -la ~/.claude/skills/research/SKILL.md
```

## Troubleshooting

- **Skill doesn't appear after install**: restart Claude Code. Skills are discovered at session start.
- **`defuddle` returns nothing useful**: the page is image-only or behind a login wall. The skill will fall back to `WebFetch` or ask you for an alternative source.
- **Vault path is different on your machine**: tell the skill the local path on first invocation: "the vault is at `/path/to/Math/` on my machine."
- **You're getting permission errors writing to the vault**: ensure Claude Code's settings include the vault path in `additionalDirectories` and the Write tool is allowed for `<vault-path>/**`. Maria has docs on this in `<vault>/_meta/canvas-setup.md`.

## Questions

Ask Maria (`#user/maumayma`).
