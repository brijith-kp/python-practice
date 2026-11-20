
# NumPy Cumulative Functions

import numpy as np

# Create an array
sales = np.array([100, 200, 150, 300, 250])

print("Daily Sales:", sales)

# Cumulative sum
cumulative_sum = np.cumsum(sales)

print("Cumulative Sales:", cumulative_sum)

# Cumulative product
numbers = np.array([1, 2, 3, 4])

cumulative_product = np.cumprod(numbers)

print("Cumulative Product:", cumulative_product)

# Cumulative maximum
values = np.array([10, 25, 15, 40, 30])

maximum = np.maximum.accumulate(values)

print("Cumulative Maximum:", maximum)

# Cumulative minimum
minimum = np.minimum.accumulate(values)

print("Cumulative Minimum:", minimum)
