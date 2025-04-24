
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

class Order(BaseModel):
    id: str | None = None
    product: str
    cost: float
    price: float
    channel: Literal["site","whatsapp","insta","revenda"]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    revendedor_id: str | None = None
