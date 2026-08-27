Derived-from: 2026-08-17_claude-opus-5_url-hunt-01-research-infrastructure.md
Topic: Databasing
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 4 — Databasing / knowledge-base architecture

Bears directly on the open workstream `2026-08-13_universal-knowledge-base-location`.

| URL | Status | What it is |
| --- | --- | --- |
| https://datasette.io/tools/markdown-to-sqlite | `[S]` | Loads markdown + YAML into SQLite. A derived-index-from-plain-text pattern |
| https://docs.datasette.io | `[K]` | Datasette docs — publish and query SQLite; the canonical "derived, rebuildable index" tool |
| https://datasette.io/tutorials/data-analysis | `[S]` | Datasette + Python tutorial |
| https://markdowndb.com/ | `[S]` | MarkdownDB — markdown files into queryable SQL/JSON |
| https://github.com/sqliteai/sqlite-memory | `[S]` | Markdown-based agent memory over SQLite, offline-first sync |
| https://til.simonwillison.net/ | `[S]` | Working example: markdown files in git, SQLite index built from them |
| https://help.noteplan.co/article/155-how-to-organize-your-notes-and-folders-using-johnny-decimal-and-para | `[S]` | Johnny.Decimal + PARA combined into one folder scheme |
| https://johnnydecimal.com | `[K]` | Johnny.Decimal — the numbered-folder system this module's `00_/01_/02_` prefixes resemble |
| https://www.dsebastien.net/2022-04-29-johnny-decimal/ | `[S]` | Johnny.Decimal walkthrough |
| https://www.dsebastien.net/personal-knowledge-management-at-scale-analyzing-8-000-notes-and-64-000-links/ | `[S]` | What a PKM looks like at 8,000 notes — failure modes at scale |
| https://forum.zettelkasten.de/discussion/3205/information-and-knowledge-management-before-starting-doubts-and-questions | `[S]` | Zettelkasten forum — the "before starting" questions |
| https://zettelkasten.de | `[K]` | Zettelkasten.de root — method reference |
| https://help.obsidian.md | `[K]` | Obsidian help — plain-markdown vault, git-versionable |
| https://docs.logseq.com | `[K]` | Logseq docs — local-first outliner over plain files |

**The one that matters most:** the single-canonical-copy-plus-derived-index
pattern (`til.simonwillison.net`, `markdown-to-sqlite`) is exactly the shape this
module already asserts — `Returns/` is the only copy, `02_Corpus` is derived and
rebuildable. Worth putting in that workstream's `Context/` if Master chooses to.

## Associated companions

Official docs, source repos, sibling tools named in the blurbs, and well-known companion sites. `[K]` — asserted from knowledge, not a live-search mark.

| URL | Status | What it is |
| --- | --- | --- |
| https://www.sqlite.org | `[K]` | SQLite — the database the derived-index pattern actually uses |
| https://github.com/simonw/datasette | `[K]` | Datasette source |
| https://github.com/simonw/markdown-to-sqlite | `[K]` | markdown-to-sqlite source |
| https://datasette.io | `[K]` | Datasette project home |
| https://logseq.com | `[K]` | Logseq product home (docs already listed) |
