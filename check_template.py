#!/usr/bin/env python3
"""Consistency check for the obsidian-vault-template.

Verifies that the things the template promises actually exist and agree:
  - every folder a QuickAdd macro writes into exists in the tree
  - every template a macro references exists
  - every plugin listed in community-plugins.json has a data.json
  - every plugin with a data.json is listed
  - every folder the docs name exists
  - the markdown tables in the docs are well-formed
  - no string that belongs to the author's private system survives

Read-only.
"""
import json, os, re, subprocess, sys

# The repo root, derived from this file so the check runs wherever the
# repo is checked out — CI, a fork, or a local clone.
ROOT = os.path.dirname(os.path.abspath(__file__))
FORBIDDEN = ["Personal-OS", "LLM-Wiki", "fast-note-sync", "shared-vault",
             "/home/gary", ".ts.net", "140.112.244.110"]

problems = []


def fail(msg):
    problems.append(msg)
    print("  ✗", msg)


def ok(msg):
    print("  ✓", msg)


print("=== 1. QuickAdd macros -> folders + templates ===")
qa = json.load(open(f"{ROOT}/.obsidian/plugins/quickadd/data.json"))
for name, macro in qa.get("macros", {}).items():
    for action in macro.get("macro", {}).get("actions", []):
        if action.get("type") != "createNote":
            continue
        path = action.get("path")
        if path and not os.path.isdir(os.path.join(ROOT, path)):
            fail(f"macro '{name}' writes to '{path}' which does not exist")
        else:
            ok(f"macro '{name}' -> {path}/")
        tmpl = action.get("template")
        if tmpl and not os.path.isfile(os.path.join(ROOT, tmpl)):
            fail(f"macro '{name}' uses template '{tmpl}' which does not exist")
        elif tmpl:
            ok(f"macro '{name}' -> template {tmpl}")

print()
print("=== 2. plugin list vs plugin config ===")
listed = json.load(open(f"{ROOT}/.obsidian/community-plugins.json"))
plugdir = f"{ROOT}/.obsidian/plugins"
withcfg = sorted(d for d in os.listdir(plugdir)
                 if os.path.isfile(f"{plugdir}/{d}/data.json"))
for p in listed:
    if p not in withcfg:
        fail(f"community-plugins.json lists '{p}' but .obsidian/plugins/{p}/data.json is missing")
    else:
        ok(f"'{p}' listed and configured")
for p in withcfg:
    if p not in listed:
        fail(f"plugin '{p}' has a config but is not in community-plugins.json")
    else:
        ok(f"'{p}' config is listed")

print()
print("=== 3. folders named in the docs exist ===")
DOC_FOLDERS = [
    "raw", "raw/captures", "raw/external", "wiki", "wiki/tasks",
    "wiki/tasks/inbox", "wiki/tasks/next", "wiki/tasks/waiting",
    "wiki/tasks/someday", "wiki/tasks/done", "wiki/calendar",
    "wiki/calendar/daily", "wiki/calendar/recurring", "wiki/calendar/synced",
    "wiki/projects", "wiki/areas", "wiki/daily", "wiki/archives",
    "wiki/archives/projects", "wiki/archives/tasks", "templates",
]
for d in DOC_FOLDERS:
    if os.path.isdir(os.path.join(ROOT, d)):
        ok(f"{d}/")
    else:
        fail(f"doc names '{d}/' but it does not exist")

print()
print("=== 4. templates referenced by app.json / docs exist ===")
app = json.load(open(f"{ROOT}/.obsidian/app.json"))
for key in ("dailyNoteTemplate",):
    t = app.get(key)
    if t and not os.path.isfile(os.path.join(ROOT, t)):
        fail(f"app.json {key}='{t}' does not exist")
    elif t:
        ok(f"app.json {key} -> {t}")
tpl_dir = f"{ROOT}/templates"
tpls = sorted(f for f in os.listdir(tpl_dir) if f.endswith(".md"))
for f in tpls:
    body = open(os.path.join(tpl_dir, f), encoding="utf-8").read()
    if "type:" not in body:
        fail(f"templates/{f} has no `type:` frontmatter key")
print(f"  ✓ {len(tpls)} templates, all with a type: field")

print()
print("=== 5. markdown table well-formedness ===")
for f in ("AGENTS.md", "README.md", "index.md", "log.md"):
    lines = open(f"{ROOT}/{f}", encoding="utf-8").read().splitlines()
    in_tbl = False
    tbl_start = 0
    ncols = 0
    for i, l in enumerate(lines, 1):
        isrow = l.startswith("|") and l.rstrip().endswith("|")
        if isrow:
            n = len(l.split("|")) - 2
            if not in_tbl:
                in_tbl, tbl_start, ncols = True, i, n
            elif n != ncols:
                fail(f"{f}:{i} table row has {n} cells, expected {ncols} "
                     f"(table starts at line {tbl_start})")
        else:
            in_tbl = False
    print(f"  ✓ {f} tables checked")

print()
print("=== 6. no private-system strings ===")
tracked = subprocess.run(["git", "-C", ROOT, "ls-files"],
                          capture_output=True, text=True).stdout.split()
tracked = [f for f in tracked if f]
scanned = 0
for f in tracked:
    if not f.endswith((".md", ".json", ".toml", ".yml", ".yaml", ".txt")):
        continue
    # log.md and CHANGELOG.md are append-only histories. They legitimately
    # record what was changed away from — a rename entry has to name the old
    # name. They are still checked for a home path, an IP, or a hostname.
    body = open(os.path.join(ROOT, f), encoding="utf-8", errors="replace").read()
    names = [b for b in FORBIDDEN if b in body]
    if f in ("log.md", "CHANGELOG.md"):
        names = [b for b in names if b in ("/home/gary", ".ts.net", "140.112.244.110")]
    for bad in names:
        fail(f"{f} contains '{bad}'")
    scanned += 1
print(f"  ✓ scanned {scanned} tracked files")

print()
print("=== 7. every tracked file ends with a newline ===")
for f in tracked:
    p = os.path.join(ROOT, f)
    try:
        body = open(p, "rb").read()
    except Exception:
        continue
    if body and not body.endswith(b"\n"):
        fail(f"{f} has no trailing newline")
print("  ✓ checked")

print()
if problems:
    print(f"TOTAL PROBLEMS: {len(problems)}")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)


if __name__ == "__main__":
    main()
