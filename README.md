# URL catalog

**Owning seat:** Master (Tim). Maintainer rebuilds. Scout searches.
**Public bookmark:** https://tk-sites.github.io/url-launcher/
**Home:** `/Volumes/FLEET-01/FLEET-01/Websites/url-catalog`

This folder is the site. Research-Sandbox is not the source of truth anymore.

Markdown in `00_Inbox/` is canonical. `urls.sqlite` and `site/urls.json` are
derived. If they vanished, `python3 _Orchestration/Url-Index/build.py` regenerates
them. There is **one database**. Future search-engine work reads that sqlite.
Do not mint a second store.

## APIs

| Who | Read | Write |
|---|---|---|
| Cursor seats | url-catalog MCP (`search_urls`, `lookup_url`) against sqlite | MCP `add_drop` → Drops, then `rebuild_index` once per batch |
| You, in this folder | sqlite / files | Drops or Topics, then `build.py` |
| ChatGPT / Claude in a browser | GET https://tk-sites.github.io/url-launcher/urls.json (last **published** snapshot) | None. Paste here, or a Cursor seat drops |

MCP lives in `_Orchestration/Url-Catalog-Mcp/`. Desktop and local MCP hosts
use the same `server.py` (read + write via Drops). Browser models GET the
published `urls.json` only. How to paste the snippet into Claude Desktop,
Claude Code, LM Studio, VS Code, and browsers:
`_Orchestration/Url-Catalog-Mcp/CLIENTS.md` (click-by-click, including
full JSON to paste). The rig does not write sqlite and does not push
Pages. Remote models lag until Master publishes.

## Feed URLs

**You paste:** add a file under `00_Inbox/Drops/` (see that folder's README).

**You tell an agent to search:** Scout checks the catalog first, then writes a
topic extract under `00_Inbox/Topics/` or a drop file. Then rebuild.

## Rebuild

```
python3 _Orchestration/Url-Index/build.py
```

Then copy `site/index.html` and `site/urls.json` into a new `99_Outbox/` release
with a Manifest. Master (or Maintainer on Master's instruction) pushes to
`TK-Sites/url-launcher`. The rig does not push.

## What this never does

- Reach into Research-Sandbox, hunt originals, Corpus, or `_Knowledge-Base`
- Overwrite an Outbox folder
- Trash files
- Write sqlite by hand

## Home decision (23 Aug 2026)

**Stay (Tim chose A).** This is the LIST of keeper URLs. It already lives at `Websites/url-catalog/`. `Websites/` is the top-level activity for sites Tim hosts. Hosted projects land as **siblings** of this folder when they exist — not inside the catalog. A FLEET-01-internal move would not race the MacAppSSD rclone; we still **do not move** because this home is already the right kind. Do not turn this catalog into a hosting farm.
