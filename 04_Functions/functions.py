# Python Functions

# Creating a simple function
def greet():
    print("Hello, Brijith!")

# Calling the function
greet()


# Function with parameters
def add(a, b):
    result = a + b
    print("Addition:", result)

add(10, 20)


# Function with return value
def multiply(a, b):
    return a * b

answer = multiply(5, 4)
print("Multiplication:", answer)


# Function with default parameter
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Brijith")
