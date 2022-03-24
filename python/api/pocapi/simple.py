from __future__ import annotations

import requests

from pocapi.settings import POCAPI_URL


def avg_list(values: list) -> float | int | None:
    url = f"{POCAPI_URL}/simple/avg-list"
    response = requests.post(url, json={"values": values})
    return response.json()
