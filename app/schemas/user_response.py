from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserListResponse(BaseModel):
    id: str
    name: str
    mobile: str
    email: str

    class Config:
        arbitrary_types_allowed = True


class UserCreateResponse(BaseModel):
    id: Optional[UUID] = None
    message: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
