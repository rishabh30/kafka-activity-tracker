from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime, time
from uuid import UUID
from sqlalchemy.dialects.postgresql import JSONB




class ScheduleCreateResponse(BaseModel):
    id: Optional[UUID] = None
    message: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

