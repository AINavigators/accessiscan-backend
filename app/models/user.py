from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    password_hash: Optional[str] = None

    role: str = "inspector"  # admin, inspector, reviewer
    created_at: datetime = Field(default_factory=datetime.utcnow)