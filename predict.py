from fastapi import APIRouter
from services.predict_service import make_prediction

router = APIRouter()

@router.post("/predict")
async def predict(value: int):
    prediction = make_prediction(value)
    return {"prediction": prediction}