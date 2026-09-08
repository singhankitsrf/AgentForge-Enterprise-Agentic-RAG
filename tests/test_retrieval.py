from agentforge.retrieval import retrieve


def test_retrieval_returns_evidence_ids():
    results = retrieve("incident response approval", top_k=2)
    assert results
    assert all(item["id"].startswith("kb-") for item in results)
    assert results[0]["score"] >= results[-1]["score"]
