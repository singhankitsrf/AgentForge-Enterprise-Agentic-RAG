# AgentForge Enterprise

**Governed Agentic RAG + Tool-Use Platform with LangGraph, LangChain, MCP, Evaluation, Observability, and Human Approval**

> Portfolio project by **Ankit Kumar Singh** for AI Lead / Staff AI Engineer / GenAI Architect / AI Platform Architect positioning.

AgentForge Enterprise is a production-oriented reference implementation for building auditable LLM agents that can retrieve evidence, select tools, enforce policy, pause for human approval, and emit machine-readable execution traces. It deliberately separates **executed evidence** from **architecture claims**: the default demo works without an API key using a deterministic planner, while real LLM providers can be enabled explicitly.

## Why this project is different

Most RAG demos stop at `question -> retrieve -> generate`. AgentForge models the controls expected around a serious agentic system:

- **LangGraph state machine** for deterministic + agentic orchestration
- **LangChain agent/model adapter** for provider-neutral LLM integration
- **MCP v2 server** exposing typed enterprise tools
- hybrid retrieval interface with evidence scoring
- allowlisted tool policy + write-action approval boundary
- prompt-injection heuristics and PII-aware handling hooks
- reproducible offline evaluation dataset and quality gates
- trace IDs, latency, tool-call counts, evidence IDs, and policy events
- FastAPI service boundary
- Docker and GitHub Actions
- free-plan-compatible Hugging Face static evidence/demo surface

## Architecture

```text
User / API
   |
   v
Request validation + policy pre-check
   |
   v
LangGraph Supervisor
   |-------------------------------|
   v               v               v
Research node    Tool node      Approval node
   |               |               |
   v               v               v
Retriever       MCP registry    Human decision
   |               |               |
   |---------------|---------------|
                   v
             Evidence grader
                   |
                   v
             Answer synthesis
                   |
                   v
       Trace + evaluation artifacts
```

## Safe default mode

`AGENTFORGE_MODE=deterministic` is the default. It requires **no model API key** and demonstrates orchestration, retrieval, policy, MCP-style tools, approvals, and evaluation without pretending a proprietary LLM executed anything.

Set `AGENTFORGE_MODE=langchain` and configure `AGENTFORGE_MODEL` only when a supported LangChain provider is intentionally available.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
uvicorn agentforge.api:app --reload
```

Then:

```bash
curl -X POST http://127.0.0.1:8000/v1/agent/run \
  -H 'Content-Type: application/json' \
  -d '{"task":"Summarize the incident-response policy and identify actions that require approval."}'
```

## MCP server

The project targets the **MCP Python SDK v2** and exposes a minimal typed server:

```bash
python -m agentforge.mcp_server
```

The server contains read-only knowledge search and a guarded action proposal tool. Write-like actions return an approval requirement instead of executing side effects.

## Evaluation

```bash
python scripts/evaluate.py
```

The evaluator reads `evals/golden.jsonl` and writes `evaluation.json`. Current checks are deterministic contract tests—not fabricated LLM-quality scores.

Tracked metrics include:

- task completion contract
- expected evidence coverage
- tool-selection correctness
- approval-policy correctness
- citation/evidence-ID presence
- latency and tool-call count

Future provider-backed releases can extend this with groundedness, faithfulness, retrieval Recall@K/MRR/NDCG, trajectory grading, and cost regression.

## API response contract

Every run returns a structured envelope:

```json
{
  "trace_id": "...",
  "status": "completed",
  "answer": "...",
  "evidence": [{"id":"kb-001","title":"...","score":0.9}],
  "tool_calls": [],
  "policy_events": [],
  "requires_approval": false,
  "latency_ms": 12.3
}
```

## Repository map

```text
src/agentforge/
  api.py            FastAPI service
  config.py         runtime settings
  graph.py          LangGraph orchestration
  model.py          deterministic + LangChain model adapter
  policy.py         tool/action policy gates
  retrieval.py      evidence retrieval contract
  state.py          graph state types
  mcp_server.py     MCP v2 typed tools
  observability.py  traces and timing
  evaluation.py     offline evaluation primitives

evals/              reproducible benchmark cases
scripts/            evaluation runner
hf_static/          recruiter-facing static Space bundle
tests/              policy/retrieval/API-contract tests
.github/workflows/  CI and security checks
```

## Engineering boundaries

- No fabricated benchmark numbers.
- No autonomous destructive actions.
- No secrets in the repository.
- No claim that external cloud infrastructure is deployed unless execution evidence is committed.
- Tool side effects should be protected by authentication, authorization, audit logging, and explicit approval in a real deployment.

## Current evidence status

| Capability | Status |
|---|---|
| Deterministic agent orchestration | Implemented |
| LangGraph graph | Implemented |
| LangChain provider adapter | Implemented, provider opt-in |
| MCP v2 typed tool server | Implemented |
| Read-only retrieval | Implemented |
| Write-action approval boundary | Implemented |
| Offline evaluation contract | Implemented |
| FastAPI service | Implemented |
| Docker packaging | Implemented |
| GitHub Actions CI | Implemented |
| Provider-backed LLM benchmark | Not yet claimed |
| Production cloud deployment | Not yet claimed |

## Technology signal

**LangGraph · LangChain · MCP · Agentic RAG · FastAPI · Pydantic · Docker · CI/CD · Evaluation · Guardrails · Human-in-the-loop · Observability · Responsible AI**

## License

MIT
