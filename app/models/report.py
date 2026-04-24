from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    inspection_id: int = Field(foreign_key="inspection.id")

    title: str
    summary: Optional[str] = None
    report_url: Optional[str] = None

    status: str = "generated"  # generated, reviewed, approved
    generated_at: datetime = Field(default_factory=datetime.utcnow)