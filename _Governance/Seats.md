# Seats

**Owning seat:** Master (Tim)
**Status:** Live. 2026-08-17.

Seats can be added later without changing the database. Every seat still writes
into `00_Inbox/` (or runs the rebuild). Nobody writes sqlite by hand.

Cursor seats that hunt or cite URLs use the **url-catalog MCP** (search + drop).
The same `server.py` is what other desktop MCP hosts paste (see
`_Orchestration/Url-Catalog-Mcp/CLIENTS.md`). Remote models only GET
https://tk-sites.github.io/url-launcher/urls.json (last published snapshot).
They cannot write.

## Master (Tim)

Only bridge off this folder. Feeds URLs. Tells Scout to search. Names
destinations. Publishes Pages (or orders Maintainer to push `TK-Sites/url-launcher`).
May use every MCP tool.

## Maintainer (Cursor)

Runs `build.py` (MCP `rebuild_index`). Writes receipts. Assembles `99_Outbox`
copies. Does not edit ingest files unless Master said to. Does not invent a
second database. Does not push Pages unless Master said to.

## Scout

Search-the-web. **Before a hunt:** MCP `search_urls` / `lookup_url`. **Keepers:**
MCP `add_drop` (or a topic extract when the table is the unit of work). **End of
batch:** `rebuild_index` once. Never sqlite by hand. Never Pages push unless
Master said to.

New hunt seats later: same as Scout (search + drop). Add a heading here and, if
needed, `_Orchestration/<Seat>-Rig/`. They still dump into `00_Inbox/` and the
same rebuild. Schema does not change.
