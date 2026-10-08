# Create a dictionary
task: dict[str, object] = {
    "id": 101,
    "title": "Learn Python",
    "status": "TODO"
}

# Access values
print(task["title"])

# Safe access
print(task.get("priority", "MEDIUM"))

# Update an existing entry
task["status"] = "IN_PROGRESS"

# Add a new entry
task["priority"] = "HIGH"

# Iterate over entries
for key, value in task.items():
    print(key, ":", value)

# Delete an entry
del task["priority"]

# Check whether a key exists
print("priority" in task)

print(task)