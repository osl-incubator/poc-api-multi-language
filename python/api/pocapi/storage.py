from __future__ import annotations

import requests

from pocapi.settings import POCAPI_URL


def avg_price(
    groupby: str,
    field: str,
    input_path: str,
    output_path: str,
) -> bool:
    url = f"{POCAPI_URL}/storage/avg-price"
    response = requests.post(
        url,
        json={
            "groupby": groupby,
            "field": field,
            "input_path": input_path,
            "output_path": output_path,
        },
    )
    return response.json()["status"]
