#!/usr/bin/env python3
"""Claude Code hook: keep a readable transcript of the human <-> Lead conversation.

Created by: Alex Myasnikov
Date: October 14, 2026

Appends every message the human sends to Lead and every reply Lead shows the
human to
    <vault>/Agents/<handle>/Lead/transcripts/lead-human-YYYY-MM.md
as Markdown: one `## YYYY-MM-DD` heading per day, one `### HH:MM · Human` or
`### HH:MM · Lead` heading per message, the full text below it. Messages from
other agents that arrive in Lead's terminal (a `TYPE:`/`FROM:` header, or
pasted content) are kept as collapsed `[!note]-` callouts so the human dialogue
stays readable. Tool calls, tool output, thinking and system notifications are
left out; the full machine record stays in Claude Code's session JSONL.

Modes:
  stop                   Stop hook (JSON on stdin): append what is new in the
                         session transcript since the last run.
  backfill <jsonl>...    one-off: process whole session transcripts in order.

Options:
  --vault <path>    vault root (default: ../../obsidian relative to this file)
  --handle <name>   owning user handle (default: $MATH_VAULT_HANDLE, then the
                    "My vault handle:" line in ~/.claude/CLAUDE.md)
  --name <name>     canvas name of the terminal to record (default: Lead); the
                    hook is a no-op in any other terminal.

Prints nothing to stdout and always exits 0.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from maestri_message_log import handle_from_claude_md, my_name, opt  # noqa: E402

REMINDER_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PASTED_RE = re.compile(r"<pasted_content[^>]*>(.*?)</pasted_content[^>]*>", re.S)
HEADER_RE = re.compile(r"^\s*(TYPE|FROM):", re.M)
FROM_RE = re.compile(r"^\s*FROM:\s*(.+)$", re.M)
SKIP_PREFIXES = ("<task-notification>", "[SYSTEM NOTIFICATION", "<local-command-stdout>",
                 "<local-command-caveat>", "Caveat:")
COMMAND_RE = re.compile(r"<command-name>(.*?)</command-name>", re.S)


def local_time(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
    except (AttributeError, ValueError):
        return datetime.now(timezone.utc).astimezone()


def prompt_text(entry):
    """(text, ts) of a human-side prompt in a transcript entry, else None."""
    t = entry.get("type")
    if t == "user" and not entry.get("isMeta"):
        content = entry.get("message", {}).get("content")
        if isinstance(content, list):
            if any(b.get("type") == "tool_result" for b in content):
                return None
            content = "\n\n".join(b.get("text", "") for b in content if b.get("type") == "text")
        if isinstance(content, str):
            return content, entry.get("timestamp")
    if t == "attachment":
        a = entry.get("attachment", {})
        if a.get("type") == "queued_command" and isinstance(a.get("prompt"), str):
            return a["prompt"], entry.get("timestamp")
    return None


def reply_text(entry):
    if entry.get("type") != "assistant" or entry.get("isSidechain"):
        return None
    content = entry.get("message", {}).get("content")
    if not isinstance(content, list):
        return None
    text = "\n\n".join(b.get("text", "") for b in content if b.get("type") == "text").strip()
    return text or None


def classify(raw):
    """(kind, label, body) for a prompt; kind in human | agent | command | skip."""
    text = REMINDER_RE.sub("", raw).strip()
    cmd = COMMAND_RE.search(text)
    if cmd:
        return "command", cmd.group(1).strip(), ""
    if not text or text.startswith(SKIP_PREFIXES):
        return "skip", "", ""
    pasted = PASTED_RE.search(text)
    body = pasted.group(1).strip() if pasted else text
    if pasted or HEADER_RE.search(body):
        m = FROM_RE.search(body)
        return "agent", (m.group(1).strip() if m else "agent, no header"), body
    return "human", "Human", body


def callout(label, body):
    lines = ["> [!note]- Agent → Lead · %s" % label]
    lines += ["> " + ln if ln else ">" for ln in body.splitlines()]
    return "\n".join(lines)


class Writer:
    def __init__(self, out_dir, state):
        self.out_dir = out_dir
        self.state = state
        self.reply = []  # pending Lead text blocks of the current turn
        self.reply_ts = None

    def _write(self, when, block):
        path = os.path.join(self.out_dir, "lead-human-%s.md" % when.strftime("%Y-%m"))
        new_file = not os.path.exists(path)
        day = when.strftime("%Y-%m-%d")
        with open(path, "a", encoding="utf-8") as f:
            if new_file:
                f.write("# Lead ↔ human transcript, %s\n\n"
                        "Written by `claude/hooks/lead_human_transcript.py`. Agent messages "
                        "that arrive in Lead's terminal are collapsed callouts.\n\n"
                        % when.strftime("%Y-%m"))
            if new_file or self.state.get("day") != day:
                f.write("## %s\n\n" % day)
                self.state["day"] = day
            f.write(block.rstrip() + "\n\n")

    def flush_reply(self):
        if self.reply:
            when = local_time(self.reply_ts)
            self._write(when, "### %s · Lead\n\n%s" % (when.strftime("%H:%M"), "\n\n".join(self.reply)))
        self.reply, self.reply_ts = [], None

    def prompt(self, raw, ts):
        kind, label, body = classify(raw)
        if kind == "skip":
            return
        self.flush_reply()
        when = local_time(ts)
        hhmm = when.strftime("%H:%M")
        if kind == "command":
            self._write(when, "### %s · Human\n\n`%s`" % (hhmm, label))
        elif kind == "agent":
            self._write(when, "### %s · %s\n\n%s" % (hhmm, label, callout(label, body)))
        else:
            self._write(when, "### %s · Human\n\n%s" % (hhmm, body))

    def assistant(self, text, ts):
        if not self.reply:
            self.reply_ts = ts
        self.reply.append(text)


def process(path, writer, start):
    """Feed transcript lines from index `start`; return the number of lines read."""
    n = 0
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            n = i + 1
            if i < start:
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            p = prompt_text(entry)
            if p:
                writer.prompt(*p)
                continue
            r = reply_text(entry)
            if r:
                writer.assistant(r, entry.get("timestamp"))
    writer.flush_reply()
    return n


def main(argv):
    mode = argv[0] if argv else ""
    here = os.path.dirname(os.path.abspath(__file__))
    vault = opt(argv, "--vault") or os.path.normpath(os.path.join(here, "..", "..", "obsidian"))
    handle = opt(argv, "--handle") or os.environ.get("MATH_VAULT_HANDLE") or handle_from_claude_md()
    name = opt(argv, "--name") or "Lead"
    if not handle:
        return
    out_dir = os.path.join(vault, "Agents", handle, "Lead", "transcripts")
    os.makedirs(out_dir, exist_ok=True)
    state_path = os.path.join(out_dir, ".state.json")
    try:
        with open(state_path, encoding="utf-8") as f:
            state = json.load(f)
    except (OSError, ValueError):
        state = {}
    sessions = state.setdefault("sessions", {})
    writer = Writer(out_dir, state)

    if mode == "stop":
        if not (os.environ.get("MAESTRI_TERMINAL_ID") or os.environ.get("MAESTRI_SOCKET")):
            return
        if my_name() != name:
            return
        hook = json.load(sys.stdin)
        path = hook.get("transcript_path")
        sid = hook.get("session_id") or path
        if not path or not os.path.exists(path):
            return
        sessions[sid] = process(path, writer, sessions.get(sid, 0))
    elif mode == "backfill":
        for path in [a for a in argv[1:] if a.endswith(".jsonl")]:
            sid = os.path.splitext(os.path.basename(path))[0]
            sessions[sid] = process(path, writer, 0)
    else:
        return
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=1)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception:  # never block the agent
        pass
    sys.exit(0)
