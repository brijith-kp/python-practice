
# NumPy Sorting 2D Arrays

import numpy as np

# Create a 2D array
data = np.array([
    [30, 10, 20],
    [60, 40, 50],
    [90, 70, 80]
])

print("Original Array:")
print(data)

# Sort each row
row_sorted = np.sort(data, axis=1)

print("\nRow-wise Sorting:")
print(row_sorted)

# Sort each column
column_sorted = np.sort(data, axis=0)

print("\nColumn-wise Sorting:")
print(column_sorted)

# Sort entire array after flattening
flat_sorted = np.sort(data, axis=None)

print("\nEntire Array Sorted:")
print(flat_sorted)

# Sort in descending order row-wise
descending = np.sort(data, axis=1)[:, ::-1]

print("\nDescending Row-wise:")
print(descending)
