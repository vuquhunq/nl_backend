import uuid
from datetime import datetime
from time import sleep

from bson import ObjectId
from pydantic import BaseModel, Field


class CreateAtModel(BaseModel):
    createdAt: datetime = Field(default=datetime.now(), alias='CreatedAt')
class IDModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
