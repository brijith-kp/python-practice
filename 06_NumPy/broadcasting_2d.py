
# NumPy Broadcasting with 2D Arrays

import numpy as np

# Student marks in three subjects
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70]
])

print("Original Marks:")
print(marks)

# Add bonus marks to every subject
bonus = np.array([5, 10, 5])

updated_marks = marks + bonus

print("\nUpdated Marks:")
print(updated_marks)

# Subtract 5 marks from every student
adjusted_marks = marks - 5

print("\nAdjusted Marks:")
print(adjusted_marks)

# Multiply every mark by 2
doubled_marks = marks * 2

print("\nDoubled Marks:")
print(doubled_marks)

# Calculate each student's total marks
total = np.sum(marks, axis=1)

print("\nTotal Marks:")
print(total)
