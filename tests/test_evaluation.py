from agentforge.evaluation import evaluate_case


def test_evaluation_contract_passes_when_expected_evidence_present():
    result = evaluate_case(
        expected_evidence={"kb-001"},
        observed_evidence={"kb-001", "kb-002"},
        expected_approval=False,
        observed_approval=False,
    )
    assert result.passed
    assert result.evidence_recall == 1.0
