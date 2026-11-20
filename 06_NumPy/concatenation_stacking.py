
# NumPy Concatenation and Stacking

import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Concatenate arrays
combined = np.concatenate((arr1, arr2))
print("Concatenated Array:", combined)

# Horizontal stacking
horizontal = np.hstack((arr1, arr2))
print("Horizontal Stack:", horizontal)

# Vertical stacking
vertical = np.vstack((arr1, arr2))
print("Vertical Stack:")
print(vertical)

# Create two 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Concatenate along rows
result = np.concatenate((a, b), axis=0)
print("Row-wise Concatenation:")
print(result)

# Concatenate along columns
result2 = np.concatenate((a, b), axis=1)
print("Column-wise Concatenation:")
print(result2)
