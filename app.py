from core.task_manager import TaskManager
from infrastructure.json_storage import JSONStorage


class App:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        MANAGER = TaskManager() 
        STORAGE = JSONStorage()


if __name__ == "__main__":
    app = App()

    app.run()
