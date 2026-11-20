
# NumPy Searching Functions

import numpy as np

# Create an array
numbers = np.array([10, 20, 30, 40, 50, 30, 60])

print("Original Array:", numbers)

# Find positions of value 30
positions = np.where(numbers == 30)
print("Positions of 30:", positions[0])

# Find positions of values greater than 30
result = np.where(numbers > 30)
print("Positions Greater Than 30:", result[0])

# Find the index of the first minimum value
min_index = np.argmin(numbers)
print("Index of Minimum:", min_index)

# Find the index of the first maximum value
max_index = np.argmax(numbers)
print("Index of Maximum:", max_index)

# Find the sorted positions
sorted_indices = np.argsort(numbers)
print("Sorted Indices:", sorted_indices)
