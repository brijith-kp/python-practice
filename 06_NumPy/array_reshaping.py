# NumPy Array Reshaping

import numpy as np

# Creating a 1D array
numbers = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(numbers)

# Reshape into 2 rows and 3 columns
matrix = numbers.reshape(2, 3)

print("Reshaped Array:")
print(matrix)

# Reshape into 3 rows and 2 columns
matrix2 = numbers.reshape(3, 2)

print("Another Reshaped Array:")
print(matrix2)

# Flatten: Convert 2D array into 1D
flat_array = matrix.flatten()

print("Flattened Array:")
print(flat_array)

# Axis operations
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Column-wise Sum:", np.sum(data, axis=0))
print("Row-wise Sum:", np.sum(data, axis=1))
