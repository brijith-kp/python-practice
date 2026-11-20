
# NumPy Aggregate Functions Along Axis

import numpy as np

# Create a 2D array
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(data)

# Calculate total sum
print("Total Sum:", np.sum(data))

# Sum along columns (axis=0)
print("Column-wise Sum:", np.sum(data, axis=0))

# Sum along rows (axis=1)
print("Row-wise Sum:", np.sum(data, axis=1))

# Column-wise average
print("Column-wise Mean:", np.mean(data, axis=0))

# Row-wise maximum
print("Row-wise Maximum:", np.max(data, axis=1))

# Column-wise minimum
print("Column-wise Minimum:", np.min(data, axis=0))
