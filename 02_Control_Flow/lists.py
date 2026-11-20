# Python Lists

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Display the list
print("Numbers:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding an element
numbers.append(60)
print("After append:", numbers)

# Removing an element
numbers.remove(30)
print("After remove:", numbers)

# Finding list length
print("Length:", len(numbers))

# Loop through a list
for num in numbers:
    print(num)
