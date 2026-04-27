from textual import on
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer

from core.manager import BaseTaskManager, TaskManager
from ui.widgets.task_widget import TaskWidget, TaskAdder


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
            yield TaskAdder()

            for id, task in self.manager.list().items():
                wd = TaskWidget(
                    id,
                    task["content"],
                    task["uploaded"].strftime("%d %b %Y • %H:%M"),
                    task["deadline"].strftime("%d %b %Y • %H:%M"),
                    task["complete"],
                )
                wd.border_subtitle = id
                yield wd

    @on(TaskWidget.DeleteRequested)
    def on_task_delete(self, message: TaskWidget.DeleteRequested) -> None:
        self.manager.delete(message.id)

    @on(TaskWidget.CompleteRequested)
    def on_task_complete(self, message: TaskWidget.CompleteRequested) -> None:
        self.manager.update(message.id, {"complete": message.complete})
