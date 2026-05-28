---
description: One-time onboarding for a new contributor to the math-agents Obsidian vault. Installs kepano's obsidian-skills + this repo's /research skill, registers the user's handle, and creates their People page.
---

# /setup — Math vault onboarding

Run this ONCE when you join the vault. After this, you're registered and can use `/research`.

## Steps

Execute these steps sequentially. Stop and ask the user if anything blocks.

### 1. Verify repo + vault path

The current working directory should be the math-agents repo root. Verify:

```bash
test -d obsidian/ && test -f CLAUDE.md && test -f README.md
```

If this fails, the user is in the wrong directory. Tell them: "I expected to be in the math-agents repo root (the dir with `obsidian/`, `CLAUDE.md`, and `README.md`). Please `cd` into it and re-run `/setup`."

Record the absolute repo path:

```bash
REPO_ROOT=$(pwd)
VAULT_PATH="$REPO_ROOT/obsidian"
```

### 2. Ask the user for identity

Use the AskUserQuestion tool. Ask in one go:

- **Full name** (e.g. `Anna Petrova`) — will be used as the display name in `People/<handle>.md`
- **Handle** (kebab-case, e.g. `anna-p`) — will be used for `#user/<handle>` tag + `Agents/<handle>/` subtree + `People/<handle>.md` filename

If the handle is unclear or has spaces / caps, ask again.

Store these as `FULL_NAME` and `HANDLE`.

### 3. Check if already registered

```bash
grep -q "#user/$HANDLE" obsidian/_meta/tags.md && echo REGISTERED || echo NEW
```

- If `REGISTERED`: tell the user they're already set up. Skip to step 9 (welcome summary only — don't reinstall skills, they're already there).
- If `NEW`: proceed.

### 4. Install kepano's obsidian-skills

Detect symlink support. macOS and Linux have it; Windows needs developer mode or admin. Try symlink first, fall back to copy.

```bash
mkdir -p ~/.claude/skills
TMP=$(mktemp -d)
git clone --depth 1 https://github.com/kepano/obsidian-skills "$TMP/obsidian-skills"

for skill in obsidian-markdown obsidian-bases obsidian-cli json-canvas defuddle; do
  SRC="$TMP/obsidian-skills/skills/$skill"
  DST="$HOME/.claude/skills/$skill"
  if [ ! -d "$SRC" ]; then
    echo "WARN: $skill not found in kepano's repo — skipping"
    continue
  fi
  if [ -e "$DST" ] || [ -L "$DST" ]; then
    echo "INFO: $skill already installed — leaving as-is"
    continue
  fi
  if ln -s "$SRC" "$DST" 2>/dev/null; then
    echo "OK: symlinked $skill"
  else
    cp -r "$SRC" "$DST"
    echo "OK: copied $skill (symlink unsupported)"
  fi
done
```

Note: the symlink fallback keeps `$TMP` referenced. If the user reboots, the tmp dir may be cleaned and skills break. For long-term install, copy instead of symlink for kepano's skills. Default to copy:

**Better default:**

```bash
for skill in obsidian-markdown obsidian-bases obsidian-cli json-canvas defuddle; do
  SRC="$TMP/obsidian-skills/skills/$skill"
  DST="$HOME/.claude/skills/$skill"
  [ -d "$SRC" ] || continue
  [ -e "$DST" ] && continue
  cp -r "$SRC" "$DST"
  echo "OK: installed $skill"
done
```

### 5. Install this repo's `/research` skill via symlink

The `/research` skill lives inside the vault and should propagate updates automatically. Symlink it (or copy fallback):

```bash
SRC="$VAULT_PATH/_meta/skills/research"
DST="$HOME/.claude/skills/research"

if [ -L "$DST" ] || [ -e "$DST" ]; then
  echo "INFO: /research skill already installed — leaving as-is"
elif ln -s "$SRC" "$DST" 2>/dev/null; then
  echo "OK: symlinked /research skill (updates propagate from vault)"
else
  cp -r "$SRC" "$DST"
  echo "OK: copied /research skill (re-run /setup after major vault updates to pick them up)"
fi
```

### 6. Register handle in `_meta/tags.md`

Find the "Registered handles" list in `obsidian/_meta/tags.md` § "Axis 2 — `#user/*`". The list looks like:

