from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Inspection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    site_name: str
    location: str
    description: Optional[str] = None

    status: str = "draft"  # draft, submitted, reviewed, approved
    inspector_id: Optional[int] = Field(default=None, foreign_key="user.id")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)