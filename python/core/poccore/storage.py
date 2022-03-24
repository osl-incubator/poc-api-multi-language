"""Main module."""
from __future__ import annotations

import pandas as pd


def avg_price(
    groupby: str,
    field: str,
    input_path: str,
    output_path: str,
):
    df = pd.read_parquet(input_path)

    series = df.groupby(groupby)[field].mean()
    result = pd.DataFrame(series).reset_index()

    result.to_parquet(output_path)

    return True
