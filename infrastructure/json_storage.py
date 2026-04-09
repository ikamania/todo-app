import json


class JSONStorage:
    def __init__(self, path: str = "data.json") -> None:
        self.path = path

    def save(self, tasks: list) -> None:
        pass

    def load(self) -> list:
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []
