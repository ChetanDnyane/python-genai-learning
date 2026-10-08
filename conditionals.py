priority: int = 2
status: str = "TODO"

# Basic conditional
if priority == 1:
    print("HIGH")
elif priority == 2:
    print("MEDIUM")
else:
    print("LOW")

# Multiple conditions
if status == "TODO" and priority <= 2:
    print("Task should be started")

# Membership checking
allowed_statuses = {"TODO", "IN_PROGRESS", "DONE"}

if status in allowed_statuses:
    print("Valid task status")

# Conditional expression
result = "Active" if status == "IN_PROGRESS" else "Inactive"

print(result)