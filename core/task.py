from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    name: str 
    created_at: datetime
    deadline: datetime
    complete: bool
