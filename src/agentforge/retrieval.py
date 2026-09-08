from __future__ import annotations

import re
from dataclasses import dataclass

from agentforge.state import Evidence


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


DEFAULT_KB = [
    Document(
        "kb-001",
        "Incident response policy",
        "Read-only investigation may proceed automatically. Changes to production systems, "
        "credentials, access controls, or external notifications require explicit approval.",
    ),
    Document(
        "kb-002",
        "Agent tool policy",
        "Knowledge search, calculations, and repository reads are read-only. Creating issues, "
        "changing infrastructure, sending messages, or modifying records are write actions.",
    ),
    Document(
        "kb-003",
        "Evidence and provenance standard",
        "Agent answers must include evidence identifiers for material factual claims. Executed "
        "benchmarks must be distinguished from planned or architectural capabilities.",
    ),
]


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(
    query: str,
    *,
    top_k: int = 3,
    documents: list[Document] | None = None,
) -> list[Evidence]:
    docs = documents or DEFAULT_KB
    q = _tokens(query)
    ranked: list[Evidence] = []
    for doc in docs:
        d = _tokens(f"{doc.title} {doc.text}")
        overlap = len(q & d)
        score = overlap / max(1, len(q))
        ranked.append(
            {
                "id": doc.id,
                "title": doc.title,
                "text": doc.text,
                "score": round(score, 4),
            }
        )
    ranked.sort(key=lambda item: (item["score"], item["id"]), reverse=True)
    return ranked[:top_k]
