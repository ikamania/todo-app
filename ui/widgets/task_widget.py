from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import Button, Checkbox, Label, Input
from textual.message import Message
from datetime import datetime


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
    class AddRequested(Message):
        def __init__(self, content: str, deadline: datetime) -> None:
            self.content = content
            self.deadline = deadline
            super().__init__()

    def compose(self) -> ComposeResult:
        yield VerticalGroup(
            HorizontalGroup (
                Input(placeholder="Write your task here..", classes="task-input"),
                Input(placeholder="YYYY-MM-DD HH:MM - deadline", classes="deadline-input"),

                HorizontalGroup (
                    Button("add", variant="success"),
                    classes="delete-complete"
                ),
            ),
        )

    def parse_deadline(self, date: str) -> datetime:
        return datetime.strptime(date.strip(), "%Y-%m-%d %H:%M")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        content_input = self.query_one(".task-input", Input)
        deadline_input = self.query_one(".deadline-input", Input)
    
        content = content_input.value.strip()
        if not content:
            self.notify("Task cannot be empty")
            return

        try:
            parsed_deadline = self.parse_deadline(deadline_input.value)
        except ValueError:
            self.notify("Invalid format. Use YYYY-MM-DD HH:MM")
            return

        self.post_message(self.AddRequested(content, parsed_deadline))

        content_input.value = ""
        deadline_input.value = ""
