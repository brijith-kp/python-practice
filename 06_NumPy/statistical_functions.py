
# NumPy Statistical Functions

import numpy as np

# Create an array
marks = np.array([70, 85, 90, 60, 95, 80])

print("Marks:", marks)

# Calculate mean (average)
print("Mean:", np.mean(marks))

# Calculate median
print("Median:", np.median(marks))

# Find maximum value
print("Maximum:", np.max(marks))

# Find minimum value
print("Minimum:", np.min(marks))

# Calculate standard deviation
print("Standard Deviation:", np.std(marks))

# Calculate variance
print("Variance:", np.var(marks))

# Calculate sum
print("Sum:", np.sum(marks))

# Calculate percentile
print("75th Percentile:", np.percentile(marks, 75))
