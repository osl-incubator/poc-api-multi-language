"""Tests for `poc-multi-api` package."""
from uuid import uuid4

import pandas as pd
from poccore import storage


def parquet_tmp_path():
    return f"/tmp/{uuid4()}.parquet"


def test_avg_parquet_local(df_prices):
    prices_path = parquet_tmp_path()
    result_path = parquet_tmp_path()

    df_prices.to_parquet(prices_path)

    storage.avg(prices_path, result_path)

    result = pd.read_parquet(result_path)
    assert result["price"] == 20000
