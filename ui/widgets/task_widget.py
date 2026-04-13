from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import Button, Checkbox, Label


class TaskWidget(HorizontalGroup):
    def __init__(self, id: int, name: str, created_at: str, deadline: str, complete: bool):
            super().__init__()
            self.task_name = name
            self.created_at = created_at
            self.deadline = deadline
            self.complete = complete

    def compose(self) -> ComposeResult:
        yield VerticalGroup(
            HorizontalGroup (
                Label(self.task_name, classes="name"),

                HorizontalGroup (
                    Checkbox("complete", classes="complete"),
                    Button("delete", classes="delete", variant="error"),
                    classes="delete-complete"
                ),
            ),

            HorizontalGroup (
                Label(f"Created: {self.created_at}", classes="date"),
                Label(f"Deadline: {self.deadline}", classes="date"),
                classes="dates"
            )
        )

