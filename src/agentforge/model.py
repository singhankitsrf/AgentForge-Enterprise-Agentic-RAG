from __future__ import annotations

from agentforge.state import Evidence


def deterministic_synthesis(task: str, evidence: list[Evidence]) -> str:
    refs = ", ".join(item["id"] for item in evidence) or "none"
    if not evidence:
        return "No sufficient evidence was retrieved; escalation is recommended."
    strongest = evidence[0]
    return (
        f"Task: {task}\n\n"
        f"Evidence-backed summary: {strongest['text']}\n\n"
        f"Evidence IDs: {refs}."
    )


def langchain_synthesis(task: str, evidence: list[Evidence], model_id: str) -> str:
    from langchain.agents import create_agent

    context = "\n".join(f"[{e['id']}] {e['title']}: {e['text']}" for e in evidence)
    agent = create_agent(
        model=model_id,
        tools=[],
        system_prompt=(
            "You are an enterprise evidence-synthesis agent. Use only supplied evidence, cite "
            "evidence IDs, and state when evidence is insufficient."
        ),
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": f"Task: {task}\nEvidence:\n{context}"}]}
    )
    messages = result.get("messages", [])
    if not messages:
        raise RuntimeError("LangChain agent returned no messages")
    return str(messages[-1].content)
