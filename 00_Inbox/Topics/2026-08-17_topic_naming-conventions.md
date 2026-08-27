Derived-from: 2026-08-17_claude-opus-5_url-hunt-01-research-infrastructure.md
Topic: Naming Conventions
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 5 — Naming Conventions

| URL | Status | What it is |
| --- | --- | --- |
| https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions | `[S]` | Harvard Medical School — the most-cited short guide |
| https://guides.lib.uconn.edu/c.php?g=832372&p=8226285 | `[S]` | UConn — file naming and date formatting, ISO 8601 |
| https://libguides.utsa.edu/c.php?g=714236&p=10373953 | `[S]` | UTSA — file naming conventions |
| https://ubc-library-rc.github.io/rdm/content/01_file_naming.html | `[S]` | UBC Research Commons — file naming, in a versioned repo |
| https://library.sjsu.edu/c.php?g=769588&p=5523042 | `[S]` | San José State — naming and organisation together |
| https://libguides.stthomas.edu/c.php?g=437561&p=4529210 | `[S]` | St. Thomas — file management |
| https://library.viu.ca/c.php?g=188929&p=5231205 | `[S]` | Vancouver Island University — naming and organising data files |
| https://www.iso.org/iso-8601-date-and-time-format.html | `[K]` | ISO 8601 — the date standard this module's `YYYY-MM-DD` already follows |

**Note against `_Governance/Naming-Standard.md`:** every guide above converges on
*underscore separates elements, hyphen joins words within an element, ISO 8601
dates, no spaces or special characters, leading zeros for sortability*. That is
the fleet rule, arrived at independently. **The one place the guides diverge from
this module is case** — most recommend lowercase throughout for
cross-platform safety, which is the substance of open questions **OQ-R1** and
**OQ-R6**. Logged, not resolved.

## Associated companions

Official docs, source repos, sibling tools named in the blurbs, and well-known companion sites. `[K]` — asserted from knowledge, not a live-search mark.

| URL | Status | What it is |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/ISO_8601 | `[K]` | ISO 8601 — Wikipedia companion to the ISO page already listed |
| https://www.w3.org/TR/NOTE-datetime | `[K]` | W3C Date and Time Formats — ISO 8601 profile used on the web |
| https://datatracker.ietf.org/doc/html/rfc3339 | `[K]` | RFC 3339 — timestamps on the internet |
| https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ | `[K]` | Dublin Core terms — element names for shared metadata |
