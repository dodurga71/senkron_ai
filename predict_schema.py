from pydantic import BaseModel

class PredictResponse(BaseModel):
    prediction: str