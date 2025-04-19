from fastapi import APIRouter
from predict_service import predict_logic

router = APIRouter()

@router.get("/predict")
def make_prediction(value: int):
    result = predict_logic(value)
    return {"value": value, "prediction": result}
