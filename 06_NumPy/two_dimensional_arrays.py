# NumPy 2D Arrays

import numpy as np

# Creating a 2D array
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Display array
print("2D Array:")
print(data)

# Array properties
print("Shape:", data.shape)
print("Dimensions:", data.ndim)
print("Size:", data.size)

# Accessing rows
print("First Row:", data[0])
print("Second Row:", data[1])

# Accessing elements
print("First row, second column:", data[0, 1])

# Accessing columns
print("First Column:", data[:, 0])

# Calculate statistics
print("Total:", np.sum(data))
print("Mean:", np.mean(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
