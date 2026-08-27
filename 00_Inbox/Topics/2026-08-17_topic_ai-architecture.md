Derived-from: 2026-08-17_remaining-topic-cycle.md
Topic: AI Architecture
On: 2026-08-17
Kind: Topic extract. Original hunt file is the source. This is a copy of one section.

HTTP-checked this session (200/301). Architecture was not a hunt-01–05 section; this extract is a new pass (GitHub, HN Algolia, Wikipedia externals, then HEAD/GET). Canonical homepages preferred. Not an endorsement of any page's contents.

### Software architecture (notation, ADRs, classics)

| URL | Description |
|-----|-------------|
| https://c4model.com/ | C4 model — System Context, Container, Component, Code; Simon Brown |
| https://en.wikipedia.org/wiki/C4_model | Wikipedia — C4 model overview and tool list |
| https://www.infoq.com/articles/C4-architecture-model/ | InfoQ — C4 architecture model explainer |
| https://structurizr.com/ | Structurizr — diagrams-as-code for C4 |
| https://icepanel.io/ | IcePanel — C4-style landscape diagrams (vendor) |
| https://arc42.org/ | arc42 — architecture documentation template |
| https://arc42.org/overview | arc42 template overview (the twelve sections) |
| https://docs.arc42.org/home/ | arc42 documentation |
| https://www.innoq.com/en/blog/2022/08/brief-introduction-to-arc42/ | innoq — brief introduction to arc42 |
| https://github.com/adr/madr | MADR — Markdown Architectural Decision Records |
| https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html | Quinn — original "Documenting Architecture Decisions" post |
| https://www.sei.cmu.edu/software-architecture/ | Carnegie Mellon SEI — software architecture practice |
| https://en.wikipedia.org/wiki/Software_architecture | Wikipedia — software architecture |
| https://12factor.net/ | The Twelve-Factor App — still the baseline for SaaS/runtime design |
| https://www.melconway.com/Home/Conways_Law.html | Conway's Law — org structure becomes system structure |
| https://martinfowler.com/architecture/ | Martin Fowler — architecture essays |
| https://microservices.io/ | Chris Richardson — microservice patterns (service decomposition, saga, CQRS) |
| https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf | Sculley et al. — Hidden Technical Debt in Machine Learning Systems (NIPS 2015) |

### Agent systems, orchestration, frameworks

