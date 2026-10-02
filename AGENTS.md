<!--
📦 TEMPLATE-NOTE
This file is the operations manual for the vault-template repo. It supports
two main use modes (Personal-OS and Knowledge-base) plus a hybrid variant.

When forking this repo for a new vault:
1. Decide your mode (Personal-OS / Knowledge-base / Hybrid) — see top section
2. Rename the wiki/ subfolders to match your mode
3. Replace template names with your vault name in any prose
4. Update the "What YOU provide" section to match what data you will keep
5. Delete this banner block once adapted
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

This template ships with Personal-OS scaffolding but the same skeleton supports **three modes**. Choose based on what your vault is for:

| Mode | Best for | `wiki/` subfolders | Example vault |
|---|---|---|---|
| **A. Personal-OS** (productivity) | GTD, calendar, areas, projects, daily notes | `tasks/{inbox,next,waiting,someday,done}/`, `calendar/{daily,recurring,synced}/`, `projects/`, `areas/`, `daily/`, `archives/{projects,tasks}/` | This repo's default |
| **B. Knowledge-base** (LLM Wiki style) | Course notes, papers, book summaries, concepts | `entities/`, `concepts/`, `overviews/`, `comparisons/`, `summaries/`, `lessons/` | <companion vault> (see README "Reference" section) |
| **C. Hybrid** | Both — personal vault + linked knowledge base | **A — plus** — symlink or git submodule to a sibling knowledge-base vault | Common: Personal-OS vault + <companion vault> vault side-by-side |

**Choose now and continue to the matching Workflow section below:**

