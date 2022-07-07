from typing import Optional
from pydantic import BaseModel

class Dishes(BaseModel):
    id: Optional[int]
    name: str