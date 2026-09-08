from __future__ import annotations

from mcp.server import MCPServer

from agentforge.policy import authorize_tool
from agentforge.retrieval import retrieve

mcp = MCPServer("AgentForge Enterprise")


@mcp.tool()
def knowledge_search(query: str) -> dict:
    """Search the local evidence base. This tool is read-only."""
    return {"results": retrieve(query, top_k=3)}


@mcp.tool()
def propose_action(action: str, rationale: str) -> dict:
    """Propose an enterprise write action without executing the side effect."""
    decision = authorize_tool(action)
    return {
        "action": action,
        "rationale": rationale,
        "allowed": decision.allowed,
        "requires_approval": decision.requires_approval,
        "reason": decision.reason,
        "executed": False,
    }


if __name__ == "__main__":
    mcp.run()
