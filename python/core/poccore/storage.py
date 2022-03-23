"""Main module."""
from __future__ import annotations

from dataclasses import dataclass

import boto3
import pandas as pd


def price_avg(
    path_parquet_input: str,
    path_parquet_output: str,
    groupby: str,
    key: str,
):
    df = pd.read_parquet(path_parquet_input)

    series = df.groupby(groupby)[key].mean()
    result = pd.DataFrame(series).reset_index()

    result.to_parquet(path_parquet_output)
