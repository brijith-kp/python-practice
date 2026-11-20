
# NumPy Set Operations

import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([30, 40, 50, 60, 70])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Union: All unique values from both arrays
union = np.union1d(arr1, arr2)
print("Union:", union)

# Intersection: Common values
intersection = np.intersect1d(arr1, arr2)
print("Intersection:", intersection)

# Difference: Values in arr1 but not in arr2
difference = np.setdiff1d(arr1, arr2)
print("Difference:", difference)

# Symmetric difference: Values not shared
symmetric = np.setxor1d(arr1, arr2)
print("Symmetric Difference:", symmetric)

# Check whether values are present in another array
result = np.isin(arr1, arr2)
print("Common Value Check:", result)
