
# NumPy Conditional Functions

import numpy as np

# Create an array
marks = np.array([35, 60, 85, 45, 90, 25, 75])

print("Original Marks:", marks)

# np.where(): Replace values based on a condition
result = np.where(marks >= 50, "Pass", "Fail")
print("Results:", result)

# np.clip(): Restrict values within a range
clipped = np.clip(marks, 40, 80)
print("Clipped Marks:", clipped)

# np.select(): Apply multiple conditions
conditions = [
    marks >= 80,
    marks >= 60,
    marks >= 40
]

choices = ["Excellent", "Good", "Average"]

grades = np.select(conditions, choices, default="Fail")

print("Grades:", grades)

# np.any(): Check if at least one value meets condition
print("Any mark above 90:", np.any(marks > 90))

# np.all(): Check if every value meets condition
print("All marks above 20:", np.all(marks > 20))
