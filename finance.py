from fastapi import APIRouter

router = APIRouter()

@router.get('/finance')
async def finance():
    return {'finance': 'Finansal analizler burada olacak'}