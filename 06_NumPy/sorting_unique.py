
# NumPy Sorting and Unique Values

import numpy as np

# Original array
arr = np.array([40, 10, 30, 20, 10, 50])

print("Original Array:", arr)

# Sort array in ascending order
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Find unique values
unique_arr = np.unique(arr)
print("Unique Values:", unique_arr)

# Sort in descending order
descending = np.sort(arr)[::-1]
print("Descending Order:", descending)

# Count unique values
values, counts = np.unique(arr, return_counts=True)

print("Values:", values)
print("Counts:", counts)
