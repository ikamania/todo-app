from core.services.task_service import TaskManager
from infrastructure.json_storage import JSONStorage, Task


class App:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        storage = JSONStorage()
        manager = TaskManager(storage) 

        t1: Task = {
            "id": 1,
            "name": "homework",
            "created_at": "today",
            "deadline": "tommorow",
            "status": True,
        }
        manager.add(t1)
        manager.save_all()




if __name__ == "__main__":
    app = App()

    app.run()
