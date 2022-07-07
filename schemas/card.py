from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    id: Optional[int]
    name: str
    description: str
    id_R: int
    id_tc: int
    id_TClass: int
