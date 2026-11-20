# NumPy Boolean Indexing

import numpy as np

# Creating an array
numbers = np.array([10, 20, 30, 40, 50, 60])

# Filter numbers greater than 30
result = numbers[numbers > 30]

print("Numbers greater than 30:", result)

# Filter even numbers
even = numbers[numbers % 2 == 0]

print("Even numbers:", even)

# Filter numbers less than 40
small_numbers = numbers[numbers < 40]

print("Numbers less than 40:", small_numbers)

# Multiple conditions
filtered = numbers[(numbers > 20) & (numbers < 60)]

print("Between 20 and 60:", filtered)

# Boolean mask
condition = numbers > 30

print("Boolean Mask:", condition)
