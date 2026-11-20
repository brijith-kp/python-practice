
# NumPy Array Iteration

import numpy as np

# 1D Array
arr = np.array([10, 20, 30, 40, 50])

print("1D Array Iteration:")

for x in arr:
    print(x)


# 2D Array
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array Iteration:")

for row in data:
    print(row)


# Iterate through every element in a 2D array
print("\nEvery Element:")

for x in np.nditer(data):
    print(x)


# Iterate with index positions
print("\nIndex and Value:")

for index, value in np.ndenumerate(data):
    print("Index:", index, "Value:", value)
