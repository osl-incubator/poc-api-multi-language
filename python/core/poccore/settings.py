import os

import s3fs

config = {}
config["S3_BUCKET"] = os.getenv("S3_BUCKET")
config["S3_SECRET_KEY"] = os.getenv("S3_SECRET_KEY")
config["S3_ACCESS_KEY"] = os.getenv("S3_ACCESS_KEY")
config["S3_REGION"] = os.getenv("S3_REGION")
config["S3_ENDPOINT"] = os.getenv("S3_ENDPOINT")


def get_cloud_connection(config=config):
    return s3fs.S3FileSystem(
        key=config["S3_SECRET_KEY"],
        secret=config["S3_ACCESS_KEY"],
        client_kwargs={"endpoint_url": config["S3_ENDPOINT"]},
        skip_instance_cache=True,
    )