```
Registered handles:
- `#user/maumayma` — Maria Matveeva (see [[People/maumayma]])
```

Add a line:

```
- `#user/<HANDLE>` — <FULL_NAME> (see [[People/<HANDLE>]])
```

Preserve alphabetical order if possible (insert in the right place). If the list is missing or hard to find, ask the user; do not invent placement.

### 7. Create `People/<HANDLE>.md`

Use `obsidian/People/maumayma.md` as a template. Read it, then write a new file at `obsidian/People/<HANDLE>.md` with:

- `author: <HANDLE>` frontmatter
- `tags: [user/<HANDLE>, meta]` (or whatever the existing maumayma.md uses)
- Title: `# <FULL_NAME>`
- A short blurb section: "Joined: <today's date>. Domains of focus: TBD. Active projects: TBD." Tell the user they can edit this later.

Do NOT copy Maria's content verbatim — only the structure.

### 8. Commit + push the registration

The vault is at `<repo>/obsidian/` inside a git repo. The two files we changed are:

- `obsidian/_meta/tags.md` (added one line)
- `obsidian/People/<HANDLE>.md` (new file)

```bash
cd "$REPO_ROOT"
git add obsidian/_meta/tags.md obsidian/People/<HANDLE>.md
git status
```

Show the user the staged changes. Then commit + push:

```bash
git commit -m "chore(onboarding): register <HANDLE> (<FULL_NAME>)"
git push origin main
```

If the push fails (auth, branch protection, no write access):

- Tell the user the local registration succeeded but the push didn't
- Show the failure message
- Suggest: "Either Maria needs to add you as a repo collaborator, or you push via a feature branch + PR. Ask Maria."

Do NOT retry destructively (no `--force`).

### 9. Welcome summary

Print this (substituting actual paths/handle):

```
✓ Vault path: <VAULT_PATH>
✓ Skills installed: obsidian-markdown, obsidian-bases, obsidian-cli, json-canvas, defuddle, research
✓ Handle registered: #user/<HANDLE> in obsidian/_meta/tags.md
✓ People page: obsidian/People/<HANDLE>.md (edit later to add domain focus + projects)
✓ Registration committed to git (or branch pushed if direct push failed — see above)

Next steps:

1. **Restart Claude Code.** Skills load at session start. Quit and reopen, then come back here.

2. **Try ingesting a paper.** From any Claude Code session:
   /research https://arxiv.org/abs/<some-id>

   The skill fetches, summarizes, tags with the 6-axis taxonomy, and saves under
   <VAULT_PATH>/Research/<domain>/<topic>/<paper-id>.md.

3. **Open the vault in Obsidian.** File → Open vault → "Open folder as vault" → <VAULT_PATH>.
   Once open, read:
   - obsidian/README.md           — vault-internal walkthrough
   - obsidian/_meta/tags.md       — the 6-axis taxonomy (skim it, you'll absorb the rest by use)
   - obsidian/_meta/research-folder-convention.md — how Research/ is organized
   - Architecture/Mixer/Bases/Papers.base — open this Base for filtered views of all papers

4. **Tag your People page.** Open obsidian/People/<HANDLE>.md and fill in your domain focus,
   active projects, etc. Save in Obsidian (no need to commit; or commit if you want to share).

5. **Questions?** Ping Maria (#user/maumayma in vault, @maumayma on GitHub).
```

## Stop conditions

- Repo path wrong → tell user to cd into repo root and re-run
- User refuses to provide handle → can't proceed; stop and explain why
- Handle conflict (already registered to someone else) → ask user to pick a different handle
- Git push fails → don't retry; report to user with the failure message and stop
- kepano's obsidian-skills clone fails (network, dead repo) → install /research anyway and warn user kepano's skills are missing; suggest manual install later
- Vault path doesn't exist at `<repo>/obsidian/` → user may have a structural issue; ask them to verify with `ls obsidian/` and stop

## What this command does NOT do

- Does not create an `Agents/<HANDLE>/` subtree. That's only needed for Maestri-canvas users (advanced workflow). If you later want to run the canvas, see `obsidian/_meta/canvas-setup.md` and create the subtree at that point.
- Does not modify any existing user's content. Only adds new entries.
- Does not push to remote on the user's behalf for anything other than the one-time registration. After setup, normal git workflow applies — the user is in control.
