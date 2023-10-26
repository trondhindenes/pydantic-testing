from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SuperModel(BaseModel):
    name: str  # We always require SUperModel instances to have a name
    created: Optional[datetime] = None  # There "may" be a "created" field. Don't fail if there isnt