Derived-from: 2026-08-17_claude-opus-5_url-hunt-01-research-infrastructure.md
Topic: Ai Project Management
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 2 — Ai Project Management / agent orchestration

| URL | Status | What it is |
| --- | --- | --- |
| https://www.anthropic.com/engineering/building-effective-agents | `[S]` | Anthropic — the reference text on agent design; "do the simplest thing that works" |
| https://www.anthropic.com/engineering/multi-agent-research-system | `[S]` | Anthropic — how a multi-agent *research* system was actually built. Closest published analogue to this module |
| https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | `[S]` | Anthropic — context engineering; context rot; just-in-time retrieval |
| https://www.anthropic.com/engineering | `[S]` | Anthropic engineering index — parent of the above |
| https://www.langchain.com/blog/context-engineering-for-agents | `[S]` | LangChain's parallel treatment of context engineering |
| https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production | `[S]` | Six orchestration patterns framed for production |
| https://www.digitalapplied.com/blog/multi-agent-orchestration-5-patterns-that-work | `[S]` | Fan-out / pipeline / debate / supervisor / swarm, with a framework matrix |
| https://www.dataiku.com/blog/agent-orchestration-explained | `[S]` | Enterprise framing of orchestration and governance |

**Direct relevance:** the dispatch → context → returns → corpus → synthesis shape
in this module is a supervisor/fan-out orchestration built out of folders instead
of code. The Anthropic multi-agent research post is the nearest published account
of the same problem.

## Appended 2026-08-17 — PM tools, specs, evals, delivery

HTTP-checked this session (200/301). `[S]` also appeared in this run's live search (GitHub, HN Algolia, Wikipedia). `[K]` is a canonical page confirmed by HTTP after being asserted from knowledge. Height.app is omitted: TLS fails and public reports say the product shut down.