- Mode A → [§ Workflow — Personal-OS](#workflow--personal-os-mode)
- Mode B → [§ Workflow — Knowledge-base](#workflow--knowledge-base-mode)
- Mode C → run two sibling repos (this template forked twice)

---

## The 3-layer model (every mode)

```
Layer 1  raw/        immutable inbox. Agents read; never edit.
Layer 2  wiki/       work surface. Edit, evolve, wikilink.
Layer 3  meta        AGENTS.md + index.md + log.md (schema, map, history)
```

| Layer | What lives here | Rule |
|---|---|---|
| `raw/` | Captures, emails, source files (PDFs, lecture notes, transcripts) | **Two sub-layers**: root = uncategorized buffer, subfolders = categorized. See § raw/ two-layer model below. |
| `wiki/` | Tasks, events, projects, areas, daily notes, summaries, entities, concepts | Edit freely. Use wikilinks. Follow Method B for status. |
| meta | `AGENTS.md` (this file), `index.md` (map), `log.md` (history) | `index.md` = wikilinks-only, never describe. `log.md` = append-only. |

---

## raw/ two-layer model

The `raw/` layer itself splits into two:

| Sub-layer | Location | Purpose |
|---|---|---|
| **Layer 1 — uncategorized** | `raw/` root (e.g. `raw/2026-10-02-meeting-thought.md`) | Quick-drop buffer. No `type:` required. Triage target. |
| **Layer 2 — categorized** | `raw/<sub>/` subfolders | Post-triage home. Organized by source type. |

### The three categorized subfolders

| Subfolder | Holds | Naming convention |
|---|---|---|
| `raw/captures/` | Your own time-stamped records: voice notes, screenshots, reflections, meeting minutes | `YYYY-MM-DD-<slug>.md` |
| `raw/external/` | Third-party sources ingested for reading: web clips, book chapters, lecture handouts, PDFs → markdown | `<source-slug>.md` (often includes source identifier, e.g. `fluid-mech-2026-09-30-handout.md`) |
| `raw/emails/` | Email correspondence, both inbound and outbound (including AI-drafted replies) | `YYYY-MM-DD-<subject-or-sender>.md` |

### Triage flow

1. **Drop** anything into `raw/` root first — no classification needed (e.g. `raw/2026-10-02-something.md`)
2. **Triage** daily (or as needed): move the file into the matching subfolder and rename to convention if needed
3. **Add provenance**: when the file is consumed into a wiki page, link via frontmatter `source: raw/...`

### Rules

- ❌ Never leave files in `raw/` root indefinitely — backlog kills the buffer
- ❌ Never edit a raw/ file once written (append a new capture instead)
- ✅ When unsure which subfolder fits, leave in root and decide next triage
- ✅ Filenames in root can be informal — rename when triaged

---

## Method B: location = status

**No `status:` field.** Folder placement encodes state.

| Concept | "Active" location | "Done" location |
|---|---|---|
| Task (active work) | `wiki/tasks/next/` | `wiki/tasks/done/` |
| Task (blocked) | `wiki/tasks/waiting/` | `wiki/tasks/done/` (with `resolved:` date) |
| Task (untriaged) | `raw/captures/YYYY-MM-DD-*.md` | `wiki/tasks/inbox/` (with `triaged:` + `triage_target:`) |
| Task (maybe later) | `wiki/tasks/someday/` | `wiki/tasks/done/` or `archives/tasks/` |
| Calendar event (one-time) | `wiki/calendar/synced/` | end date `===` passes |
| Calendar event (recurring instance) | `wiki/calendar/daily/` | end date passes |
| Daily note | `wiki/daily/YYYY-MM-DD.md` | today's file exists |
| **KB — Source** | `raw/<source>.md` (or root before triage) | stays there forever |
| **KB — Summary** | `wiki/summaries/<source>.md` | superseded → `wiki/archives/summaries/` |
| **KB — Lesson** | `wiki/lessons/<topic>.md` | rarely archive; superseded by newer lesson |

---

## Workflow — Personal-OS mode

#### 1. Capture

New stuff always goes to `raw/` first (root or subfolder, see § raw/ two-layer model).

- Voice-to-text notes, quick thoughts, screenshots → `raw/` root (triage later) or straight to `raw/captures/`
- AI-written email reply drafts → `raw/emails/`
- Web clipper outputs, book/PDF highlights → `raw/external/`

**Rule: capture without classification. Triage later.**

#### 2. Triage

Daily (or as needed): move things from `raw/` root to their right home.

- Is a task? → `wiki/tasks/inbox/` (or straight to `next/` / `waiting/` / `someday/`)
- Is a calendar event? → `wiki/calendar/synced/` (one-time) or `wiki/calendar/recurring/` (recurring)
- Is a project? → `wiki/projects/<project-slug>/`
- Is an ongoing responsibility? → append to `wiki/areas/<area>.md`
- Is study / book note / topic wiki? → **out of scope, push to <companion vault> vault**

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

## Workflow — Knowledge-base mode

#### 1. Ingest (the core operation)

Read sources, write wiki pages, leave trace.

1. **Drop source into `raw/`** — either `raw/<source-slug>.md` directly, or `raw/` root first then triage to `raw/external/`. Never edit after writing.
2. **Write a summary** — `wiki/summaries/<source-slug>.md` (1-3 paragraphs capturing essence). One source → one summary (usually).
3. **Extract entities** — `wiki/entities/<name>.md` for concrete things (persons, systems, tools). Update existing pages instead of duplicating.
4. **Extract concepts** — `wiki/concepts/<concept-slug>.md` for abstract patterns / theories / definitions.
5. **Write overview** (if a topic emerges) — `wiki/overviews/<topic>.md` ties multiple concepts together.
6. **Write comparison** (if comparing things helps) — `wiki/comparisons/<comparison-slug>.md` (e.g. "water pump vs air pump").
7. **Update `index.md`** — add new entries to the right section (Entities / Concepts / Comparisons / Summaries / Overviews / Lessons).
8. **Append `log.md`** — `## [YYYY-MM-DD] ingest | <source-title>`
9. **Leave capture trace** — `raw/captures/<date>-<slug>.md` pointing to all pages created from this source.

**Expect 10-15 wiki pages per source.** That is the point.

#### 2. Query (also accumulates)

When the user asks a question:

1. Read `index.md` to locate relevant entries.
2. Synthesize an answer.
3. **Save the answer back to a wiki page** (usually `comparison` or `overview`) — so future queries compound.

#### 3. Lint (every 1-2 weeks)

Find and fix:

- **Orphan pages** — pages with no incoming wikilinks
- **Conflict candidates** — same entity with conflicting attributes across pages
- **Superseded statements** — newer source contradicts older page
- **Broken wikilinks** — links to non-existent pages

Append `log.md`: `## [YYYY-MM-DD] lint | pass`

#### 4. raw-only mode (lightweight variant)

If you only want to capture sources without writing wiki pages: just write to `raw/`, skip the rest. The mode is what you do, not what the repo forces.

---

## Naming conventions

| Item | Convention | Example |
|---|---|---|
| Folders, files | lowercase + dash | `engineering-mechanics-3/` |
| Dates | ISO 8601 (`YYYY-MM-DD`) | `2026-10-02.md` |
| Times in filenames | `HH-MM` (24h, dash not colon — colon breaks some filesystems) | `2026-10-02-09-30-meeting.md` |
| Slugs | dash-separated keywords | `cs-team-meeting` |
| Completed tasks archive | `wiki/tasks/done/YYYY-MM/` | `wiki/tasks/done/2026-10/...` |
| KB lessons | prefix `LESSON: ` in title | `LESSON: wikilink path-vs-basename` |
| raw/ root files (informal) | descriptive slug | `meeting-thoughts.md` |
| raw/captures/ | `YYYY-MM-DD-<slug>.md` | `2026-10-02-think-pomodoro.md` |
| raw/external/ | `<source-slug>.md` (date optional) | `fluid-mech-2026-09-30-handout.md` |
| raw/emails/ | `YYYY-MM-DD-<subject-or-sender>.md` | `2026-10-02-reply-to-bill.md` |

---

## Frontmatter conventions

#### Personal-OS mode

| Type | Required fields | Template |
|---|---|---|
| task | `date`, `type: task`, optional `project:`, `area:` | `templates/task.md` |
| project | `type: project`, `status:`, `area:` | `templates/project.md` |
| area | `type: area`, `status:` | `templates/area.md` |
| daily | `date`, `type: daily` | `templates/daily.md` |
| capture | `date`, `type: capture`, `source:` | `templates/capture.md` |
| event | `date`, `type: event`, `title`, `start`, `end` | `templates/event.md` |
| recurring-event | `type: recurring-event`, `title`, `start-time`, `duration`, `days`, `start-date` | `templates/recurring-event.md` |

#### Knowledge-base mode

Every wiki page:

```yaml
---
date: YYYY-MM-DD          # when this wiki page was written
type: entity | concept | overview | comparison | summary | lesson
tags: [tag1, tag2]
status: active | superseded | archived
sources: N               # how many raw/ sources back this page
---
```

`type` is required so adopters can Dataview-query by type.

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
| `ingest` | KB-mode: ingest new source (produces multiple wiki pages) |
| `lint` | KB-mode: fix wikilinks / orphans / conflicts |
| `comparison` | KB-mode: new comparison page |
| `overview` | KB-mode: new overview page |
| `lesson` | KB-mode: new lesson card |
| `cleanup` | Delete / archive / reorganize |
| `fix` | Bug fix, broken link, typo |
| `restructure` | Folder restructure |
| `plugins` | Plugin install / config / remove |
| `dashboard` | Dashboard layout / Dataview query |
| `sim` | Simulation run |

Commit body (after the title) should explain *why*, not restate *what*. 2-5 lines.

---

## What's excluded (YOU provide)

These are intentionally not in the template — your vault needs its own:

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

#### If forking for Personal-OS (Mode A):

Default state. Just delete the TEMPLATE banner.

#### If forking for Knowledge-base (Mode B):

1. **Restructure `wiki/`** — delete `{tasks,calendar,projects,areas,daily,archives}/`, add `{entities,concepts,overviews,comparisons,summaries,lessons}/`
2. **Update `templates/`** — keep `capture.md`, add `summary.md`, `entity.md`, `concept.md`, `overview.md`, `comparison.md`, `lesson.md`
3. **Update AGENTS.md** — change § Workflow — Personal-OS to § Workflow — Knowledge-base
4. **Update `index.md`** — keep Entities / Concepts / Overviews / Comparisons / Lessons, drop Tasks / Calendar / Projects / Areas / Daily
5. **Add `type:` field** — see Frontmatter Knowledge-base above

#### If forking for Hybrid (Mode C):

Fork the repo twice — one as Mode A, one as Mode B. Use wikilinks (e.g. `[[other-vault:concept-name]]`) to cross-reference between them.

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
- ❌ Put book notes / study notes / topic wiki into a Personal-OS vault (they belong in a KB vault)
- ❌ Add a `status:` field when Method B (folder location) already encodes it
- ❌ Leave `raw/` root backlog unprocessed for long periods (defeats the uncategorized buffer purpose)

---

## License

MIT License — Copyright © 2026 Gary Xie. See [LICENSE](LICENSE) for the full text.