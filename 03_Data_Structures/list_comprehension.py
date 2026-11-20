# Python List Comprehension

# Normal method
numbers = []

for i in range(1, 6):
    numbers.append(i)

print("Normal List:", numbers)


# List comprehension
squares = [i * i for i in range(1, 6)]

print("Squares:", squares)


# Even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print("Even Numbers:", even_numbers)


# Odd numbers
odd_numbers = [i for i in range(1, 11) if i % 2 != 0]

print("Odd Numbers:", odd_numbers)


# Convert names to uppercase
names = ["brijith", "arun", "rahul"]

upper_names = [name.upper() for name in names]

print("Uppercase Names:", upper_names)
