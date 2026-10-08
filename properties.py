class Task:

    def __init__(self, title: str) -> None:
        self.title = title

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Title cannot be empty")

        self._title = value


task = Task("Learn Python")

# Calls the getter
print(task.title)

# Calls the setter
task.title = "Learn FastAPI"

print(task.title)

# Invalid value
try:
    task.title = ""
except ValueError as error:
    print("Validation failed:", error)