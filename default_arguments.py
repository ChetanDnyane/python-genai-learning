# Default parameters and keyword arguments
def create_task(
    title: str,
    priority: str = "MEDIUM",
    status: str = "TODO"
) -> None:
    print(f"{title} | {priority} | {status}")


create_task("Learn Python")

create_task("Learn FastAPI", "HIGH")

create_task(
    title="Learn MCP",
    status="IN_PROGRESS"
)

create_task(
    status="DONE",
    priority="LOW",
    title="Learn Java"
)


# Safe mutable default parameter
def add_task(
    task: str,
    tasks: list[str] | None = None
) -> list[str]:

    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("Python"))
print(add_task("FastAPI"))