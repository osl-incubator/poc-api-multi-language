from __future__ import annotations

from fastapi import APIRouter, Request
from poccore import storage

router = APIRouter()


@router.post("/storage/avg-price", tags=["storage"])
async def avg_price(request: Request):
    data = await request.json()
    storage.avg_price(
      groupby=data["groupby"],
      field=data["field"],
      input_path=data["input_path"],
      output_path=data["output_path"]
    )
    return True
