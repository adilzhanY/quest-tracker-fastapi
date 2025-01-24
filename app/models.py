from pydantic import BaseModel, Field
from datetime import date, datetime

class Quest(BaseModel):
    id: int
    title: str
    is_completed: bool = False
    description: str = None
    deadline: date = Field(..., example="2025-01-01", description="Deadline")