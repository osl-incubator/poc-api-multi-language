"""Main module."""
from __future__ import annotations

from dataclasses import dataclass

import boto3
import pandas as pd
from poccore.settings import get_cloud_connection


@dataclass(frozen=True)
class S3ConnectionConfig:
    bucket: str
    access_key: str
    secret_key: str
    region: str | None = None
    endpoint: str | None = None

    def get_client(self):
        return boto3.client(
            "s3",
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region,
            endpoint_url=self.endpoint,
        )


def avg(path_parquet_input: str, path_parquet_output: str):
    fs = get_cloud_connection()
    df = pd.read_parquet(path_parquet_input, fs=fs)
    df.mean(inplace=True)
    df.write_parquet(path_parquet_output, fs=fs)
