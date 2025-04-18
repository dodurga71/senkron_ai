from fastapi import APIRouter

router = APIRouter()

@router.get('/energy')
async def energy():
    return {'energy': 'Enerji analizleri burada olacak'}