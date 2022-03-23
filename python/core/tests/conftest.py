import botocore
import pandas as pd
import pytest
from poccore import settings
from poccore.storage import S3ConnectionConfig


@pytest.fixture
def df_prices():
    return pd.DataFrame(
        {
            "product": ["car 1", "car 2", "car 3"],
            "price": [10000, 20000, 30000],
        }
    )


@pytest.fixture(scope="function", autouse=True)
def minio_credentials():
    settings.config["S3_BUCKET"] = "poc-api-data"
    settings.config["S3_SECRET_KEY"] = "poc-multi-api"
    settings.config["S3_ACCESS_KEY"] = "poc-multi-api"
    settings.config["S3_REGION"] = None
    settings.config["S3_ENDPOINT"] = "http://localhost:9000/"

    conn = S3ConnectionConfig(
        bucket="/",
        access_key=settings.config["S3_ACCESS_KEY"],
        secret_key=settings.config["S3_SECRET_KEY"],
        endpoint=settings.config["S3_ENDPOINT"],
        region=settings.config["S3_REGION"],
    )

    client = conn.get_client()
    try:
        client.create_bucket(Bucket=settings.config["S3_BUCKET"])
    except botocore.exceptions.ClientError:
        pass


@pytest.fixture(scope="function")
def s3_credentials(flask_client):
    return S3ConnectionConfig(
        bucket="S3BUCKET",
        access_key="S3ACCESSKEY",
        secret_key="S3SECRETACCESSKEY",
        endpoint=None,
        region="S3REGION",
    )
