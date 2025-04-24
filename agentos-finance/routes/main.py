
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def ping():
    return {"service": "finance", "status": "ok"}
