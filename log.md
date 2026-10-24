# Operation Log

Chronological, append-only record of changes to this notes.

Each entry:

```
## [YYYY-MM-DD] <type> | <short description>

- bullet describing what changed
- bullet describing another change
- file: path/to/file.md
```

`<type>` is one of:

| Type | Use for |
|---|---|
| `init` | Initial scaffold / new notes setup |
| `docs` | AGENTS.md / README / index.md edits |
| `schema` | Frontmatter schemas, folder structure changes |
| `test` | Importing test data (then clean up with `cleanup`) |
| `sim` | Simulator runs / agent exercises |
| `dashboard` | Home / Dataview queries |
| `plugins` | Plugin install / enable / config |
| `cleanup` | Removing test data, empty files, leftovers |
| `fix` | Bug fixes, broken links, typos |
| `restructure` | Folder / file relocation |
| `task` | New / completed / moved task |
| `area` | New / edited area page |
| `project` | New / edited project page |
| `capture` | New capture moved from raw to wiki |
| `ingest` | Raw → wiki ingest of a source |
| `lesson` | New #lesson card |
| `comparison` | New comparison page |
| `overview` | New overview page |

---

## [YYYY-MM-DD] init | notes-template skeleton

- Add AGENTS.md (operations manual)
- Add 7 templates under `templates/` (area, capture, daily, event, project, recurring-event, task)
- Add `.obsidian/` config: app.json, community-plugins.json, core-plugins.json
- Add 5 plugin data.json: calendar, dataview, obsidian-tasks, quickadd, templater
- Create folder skeleton: `raw/{captures,external}/` + `wiki/{tasks,calendar,projects,areas,daily,archives}/`
- Add README.md, index.md (skeleton), log.md (this file)

Reusable Obsidian notes skeleton. Adapt the wiki/ folder layout to match your workflow.

## [2026-10-24] fix | make the template internally consistent

- Rename the `Productivity` mode to `Productivity` and add the `Knowledge` mode row
  the docs already promised — the template is forked by strangers, and one of
  them was named in it
- Drop `the sync plugin` from `community-plugins.json`: it was in the list but had
  no committed config, so Obsidian would enable a plugin the template never set up
- Add the missing `calendar/data.json` so all 5 advertised plugins are configured
- Fix a broken table row in AGENTS.md (the `cleanup` row was missing its leading pipe)
- Add trailing newlines to the 7 files that lacked one
- Add `check_template.py` and wire it into CI so the next drift is caught automatically
- Add CI, Dependabot, CONTRIBUTING.md, and issue templates