| URL | Description |
|-----|-------------|
| https://github.com/humanlayer/12-factor-agents | 12-Factor Agents — production principles for LLM software (HumanLayer) |
| https://developers.openai.com/cookbook | OpenAI Cookbook — agents, RAG, evals, production examples |
| https://github.com/openai/openai-cookbook | OpenAI Cookbook source |
| https://developers.openai.com/api/docs/guides/agents | OpenAI — Agents SDK guide |
| https://openai.github.io/openai-agents-python/ | OpenAI Agents SDK (Python) docs |
| https://github.com/openai/openai-agents-python | OpenAI Agents SDK source |
| https://docs.langchain.com/oss/python/langgraph/overview | LangGraph docs — stateful agent graphs, persistence, human-in-the-loop |
| https://github.com/langchain-ai/langgraph | LangGraph source |
| https://www.langchain.com/langgraph | LangGraph product page |
| https://www.langchain.com/blog/langgraph-multi-agent-workflows | LangGraph — multi-agent workflow patterns |
| https://dspy.ai/ | DSPy — program, not prompt, language models (Stanford) |
| https://github.com/stanfordnlp/dspy | DSPy source |
| https://ai.pydantic.dev/ | PydanticAI — typed Python agents on Pydantic |
| https://github.com/pydantic/pydantic-ai | PydanticAI source |
| https://haystack.deepset.ai/ | Haystack — production RAG and agents (deepset) |
| https://docs.haystack.deepset.ai/docs/intro | Haystack docs |
| https://github.com/deepset-ai/haystack | Haystack source |
| https://www.llamaindex.ai/ | LlamaIndex — data framework for LLM apps and RAG |
| https://docs.llamaindex.ai/ | LlamaIndex docs (redirects to current developer docs) |
| https://github.com/run-llama/llama_index | LlamaIndex source |
| https://crewai.com/ | CrewAI — role-based multi-agent crews |
| https://github.com/crewAIInc/crewAI | CrewAI source |
| https://microsoft.github.io/autogen/ | AutoGen — Microsoft multi-agent framework docs |
| https://github.com/microsoft/autogen | AutoGen source |
| https://learn.microsoft.com/en-us/agent-framework/ | Microsoft Agent Framework docs (AutoGen + Semantic Kernel lineage) |
| https://github.com/microsoft/agent-framework | Microsoft Agent Framework source |
| https://learn.microsoft.com/en-us/semantic-kernel/ | Semantic Kernel docs |
| https://github.com/microsoft/semantic-kernel | Semantic Kernel source |
| https://adk.dev/ | Google Agent Development Kit (ADK) |
| https://github.com/google/adk-python | Google ADK (Python) source |
| https://mastra.ai/ | Mastra — TypeScript agent framework |
| https://ai-sdk.dev/ | Vercel AI SDK |
| https://github.com/vercel/ai | Vercel AI SDK source |
| https://www.inngest.com/ai | Inngest AgentKit — durable agent runs |
| https://github.com/inngest/agent-kit | Inngest AgentKit source |
| https://github.com/lastmile-ai/mcp-agent | mcp-agent — agents composed over MCP |
| https://temporal.io/ | Temporal — durable workflow engine used to run agents in production |
| https://temporal.io/blog/announcing-openai-agents-sdk-integration | Temporal + OpenAI Agents SDK |
| https://restate.dev/ | Restate — low-latency durable execution (workflows/agents) |
| https://dapr.io/ | Dapr — distributed application runtime (actors, pub/sub, state) |
| https://www.prefect.io/ | Prefect — Python workflow orchestration |
| https://airflow.apache.org/ | Apache Airflow — DAG orchestration |
| https://martinfowler.com/articles/build-own-coding-agent.html | Fowler — building a CLI coding agent with PydanticAI |
| https://simonwillison.net/tags/ai-agents/ | Simon Willison — ai-agents tag (implementation notes, not vendor docs) |

### Agent protocols

| URL | Description |
|-----|-------------|
| https://a2a-protocol.org/ | A2A (Agent2Agent) protocol homepage |
| https://a2a-protocol.org/latest/specification/ | A2A specification |
| https://github.com/a2aproject/A2A | A2A protocol source (Linux Foundation / former Google A2A) |
| https://docs.ag-ui.com/introduction | AG-UI — agent/user-interaction protocol for frontends |
| https://github.com/ag-ui-protocol/ag-ui | AG-UI source |

### RAG pipelines and retrieval

| URL | Description |
|-----|-------------|
| https://en.wikipedia.org/wiki/Retrieval-augmented_generation | Wikipedia — RAG |
| https://arxiv.org/abs/2005.11401 | Lewis et al. 2020 — original RAG paper |
| https://www.anthropic.com/engineering/contextual-retrieval | Anthropic — contextual retrieval (chunk + context prefixes) |
| https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval | Azure Architecture Center — RAG information-retrieval phase |
| https://github.com/microsoft/graphrag | Microsoft GraphRAG — graph-based RAG |
| https://microsoft.github.io/graphrag/ | GraphRAG docs |
| https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/ | MSR — GraphRAG announcement |
| https://unstructured.io/ | Unstructured — document parsing into RAG-ready chunks |
| https://qdrant.tech/ | Qdrant — open-source vector database |
| https://weaviate.io/ | Weaviate — open-source vector database |
| https://github.com/pgvector/pgvector | pgvector — vectors in Postgres |
| https://www.trychroma.com/ | Chroma — embedding database for AI apps |
| https://www.pinecone.io/ | Pinecone — hosted vector database |
| https://github.com/getzep/graphiti | Graphiti — temporal knowledge graphs for agents |
| https://graphiti.dev/ | Graphiti docs |
| https://github.com/stanford-futuredata/ColBERT | ColBERT — late-interaction retrieval |
| https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html | Drew Breunig — how contexts fail (context engineering failure modes) |

### Evals, observability, guardrails

