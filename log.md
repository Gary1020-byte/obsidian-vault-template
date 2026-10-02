# Operation Log

Chronological, append-only record of changes to this vault.

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
| `init` | Initial scaffold / new vault setup |
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

## [YYYY-MM-DD] init | vault-template skeleton

- Add AGENTS.md (operations manual)
- Add 7 templates under `templates/` (area, capture, daily, event, project, recurring-event, task)
- Add `.obsidian/` config: app.json, community-plugins.json, core-plugins.json
- Add 4 plugin data.json: dataview, obsidian-tasks, quickadd, templater
- Create folder skeleton: `raw/{captures,emails,drafts,external}/` + `wiki/{tasks,calendar,projects,areas,daily,archives}/`
- Add README.md, index.md (skeleton), log.md (this file)

Reusable Obsidian vault skeleton. Adapt the wiki/ folder layout to match your workflow.