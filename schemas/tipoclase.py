from typing import Optional
from pydantic import BaseModel

class tipoclase(BaseModel):
    id: Optional[int]
    name: str