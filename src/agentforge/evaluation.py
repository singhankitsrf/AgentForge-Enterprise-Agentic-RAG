from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvalResult:
    passed: bool
    evidence_recall: float
    approval_correct: bool


def evaluate_case(*, expected_evidence: set[str], observed_evidence: set[str], expected_approval: bool, observed_approval: bool) -> EvalResult:
    if expected_evidence:
        recall = len(expected_evidence & observed_evidence) / len(expected_evidence)
    else:
        recall = 1.0
    approval_correct = expected_approval == observed_approval
    return EvalResult(passed=(recall == 1.0 and approval_correct), evidence_recall=recall, approval_correct=approval_correct)
