[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Obsidian Vault Template
Reusable Obsidian vault skeleton for Personal-OS: tasks, calendar, projects, areas, and daily notes - built on a 3-layer architecture (raw/ -> wiki/ -> archive/) with method-based status (Method B: folder location = status).

- **`raw/`** — immutable inbox, two sub-layers: root = uncategorized drop zone; subfolders = categorized (`captures/` + `external/` required, `emails/` opt-in). Never edit after writing.
- **`wiki/`** — linked data network (the work surface; edited and re-edited)
- **`meta`** — `AGENTS.md` + `index.md` + `log.md` (conventions + map + history)

## Features

- **5 community plugins pre-configured**: Templater, Dataview, obsidian-tasks, QuickAdd, Calendar (liamcain)
- **7 templates** (in `templates/`): `area`, `capture`, `daily`, `event`, `project`, `recurring-event`, `task`
- **Folder skeleton** for tasks / calendar / projects / areas / daily / archives
- **Method B** rule: *location = status* (no `status:` field needed — folder placement says done/waiting/inbox/...)
- **Commit convention**: `YYYY-MM-DD <type> | <description>`
- **Capture traces** in `raw/captures/` for full provenance of every wiki page

## Quick Start

```bash
git clone https://github.com/Gary1020-byte/obsidian-vault-template.git ~/my-vault
cd ~/my-vault
# In Obsidian: "Open folder as vault" → pick ~/my-vault
# Reload Obsidian to activate community plugins
```

On first launch, Obsidian will download plugin code from its registry (only `data.json` is committed here).

## Folder Structure

```
.
├── AGENTS.md            ← operations manual (read first)
├── README.md            ← this file
├── index.md             ← vault contents index (wikilinks only)
├── log.md               ← operation log (append-only)
├── .gitignore           ← ignores workspace.json, cache, trash
├── .obsidian/           ← Obsidian config (plugins, app settings)
│   ├── app.json         ← dailyNotesFolder, templates folder
│   ├── community-plugins.json
│   ├── core-plugins.json
│   └── plugins/{templater,dataview,obsidian-tasks,quickadd,calendar}/data.json
├── templates/           ← 7 Templater templates
│   ├── area.md
│   ├── capture.md
│   ├── daily.md
│   ├── event.md
│   ├── project.md
│   ├── recurring-event.md
│   └── task.md
├── raw/                 ← immutable, two sub-layers
│   ├── <root>           ← Layer 1: uncategorized drop zone (triage target)
│   ├── captures/        ← Layer 2a: your time-stamped records (YYYY-MM-DD-*.md) — REQUIRED
│   ├── external/        ← Layer 2b: third-party sources (web clips, papers, lecture notes) — REQUIRED
│   └── emails/          ← Layer 2c: email (inbound + outbound, including AI drafts) — OPT-IN
└── wiki/                ← editable, source of work
    ├── tasks/           ← task state machine (Method B: location = status)
    │   ├── inbox/       ← untriaged captures from raw/captures/
    │   ├── next/        ← active tasks
    │   ├── waiting/     ← blocked-on tasks
    │   ├── someday/     ← maybe-later tasks
    │   └── done/        ← completed tasks (archive; archive >10/month → done/YYYY-MM/)
    ├── calendar/
    │   ├── daily/       ← per-day recurring event instances
    │   ├── recurring/   ← recurring event templates
    │   └── synced/      ← from external calendar sync
    ├── projects/        ← one folder per project
    ├── areas/           ← ongoing responsibilities
    ├── daily/           ← daily notes (YYYY-MM-DD.md)
    └── archives/
        ├── projects/     ← closed projects
        └── tasks/       ← old done tasks (moved out of done/)
```

## Method B: location = status

| Concept | Where it lives | "Done" means |
|---|---|---|
| Task (active) | `wiki/tasks/next/` | moved to `wiki/tasks/done/` with `completed:` date |
| Task (blocked) | `wiki/tasks/waiting/` | moved to `wiki/tasks/done/` with `resolved:` date |
| Capture (untriaged) | `raw/captures/YYYY-MM-DD-*.md` | triaged → moved to `wiki/tasks/inbox/` + adds `triaged:` + `triage_target:` |
| Calendar event (one-time) | `wiki/calendar/synced/` | end date `===` passed |
| Calendar event (recurring instance) | `wiki/calendar/daily/` | end date passed |
| Daily note | `wiki/daily/YYYY-MM-DD.md` | today's file exists |

## Commit Convention

Format: `YYYY-MM-DD <type> | <description>`

Types: `docs`, `test`, `schema`, `init`, `dashboard`, `sim`, `plugins`, `task`, `area`, `project`, `cleanup`, `fix`, `restructure`, `ingest`, `lesson`, `comparison`, `overview`, `area`, `capture`.

## What's NOT included (you provide)

- `wiki/daily/*.md` — your daily notes (created on demand)
- `wiki/tasks/next/*.md` — your tasks
- `wiki/areas/*.md` — your areas
- `raw/captures/*.md` — your source captures
- `dashboard/` — your home dashboard (if any)
- `.obsidian/workspace.json` — Obsidian window layout (per-machine)

## Adapting this template

Fork / clone freely. When forking:

1. Update vault name in prose
2. Add your first task via Ctrl+P -> QuickAdd -> Task
3. Open wiki/daily/today.md

## License
MIT License — Copyright © 2026 Gary Xie. See [LICENSE](LICENSE) for the full text.