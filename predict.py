from fastapi import APIRouter
from schemas.predict_schema import PredictRequest, PredictResponse
from services.predict_service import predict_category

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    category = predict_category(request.value)
    return PredictResponse(prediction=category)