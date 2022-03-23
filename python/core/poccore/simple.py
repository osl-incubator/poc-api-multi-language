from __future__ import annotations


def avg_list(values: list) -> float | int | None:
    size = len(values)
    return sum(values) / size if size else None
