Derived-from: 2026-08-17_claude-sonnet-4-6_url-hunt-03-visual-production.md
Topic: Image Generation
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

## How to read the status marks

| Mark | Meaning |
| --- | --- |
| `[S]` | URL was returned in this session's live search results |
| `[K]` | Canonical root URL asserted from prior knowledge, **not re-checked this session** — treat as CLAIMED, not VERIFIED |

No URL below was opened and read. This is a list of candidates, not an endorsement of any page's contents.

## 6 — Image Generation (AI)

### Models and model hubs

| URL | Status | What it is |
| --- | --- | --- |
| https://huggingface.co/ | `[K]` | Hugging Face — the canonical model hub; FLUX, Stable Diffusion, and every major image model ships here first |
| https://civitai.com/ | `[K]` | Civitai — AI art community hub: checkpoints, LoRAs, embeddings, on-site generator, sample images |
| https://black-forest-labs.com/ | `[K]` | Black Forest Labs — creators of FLUX.1, the leading open-weight image model in 2026 |
| https://stability.ai/ | `[K]` | Stability AI — Stable Diffusion origin; SD 3.5 is the current release |
| https://www.edenai.co/post/top-free-image-generation-tools-apis-and-open-source-models | `[S]` | Eden AI — Top Free AI Image Generation APIs and Open-Source Models, current survey |
| https://www.secondtalent.com/resources/top-open-source-ai-image-generators/ | `[S]` | Second Talent — Top 5 Open-Source AI Image Generators 2026 (FLUX.2, SD 3.5, Qwen-Image, HunyuanImage 3.0, Sana) |
| https://pinggy.io/blog/best_free_open_source_ai_image_generators_to_self_host/ | `[S]` | Pinggy — Best Free & Open-Source AI Image Generators to Self-Host |
| https://zplatform.ai/best-ai-tools/best-free-ai-image-generators/ | `[S]` | zPlatform — 61 Best Free AI Image Generators 2026, ranked |

### Local inference and workflow tools

| URL | Status | What it is |
| --- | --- | --- |
| https://comfyui-wiki.com/en | `[S]` | ComfyUI Wiki — the community reference for node-based workflow construction: tutorials, example workflows, model guides |
| https://www.local-llm.net/guides/local-image-generation/ | `[S]` | local-llm.net — Local Image Generation 2026: Stable Diffusion, FLUX, and ComfyUI setup guide |
| https://comfyui.org/en/stable-diffusion-workflow-guide | `[S]` | ComfyUI.org — Step-by-Step Stable Diffusion Workflow Guide |
| https://aiofm.info/en/guides/civitai-vs-huggingface-vs-tensor-art | `[S]` | Civitai vs Hugging Face vs Tensor.Art — which model hub to use in 2026, compared plainly |

### Prompt engineering

| URL | Status | What it is |
| --- | --- | --- |
| https://www.comflowy.com/basics/prompt | `[S]` | Comflowy — Stable Diffusion Prompt Basics: structure, weighting, negative prompts |
| https://comfy.icu/docs/prompt-engineering | `[S]` | ComfyICU — Prompt Engineering guide: parentheses weights, keyword ordering, style tokens |
| https://comfyuiweb.com/posts/essential-comfyui-tips-and-tricks | `[S]` | 25 ComfyUI Tips and Tricks for AI Image Generation (2026) |

**The two things that matter most at the start:** (1) which model you use
determines what is possible — a model fine-tuned for illustration behaves
differently from a photorealism base. (2) Prompt phrasing matters less than the
model expects; LoRA selection and sampler settings matter more. Civitai's sample
images are a faster model-evaluation tool than any roundup article.

---

## Associated companions

Official docs, source repos, sibling tools named in the blurbs, and well-known companion sites. `[K]` — asserted from knowledge, not a live-search mark.

| URL | Status | What it is |
| --- | --- | --- |
| https://github.com/comfyanonymous/ComfyUI | `[K]` | ComfyUI source — the node UI the wiki already listed documents |
| https://docs.comfy.org | `[K]` | ComfyUI official docs |
| https://github.com/AUTOMATIC1111/stable-diffusion-webui | `[K]` | Stable Diffusion WebUI (A1111) — the other common local frontend |
| https://www.invoke.com | `[K]` | Invoke — local/open image-gen studio, sibling to ComfyUI |
| https://www.midjourney.com | `[K]` | Midjourney — closed image model named throughout the prompt libraries |
| https://openai.com/index/dall-e-3/ | `[K]` | OpenAI — DALL·E (API image generation) |
| https://tensor.art | `[K]` | Tensor.Art — model hub named in the Civitai vs Hugging Face comparison already listed |
