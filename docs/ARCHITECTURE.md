# Architecture Notes

## Control plane

AgentForge uses LangGraph as the workflow runtime because enterprise agent systems benefit from explicit state transitions, deterministic control nodes, and auditable boundaries around LLM-driven steps.

## Model plane

The default deterministic synthesizer exists for reproducibility and CI. The LangChain adapter is opt-in. A production implementation should add dynamic model routing based on task complexity, privacy, latency, and cost budgets.

## Tool plane

MCP is the interoperability boundary. Read tools can run automatically when authorized. Side-effecting tools must be allowlisted and should pause for human approval before execution.

## Evidence plane

The included lexical retriever is intentionally small and deterministic. A production release can swap in hybrid BM25 + dense retrieval + reranking while preserving the `Evidence` contract and evaluation interface.

## Evaluation plane

CI runs contract evaluations. Provider-backed releases should add retrieval metrics, trajectory grading, groundedness/faithfulness, safety/adversarial suites, latency, and cost regression thresholds.
