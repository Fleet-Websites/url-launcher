#!/usr/bin/env python3
"""Derived URL index for this folder only. Markdown is canonical. urls.sqlite is rebuildable."""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

HERE = Path(__file__).resolve().parent
MODULE_ROOT = HERE.parent.parent
TOPICS = MODULE_ROOT / "00_Inbox" / "Topics"
DROPS = MODULE_ROOT / "00_Inbox" / "Drops"
RECEIPTS = MODULE_ROOT / "_Orchestration" / "Receipts"
DB_PATH = HERE / "urls.sqlite"
JSON_PATH = HERE / "site" / "urls.json"
TODAY = date.today().isoformat()

URL_RE = re.compile(r"https?://[^\s)\]<>\"']+")
STATUS_CELL = re.compile(r"^`?\[([SK])\]`?$")
HEADER_KEYS = ("Derived-from", "Topic", "On", "Kind", "Topic-slug")


def fail(msg: str) -> None:
    print(f"URL-INDEX FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def receipt_path() -> Path:
    base = RECEIPTS / f"{TODAY}_url-index.md"
    if not base.exists():
        return base
    for letter in "bcdefghijklmnopqrstuvwxyz":
        cand = RECEIPTS / f"{TODAY}_url-index-{letter}.md"
        if not cand.exists():
            return cand
    fail(f"no unused receipt name left for {TODAY}")


def normalize(raw: str) -> tuple[str, str, str]:
    raw = raw.strip().rstrip(".,;:)")
    parts = urlsplit(raw)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ValueError(f"not a URL: {raw!r}")
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    path = parts.path
    if path in ("", "/"):
        path = ""
    elif path.endswith("/"):
        path = path[:-1]
    norm = urlunsplit((scheme, netloc, path, parts.query, ""))
    host = netloc.split("@")[-1].split(":")[0]
    return norm, raw, host


def parse_header(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines()[:12]:
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        if key in HEADER_KEYS:
            out[key] = val.strip()
    return out


def parse_table_rows(text: str) -> list[tuple[str, str | None, str]]:
    rows: list[tuple[str, str | None, str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        inner = stripped.strip("|")
        if re.fullmatch(r"[\s:|-]+", inner):
            continue
        cells = [c.strip() for c in inner.split("|")]
        if not cells or not cells[0].startswith("http"):
            continue
        url = cells[0]
        status = None
        blurb = ""
        if len(cells) >= 2:
            m = STATUS_CELL.match(cells[1])
            if m:
                status = m.group(1)
                blurb = cells[2] if len(cells) >= 3 else ""
            else:
                blurb = cells[1]
        rows.append((url, status, blurb))
    return rows


def parse_loose_url_lines(text: str) -> list[tuple[str, str | None, str]]:
    rows: list[tuple[str, str | None, str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("|") or stripped.startswith("#"):
            continue
        if ":" in stripped and not stripped.startswith("http"):
            key = stripped.split(":", 1)[0].strip()
            if key in HEADER_KEYS:
                continue
        match = URL_RE.search(stripped)
        if not match:
            continue
        token = match.group(0).rstrip(".,;:)")
        blurb = stripped[match.end() :].strip()
        rows.append((token, None, blurb))
    return rows


def topic_slug_from_name(name: str) -> str:
    stem = Path(name).stem
    _, sep, slug = stem.partition("_topic_")
    if not sep:
        fail(f"extract filename missing _topic_: {name}")
    return slug


def drop_slug_from_name(name: str, header: dict[str, str]) -> str:
    stem = Path(name).stem
    _, sep, slug = stem.partition("_drop_")
    if sep:
        return slug
    return header.get("Topic-slug") or "drop"


def write_receipt(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_mentions(
    path: Path,
    kind: str,
    topic: str,
    slug: str,
    hunt_file: str | None,
    rows: list[tuple[str, str | None, str]],
    sources: list[dict],
    mentions: list[dict],
    counts: dict[str, int],
) -> None:
    rel = path.relative_to(MODULE_ROOT).as_posix()
    sources.append(
        {
            "path": rel,
            "kind": kind,
            "topic": topic or None,
            "topic_slug": slug or None,
            "hunt_file": hunt_file,
            "workstream": None,
        }
    )
    seen_in_file: set[str] = set()
    for raw, status, blurb in rows:
        try:
            norm, raw_kept, host = normalize(raw)
        except ValueError:
            counts["bad_urls"] += 1
            continue
        if norm in seen_in_file:
            counts["mention_dupes"] += 1
            continue
        seen_in_file.add(norm)
        mentions.append(
            {
                "url_norm": norm,
                "url_raw": raw_kept,
                "host": host,
                "source_path": rel,
                "status": status,
                "blurb": blurb,
                "topic": topic or "",
            }
        )


def main() -> None:
    if not TOPICS.is_dir():
        fail(f"missing {TOPICS}")
    DROPS.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)

    sources: list[dict] = []
    mentions: list[dict] = []
    counts = {
        "files_read": 0,
        "skipped_readme": 0,
        "skipped_non_extract": 0,
        "skipped_non_drop": 0,
        "extract_files": 0,
        "drop_files": 0,
        "mention_dupes": 0,
        "bad_urls": 0,
    }

    for path in sorted(TOPICS.iterdir()):
        if not path.is_file():
            continue
        if path.name == "README.md":
            counts["skipped_readme"] += 1
            continue
        if "_topic_" not in path.name:
            counts["skipped_non_extract"] += 1
            continue
        counts["files_read"] += 1
        counts["extract_files"] += 1
        text = path.read_text(encoding="utf-8")
        header = parse_header(text)
        slug = topic_slug_from_name(path.name)
        hunt_file = header.get("Derived-from", "")
        if " " in hunt_file or "·" in hunt_file:
            hunt_file = hunt_file.split()[0]
        append_mentions(
            path,
            "hunt_extract",
            header.get("Topic", ""),
            slug,
            hunt_file or None,
            parse_table_rows(text),
            sources,
            mentions,
            counts,
        )

    for path in sorted(DROPS.iterdir()):
        if not path.is_file():
            continue
        if path.name == "README.md":
            counts["skipped_readme"] += 1
            continue
        if "_drop_" not in path.name:
            counts["skipped_non_drop"] += 1
            continue
        counts["files_read"] += 1
        counts["drop_files"] += 1
        text = path.read_text(encoding="utf-8")
        header = parse_header(text)
        slug = drop_slug_from_name(path.name, header)
        topic = header.get("Topic", "")
        rows = parse_table_rows(text) + parse_loose_url_lines(text)
        append_mentions(
            path,
            "drop",
            topic,
            slug,
            None,
            rows,
            sources,
            mentions,
            counts,
        )

    tmp = HERE / f".urls.{TODAY}.tmp.sqlite"
    if tmp.exists():
        fail(f"temp db already exists, will not overwrite: {tmp}")
    try:
        conn = sqlite3.connect(tmp)
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            conn.execute("CREATE VIRTUAL TABLE probe_fts USING fts5(x)")
            conn.execute("DROP TABLE probe_fts")
        except sqlite3.OperationalError as exc:
            conn.close()
            tmp.unlink(missing_ok=True)
            fail(f"FTS5 unavailable: {exc}")
        conn.executescript(
            """
            CREATE TABLE url (
              url_norm TEXT PRIMARY KEY,
              url_raw TEXT NOT NULL,
              host TEXT NOT NULL
            );
            CREATE TABLE source (
              path TEXT PRIMARY KEY,
              kind TEXT NOT NULL,
              topic TEXT,
              topic_slug TEXT,
              hunt_file TEXT,
              workstream TEXT
            );
            CREATE TABLE mention (
              id INTEGER PRIMARY KEY,
              url_norm TEXT NOT NULL REFERENCES url(url_norm),
              source_path TEXT NOT NULL REFERENCES source(path),
              status TEXT,
              blurb TEXT,
              UNIQUE (url_norm, source_path)
            );
            CREATE INDEX idx_url_host ON url(host);
            CREATE INDEX idx_source_topic ON source(topic_slug);
            CREATE INDEX idx_source_ws ON source(workstream);
            CREATE INDEX idx_mention_status ON mention(status);
            CREATE VIRTUAL TABLE mention_fts USING fts5(
              url_raw,
              blurb,
              topic
            );
            """
        )
        urls: dict[str, tuple[str, str]] = {}
        for m in mentions:
            urls.setdefault(m["url_norm"], (m["url_raw"], m["host"]))
        conn.executemany(
            "INSERT INTO url(url_norm, url_raw, host) VALUES (?, ?, ?)",
            [(norm, raw, host) for norm, (raw, host) in urls.items()],
        )
        conn.executemany(
            """INSERT INTO source(path, kind, topic, topic_slug, hunt_file, workstream)
               VALUES (?, ?, ?, ?, ?, ?)""",
            [
                (
                    s["path"],
                    s["kind"],
                    s["topic"],
                    s["topic_slug"],
                    s["hunt_file"],
                    s["workstream"],
                )
                for s in sources
            ],
        )
        fts_rows: list[tuple[int, str, str, str]] = []
        for m in mentions:
            cur = conn.execute(
                """INSERT INTO mention(url_norm, source_path, status, blurb)
                   VALUES (?, ?, ?, ?)""",
                (m["url_norm"], m["source_path"], m["status"], m["blurb"]),
            )
            fts_rows.append(
                (cur.lastrowid, m["url_raw"], m["blurb"] or "", m["topic"] or "")
            )
        conn.executemany(
            "INSERT INTO mention_fts(rowid, url_raw, blurb, topic) VALUES (?, ?, ?, ?)",
            fts_rows,
        )
        conn.commit()
        conn.close()
        tmp.replace(DB_PATH)
    except Exception:
        if tmp.exists():
            tmp.unlink()
        raise

    source_by_path = {s["path"]: s for s in sources}
    payload = {
        "built": TODAY,
        "mentions": [
            {
                "url": m["url_raw"],
                "url_norm": m["url_norm"],
                "host": m["host"],
                "topic": (source_by_path[m["source_path"]].get("topic") or "") or "",
                "topic_slug": (source_by_path[m["source_path"]].get("topic_slug") or "")
                or "",
                "status": m["status"],
                "blurb": m["blurb"] or "",
                "kind": source_by_path[m["source_path"]]["kind"],
                "source": m["source_path"],
            }
            for m in mentions
        ],
    }
    site_dir = HERE / "site"
    site_dir.mkdir(exist_ok=True)
    json_tmp = site_dir / ".urls.json.tmp"
    if json_tmp.exists():
        fail(f"temp json already exists, will not overwrite: {json_tmp}")
    json_tmp.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    json_tmp.replace(JSON_PATH)

    rec = receipt_path()
    write_receipt(
        rec,
        [
            "Rig: URL-Index",
            f"On: {TODAY}",
            f"Module: {MODULE_ROOT}",
            "",
            "## Result",
            "OK",
            "",
            "## Counts",
            f"- files read: {counts['files_read']}",
            f"- topic extracts: {counts['extract_files']}",
            f"- drops: {counts['drop_files']}",
            f"- sources: {len(sources)}",
            f"- unique urls: {len({m['url_norm'] for m in mentions})}",
            f"- mentions: {len(mentions)}",
            f"- skipped README.md: {counts['skipped_readme']}",
            f"- skipped non-extract inbox topics: {counts['skipped_non_extract']}",
            f"- skipped non-drop inbox drops: {counts['skipped_non_drop']}",
            f"- duplicate mentions in one file: {counts['mention_dupes']}",
            f"- bad URLs skipped: {counts['bad_urls']}",
            "",
            "## Notes",
            "Did not edit, move, or delete markdown.",
            "Did not parse Research-Sandbox, hunt originals, or any folder outside this module.",
            "urls.sqlite and site/urls.json are derived and were atomically replaced.",
            "Did not write into 99_Outbox.",
        ],
    )
    print(
        f"URL-Index OK. extracts={counts['extract_files']} drops={counts['drop_files']} "
        f"mentions={len(mentions)} urls={len({m['url_norm'] for m in mentions})}"
    )
    print(f"DB: {DB_PATH}")
    print(f"JSON: {JSON_PATH}")
    print(f"Receipt: {rec}")


if __name__ == "__main__":
    main()
