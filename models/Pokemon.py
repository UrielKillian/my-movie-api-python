from pydantic import BaseModel, Field
from typing import Optional


class Pokemon(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 9999,
                "name": "Pikachu"
            }
        }