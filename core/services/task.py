class Task:
    def __init__(
        self, id: int, name: str, created_at: str, deadline: str, status: bool
    ) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at 
        self.deadline = deadline
        self.status = status

    def complete(self) -> None:
        pass

    def rename(self) -> None:
        pass

    def reschedule(self) -> None:
        pass
