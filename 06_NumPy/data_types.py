
# NumPy Data Types

import numpy as np

# Integer array
int_arr = np.array([10, 20, 30])

print("Integer Array:", int_arr)
print("Data Type:", int_arr.dtype)

# Float array
float_arr = np.array([10.5, 20.5, 30.5])

print("Float Array:", float_arr)
print("Data Type:", float_arr.dtype)

# String array
str_arr = np.array(["Python", "NumPy", "Pandas"])

print("String Array:", str_arr)
print("Data Type:", str_arr.dtype)

# Specify data type
arr = np.array([1, 2, 3], dtype=np.float64)

print("Converted Array:", arr)
print("New Data Type:", arr.dtype)

# Convert float to integer
numbers = np.array([10.8, 20.5, 30.9])

converted = numbers.astype(int)

print("Original:", numbers)
print("Converted:", converted)
print("Converted Data Type:", converted.dtype)

