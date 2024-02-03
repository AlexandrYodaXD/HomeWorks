from typing import Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=64)
    description: str = Field(..., min_length=1, max_length=128)
    status_complete: bool = False

class TaskNew(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)
    description: str = Field(..., min_length=1, max_length=128)
    status_complete: bool = False
