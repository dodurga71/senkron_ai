from fastapi import APIRouter
from app.schemas.predict_schema import PredictRequest, PredictResponse
from app.services.predict_service import predict_logic

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    prediction = predict_logic(request.value)
    return PredictResponse(prediction=prediction)