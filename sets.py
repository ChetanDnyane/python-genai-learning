backend: set[str] = {"Java", "Python", "Spring Boot"}
ai: set[str] = {"Python", "RAG", "MCP"}

# Add an element
backend.add("REST APIs")

# Duplicate elements are ignored
backend.add("Java")

# Membership test
print("Java" in backend)

# Number of elements
print(len(backend))

# Union
print(backend | ai)

# Intersection
print(backend & ai)

# Difference
print(backend - ai)

# Remove safely
backend.discard("Spring Boot")

print(backend)