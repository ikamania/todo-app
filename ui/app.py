from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer
from widgets.task_widget import TaskWidget


class TodoApp(App[None]):
    CSS_PATH = [
        "tcss/styles.tcss",
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(
            TaskWidget(),
        )


if __name__ == "__main__":
    app = TodoApp()
    app.run()
