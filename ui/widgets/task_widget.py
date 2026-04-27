from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import Button, Checkbox, Label, Input
from textual.message import Message


class TaskWidget(HorizontalGroup):
    class DeleteRequested(Message):
        def __init__(self, id: str) -> None:
            self.id = id
            super().__init__()

    class CompleteRequested(Message):
        def __init__(self, id: str, complete: bool) -> None:
            self.id = id
            self.complete = complete
            super().__init__()

    def __init__(self, task_id: str, content: str, uploaded: str, deadline: str, complete: bool):
            super().__init__()
            self.task_id = task_id
            self.content = content
            self.uploaded = uploaded
            self.deadline = deadline
            self.complete = complete

    def compose(self) -> ComposeResult:
        yield VerticalGroup(
            HorizontalGroup (
                Label(self.content, classes="content"),

                HorizontalGroup (
                    Checkbox("complete", value=self.complete, classes="complete"),
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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.post_message(self.DeleteRequested(self.task_id))
        self.remove()

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        self.complete = event.value
        self.post_message(self.CompleteRequested(self.task_id, self.complete))

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
