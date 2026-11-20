# NumPy Random Module

import numpy as np

# Generate a random integer
number = np.random.randint(1, 100)
print("Random Integer:", number)

# Generate 5 random integers
numbers = np.random.randint(1, 100, size=5)
print("Random Numbers:", numbers)

# Generate random decimal numbers
decimal = np.random.rand(5)
print("Random Decimals:", decimal)

# Generate random numbers from normal distribution
normal = np.random.randn(5)
print("Normal Distribution:", normal)

# Generate random array
data = np.random.randint(1, 50, size=(3, 3))
print("Random 2D Array:")
print(data)

# Set random seed
np.random.seed(42)
print("Reproducible Random Numbers:")
print(np.random.randint(1, 100, size=5))
