from __future__ import annotations

import requests

POC_URL = "http://localhost:8000"


def avg_list(values: list) -> float | int | None:
    url = f"{POC_URL}/simple/avg-list"
    x = requests.post(url, json={"values": values})
    return x.json()
