from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "success", "message": "SENKRON AI Core is online!"}