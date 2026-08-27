# URL Catalog MCP

**Owning seat:** Maintainer (Cursor)
**Status:** Live. 2026-08-17.

Stdio MCP. Absolute paths to this module, so any chat can use it.
Cursor is already registered. Other desktop apps: see `CLIENTS.md`.

- **Read:** `urls.sqlite` (FTS). Never a second store.
- **Write:** append `00_Inbox/Drops/YYYY-MM-DD_drop_<slug>.md` only.
- **Rebuild:** runs `../Url-Index/build.py`. Does not push Pages.
- **Framing:** newline JSON (Cursor) and `Content-Length` (Claude Desktop and most other hosts). Reply matches the client.

## Tools

| Tool | Seat | What |
|---|---|---|
| `search_urls` | Scout and up | FTS before a web hunt |
| `lookup_url` | Scout and up | One URL, every topic it is in |
| `add_drop` | Scout and up | Append a Drop line |
| `rebuild_index` | Maintainer; Scout after a batch | Regenerate sqlite + `urls.json` |

## Register

Same command everywhere:

```
python3 /Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py
```

Cursor: user-level `~/.cursor/mcp.json` server `url-catalog`. Restart Cursor MCP after changing that file.

Claude Desktop, Claude Code, LM Studio, VS Code / Continue, and browser
read-only: step-by-step in `CLIENTS.md` (written as if you have never
done this). Copy the full JSON box, not a fragment, unless the file
already has other servers.

Remote models do not use this. They GET https://tk-sites.github.io/url-launcher/urls.json
