from typing import Optional
import uuid
from pydantic import BaseModel, Field


class ListUserRequest(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None)
    name: Optional[str] = Field(default=None)
    mobile: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)

    class Config:
        arbitrary_types_allowed = True


class CreateUserRequest(BaseModel):
    name: str
    mobile: str
    email: str
