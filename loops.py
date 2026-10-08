tasks = ["Python", "FastAPI", "RAG", "MCP"]

# 1. Iterate over elements
for task in tasks:
    print(task)

# 2. Counter-based iteration
for i in range(3):
    print("Iteration:", i)

# 3. Index and element together
for index, task in enumerate(tasks, start=1):
    print(index, task)

# 4. While loop
count = 0

while count < 3:
    print("Count:", count)
    count += 1

# 5. Break and continue
for task in tasks:
    if task == "RAG":
        continue

    if task == "MCP":
        break

    print("Processing:", task)