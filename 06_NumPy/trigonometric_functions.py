
# NumPy Trigonometric Functions

import numpy as np

# Create angles in degrees
angles = np.array([0, 30, 45, 60, 90])

print("Angles:", angles)

# Convert degrees to radians
radians = np.deg2rad(angles)

print("\nRadians:")
print(radians)

# Calculate sine
print("\nSine:")
print(np.sin(radians))

# Calculate cosine
print("\nCosine:")
print(np.cos(radians))

# Calculate tangent
print("\nTangent:")
print(np.tan(radians))

# Convert radians back to degrees
print("\nDegrees:")
print(np.rad2deg(radians))
