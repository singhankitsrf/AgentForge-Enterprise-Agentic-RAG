from __future__ import annotations

from dataclasses import dataclass

READ_ONLY_TOOLS = {"knowledge_search", "calculator", "repository_read"}
WRITE_TOOLS = {"create_issue", "send_message", "change_infrastructure", "modify_record"}


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    requires_approval: bool
    reason: str


def contains_injection_pattern(text: str) -> bool:
    lowered = text.lower()
    patterns = (
        "ignore previous instructions",
        "ignore all previous",
        "reveal system prompt",
        "show your hidden prompt",
        "exfiltrate secret",
    )
    return any(pattern in lowered for pattern in patterns)


def authorize_tool(tool_name: str, *, require_approval_for_writes: bool = True) -> PolicyDecision:
    if tool_name in READ_ONLY_TOOLS:
        return PolicyDecision(True, False, "read-only tool")
    if tool_name in WRITE_TOOLS:
        return PolicyDecision(True, require_approval_for_writes, "write action")
    return PolicyDecision(False, False, "tool is not allowlisted")
