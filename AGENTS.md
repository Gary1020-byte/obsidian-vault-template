<!-- TEMPLATE-NOTE-START -->

# 📦 This is a TEMPLATE

This `AGENTS.md` is the canonical operations manual for **Personal-OS**, the vault it was forked from. When you use this repo as a starting point for a new vault:

- **Replace** any mention of "Personal-OS" or specific vault paths with your vault name
- **Keep** the general principles: three-layer model, Method B rules, commit convention, plugin workflow
- **Adapt** the folder layout section to match your mode (Personal-OS mode vs Knowledge-base mode)
- **Delete** this banner once you've adapted the file

<!-- TEMPLATE-NOTE-END -->---
date: 2026-10-02
type: meta
---

# AGENTS.md — Personal OS 代理準則

## 這個 Vault 是什麼

個人作業系統 vault。涵蓋**任務管理（GTD 簡化）、行事曆、Project 追蹤、Areas 持續責任、Email 整合、每日 reflection**。

> 書摘、學習筆記、topic wiki 不在本 vault 範圍，統一歸 <companion vault> vault。

設計借鑒 <companion vault> 的「不可變 inbox + wikilink 串連」模式，加上 GTD 與 PARA 兩個生產力方法論。

## 三層架構

```
Layer 1 ─ raw/                  不可變 inbox（所有東西先丟這）
Layer 2 ─ wiki/                tasks/ calendar/ projects/ areas/ daily/ archives/ 互相 wikilink
Layer 3 ─ meta                  index.md + log.md + AGENTS.md
```

### Layer 1 — raw/（不可變 inbox）
- 一旦寫入就不修改
- 三個子資料夾：`captures/`、`emails/drafts/`、`external/`
- 任何東西先 capture 再 triage，絕不繞過

### Layer 2 — wiki/（互相串連的資料網絡）
| 資料夾 | 角色 | 方法論 |
|---|---|---|
| [[wiki/tasks/README\|tasks/]] | 任務管理 | GTD 簡化 |
| [[wiki/calendar/README\|calendar/]] | 行事曆 | 三種檔案類型 schema |
| [[wiki/projects/README\|projects/]] | 有 deadline 的專案 | PARA |
| [[wiki/areas/README\|areas/]] | 無 deadline 的持續責任 | PARA |
| [[wiki/daily/README\|daily/]] | 每日 reflection | 1 日 1 檔 |
| [[wiki/archives/README\|archives/]] | 封存 | 不進 daily brief |

互相之間用 [[wikilinks]] 串：
- task 透過 frontmatter `project:` 欄位連到 [[templates/project]]
- task 透過 frontmatter `area:` 欄位連到 [[templates/area]]
- daily note 用 Dataview 自動拉 task / calendar / project
- dashboard 集中呈現

### Layer 3 — meta
- [[index\|index.md]] — vault 入口
- [[log\|log.md]] — append-only 變更記錄
- AGENTS.md（本檔）— 代理 / 協作準則

## Tooling 資料夾

| 資料夾 | 用途 |
|---|---|
| [[dashboard/README\|dashboard/]] | Obsidian 工作台單頁 |
| [[templates/]] | Templater 模板（task / project / area / daily / capture / event / recurring-event） |
| [[scripts/]] | 自動化腳本（future） |

## Workflow

### 1. Capture
新東西一律進 `raw/captures/`。
- 語音轉文字、隨手記、截圖 → `raw/captures/`
- AI 寫的 email reply draft → `raw/emails/drafts/`
- 從外部 ingest（網頁、書摘）→ `raw/external/`

原則：**capture 不分類，先丟再說**。

### 2. Triage
定期（建議每天）把 `raw/captures/` 分流到 `tasks/`、`calendar/`、`projects/`、`areas/`。
- 屬於任務 → `tasks/inbox/`（或直接放 `next/` / `waiting/` / `someday/`）
- 屬於行事曆事件 → `calendar/synced/` 或 `calendar/daily/`
- 屬於重複事件 → `calendar/recurring/`
- 屬於專案 → `projects/<project>/tasks/`
- 屬於持續責任 → `areas/<area>.md` 內新增段落
- 純筆記 / 學習 → 歸 <companion vault> vault（不在本 vault）

分流時 frontmatter 補上 `source: raw/captures/<filename>`。

### 3. Daily Brief
每天打開 `daily/YYYY-MM-DD.md` 看 brief。
- 模板用 [[templates/daily]]
- 自動 Dataview 拉「今天要做的 task / 過期 task / 本週 deadline / 活躍 project / 今日事件」

### 4. Review

| 頻率 | 動作 |
|---|---|
| 每日 | 清 `tasks/inbox/`、寫 daily reflection |
| 每週 | review `tasks/next/` 與 `tasks/waiting/`、確認 `calendar/recurring/` 正確 |
| 每月 | 把舊 `tasks/done/` 移到 `archives/tasks/`，review 所有 `projects/` 狀態 |
| 每季 | review `areas/`，確認每個 area 有近期重點 |

## 命名規範

- 資料夾、檔名：**lowercase + dash**
- 日期：**ISO 8601**（`YYYY-MM-DD`）
- 時間用於 event 檔名：**`HH-MM`**（24h，用 dash 不用 colon，避免檔名系統衝突）
- Slug：用 `-` 分隔關鍵字（例：`cs-team-meeting`）
- 完成 task 歸檔：`tasks/done/YYYY-MM/`

## Frontmatter 規範

各檔案類型對應模板：

| 類型 | 必填欄位 | 模板 |
|---|---|---|
| task | `date`, `type` | [[templates/task]] |
| project | `type`, `status`, `area` | [[templates/project]] |
| area | `type`, `status` | [[templates/area]] |
| daily | `date`, `type` | [[templates/daily]] |
| capture | `date`, `type` | [[templates/capture]] |
| event | `date`, `type`, `title`, `start`, `end` | [[templates/event]] |
| recurring-event | `type`, `title`, `start-time`, `duration`, `days`, `start-date` | [[templates/recurring-event]] |

詳細 schema 見各 [[templates/|Templates 資料夾]] 與各資料夾 README。

## Wikilink 風格

- 處處用 `[[wikilinks]]`
- 跨資料夾：`[[folder/page|顯示文字]]`
- 同資料夾：`[[page-name]]`
- task 連結 project / area **用 frontmatter 欄位**（不用 wikilink），方便 Dataview query
- 用 Graph View 看整體關係

## Areas vs Projects 判斷

| | Project | Area |
|---|---|---|
| Deadline | 有 | 沒有 |
| 完成條件 | 明確 | 持續責任 |
| 結束動作 | 移 `archives/projects/` | 不結束，只 review |
| 範例 | 搬家、論文、網站改版 | 健康、財務、職涯 |

## Email 整合

- 進：`raw/emails/inbox/`（未來）
- AI 寫的 reply draft：`raw/emails/drafts/`
- 標籤 / 優先序：透過 frontmatter `priority:`、`tags:` 欄位
- 送出後：把對應 task 標 `status: sent`，歸 `tasks/done/YYYY-MM/`

## 禁止

- ❌ 不要直接編輯 `raw/` 內的檔案
- ❌ 不要略過 frontmatter
- ❌ 不要混用大小寫命名
- ❌ 不要把書摘、學習筆記、topic wiki 放這——歸 <companion vault> vault
- ❌ 不要在 `projects/` 放無 deadline 的東西（那是 area）
