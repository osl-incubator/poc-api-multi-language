from __future__ import annotations

from fastapi import APIRouter, Request
from poccore import simple

router = APIRouter()


@router.post("/simple/avg-list", tags=["simple"])
async def avg_list(request: Request):
    data = await request.json()
    return simple.avg_list(data["values"])
