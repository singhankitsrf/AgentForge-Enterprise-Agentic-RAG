# AgentForge Enterprise — Project Charter

**Owner:** Ankit Kumar Singh  
**Portfolio role:** AI Lead / Staff AI Engineer / GenAI Architect / AI Platform Architect  
**Project type:** Governed agentic RAG and enterprise tool-use platform

## Product objective

Build a reproducible reference platform for auditable LLM agents that can retrieve evidence, use typed tools, enforce policy, pause for human approval, and emit traceable execution artifacts.

## Current delivered scope

- LangGraph orchestration with deterministic default execution
- LangChain provider adapter for opt-in model execution
- MCP v2 typed tool server
- retrieval and evidence scoring contract
- prompt-injection and policy checks
- approval boundary for write-like actions
- FastAPI service contract
- evaluation harness and golden cases
- structured tracing and latency fields
- Docker packaging
- CI and dependency-security audit
- Hugging Face static architecture/evidence surface

## Delivery roadmap

### Phase 1 — Platform foundation — COMPLETE
- [x] State-machine orchestration
- [x] MCP tool boundary
- [x] policy and approval controls
- [x] API contract
- [x] deterministic evaluation
- [x] container and CI pipeline

### Phase 2 — Provider-backed AgentOps — NEXT
- [ ] Add production LLM provider configuration with secret-safe setup
- [ ] Add OpenTelemetry/LangSmith-compatible distributed traces
- [ ] Add hybrid vector retrieval and reranking
- [ ] Expand MCP registry to multiple enterprise tools
- [ ] Add adversarial prompt-injection benchmark
- [ ] Measure groundedness, trajectory quality, latency, token usage and cost

### Phase 3 — Enterprise deployment
- [ ] Add authentication and RBAC policy enforcement
- [ ] Add persistent audit/event store
- [ ] Add environment-specific deployment manifests
- [ ] Add canary/release gates for agent changes
- [ ] Publish measured deployment evidence only after execution

## Success criteria

1. Deterministic tests remain reproducible in CI.
2. Every provider-backed result is traceable to model/config/evidence provenance.
3. Tool side effects remain approval- and authorization-gated.
4. New quality claims are backed by committed evaluation artifacts.

## Risks and controls

| Risk | Control |
|---|---|
| Hallucinated or unsupported output | evidence contract + groundedness evaluation |
| Unsafe tool execution | allowlist + approval boundary + future RBAC |
| Prompt injection | pre-checks + adversarial benchmark |
| Hidden regression | CI/evaluation gates |
| Inflated portfolio claims | executed-evidence-only policy |

## Recruiter signal

LangGraph · LangChain · MCP · Agentic RAG · FastAPI · Docker · CI/CD · Evaluation · Guardrails · Human-in-the-loop · Observability · Responsible AI
