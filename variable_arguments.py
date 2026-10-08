# Variable positional arguments
def print_tasks(*tasks: str) -> None:
    print("Tasks:", tasks)
    print("Type:", type(tasks))


# Variable keyword arguments
def print_properties(**properties: object) -> None:
    print("Properties:", properties)
    print("Type:", type(properties))


# Combining both
def process_task(
    task_id: int,
    *actions: str,
    **options: object
) -> None:
    print("Task ID:", task_id)
    print("Actions:", actions)
    print("Options:", options)


print_tasks("Python", "FastAPI", "MCP")

print_properties(
    priority="HIGH",
    status="TODO"
)

process_task(
    101,
    "validate",
    "update",
    priority="HIGH",
    notify=True
)


# Unpacking arguments
def create_task(title: str, priority: str) -> None:
    print(f"{title} | {priority}")


task_arguments = {
    "title": "Learn Python",
    "priority": "HIGH"
}

create_task(**task_arguments)