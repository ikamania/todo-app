from core.storage.storage import JSONStorage, BaseStorage
from core.storage.task import Task

import uuid
from typing import Unpack, Any


class TaskManager:
    def __init__(self, storage: BaseStorage | None = None) -> None:
        self.storage = storage or JSONStorage()
        self.tasks: dict[str, Task] = self.storage.load()

    def save_all(self) -> None:
        self.storage.save(self.tasks)

    def add(self, **task_data: Unpack[Task]) -> None:
        id: str = str(uuid.uuid4())

        self.tasks[id] = Task(**task_data)
        self.save_all()

    def get(self, id: str) -> Task | None:
        return self.tasks.get(id)

    def list(self) -> dict[str, Task]:
        return self.tasks

    def update(self, id: str, updates: dict[str, Any]) -> bool:
        task = self.tasks.get(id)
        if task is None:
            return False

        task.update(updates) # <
        self.save_all()

        return True

    def delete(self, id: str) -> bool:
        if id not in self.tasks:
            return False

        del self.tasks[id]
        self.save_all()

        return True
