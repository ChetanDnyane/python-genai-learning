# Function with a parameter and return value
def greet(name: str) -> str:
    return f"Hello {name}"


# Function with multiple parameters
def add(a: int, b: int) -> int:
    return a + b


# Function without an explicit return value
def print_task(title: str) -> None:
    print(f"Task: {title}")


# Calling functions
message = greet("Chetan")
print(message)

result = add(10, 20)
print(result)

return_value = print_task("Learn Python")
print(return_value)