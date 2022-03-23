import os
from uuid import uuid4

import botocore
import pandas as pd
import pytest


def parquet_tmp_path():
    return f"/tmp/{uuid4()}.parquet"


@pytest.fixture
def input_path():
    p = parquet_tmp_path()
    yield p
    os.remove(p)


@pytest.fixture
def output_path():
    p = parquet_tmp_path()
    yield p
    os.remove(p)


@pytest.fixture
def df_prices():
    return pd.DataFrame(
        {
            "product": ["car 1", "car 2", "car 3"],
            "brand": ["brand1", "brand2", "brand1"],
            "price": [10000, 20000, 30000],
        }
    )
