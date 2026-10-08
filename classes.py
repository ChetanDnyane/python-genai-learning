class Task:

    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title
        self.status = "TODO"

    def display(self) -> None:
        print(f"{self.id}: {self.title} [{self.status}]")

    def start(self) -> None:
        self.status = "IN_PROGRESS"


# Create an instance
task1 = Task(101, "Learn Python")

# Access instance attributes
print(task1.id)
print(task1.title)
print(task1.status)

# Call instance methods
task1.display()

task1.start()

task1.display()

# Create another instance
task2 = Task(102, "Learn FastAPI")

task2.display()