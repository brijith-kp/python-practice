# Python Sets

# Creating a set
numbers = {10, 20, 30, 40, 20, 10}

# Display set
print("Set:", numbers)

# Adding an element
numbers.add(50)
print("After adding:", numbers)

# Removing an element
numbers.remove(30)
print("After removing:", numbers)

# Finding length
print("Length:", len(numbers))

# Check membership
print(20 in numbers)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