| URL | Status | What it is |
| --- | --- | --- |
| https://linear.app/ | `[S]` | Linear — issue tracker used by many software/AI teams; homepage |
| https://linear.app/method | `[S]` | Linear Method — public practices for building (cycles, specs, triage) |
| https://linear.app/docs | `[K]` | Linear Docs — product docs for issues, projects, cycles, API |
| https://linear.app/now/using-ai-to-detect-similar-issues | `[S]` | Linear — using AI to detect similar issues (duplicate/triage) |
| https://www.notion.com/product/ai | `[K]` | Notion AI — AI inside docs, wikis, and project databases |
| https://www.notion.so/product/projects | `[K]` | Notion Projects — tasks/projects on top of Notion databases |
| https://www.shortcut.com/ | `[K]` | Shortcut — software-team PM explicitly pitched for humans and agents |
| https://github.com/features/issues | `[K]` | GitHub Issues — planning colocated with the repo |
| https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects | `[K]` | GitHub Projects — boards/tables/roadmaps over issues |
| https://plane.so/ | `[K]` | Plane — open-source project management (Linear-like) |
| https://github.com/makeplane/plane | `[K]` | Plane source repo |
| https://basecamp.com/shapeup | `[S]` | Shape Up (Basecamp) — appetite, betting table, six-week cycles; not Scrum |
| https://dora.dev/ | `[K]` | DORA — software delivery metrics and capabilities research |
| https://dora.dev/research/ | `[K]` | DORA research archive — Accelerate metrics, reports, AI-era delivery findings |
| https://cloud.google.com/devops | `[K]` | Google Cloud DevOps / DORA capabilities (companion to dora.dev) |
| https://teamtopologies.com/ | `[S]` | Team Topologies — team types and interaction modes for delivery orgs |
| https://martinfowler.com/bliki/TeamTopologies.html | `[S]` | Fowler — short note on Team Topologies |
| https://www.svpg.com/ai-product-management/ | `[S]` | SVPG — AI product management (Cagan et al.) |
| https://www.svpg.com/ | `[K]` | Silicon Valley Product Group — product operating model |
| https://www.reforge.com/blog/how-ai-changes-product-management | `[S]` | Reforge — how AI changes product management |
| https://www.deeplearning.ai/the-batch/issue-279 | `[S]` | DeepLearning.AI The Batch — AI product management issue |
| https://scrumguides.org/ | `[K]` | Scrum Guide — the actual Scrum definition |
| https://www.atlassian.com/agile | `[K]` | Atlassian Agile Coach — delivery vocabulary (sprints, kanban, roadmaps) |
| https://www.productboard.com/ | `[K]` | Productboard — product discovery and roadmapping |
| https://www.romanpichler.com/ | `[K]` | Roman Pichler — product strategy, vision boards, product owners |
| https://lennysnewsletter.com/ | `[K]` | Lenny's Newsletter — product/growth archive widely used by PMs |
| https://www.ycombinator.com/library | `[K]` | YC Startup Library — delivery, hiring, and product essays |
| https://review.firstround.com/ | `[K]` | First Round Review — long-form startup/product operating essays |
| https://posthog.com/ | `[K]` | PostHog — open-source product analytics (funnels, flags, session replay) |
| https://www.statsig.com/ | `[K]` | Statsig — experimentation and feature gates; common on AI product launches |
| https://launchdarkly.com/ | `[K]` | LaunchDarkly — feature flags / progressive delivery |
| https://openfeature.dev/ | `[K]` | OpenFeature — vendor-neutral feature-flag spec (CNCF) |
| https://openspec.dev/ | `[S]` | OpenSpec — spec-driven development for AI coding assistants |
| https://github.com/Fission-AI/OpenSpec | `[S]` | OpenSpec source |
| https://github.com/github/spec-kit | `[S]` | GitHub Spec Kit — spec-driven development toolkit |
| https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ | `[S]` | GitHub Blog — spec-driven development with AI (Spec Kit intro) |
| https://den.dev/blog/github-spec-kit/ | `[S]` | Den Delimarsky — what GitHub Spec Kit actually is |
| https://www.braintrust.dev/ | `[S]` | Braintrust — eval platform for AI products (datasets, scores, traces) |
| https://www.braintrust.dev/blog/evaluating-agents | `[S]` | Braintrust — evaluating agents, companion to Anthropic's agent essay |
| https://langfuse.com/ | `[S]` | Langfuse — open-source LLM observability, traces, evals, prompt management |
| https://www.promptfoo.dev/ | `[S]` | Promptfoo — open-source prompt/agent eval CLI and red-teaming |
| https://hamel.dev/blog/posts/evals/ | `[S]` | Hamel Husain — practical LLM evals (widely cited field guide) |
| https://developers.openai.com/api/docs/guides/production-best-practices | `[K]` | OpenAI — production best practices for API apps |
| https://a16z.com/ai-canon/ | `[S]` | a16z AI Canon — reading list for building AI products |
| https://sequoiacap.com/article/generative-ai-act-two | `[K]` | Sequoia — Generative AI: Act Two (product/market framing) |
| https://www.nist.gov/itl/ai-risk-management-framework | `[S]` | NIST AI Risk Management Framework — US government AI risk process |
| https://airc.nist.gov/airmf-resources/ | `[K]` | NIST AIRC — AI RMF knowledge base and playbooks |
| https://www.anthropic.com/news/anthropic-achieves-iso-42001-certification-for-responsible-ai | `[S]` | Anthropic — ISO/IEC 42001 (AI management system) certification note |
| https://aws.amazon.com/blogs/machine-learning/iso-42001-a-new-foundational-global-standard-to-advance-responsible-ai/ | `[S]` | AWS — what ISO/IEC 42001 is for AI programmes |
| https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/ | `[K]` | SPACE framework — developer productivity beyond DORA output counts |
| https://getdx.com/ | `[K]` | DX — developer-experience measurement (SPACE/DORA-adjacent) |
| https://www.thoughtworks.com/radar | `[K]` | Thoughtworks Technology Radar — techniques and platforms, including delivery |
