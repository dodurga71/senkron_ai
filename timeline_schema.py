from pydantic import BaseModel

class TimelineResponse(BaseModel):
    timeline: str