
# NumPy Correlation and Covariance

import numpy as np

# Student study hours
study_hours = np.array([1, 2, 3, 4, 5])

# Student exam marks
marks = np.array([40, 50, 60, 70, 80])

print("Study Hours:", study_hours)
print("Marks:", marks)

# Calculate correlation coefficient
correlation = np.corrcoef(study_hours, marks)

print("\nCorrelation Matrix:")
print(correlation)

# Calculate covariance matrix
covariance = np.cov(study_hours, marks)

print("\nCovariance Matrix:")
print(covariance)
