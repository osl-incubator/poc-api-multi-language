"""Tests for `poc-multi-api` package."""
from uuid import uuid4

from poccore import storage


def parquet_tmp_path():
    return f"/tmp/{uuid4()}.parquet"


def test_avg_parquet_local(response, df_prices):
    prices_path = parquet_tmp_path()
    result_path = parquet_tmp_path()

    df_prices.to_parquet(prices_path)

    storage.avg(prices_path, prices_path)
