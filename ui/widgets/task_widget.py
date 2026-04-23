from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import Button, Checkbox, Label, Input


class TaskWidget(HorizontalGroup):
    def __init__(self, content: str, uploaded: str, deadline: str, complete: bool):
            super().__init__()
            self.content = content
            self.uploaded = uploaded
            self.deadline = deadline
            self.complete = complete

    def compose(self) -> ComposeResult:
        yield VerticalGroup(
            HorizontalGroup (
                Label(self.content, classes="content"),

                HorizontalGroup (
                    Checkbox("complete", classes="complete"),
                    Button("delete", classes="delete", variant="error"),
                    classes="delete-complete"
                ),
            ),

            HorizontalGroup (
                Label(f"uploaded: {self.uploaded}", classes="date"),
                Label(f"deadline: {self.deadline}", classes="date"),
                classes="dates"
            )
        )


class TaskAdder(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield VerticalGroup(
            HorizontalGroup (
                Input(placeholder="Write your task here..", classes="task-input"),

                HorizontalGroup (
                    Button("add", variant="success"),
                    classes="delete-complete"
                ),
            ),
        )
