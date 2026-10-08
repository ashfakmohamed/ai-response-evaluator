# AI Response Evaluator

Deterministic offline metrics for checking reference coverage, answer precision, and context groundedness in generated responses.

## Use cases

- Fast regression checks for RAG pipelines
- Transparent baseline metrics before model-based judging
- CI-friendly evaluation with no provider keys or network calls

```python
from ai_response_evaluator import evaluate_response

scores = evaluate_response(reference, response, retrieved_contexts)
```

The token-overlap metrics are intentionally simple and explainable; production evaluations should combine them with semantic and human review.

Run `pip install -r requirements-dev.txt`, then `ruff check .` and `python -m pytest -q`.

No license has been selected; all rights are reserved.
