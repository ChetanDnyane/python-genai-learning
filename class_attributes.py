class Task:

    task_count = 0

    def __init__(self, title: str) -> None:
        self.title = title
        self.status = "TODO"
        self.tags: list[str] = []

        Task.task_count += 1


task1 = Task("Learn Python")
task2 = Task("Learn FastAPI")

# Instance attributes
task1.status = "IN_PROGRESS"
task1.tags.append("Backend")

print(task1.title, task1.status, task1.tags)
print(task2.title, task2.status, task2.tags)

# Shared class attribute
print("Total tasks:", Task.task_count)