| URL | Description |
|-----|-------------|
| https://docs.ragas.io/en/stable/ | RAGAS docs — RAG/agent evaluation metrics |
| https://www.ragas.io/ | RAGAS homepage |
| https://github.com/vibrantlabsai/ragas | RAGAS source (formerly explodinggradients) |
| https://deepeval.com/ | DeepEval — LLM evaluation framework |
| https://github.com/confident-ai/deepeval | DeepEval source |
| https://github.com/openai/evals | OpenAI Evals — eval harness |
| https://developers.openai.com/api/docs/guides/evals | OpenAI — evals API/guide |
| https://www.langchain.com/langsmith/evaluation | LangSmith — agent/LLM evaluation product |
| https://docs.langchain.com/langsmith/evaluation-concepts | LangSmith evaluation concepts |
| https://arize.com/docs/phoenix | Arize Phoenix — open-source LLM tracing and evals |
| https://github.com/Arize-ai/phoenix | Phoenix source |
| https://www.helicone.ai/ | Helicone — LLM observability proxy |
| https://opentelemetry.io/docs/specs/semconv/gen-ai/ | OpenTelemetry — GenAI semantic conventions |
| https://genai.owasp.org/llm-top-10/ | OWASP LLM Top 10 (GenAI project) |
| https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ | OWASP Top 10 for LLM Applications 2025 |
| https://owasp.org/www-project-top-10-for-large-language-model-applications/ | OWASP LLM Top 10 project page |
| https://github.com/NVIDIA-NeMo/Guardrails | NeMo Guardrails — programmable conversational rails |
| https://guardrailsai.com/ | Guardrails AI — validators around LLM I/O |
| https://www.evidentlyai.com/ | Evidently — ML/LLM evaluation and monitoring |
| https://www.swebench.com/ | SWE-bench — coding-agent benchmark leaderboards |
| https://github.com/SWE-bench/SWE-bench | SWE-bench source |
| https://crfm.stanford.edu/helm/ | HELM — Holistic Evaluation of Language Models (Stanford CRFM) |
| https://lmarena.ai/ | LM Arena — public LLM arena / leaderboard (Chatbot Arena) |
| https://github.com/EleutherAI/lm-evaluation-harness | EleutherAI lm-evaluation-harness |
| https://python.useinstructor.com/ | Instructor — structured LLM outputs via Pydantic |
| https://docs.boundaryml.com/home | BAML — typed LLM functions / structured generation |
| https://boundaryml.com/ | BoundaryML (BAML) homepage |

### Cloud reference architectures, MLOps, serving

| URL | Description |
|-----|-------------|
| https://learn.microsoft.com/en-us/azure/well-architected/ | Azure Well-Architected Framework |
| https://learn.microsoft.com/en-us/azure/well-architected/ai/ | Azure Well-Architected — AI workloads |
| https://learn.microsoft.com/en-us/azure/architecture/ai-ml/ | Azure Architecture Center — AI/ML |
| https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html | AWS Well-Architected — Machine Learning Lens |
| https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html | AWS Well-Architected — Generative AI Lens |
| https://docs.cloud.google.com/architecture | Google Cloud Architecture Center |
| https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning | Google — MLOps continuous delivery paper/guide |
| https://ml-ops.org/ | ml-ops.org — MLOps principles and layout |
| https://en.wikipedia.org/wiki/MLOps | Wikipedia — MLOps |
| https://mlflow.org/ | MLflow — experiment tracking and model registry |
| https://www.kubeflow.org/ | Kubeflow — ML on Kubernetes |
| https://feast.dev/ | Feast — feature store |
| https://docs.vllm.ai/en/latest/ | vLLM docs — high-throughput LLM serving |
| https://github.com/vllm-project/vllm | vLLM source |
| https://vllm.ai/ | vLLM homepage |
| https://docs.sglang.io/ | SGLang — fast LLM serving / structured generation |
| https://huggingface.co/docs/text-generation-inference/index | Hugging Face TGI — text-generation inference |
| https://www.ray.io/ | Ray — distributed Python (Train, Serve, Data) |
| https://huyenchip.com/blog/ | Chip Huyen — AI/ML systems writing |
| https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html | Chip Huyen — data distribution shifts and monitoring |
| https://fullstackdeeplearning.com/ | Full Stack Deep Learning — production ML course materials |
| https://madewithml.com/ | Made With ML — ML in production curriculum |
