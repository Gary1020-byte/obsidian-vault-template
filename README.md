# Obsidian Vault Template

Reusable Obsidian notes skeleton built on a 3-layer architecture:

- **`raw/`** — immutable captures (never edit directly; ingest sources land here first)
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
git clone <this-repo> ~/my-notes
cd ~/my-notes
# In Obsidian: "Open folder as notes" → pick ~/my-notes
# Reload Obsidian to activate community plugins
```

On first launch, Obsidian will download plugin code from its registry (only `data.json` is committed here).

## Folder Structure

```
.
├── AGENTS.md            ← operations manual (read first)
├── README.md            ← this file
├── index.md             ← notes contents index (wikilinks only)
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
├── raw/                 ← immutable
│   ├── captures/        ← date-prefixed source captures
│   ├── emails/
│   ├── drafts/
│   └── external/        ← PDFs, images, binaries linked from wiki
└── wiki/                ← editable, source of work
    ├── inbox/           ← untriaged captures from raw/captures/
    ├── next/            ← active tasks
    ├── waiting/         ← blocked-on tasks
    ├── someday/         ← maybe-later tasks
    ├── done/            ← completed tasks (archive)
    ├── calendar/
    │   ├── daily/       ← per-day recurring event instances
    │   ├── recurring/   ← recurring event templates
    │   └── synced/      ← from external calendar sync
    ├── projects/        ← one folder per project
    ├── areas/           ← ongoing responsibilities
    ├── daily/           ← daily notes (YYYY-MM-DD.md)
    └── archives/
        ├── projects/    ← closed projects
        └── tasks/       ← old done tasks (moved out of done/)
```

## Method B: location = status

| Concept | Where it lives | "Done" means |
|---|---|---|
| Task (active) | `wiki/tasks/next/` | moved to `wiki/tasks/done/` with `completed:` date |
| Task (blocked) | `wiki/tasks/waiting/` | moved to `wiki/tasks/done/` with `resolved:` date |
| Capture (untriaged) | `raw/captures/YYYY-MM-DD-*.md` | triaged → moved to `an inbox folder` + adds `triaged:` + `triage_target:` |
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

## Adapting to a different mode

This template ships with the shipped mode (tasks/calendar/projects/areas/daily). To repurpose for a **knowledge-base notes** (entities/concepts/comparisons/summaries/overviews):

1. Replace `wiki/{tasks,calendar,projects,areas,daily,archives}/` with `wiki/{entities,concepts,comparisons,summaries,overviews}/`
2. Update `AGENTS.md` with the 5-page-type ingest workflow
4. In `raw/`, captures become the destination for `source-conversion.md` outputs (e.g. course transcript, book notes, paper drafts)

## License

MIT (or your choice).