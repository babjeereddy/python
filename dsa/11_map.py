student = {"name": "Alice", "age": 21, "grade": "A"}

print(student["name"])  # Alice

student["age"] = 22
del student["grade"]

for key, value in student.items():
    print(key, value)

