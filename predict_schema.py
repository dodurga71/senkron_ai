from pydantic import BaseModel

class PredictRequest(BaseModel):
    value: int

class PredictResponse(BaseModel):
    prediction: str