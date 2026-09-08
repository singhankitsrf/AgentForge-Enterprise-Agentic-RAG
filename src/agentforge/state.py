from typing import NotRequired, TypedDict


class Evidence(TypedDict):
    id: str
    title: str
    text: str
    score: float


class ToolCall(TypedDict):
    name: str
    args: dict
    result: NotRequired[dict]


class AgentState(TypedDict):
    task: str
    trace_id: str
    evidence: list[Evidence]
    tool_calls: list[ToolCall]
    policy_events: list[dict]
    requires_approval: bool
    approved: bool
    answer: str
