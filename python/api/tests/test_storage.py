import pandas as pd

from pocapi import storage


def test_avg_price(df_prices, input_path, output_path):
    df_prices.to_parquet(input_path)

    status = storage.avg_price(
        groupby="brand",
        field="price",
        input_path=input_path,
        output_path=output_path,
    )

    assert status

    result = pd.read_parquet(output_path)

    for brand in ["brand1", "brand2"]:
        assert result[result.brand == brand].price.values[0] == 20000
