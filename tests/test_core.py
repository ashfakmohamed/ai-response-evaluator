from ai_response_evaluator import evaluate_response


def test_evaluates_overlap_and_grounding():
    result = evaluate_response(
        "Paris is the capital of France",
        "Paris is the capital",
        ["Paris is the capital of France"],
    )
    assert result.reference_coverage == 0.6667
    assert result.response_precision == 1.0
    assert result.groundedness == 1.0


def test_handles_empty_response():
    result = evaluate_response("expected answer", "", ["context"])
    assert result.response_precision == 0.0
    assert result.groundedness == 0.0
