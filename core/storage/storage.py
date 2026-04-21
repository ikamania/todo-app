from core.storage.task import Task

import json
from datetime import datetime
from abc import ABC, abstractmethod

DEFAULT_PATH: str = "core/storage/data/data.json"


class BaseStorage(ABC):
    @abstractmethod
    def save(self, tasks: dict[str, Task]) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self) -> dict[str, Task]:
        raise NotImplementedError


class JSONStorage(BaseStorage):
    def __init__(self, path: str = DEFAULT_PATH) -> None:
        self.path = path

    def save(self, tasks: dict[str, Task]) -> None:
        with open(self.path, "w") as f:
            json.dump(tasks, f, default=str, indent=2)

    def load(self) -> dict[str, Task]:
        try:
            with open(self.path, "r") as f:
                content = f.read().strip()
                if not content:
                    return {}

                data = json.loads(content)
                if not isinstance(data, dict):
                    raise ValueError("File does not contain dict")

                for task in data.values():
                    task["deadline"] = datetime.fromisoformat(task["deadline"])
                    task["uploaded"] = datetime.fromisoformat(task["uploaded"])

                return data
        except (FileNotFoundError, json.JSONDecodeError):
            raise
