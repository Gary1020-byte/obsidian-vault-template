[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Obsidian Vault Template

Reusable Obsidian notes skeleton with a 3-layer architecture. Ships in **the shipped mode** (tasks, calendar, projects, areas, daily) but the same skeleton adapts to **knowledge-base mode** (entities, concepts, comparisons, summaries, overviews, lessons) — the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

- **`raw/`** — immutable inbox, two sub-layers: root = uncategorized drop zone; subfolders = categorized (`captures/` required, `emails/` + `external/` opt-in). Never edit after writing.
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
├── raw/                 ← immutable, two sub-layers
│   ├── <root>           ← Layer 1: uncategorized drop zone (triage target)
│   ├── captures/        ← Layer 2a: your time-stamped records (YYYY-MM-DD-*.md)
│   ├── emails/          ← Layer 2b: email (inbound + outbound, including AI drafts) — OPT-IN
│   └── external/        ← Layer 2c: third-party sources (web clips, papers, lecture notes) — OPT-IN
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

## Reference: <companion notes> (knowledge-base mode in production)

A concrete deployment of this template in **knowledge-base mode** is **<companion notes>**, a personal knowledge base following the Karpathy LLM Wiki pattern. It is the source notes for course notes, paper summaries, and concept pages.

**<companion notes> at a glance:**

| Metric | Value |
|---|---|
| Wiki pages | 366 (entities / concepts / overviews / comparisons / summaries) |
| Source files (`raw/`) | 49 (lecture notes, paper PDFs, transcripts) |
| Commits in `log.md` | 13 |
| `AGENTS.md` | the 5-page-type ingest workflow |
| Provenance | every wiki page traces back to a capture in `raw/captures/` |

Use <companion notes> as a concrete example when adapting this template to knowledge-base mode.

## Adapting to a different mode

This template ships with **the shipped mode**. To repurpose for **knowledge-base mode** (LLM Wiki style):

1. **Restructure `wiki/`** — replace the the task system folders with the 5 page-type folders:
   ```
   wiki/entities/      # concrete things: persons, projects, systems, tools
   wiki/concepts/      # abstractions: theories, methods, principles
   wiki/overviews/     # big-picture essays tying concepts together
   wiki/comparisons/   # side-by-side analyses
   wiki/summaries/     # 1 source in raw/ → 1 summary page
   wiki/lessons/       # #LABEL cards: real pitfalls you tripped on
   ```
2. **Update `AGENTS.md`** with the 5-page-type ingest workflow (read sources → write entities/concepts/summaries + log entry + capture trace)
3. **Update `templates/`** — replace `task.md` / `event.md` / `recurring-event.md` with `summary.md` / `entity.md` / `concept.md` / `overview.md` / `comparison.md` / `lesson.md`
4. **Update `raw/` semantics** — `raw/captures/` and `captures/` are required by default; `raw/emails/` is opt-in (create only if your workflow needs email handling).
5. **Add `type:` field** to frontmatter: `entity | concept | overview | comparison | summary | lesson`

For a concrete reference implementation of knowledge-base mode, see **<companion notes>** (the section above).

## License

MIT License — Copyright © 2026 Gary Xie. See [LICENSE](LICENSE) for the full text.