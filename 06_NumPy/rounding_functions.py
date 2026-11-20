
# NumPy Rounding Functions

import numpy as np

# Create an array with decimal values
numbers = np.array([10.456, 20.789, 30.123, 40.567])

print("Original Array:", numbers)

# Round to nearest integer
print("Rounded:", np.round(numbers))

# Round to 2 decimal places
print("Round to 2 Decimals:", np.round(numbers, 2))

# Floor: Round down
print("Floor:", np.floor(numbers))

# Ceil: Round up
print("Ceil:", np.ceil(numbers))

# Truncate: Remove decimal part
print("Truncated:", np.trunc(numbers))

# Absolute values
negative = np.array([-10, -20, 30, -40])

print("Absolute Values:", np.abs(negative))
