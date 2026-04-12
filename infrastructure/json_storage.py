import json
from typing import TypedDict


class Task(TypedDict):
    id: int
    name: str
    created_at: str
    deadline: str
    status: bool


class JSONStorage:
    def __init__(self, path: str = "infrastructure/data/data.json") -> None:
        self.path = path

    def save(self, tasks: list[Task]) -> None:
        with open(self.path, "w") as f:
            json.dump(tasks, f, indent=2)

    def load(self) -> list[Task]:
        try:
            with open(self.path, "r") as f:
                data = json.load(f)

                return data
        except FileNotFoundError as error:
            raise error 
        except json.JSONDecodeError:
            return []
