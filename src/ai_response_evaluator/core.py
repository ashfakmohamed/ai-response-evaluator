import re
from dataclasses import dataclass

TOKEN = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Evaluation:
    reference_coverage: float
    response_precision: float
    groundedness: float


def _tokens(text: str) -> set[str]:
    return set(TOKEN.findall(text.casefold()))


def _ratio(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def evaluate_response(reference: str, response: str, contexts: list[str]) -> Evaluation:
    reference_tokens = _tokens(reference)
    response_tokens = _tokens(response)
    context_tokens = _tokens(" ".join(contexts))
    overlap = reference_tokens & response_tokens
    return Evaluation(
        reference_coverage=_ratio(len(overlap), len(reference_tokens)),
        response_precision=_ratio(len(overlap), len(response_tokens)),
        groundedness=_ratio(len(response_tokens & context_tokens), len(response_tokens)),
    )
