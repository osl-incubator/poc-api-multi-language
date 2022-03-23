"""Tests for `poc-multi-api` package."""
import pandas as pd
from poccore import storage


def test_price_avg(df_prices, input_path, output_path):
    df_prices.to_parquet(input_path)

    storage.price_avg(input_path, output_path)

    result = pd.read_parquet(output_path)

    for brand in ["brand1", "brand2"]:
        assert result[result.brand == brand].price.values[0] == 20000
