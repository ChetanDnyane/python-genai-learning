name: str = "Chetan"
age: int = 40
salary: float = 50000.50
active: bool = True

middle_name: str | None = None

print(name)
print(age)
print(salary)
print(active)
print(middle_name)

# Python does not enforce type hints at runtime
age = "Forty"

print(age)
print(type(age))