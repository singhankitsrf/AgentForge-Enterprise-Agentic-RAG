---
title: AgentForge Enterprise
emoji: 🧠
colorFrom: indigo
colorTo: blue
sdk: static
app_file: index.html
pinned: true
license: mit
short_description: Governed agentic RAG, MCP and evaluation platform
tags:
- agentic-ai
- langchain
- langgraph
- mcp
- rag
- llm
- mlops
- model-evaluation
- responsible-ai
- ci-cd
---

# AgentForge Enterprise

**Governed Agentic RAG + Tool-Use Platform with LangGraph, LangChain, MCP, Evaluation, Observability and Human Approval**

AgentForge Enterprise is a recruiter-facing demonstration of a production-oriented LLM/agent platform. The public Hugging Face Space is intentionally a free Static Space; the executable FastAPI, LangGraph, LangChain adapter, MCP v2 server, policy controls, tests and Docker implementation live in GitHub.

## Verified engineering evidence

| Check | Executed result |
|---|---|
| Dependency installation | Passed |
| Ruff quality gate | Passed |
| Unit tests | 6/6 passed |
| Deterministic contract evaluation | 3/3 passed |
| Expected evidence recall in contract cases | 1.0 for all 3 cases |
| Approval-policy correctness | Passed for all 3 cases |
| Docker image build | Passed |
| Dependency audit | Passed after audited build-toolchain hardening |

> **Evidence boundary:** the 3/3 result is a deterministic orchestration/evidence-policy contract evaluation, **not** an LLM quality benchmark. Provider-backed LLM accuracy, groundedness, latency, cost and production reliability are not claimed until separately executed and published.

## Architecture

```text
User / API
   ↓
Request validation + policy pre-check
   ↓
LangGraph supervisor workflow
   ├── Retrieval / evidence
   ├── MCP typed tools
   └── Human approval boundary for side effects
   ↓
Evidence-backed synthesis
   ↓
Trace + evaluation artifacts
```

## Senior engineering signal

- LangGraph stateful orchestration
- LangChain provider abstraction
- MCP v2 typed tool interoperability
- evidence/provenance contracts
- prompt-injection policy checks
- allowlisted read/write tool governance
- human approval boundary for side effects
- reproducible offline evaluation
- FastAPI service contract
- Docker packaging
- CI/CD and dependency auditing

## Explore

- GitHub source: https://github.com/singhankitsrf/AgentForge-Enterprise-Agentic-RAG
- Executed baseline evidence: https://github.com/singhankitsrf/AgentForge-Enterprise-Agentic-RAG/blob/main/evaluation/baseline.json
- Hugging Face Space: https://huggingface.co/spaces/singhankit491/agentforge-enterprise
