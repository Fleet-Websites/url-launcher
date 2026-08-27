#!/usr/bin/env python3
"""Stdio MCP for the URL catalog. Reads sqlite. Writes Drops only. Never sqlite."""

from __future__ import annotations

import json
import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE.parent / "Url-Index"
BUILD = INDEX / "build.py"
DB_PATH = INDEX / "urls.sqlite"
MODULE_ROOT = HERE.parent.parent
DROPS = MODULE_ROOT / "00_Inbox" / "Drops"

sys.path.insert(0, str(INDEX))
from build import URL_RE, normalize  # noqa: E402

SERVER_NAME = "url-catalog"
SERVER_VERSION = "1.1.0"
PROTOCOL = "2024-11-05"
MAX_HITS = 50
SLUG_RE = re.compile(r"[^a-z0-9]+")
FTS_BOOL = frozenset({"and", "or", "not"})

_framing = "ndjson"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def send(obj: dict) -> None:
    payload = json.dumps(obj, ensure_ascii=False)
    if _framing == "lsp":
        raw = payload.encode("utf-8")
        header = f"Content-Length: {len(raw)}\r\n\r\n".encode("ascii")
        sys.stdout.buffer.write(header + raw)
        sys.stdout.buffer.flush()
        return
    sys.stdout.write(payload + "\n")
    sys.stdout.flush()


def result(msg_id, payload) -> None:
    send({"jsonrpc": "2.0", "id": msg_id, "result": payload})


