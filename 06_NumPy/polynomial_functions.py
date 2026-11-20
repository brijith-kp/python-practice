
# NumPy Polynomial Functions

import numpy as np

# Polynomial coefficients
# Represents: 2x^2 + 3x + 1

coefficients = [2, 3, 1]

# Create polynomial
p = np.poly1d(coefficients)

print("Polynomial:")
print(p)

# Evaluate polynomial at x = 2
result = p(2)

print("\nValue at x = 2:", result)

# Find roots
roots = np.roots(coefficients)

print("\nPolynomial Roots:")
print(roots)

# Polynomial addition
p1 = np.poly1d([1, 2])
p2 = np.poly1d([3, 4])

print("\nPolynomial Addition:")
print(p1 + p2)

# Polynomial multiplication
print("\nPolynomial Multiplication:")
print(p1 * p2)
