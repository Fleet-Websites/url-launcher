Derived-from: 2026-08-17_claude-opus-5_url-hunt-01-research-infrastructure.md
Topic: Compartmentalisation
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 1 — Compartmentalisation

| URL | Status | What it is |
| --- | --- | --- |
| https://doc.qubes-os.org/en/latest/introduction/faq.html | `[S]` | Qubes OS FAQ — security-by-compartmentalisation stated as a design principle |
| https://doc.qubes-os.org/en/latest/developer/system/architecture.html | `[S]` | Qubes architecture — how isolation is made structural rather than promised |
| https://doc.qubes-os.org/en/latest/user/reference/glossary.html | `[S]` | Qubes glossary — precise vocabulary for compartments, domains, isolation |
| https://arxiv.org/pdf/2410.08434 | `[S]` | *SoK: Software Compartmentalization* — systematisation-of-knowledge paper; the academic spine of the idea |
| https://arxiv.org/pdf/2212.12904 | `[S]` | Interface vulnerabilities in compartmentalised software — where compartment boundaries actually leak |
| https://arxiv.org/pdf/0903.2171 | `[S]` | Role-Based Access Control — the formal ancestor of need-to-know |
| https://csrc.nist.gov/glossary/term/least_privilege | `[K]` | NIST definition of least privilege |

**Direct relevance:** `_Governance/Compartmentalisation.md` argues that a folder
boundary beats an instruction because it is structural. The Qubes documentation
is the same argument at OS level and is the best available external statement of it.

## Associated companions

Official docs, source repos, sibling tools named in the blurbs, and well-known companion sites. `[K]` — asserted from knowledge, not a live-search mark.

| URL | Status | What it is |
| --- | --- | --- |
| https://www.qubes-os.org | `[K]` | Qubes OS project home — security by compartmentalisation |
| https://www.qubes-os.org/doc/ | `[K]` | Qubes documentation hub (parent of the FAQ/architecture pages already listed) |
| https://github.com/QubesOS/qubes-os | `[K]` | Qubes OS source repositories |
| https://csrc.nist.gov/projects/role-based-access-control | `[K]` | NIST RBAC project — companion to the RBAC paper already listed |
| https://csrc.nist.gov/glossary/term/need_to_know | `[K]` | NIST glossary — need-to-know |
| https://arxiv.org/abs/2410.08434 | `[K]` | arXiv abs page for the SoK compartmentalization paper (PDF already listed) |
