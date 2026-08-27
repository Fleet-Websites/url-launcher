# Ingest convention

**Owning seat:** Maintainer (Cursor)
**Status:** Live. 2026-08-17.

The capture step does not grow. Two cheap shapes, same database after rebuild.

## Topic extracts — `00_Inbox/Topics/YYYY-MM-DD_topic_<slug>.md`

Four header lines, then a table:

```
Derived-from: <file or "drop" or "scout">
Topic: Human name
On: YYYY-MM-DD
Kind: Topic extract.

| URL | Description |
|-----|-------------|
| https://example.com | one-line blurb |
```

Hunt 01–03 style (`URL | Status | What it is` with `[S]`/`[K]`) is also valid.
Do not fake `[S]` unless a live search this session returned it.

Use an extract when the table is the unit of work (a real topic hunt). Standing
“I found a link in this chat” goes to Drops.

## Drops — `00_Inbox/Drops/YYYY-MM-DD_drop_<slug>.md`

One file **per topic per day**. MCP `add_drop` appends here. Thinner than
extracts. Header optional beyond `Topic:` if you have one. Then one URL per
line, optional blurb after the URL:

```
Topic: Optional topic
On: YYYY-MM-DD

https://example.com optional blurb
```

No topic → `YYYY-MM-DD_drop_untopiced.md`. Tables are accepted too. Skip
`README.md`. Same URL in the same topic is skipped; same URL in a new topic is
a second mention.

## After ingest

Maintainer (or Scout at end of a drop batch) runs `build.py` / MCP
`rebuild_index` **once per batch**, not after every URL. Same `urls.sqlite`.
Same Pages JSON. No extra fields at capture time. Rebuild does not publish.
