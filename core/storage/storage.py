import json
from datetime import datetime
from typing import TypedDict
from abc import ABC, abstractmethod


class Task(TypedDict):
    id: str
    name: str
    created_at: datetime
    deadline: datetime
    complete: bool


class BaseStorage(ABC):
    @abstractmethod
    def save(self, tasks: list[Task]) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def load(self) -> list[Task]:
        raise NotImplementedError


class JSONStorage(BaseStorage):
    def __init__(self, path: str = "core/storage/data/data.json") -> None:
        self.path = path

    def save(self, tasks: list[Task]) -> None:
        with open(self.path, "w") as f:
            json.dump(tasks, f, default=str, indent=2)

    def load(self) -> list[Task]:
        try:
            with open(self.path, "r") as f:
                data = json.load(f)

                return data
        except FileNotFoundError:
            raise
        except json.JSONDecodeError:
            raise
