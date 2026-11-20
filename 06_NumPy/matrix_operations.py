
# NumPy Matrix Operations

import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Element-wise multiplication
print("\nElement-wise Multiplication:")
print(A * B)

# Matrix multiplication
print("\nMatrix Multiplication:")
print(A @ B)

# Transpose
print("\nTranspose of A:")
print(A.T)

# Identity matrix
print("\nIdentity Matrix:")
print(np.eye(3))

# Diagonal elements
print("\nDiagonal Elements:")
print(np.diag(A))

# Trace (sum of diagonal elements)
print("\nTrace:")
print(np.trace(A))
