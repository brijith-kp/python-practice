
# NumPy Linear Algebra

import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Matrix addition
print("Addition:")
print(A + B)

# Matrix multiplication
print("Matrix Multiplication:")
print(np.dot(A, B))

# Transpose
print("Transpose of A:")
print(np.transpose(A))

# Determinant
print("Determinant of A:")
print(np.linalg.det(A))

# Inverse
print("Inverse of A:")
print(np.linalg.inv(A))

# Eigenvalues
print("Eigenvalues of A:")
print(np.linalg.eigvals(A))
