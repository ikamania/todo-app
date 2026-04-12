from storage.json_storage import JSONStorage, Task, BaseStorage


class TaskManager:
    def __init__(self, storage: BaseStorage | None = None) -> None:
        self.storage = storage or JSONStorage()
        self.tasks: list[Task] = self.storage.load()

    def save_all(self) -> None:
        self.storage.save(self.tasks)

    def add(self, task: Task) -> None:
        self.tasks.append(task)

    def get(self):
        pass

    def list(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
