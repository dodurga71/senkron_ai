from fastapi import APIRouter

router = APIRouter()

@router.get('/predict')
async def predict():
    return {'prediction': 'Bu sadece bir demo!' }