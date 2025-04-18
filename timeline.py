from fastapi import APIRouter

router = APIRouter()

@router.get('/timeline')
async def timeline():
    return {'timeline': 'Timeline verileri burada olacak'}