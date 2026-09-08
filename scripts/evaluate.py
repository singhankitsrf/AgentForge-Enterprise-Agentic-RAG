from __future__ import annotations

import json
from pathlib import Path

from agentforge.config import Settings
from agentforge.evaluation import evaluate_case
from agentforge.graph import build_graph

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    graph = build_graph(Settings(mode="deterministic"))
    results = []
    for raw in (ROOT / "evals" / "golden.jsonl").read_text().splitlines():
        case = json.loads(raw)
        output = graph.invoke(
            {
                "task": case["task"],
                "trace_id": case["id"],
                "evidence": [],
                "tool_calls": [],
                "policy_events": [],
                "requires_approval": False,
                "approved": False,
                "answer": "",
            }
        )
        observed = {item["id"] for item in output.get("evidence", [])}
        score = evaluate_case(
            expected_evidence=set(case["expected_evidence"]),
            observed_evidence=observed,
            expected_approval=case["expected_approval"],
            observed_approval=output.get("requires_approval", False),
        )
        results.append({"id": case["id"], **score.__dict__})
    payload = {
        "scope": "deterministic contract evaluation; not an LLM quality benchmark",
        "cases": len(results),
        "passed": sum(int(item["passed"]) for item in results),
        "results": results,
    }
    (ROOT / "evaluation.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    if payload["passed"] != payload["cases"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
