from typing import Optional
from pydantic import BaseModel, Field


class InsertActivityRequest(BaseModel):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
