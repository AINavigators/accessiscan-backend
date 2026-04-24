from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    inspection_id: int = Field(foreign_key="inspection.id")
    image_url: str
    image_name: Optional[str] = None

    uploaded_by: Optional[int] = Field(default=None, foreign_key="user.id")
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)