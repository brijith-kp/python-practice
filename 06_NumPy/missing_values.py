
# NumPy Handling Missing Values

import numpy as np

# Create an array with missing values
data = np.array([10, 20, np.nan, 40, np.nan, 60])

print("Original Array:", data)

# Check missing values
print("Missing Values:", np.isnan(data))

# Count missing values
print("Number of Missing Values:", np.isnan(data).sum())

# Calculate mean (ignoring missing values)
print("Mean:", np.nanmean(data))

# Calculate sum (ignoring missing values)
print("Sum:", np.nansum(data))

# Replace missing values with 0
cleaned_data = np.nan_to_num(data, nan=0)

print("Cleaned Array:", cleaned_data)
