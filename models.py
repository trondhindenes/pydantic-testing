from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class SuperModel(BaseModel):
    name: str  # We always require SUperModel instances to have a name
    created: datetime
    calculated: Optional[datetime] = None
    
    @validator("calculated")
    def validate_field(cls):
        print(cls)