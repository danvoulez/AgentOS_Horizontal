
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    id: str | None = None
    email: EmailStr
    password: str
    role: str = "revenda"
    trust_score: float = 1.0
    disabled: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
