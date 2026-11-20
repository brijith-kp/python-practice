# NumPy Indexing and Slicing

import numpy as np

# Creating an array
numbers = np.array([10, 20, 30, 40, 50, 60])

# Indexing
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# Slicing
print("First three:", numbers[0:3])
print("Middle elements:", numbers[2:5])
print("From index 2:", numbers[2:])

# Modifying elements
numbers[0] = 100
print("Updated array:", numbers)

# Two-dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("First row:", matrix[0])
print("Second row:", matrix[1])
print("Element at row 1, column 2:", matrix[0, 1])
