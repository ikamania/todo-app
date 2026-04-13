from storage.storage import JSONStorage, Task, BaseStorage
from typing import Unpack


class TaskManager:
    def __init__(self, storage: BaseStorage | None = None) -> None:
        self.storage = storage or JSONStorage()
        self.tasks: list[Task] = self.storage.load()

    def save_all(self) -> None:
        self.storage.save(self.tasks)

    def add(self, task: Task) -> None:
        if any(t["id"] == task["id"] for t in self.tasks):
            raise ValueError(f"task with id {task['id']} already exists")

        self.tasks.append(task)
        self.save_all()

    def get(self, id: int) -> Task | None:
        for task in self.tasks:
            if task["id"] == id:
                return task
        return None

    def list(self) -> list[Task]:
        return self.tasks

    def update(self, id_to_update: int, **updates: Unpack[Task]) -> bool:
        for task in self.tasks:
            if task["id"] == id_to_update:
                task.update(updates)
                self.save_all()

                return True
        return False

    def delete(self, id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task["id"] == id:
                del self.tasks[i]
                self.save_all()

                return True
        return False
