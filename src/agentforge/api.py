from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from agentforge.config import get_settings
from agentforge.graph import build_graph
from agentforge.observability import Trace

app = FastAPI(title="AgentForge Enterprise", version="0.1.0")


class RunRequest(BaseModel):
    task: str = Field(min_length=3, max_length=8000)
    approved: bool = False


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "mode": get_settings().mode}


@app.post("/v1/agent/run")
def run_agent(request: RunRequest) -> dict:
    settings = get_settings()
    trace = Trace()
    graph = build_graph(settings)
    result = graph.invoke(
        {
            "task": request.task,
            "trace_id": trace.trace_id,
            "evidence": [],
            "tool_calls": [],
            "policy_events": [],
            "requires_approval": False,
            "approved": request.approved,
            "answer": "",
        }
    )
    return {
        "trace_id": trace.trace_id,
        "status": "completed",
        "answer": result.get("answer", ""),
        "evidence": result.get("evidence", []),
        "tool_calls": result.get("tool_calls", []),
        "policy_events": result.get("policy_events", []),
        "requires_approval": result.get("requires_approval", False),
        "latency_ms": trace.latency_ms(),
        "mode": settings.mode,
    }