def rpc_error(msg_id, code: int, message: str) -> None:
    send({"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}})


def tool_text(msg_id, text: str, is_error: bool = False) -> None:
    result(
        msg_id,
        {
            "content": [{"type": "text", "text": text}],
            "isError": is_error,
        },
    )


def slugify(text: str) -> str:
    slug = SLUG_RE.sub("-", text.lower()).strip("-")
    return slug[:80] or "untopiced"


def topic_and_slug(args: dict) -> tuple[str, str]:
    topic = str(args.get("topic") or "").strip()
    slug = str(args.get("topic_slug") or "").strip()
    if slug:
        slug = slugify(slug)
    elif topic:
        slug = slugify(topic)
    else:
        slug = "untopiced"
    if not topic:
        topic = "" if slug == "untopiced" else slug.replace("-", " ")
    return topic, slug


def drop_path(slug: str) -> Path:
    return DROPS / f"{date.today().isoformat()}_drop_{slug}.md"


def fts_queries(q: str) -> list[str]:
    q = q.strip()
    if not q:
        return []
    escaped = q.replace('"', '""')
    queries = [f'"{escaped}"']
    tokens = [
        t for t in re.findall(r"[A-Za-z0-9]+", q) if t.lower() not in FTS_BOOL
    ]
    if tokens:
        and_q = " AND ".join(f'"{t}"' for t in tokens)
        if and_q not in queries:
            queries.append(and_q)
    return queries


def mention_row(cur: sqlite3.Row) -> dict:
    return {
        "url": cur["url_raw"],
        "url_norm": cur["url_norm"],
        "host": cur["host"],
        "blurb": cur["blurb"] or "",
        "status": cur["status"],
        "topic": cur["topic"] or "",
        "topic_slug": cur["topic_slug"] or "",
        "kind": cur["kind"],
        "source": cur["path"],
    }


def open_db() -> sqlite3.Connection:
    if not DB_PATH.is_file():
        raise FileNotFoundError(
            f"missing {DB_PATH}; run rebuild_index (python3 {BUILD})"
        )
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def search_urls(args: dict) -> dict:
    q = str(args.get("q") or "").strip()
    topic_slug = str(args.get("topic_slug") or "").strip()
    try:
        limit = int(args.get("limit") or 25)
    except (TypeError, ValueError):
        limit = 25
    limit = max(1, min(limit, MAX_HITS))
    if not q:
        raise ValueError("q is required")
    queries = fts_queries(q)
    conn = open_db()
    try:
        seen: set[tuple[str, str]] = set()
        hits: list[dict] = []
        for fts_q in queries:
            sql = """
                SELECT url.url_raw, url.url_norm, url.host, mention.blurb, mention.status,
                       source.topic, source.topic_slug, source.kind, source.path
                FROM mention_fts
                JOIN mention ON mention.rowid = mention_fts.rowid
                JOIN url ON url.url_norm = mention.url_norm
                JOIN source ON source.path = mention.source_path
                WHERE mention_fts MATCH ?
            """
            params: list = [fts_q]
            if topic_slug:
                sql += " AND source.topic_slug = ?"
                params.append(topic_slug)
            sql += " LIMIT ?"
            params.append(limit)
            try:
                rows = conn.execute(sql, params).fetchall()
            except sqlite3.OperationalError:
                continue
            for row in rows:
                key = (row["url_norm"], row["path"])
                if key in seen:
                    continue
                seen.add(key)
                hits.append(mention_row(row))
                if len(hits) >= limit:
                    break
            if len(hits) >= limit:
                break
        return {"query": q, "count": len(hits), "mentions": hits}
    finally:
        conn.close()


def lookup_url(args: dict) -> dict:
    raw = str(args.get("url") or "").strip()
    if not raw:
        raise ValueError("url is required")
    norm, raw_kept, host = normalize(raw)
    conn = open_db()
    try:
        rows = conn.execute(
            """
            SELECT url.url_raw, url.url_norm, url.host, mention.blurb, mention.status,
                   source.topic, source.topic_slug, source.kind, source.path
            FROM mention
            JOIN url ON url.url_norm = mention.url_norm
            JOIN source ON source.path = mention.source_path
            WHERE mention.url_norm = ?
            """,
            (norm,),
        ).fetchall()
        mentions = [mention_row(r) for r in rows]
        return {
            "url": raw_kept,
            "url_norm": norm,
            "host": host,
            "in_catalog": bool(mentions),
            "count": len(mentions),
            "mentions": mentions,
        }
    finally:
        conn.close()


def urls_in_drop_file(path: Path) -> set[str]:
    found: set[str] = set()
    if not path.is_file():
        return found
    text = path.read_text(encoding="utf-8")
    for match in URL_RE.finditer(text):
        token = match.group(0).rstrip(".,;:)")
        try:
            norm, _, _ = normalize(token)
        except ValueError:
            continue
        found.add(norm)
    return found


def already_in_topic(norm: str, slug: str) -> dict | None:
    try:
        conn = open_db()
    except FileNotFoundError:
        return None
    try:
        row = conn.execute(
            """
            SELECT url.url_raw, url.url_norm, url.host, mention.blurb, mention.status,
                   source.topic, source.topic_slug, source.kind, source.path
            FROM mention
            JOIN url ON url.url_norm = mention.url_norm
            JOIN source ON source.path = mention.source_path
            WHERE mention.url_norm = ? AND IFNULL(source.topic_slug, '') = ?
            LIMIT 1
            """,
            (norm, slug),
        ).fetchone()
        return mention_row(row) if row else None
    finally:
        conn.close()


def add_drop(args: dict) -> dict:
    raw = str(args.get("url") or "").strip()
    blurb = re.sub(r"\s+", " ", str(args.get("blurb") or "").strip())
    if not raw:
        raise ValueError("url is required")
    norm, raw_kept, host = normalize(raw)
    topic, slug = topic_and_slug(args)
    existing = already_in_topic(norm, slug)
    if existing:
        return {
            "added": False,
            "reason": "already in this topic",
            "url": raw_kept,
            "url_norm": norm,
            "topic": topic,
            "topic_slug": slug,
            "existing": existing,
        }
    DROPS.mkdir(parents=True, exist_ok=True)
    path = drop_path(slug)
    if norm in urls_in_drop_file(path):
        return {
            "added": False,
            "reason": "already in today's drop file for this topic",
            "url": raw_kept,
            "url_norm": norm,
            "topic": topic,
            "topic_slug": slug,
            "file": path.relative_to(MODULE_ROOT).as_posix(),
        }
    line = raw_kept if not blurb else f"{raw_kept} {blurb}"
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        if text and not text.endswith("\n"):
            text += "\n"
        path.write_text(text + line + "\n", encoding="utf-8")
    else:
        header = [f"On: {date.today().isoformat()}", ""]
        if topic:
            header.insert(0, f"Topic: {topic}")
        path.write_text("\n".join(header) + "\n" + line + "\n", encoding="utf-8")
    return {
        "added": True,
        "url": raw_kept,
        "url_norm": norm,
        "host": host,
        "blurb": blurb,
        "topic": topic,
        "topic_slug": slug,
        "file": path.relative_to(MODULE_ROOT).as_posix(),
        "note": "sqlite is stale until rebuild_index",
    }


def rebuild_index() -> dict:
    if not BUILD.is_file():
        raise FileNotFoundError(f"missing {BUILD}")
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(INDEX),
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    if proc.returncode != 0:
        raise RuntimeError(err or out or f"build.py exited {proc.returncode}")
    return {"ok": True, "stdout": out, "stderr": err}


TOOLS = [
    {
        "name": "search_urls",
        "description": (
            "Search the URL catalog sqlite (FTS on url, blurb, topic). "
            "Call before a web hunt. Does not write."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Search text"},
                "topic_slug": {
                    "type": "string",
                    "description": "Optional topic slug filter, e.g. cryptids",
                },
                "limit": {"type": "integer", "description": "Max hits, default 25, max 50"},
            },
            "required": ["q"],
        },
    },
    {
        "name": "lookup_url",
        "description": "Look up one URL in the catalog. Returns every topic it already sits in.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "http(s) URL"},
            },
            "required": ["url"],
        },
    },
    {
        "name": "add_drop",
        "description": (
            "Append a URL to today's Drop file for a topic. Markdown only; does not "
            "write sqlite. Skip if that URL is already in the same topic. After a "
            "batch, call rebuild_index once."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "blurb": {"type": "string", "description": "One-line blurb"},
                "topic": {"type": "string", "description": "Human topic name"},
                "topic_slug": {"type": "string", "description": "Topic slug if known"},
            },
            "required": ["url"],
        },
    },
    {
        "name": "rebuild_index",
        "description": (
            "Rebuild urls.sqlite and site/urls.json from Topics + Drops. "
            "Call once per drop batch, not after every URL. Does not push Pages."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def dispatch_tool(name: str, args: dict):
    if name == "search_urls":
        return search_urls(args)
    if name == "lookup_url":
        return lookup_url(args)
    if name == "add_drop":
        return add_drop(args)
    if name == "rebuild_index":
        return rebuild_index()
    raise ValueError(f"unknown tool: {name}")


def handle(msg: dict) -> None:
    method = msg.get("method")
    msg_id = msg.get("id")
    if method is None:
        return
    if msg_id is None and str(method).startswith("notifications/"):
        return
    if method == "initialize":
        params = msg.get("params") or {}
        version = params.get("protocolVersion") or PROTOCOL
        result(
            msg_id,
            {
                "protocolVersion": version,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            },
        )
        return
    if method == "ping":
        result(msg_id, {})
        return
    if method == "tools/list":
        result(msg_id, {"tools": TOOLS})
        return
    if method == "tools/call":
        params = msg.get("params") or {}
        name = params.get("name") or ""
        args = params.get("arguments") or {}
        if not isinstance(args, dict):
            args = {}
        try:
            payload = dispatch_tool(name, args)
            tool_text(msg_id, json.dumps(payload, ensure_ascii=False, indent=2))
        except Exception as exc:
            tool_text(msg_id, f"{type(exc).__name__}: {exc}", is_error=True)
        return
    if method in ("resources/list", "prompts/list"):
        key = "resources" if method == "resources/list" else "prompts"
        result(msg_id, {key: []})
        return
    if msg_id is not None:
        rpc_error(msg_id, -32601, f"Method not found: {method}")


def _read_byte(stream):
    chunk = stream.read(1)
    return chunk if chunk else None


def read_message(stream):
    """Read one JSON-RPC object: NDJSON line or Content-Length frame."""
    global _framing
    while True:
        first = _read_byte(stream)
        if first is None:
            return None
        if first in b" \t\r\n":
            continue
        break
    if first == b"{":
        _framing = "ndjson"
        buf = bytearray(first)
        while True:
            chunk = _read_byte(stream)
            if chunk is None or chunk == b"\n":
                break
            if chunk == b"\r":
                continue
            buf.extend(chunk)
        return json.loads(buf.decode("utf-8"))
    _framing = "lsp"
    buf = bytearray(first)
    while True:
        if buf.endswith(b"\r\n\r\n"):
            header_blob = bytes(buf[:-4])
            break
        if buf.endswith(b"\n\n"):
            header_blob = bytes(buf[:-2])
            break
        chunk = _read_byte(stream)
        if chunk is None:
            return None
        buf.extend(chunk)
        if len(buf) > 64 * 1024:
            raise ValueError("MCP headers too large")
    headers = {}
    for line in header_blob.replace(b"\r\n", b"\n").split(b"\n"):
        if not line or b":" not in line:
            continue
        key, _, val = line.partition(b":")
        headers[key.decode("ascii", "replace").strip().lower()] = val.decode(
            "ascii", "replace"
        ).strip()
    try:
        size = int(headers.get("content-length") or "0")
    except ValueError:
        size = 0
    if size <= 0:
        return None
    body = stream.read(size)
    if not body or len(body) < size:
        return None
    return json.loads(body.decode("utf-8"))


def main() -> None:
    stream = sys.stdin.buffer
    while True:
        try:
            msg = read_message(stream)
        except json.JSONDecodeError as exc:
            log(f"bad json: {exc}")
            continue
        except ValueError as exc:
            log(f"bad frame: {exc}")
            continue
        if msg is None:
            break
        if not isinstance(msg, dict):
            continue
        handle(msg)


if __name__ == "__main__":
    main()
