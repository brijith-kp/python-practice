
# NumPy Broadcasting

import numpy as np

# Example 1: Add a scalar to an array
arr = np.array([10, 20, 30, 40])

result = arr + 5

print("Original Array:", arr)
print("After Adding 5:", result)


# Example 2: Add two arrays of different shapes
a = np.array([10, 20, 30])
b = np.array([[1], [2], [3]])

result = a + b

print("Broadcasting Result:")
print(result)


# Example 3: Multiply an array by a scalar
numbers = np.array([2, 4, 6])

result = numbers * 3

print("Multiplication Result:", result)
