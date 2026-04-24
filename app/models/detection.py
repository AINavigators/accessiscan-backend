from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Detection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    inspection_id: int = Field(foreign_key="inspection.id")
    image_id: Optional[int] = Field(default=None, foreign_key="image.id")

    detected_object: str
    confidence_score: float

    bounding_box: Optional[str] = None  # JSON string for now
    recommendation: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)