import botocore
import pandas as pd
import pytest
from poccore import settings
from poccore.storage import S3ConnectionConfig, get_cloud_connection


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
    settings.config["S3_SECRET_KEY"] = "poc-api"
    settings.config["S3_ACCESS_KEY"] = "poc-api"
    settings.config["S3_REGION"] = None
    settings.config["S3_ENDPOINT"] = "http://localhost:9000/"

    creds = get_cloud_connection()

    client = creds.get_client()
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
