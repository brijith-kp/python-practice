
# NumPy Copy vs View

import numpy as np

# Original array
arr = np.array([10, 20, 30, 40])

print("Original Array:", arr)

# Example 1: Copy
copy_arr = arr.copy()

copy_arr[0] = 100

print("\nAfter Changing Copy:")
print("Original Array:", arr)
print("Copied Array:", copy_arr)


# Example 2: View
view_arr = arr.view()

view_arr[1] = 200

print("\nAfter Changing View:")
print("Original Array:", arr)
print("View Array:", view_arr)
