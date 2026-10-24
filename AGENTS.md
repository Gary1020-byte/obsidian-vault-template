<!--
📦 TEMPLATE-NOTE
This file is the operations manual for the notes-template repo. It covers
Productivity mode (tasks / calendar / projects / areas / daily) plus the
shared architecture (3-layer model, Method B, raw/ two-layer, SOPs).

When forking this repo for a new notes:
1. Rename the wiki/ subfolders to fit your taxonomy
2. Replace template names with your notes name in any prose
3. Update the "What YOU provide" section to match what data you will keep
4. Delete this banner block once adapted
-->

---
date: 2026-10-02
type: meta
tags: [schema, operations-manual]
status: active
---

# AGENTS.md — Operations Manual

> **TL;DR** — Drop uncategorized stuff in `raw/` root, triage to `raw/<sub>/`. Work lives in `wiki/`. Folder location = status (Method B). Commit format: `YYYY-MM-DD <type> | <description>`.

---

## Pick your mode (do this first)

This template ships in **Productivity mode**. The same 3-layer skeleton also works for a
knowledge notes (see § Adapting this template).

| Mode | Best for | `wiki/` subfolders |
|---|---|---|
| **Productivity** (default) | GTD, calendar, areas, projects, daily notes | `tasks/{inbox,next,waiting,someday,done}/`, `calendar/{daily,recurring,synced}/`, `projects/`, `areas/`, `daily/`, `archives/{projects,tasks}/` |
| **Knowledge** | Concept pages, entities, comparisons, summaries | `concepts/`, `entities/`, `comparisons/`, `summaries/`, `overviews/` — replace the `tasks/` + `calendar/` trees with these |

---

## The 3-layer model (every mode)

```
Layer 1  raw/        immutable inbox. Agents read; never edit.
Layer 2  wiki/       work surface. Edit, evolve, wikilink.
Layer 3  meta        AGENTS.md + index.md + log.md (schema, map, history)
```

| Layer | What lives here | Rule |
|---|---|---|
| `raw/` | Your captures + external third-party sources (both required) + emails (opt-in) | **Two sub-layers**: root = uncategorized buffer, subfolders = categorized. `raw/captures/` and `captures/` are created by default; `raw/emails/` is opt-in. See § raw/ two-layer model below. |
| `wiki/` | Tasks, events, projects, areas, daily notes, summaries, entities, concepts | Edit freely. Use wikilinks. Follow Method B for status. |
| meta | `AGENTS.md` (this file), `index.md` (map), `log.md` (history) | `index.md` = wikilinks-only, never describe. `log.md` = append-only. |

---

## raw/ two-layer model

The `raw/` layer itself splits into two:

| Sub-layer | Location | Purpose |
|---|---|---|
| **Layer 1 — uncategorized** | `raw/` root (e.g. `raw/2026-10-02-meeting-thought.md`) | Quick-drop buffer. No `type:` required. Triage target. |
| **Layer 2 — categorized** | `raw/<sub>/` subfolders | Post-triage home. Organized by source type. |

### The categorized subfolders (1 required + 2 opt-in)

| Subfolder | Holds | Naming convention | Required? |
|---|---|---|---|
| `raw/captures/` | Your own time-stamped records: voice notes, screenshots, reflections, meeting minutes | `YYYY-MM-DD-<slug>.md` | ✅ Required |
| `captures/` | Third-party sources ingested for reading: web clips, book chapters, lecture handouts, PDFs → markdown | `<source-slug>.md` (often includes source identifier, e.g. `fluid-mech-2026-09-30-handout.md`) | ✅ Required |
| `raw/emails/` | Email correspondence, both inbound and outbound (including AI-drafted replies) | `YYYY-MM-DD-<subject-or-sender>.md` | ⭕ Opt-in |

`raw/captures/` and `captures/` are created by default. Enable `raw/emails/` only if your workflow needs it:

```bash
# Enable email flow
mkdir -p raw/emails && touch raw/emails/.gitkeep
```

To disable an opt-in folder: just delete it. No migration needed — the workflows reference it only when it exists.

To disable any opt-in folder: just delete it. No migration needed — the workflows reference these folders only when they exist.

### Triage flow

1. **Drop** anything into `raw/` root first — no classification needed (e.g. `raw/2026-10-02-something.md`)
2. **Triage** daily (or as needed): move the file into the matching subfolder and rename to convention if needed
3. **Add provenance**: when the file is consumed into a wiki page, link via frontmatter `source: raw/...`

