from pydantic import BaseModel
from typing import Dict, Any


class JobCreate(BaseModel):
    type: str
    payload: Dict[str, Any]
