from typing import Optional
from pydantic import BaseModel

class rareza(BaseModel):
    id: Optional[int]
    name: str