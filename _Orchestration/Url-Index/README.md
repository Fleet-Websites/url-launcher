# URL Index

**Owning seat:** Maintainer (Cursor)
**Status:** Live. 2026-08-17. This module is the site.

Parses **only** `00_Inbox/Topics/` (`*_topic_*`) and `00_Inbox/Drops/` (`*_drop_*`)
in this folder. Does not reach Research-Sandbox, hunt originals, Corpus, or KB.

Markdown is canonical. `urls.sqlite` and `site/urls.json` are derived. One
database. Cursor seats query this sqlite through `_Orchestration/Url-Catalog-Mcp/`.
Remote models GET the published `urls.json`. Do not mint a second store.

## Run

```
python3 build.py
```

Safe to run repeatedly. Receipts use `-b`, `-c` if today's name is taken.
This rig does not write Outbox and does not push.

## Schema

Same as the original index: `url`, `source` (`kind` `hunt_extract` or `drop`),
`mention`, `mention_fts`. `workstream` stays in the schema as null so the
database shape does not change when seats are added.

## Publish

After a rebuild, copy `site/index.html` and `site/urls.json` into a new
`99_Outbox/` release with a Manifest. Master publishes to
`TK-Sites/url-launcher`. Bookmark: https://tk-sites.github.io/url-launcher/
