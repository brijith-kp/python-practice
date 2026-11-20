
# NumPy Saving and Loading Arrays

import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Save array as a binary .npy file
np.save("my_array.npy", arr)

# Load the saved array
loaded_array = np.load("my_array.npy")

print("Loaded Array:", loaded_array)


# Create another array
data = np.array([[1, 2, 3], [4, 5, 6]])

# Save as a CSV-style text file
np.savetxt("my_data.csv", data, delimiter=",", fmt="%d")

# Load the CSV file
loaded_data = np.loadtxt("my_data.csv", delimiter=",")

print("Loaded 2D Array:")
print(loaded_data)
