tasks: list[str] = ["Python", "FastAPI", "RAG"]

# Add an element
tasks.append("MCP")

# Access elements
print(tasks[0])
print(tasks[-1])

# Number of elements
print(len(tasks))

# Slicing
print(tasks[1:3])

# Update an element
tasks[0] = "Python 3.14"

# Remove an element
tasks.remove("RAG")

print(tasks)