Derived-from: 2026-08-17_claude-opus-5_url-hunt-01-research-infrastructure.md
Topic: Project Planning
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 6 — Project Planning / decision records / preservation

| URL | Status | What it is |
| --- | --- | --- |
| https://adr.github.io/ | `[S]` | Architectural Decision Records — home of the format |
| https://github.com/architecture-decision-record/architecture-decision-record | `[S]` | ADR examples and templates |
| https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record | `[S]` | Microsoft Well-Architected — maintaining an ADR log |
| https://www.redhat.com/en/blog/architecture-decision-records | `[S]` | Red Hat — why to use ADRs at all |
| https://www.atlassian.com/agile/agile-at-scale/okr | `[S]` | Atlassian — OKRs |
| https://www.ibm.com/think/topics/okrs | `[S]` | IBM — what OKRs are |
| https://www.oclc.org/research/publications/2000/lavoie-oais.html | `[S]` | Lavoie — the standard introduction to the OAIS reference model |
| https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file | `[S]` | DPC Technology Watch Report on OAIS |
| https://www.oclc.org/content/dam/research/activities/pmwg/pm_framework.pdf | `[S]` | Preservation metadata and the OAIS information model |
| https://preservica.com/resources/blogs-and-news/what-you-need-to-know-about-the-most-recent-oais-revision | `[S]` | OAIS v3 (Dec 2024) — what changed |
| https://public.ccsds.org/Pubs/650x0m3.pdf | `[K]` | CCSDS — the OAIS standard itself (magenta book) |
| https://arxiv.org/pdf/1707.06336 | `[S]` | Survey of open-source digital preservation repositories |

**Direct relevance:** ADR is the closest published format to what
`_Governance/` and the fleet Decisions Ledger already do — context, decision,
consequences, never edited after the fact. OAIS is the formal model behind
"nothing is ever deleted; superseded material is retained."

## Associated companions

Official docs, source repos, sibling tools named in the blurbs, and well-known companion sites. `[K]` — asserted from knowledge, not a live-search mark.

| URL | Status | What it is |
| --- | --- | --- |
| https://adr.github.io/madr/ | `[K]` | MADR — Markdown Architectural Decision Records |
| https://github.com/npryce/adr-tools | `[K]` | adr-tools — CLI for maintaining ADR files in git |
| https://public.ccsds.org | `[K]` | CCSDS — publisher of the OAIS magenta book already listed |
| https://www.dpconline.org | `[K]` | Digital Preservation Coalition — OAIS companion community |
