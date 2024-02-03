from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status_complete: bool
