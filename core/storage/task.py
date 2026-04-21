from datetime import datetime
from typing import TypedDict


class Task(TypedDict):
    content: str 
    uploaded: datetime
    deadline: datetime
    complete: bool
