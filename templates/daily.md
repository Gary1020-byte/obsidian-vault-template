---
date: <% tp.date.now("YYYY-MM-DD") %>
type: daily
---

# <% tp.date.now("YYYY-MM-DD") %>

## 今天要做

\`\`\`dataview
TASK
FROM "wiki/tasks"
WHERE due = date(<% tp.date.now("YYYY-MM-DD") %>) AND !completed
\`\`\`

## 過期 task

\`\`\`dataview
TASK
FROM "wiki/tasks"
WHERE due < date(<% tp.date.now("YYYY-MM-DD") %>) AND status != "done"
SORT due ASC
\`\`\`

## 本週 deadline

\`\`\`dataview
TASK
FROM "wiki/tasks"
WHERE due >= date(<% tp.date.now("YYYY-MM-DD") %>) AND due <= date(<% tp.date.now("YYYY-MM-DD", 7) %>) AND status != "done"
SORT due ASC
\`\`\`

## 活躍 project

\`\`\`dataview
LIST
FROM "wiki/projects"
WHERE status = "active"
SORT file.mtime DESC
\`\`\`

## Calendar 今日事件

## 今日 reflection

### 做了什麼

### 學到什麼

### 卡在哪