### Rules

- ❌ Never leave files in `raw/` root indefinitely — backlog kills the buffer
- ❌ Never edit a raw/ file once written (append a new capture instead)
- ❌ Don't reference `raw/emails/` path unless you created it (it's opt-in)
- ✅ When unsure which subfolder fits, leave in root and decide next triage
- ✅ Filenames in root can be informal — rename when triaged
- ✅ `raw/emails/` is truly optional — delete if you don't need it

---

## Method B: location = status

**No `status:` field.** Folder placement encodes state.

| Concept | "Active" location | "Done" location |
|---|---|---|
| Task (active work) | `wiki/tasks/next/` | `wiki/tasks/done/` |
| Task (blocked) | `wiki/tasks/waiting/` | `wiki/tasks/done/` (with `resolved:` date) |
| Task (untriaged) | `raw/captures/YYYY-MM-DD-*.md` | `an inbox folder` (with `triaged:` + `triage_target:`) |
| Task (maybe later) | `wiki/tasks/someday/` | `wiki/tasks/done/` or `archives/tasks/` |
| Calendar event (one-time) | `wiki/calendar/synced/` | end date `===` passes |
| Calendar event (recurring instance) | `wiki/calendar/daily/` | end date passes |
| Daily note | `wiki/daily/YYYY-MM-DD.md` | today's file exists |


---

## Workflow — Productivity mode

#### 1. Capture

New stuff always goes to `raw/` first (root or subfolder, see § raw/ two-layer model).

- Voice-to-text notes, quick thoughts, screenshots → `raw/` root (triage later) or straight to `raw/captures/`
- Web clipper outputs, book/PDF highlights, lecture notes → `captures/`
- AI-written email reply drafts → `raw/emails/` *(if that opt-in folder exists)*

**Rule: capture without classification. Triage later.** If a target subfolder doesn't exist (e.g. `raw/emails/` not enabled), leave the file in `raw/` root until you decide.

#### 2. Triage

Daily (or as needed): move things from `raw/` root to their right home.

- Is a task? → `an inbox folder` (or straight to `next/` / `waiting/` / `someday/`)
- Is a calendar event? → `wiki/calendar/synced/` (one-time) or `wiki/calendar/recurring/` (recurring)
- Is a project? → `wiki/projects/<project-slug>/`
- Is an ongoing responsibility? → append to `wiki/areas/<area>.md`


When triaging, add `source: raw/captures/<filename>` to frontmatter for provenance.

#### 3. Daily brief

Open `wiki/daily/YYYY-MM-DD.md` each morning. Templater + Dataview auto-pull:

- Today's tasks (from `wiki/tasks/next/`)
- Overdue tasks
- This-week deadlines
- Active project names
- Today's calendar events

#### 4. Review cadence

| Frequency | Action |
|---|---|
| Daily | Clear `tasks/inbox/`, write daily reflection |
| Weekly | Review `tasks/next/` + `tasks/waiting/`, verify `calendar/recurring/` |
| Monthly | Move old `tasks/done/` → `archives/tasks/`, review all `projects/` status |
| Quarterly | Review all `areas/`, confirm each has recent focus |

---

## Naming conventions

| Item | Convention | Example |
|---|---|---|
| Folders, files | lowercase + dash | `engineering-mechanics-3/` |
| Dates | ISO 8601 (`YYYY-MM-DD`) | `2026-10-02.md` |
| Times in filenames | `HH-MM` (24h, dash not colon — colon breaks some filesystems) | `2026-10-02-09-30-meeting.md` |
| Slugs | dash-separated keywords | `cs-team-meeting` |
| Completed tasks archive | `wiki/tasks/done/YYYY-MM/` | `wiki/tasks/done/2026-10/...` |

| raw/ root files (informal) | descriptive slug | `meeting-thoughts.md` |
| `raw/captures/` | `YYYY-MM-DD-<slug>.md` | `2026-10-02-think-pomodoro.md` |
| `captures/` | `<source-slug>.md` (date optional) | `fluid-mech-2026-09-30-handout.md` |
| `raw/emails/` *(opt-in)* | `YYYY-MM-DD-<subject-or-sender>.md` | `2026-10-02-reply-to-bill.md` |

---

## Frontmatter conventions

#### Productivity mode

