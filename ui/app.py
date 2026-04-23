from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer

from core.storage.task import Task
from core.manager import BaseTaskManager, TaskManager
from ui.widgets.task_widget import TaskWidget


class TodoApp(App[None]):
    CSS_PATH = [
        "tcss/styles.tcss",
    ]
    def __init__(self, manager: BaseTaskManager | None = None) -> None:
        super().__init__()
        self.manager = manager or TaskManager()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with VerticalScroll():
            for id, task in self.manager.list().items():
                yield TaskWidget(
                    id, 
                    task["content"],
                    task["uploaded"].strftime("%d %b %Y • %H:%M"),
                    task["deadline"].strftime("%d %b %Y • %H:%M"),
                    task["complete"],
                )
