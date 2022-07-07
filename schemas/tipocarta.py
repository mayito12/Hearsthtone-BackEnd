from typing import Optional
from pydantic import BaseModel

class tipocarta(BaseModel):
    id: Optional[int]
    name: str