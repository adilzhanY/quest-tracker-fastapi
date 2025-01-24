from pydantic import BaseModel
from datetime import datetime

class Quest(BaseModel):
    name: str
    is_done: bool = False
    description: str = None
    due_date: datetime