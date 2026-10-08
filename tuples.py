# Tuple containing strings
technologies: tuple[str, ...] = (
    "Java",
    "Python",
    "Spring AI"
)

print(technologies[0])
print(technologies[-1])
print(len(technologies))

# Tuple with different element types
model: tuple[str, int] = ("gpt-model", 128000)

# Tuple unpacking
name, context_window = model

print(name)
print(context_window)

# A tuple containing exactly one element
single_item = ("Python",)

print(type(single_item))