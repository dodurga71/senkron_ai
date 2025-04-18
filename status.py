from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def get_status():
    return {
        "status": "aktif",
        "message": "SENKRON AI çalışıyor! Gelecek senkronize ediliyor!",
        "version": "1.0.0"
    }