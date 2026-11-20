
# NumPy Filtering Arrays

import numpy as np

# Create an array
marks = np.array([45, 60, 75, 30, 90, 55, 85])

print("Original Marks:", marks)

# Filter marks greater than 60
result = marks[marks > 60]

print("Marks Greater Than 60:", result)

# Filter marks less than 50
result2 = marks[marks < 50]

print("Marks Less Than 50:", result2)

# Filter marks between 50 and 80
result3 = marks[(marks >= 50) & (marks <= 80)]

print("Marks Between 50 and 80:", result3)

# Filter even numbers
numbers = np.array([10, 15, 20, 25, 30, 35])

even_numbers = numbers[numbers % 2 == 0]

print("Even Numbers:", even_numbers)

# Filter odd numbers
odd_numbers = numbers[numbers % 2 != 0]

print("Odd Numbers:", odd_numbers)
