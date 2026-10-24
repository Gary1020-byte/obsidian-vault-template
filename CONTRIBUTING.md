# Contributing

Thanks for considering a change to `obsidian-vault-template`.

## What this repo is

A reusable Obsidian vault skeleton — a folder tree, a set of Templater
templates, pre-configured community plugins, and an operations manual
(`AGENTS.md`) that explains the conventions.

## The one rule that matters

**The template must stay template-shaped.** It ships a skeleton, not
content. If a change adds a note with real content in it, or hardcodes a
personal path, a personal course, or a specific vault name, it does not
belong here.

Concretely, a pull request should not introduce:

- a real task, project, area, or daily note
- an absolute path from anyone's home directory
- the name of a specific person's vault, notes system, or private repo
- a plugin configured to point at a specific server

## Before you open a pull request

Run the consistency check:

```bash
python3 check_template.py
```

It verifies that every folder the docs name exists, every QuickAdd macro
points at a real folder and template, the plugin list matches the committed
plugin configs, the markdown tables are well-formed, every file ends with a
newline, and no private-system string slipped in. CI runs the same check.

## Commit convention

```
YYYY-MM-DD <type> | <description>
```

The body explains *why*, not *what*. Two to five lines.

Types: `docs`, `test`, `schema`, `init`, `dashboard`, `sim`, `plugins`,
`task`, `area`, `project`, `cleanup`, `fix`, `restructure`, `ingest`,
`lesson`, `comparison`, `overview`, `capture`.

## Changing the folder structure

If you change a folder, three things have to move together:

1. the actual folder
2. `AGENTS.md` — the layer tables and the Method B table
3. `README.md` — the folder-structure tree

`check_template.py` fails if the docs name a folder that does not exist, but
it cannot tell you that you forgot to *mention* a new folder. Check by hand.

## Changing a QuickAdd macro

A macro's `path` must point at a folder that exists in the tree, and its
`template` must point at a file in `templates/`. The checker enforces both.

## License

MIT — see [LICENSE](LICENSE).