| Type | Required fields | Template |
|---|---|---|
| task | `date`, `type: task`, optional `project:`, `area:` | `templates/task.md` |
| project | `type: project`, `status:`, `area:` | `templates/project.md` |
| area | `type: area`, `status:` | `templates/area.md` |
| daily | `date`, `type: daily` | `templates/daily.md` |
| capture | `date`, `type: capture`, `source:` | `templates/capture.md` |
| event | `date`, `type: event`, `title`, `start`, `end` | `templates/event.md` |
| recurring-event | `type: recurring-event`, `title`, `start-time`, `duration`, `days`, `start-date` | `templates/recurring-event.md` |

---

## Wikilink style

- **Basename only**: `[[page-name]]` — never `[[wiki/summaries/foo]]`
- **Cross-folder**: `[[folder/page|Display Text]]` (only when needed)
- **Tasks ↔ projects/areas**: use frontmatter fields, not wikilinks (so Dataview can query)
- **Graph View**: shows the network — let it surprise you

If a wikilink target doesn't exist, it shows as broken (red). Lint pass should fix these.

---

## Commit convention

```
YYYY-MM-DD <type> | <description>
```

Common types:

| Type | Use for |
|---|---|
| `docs` | Documentation, READMEs, AGENTS.md changes |
| `init` | Initial commit / scaffold |
| `schema` | Frontmatter or folder schema changes |
| `task` | New task / task update |
| `area` | New area / area update |
| `project` | New project / project update |
| `event` | Calendar event |
| `cleanup` | Delete / archive / reorganize |
| `fix` | Bug fix, broken link, typo |
| `restructure` | Folder restructure |
| `plugins` | Plugin install / config / remove |
| `dashboard` | Dashboard layout / Dataview query |
| `sim` | Simulation run |

Commit body (after the title) should explain *why*, not restate *what*. 2-5 lines.

---

## What's excluded (YOU provide)

These are intentionally not in the template — your notes needs its own:

- `wiki/daily/YYYY-MM-DD.md` — your daily notes
- `wiki/tasks/next/*.md` — your active tasks
- `wiki/areas/*.md` — your areas of responsibility
- `wiki/projects/*/` — your projects
- `raw/captures/*.md` — your source captures
- `dashboard/` — your home dashboard (if any)
- `.obsidian/workspace.json` — Obsidian window layout (per-machine)
- `.obsidian/appearance.json` — your theme preferences

The skeleton gives you **shape**, you give it **life**.

---

## Adapting to your use

#### If forking for Productivity mode (default):

Delete the TEMPLATE banner and start adding tasks.

#### If forking for Knowledge mode:

Replace the `wiki/tasks/`, `wiki/calendar/` and `wiki/areas/` trees with the knowledge
folders, and swap the Task/Event/Area frontmatter rows in § Frontmatter conventions for
Concept/Entity rows. The `raw/` layer and the 3-layer model do not change.

#### If you need both:

Fork the repo twice — one per mode — and cross-reference with wikilinks
(e.g. `[[other-notes:concept-name]]`).

---

## Provenance (capture trace)

For every wiki page that came from a source, the trail should be:

```
raw/<source>.md  ──────┐
                       │  produced these wiki pages:
raw/captures/<date>-<slug>.md  (the "trace" — points to:)
                       ↓
              ┌────────┼────────┬────────┬────────┐
              ↓        ↓        ↓        ↓        ↓
         summary.md entity.md concept.md  ...    ...
```

The capture file in `raw/captures/` records which wiki pages were produced from which source. This is the source of truth for "where did this page come from?".

---

## Prohibited (across all modes)

- ❌ Edit files inside `raw/` once written (append a new capture instead)
- ❌ Skip frontmatter on any wiki page
- ❌ Mix uppercase / lowercase / camelCase in filenames
- ❌ Use `[[wiki/...]]` path-based wikilinks (use `[[basename]]`)
- ❌ Skip `log.md` updates — append-only, never rewrite
- ❌ Put book notes / study notes / topic wiki into a Productivity-mode notes — knowledge work belongs in a Knowledge-mode fork
- ❌ Add a `status:` field when Method B (folder location) already encodes it
- ❌ Leave `raw/` root backlog unprocessed for long periods (defeats the uncategorized buffer purpose)

---

## License

MIT License — Copyright © 2026 Gary Xie. See [LICENSE](LICENSE) for the full text.
