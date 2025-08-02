# Creating a vector (list)
vec = [10, 20, 30]

# Add elements
vec.append(40)
vec.extend([50, 60])

# Access elements
print(vec[2])  # 30

# Insert at position
vec.insert(1, 15)  # [10, 15, 20, 30, 40, 50, 60]

# Remove element
vec.remove(30)

# Iterate
for item in vec:
    print(item)
