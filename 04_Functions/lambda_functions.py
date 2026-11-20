# Python Lambda Functions

# Normal function
def square(x):
    return x * x

print("Normal Function:", square(5))


# Lambda function
square_lambda = lambda x: x * x

print("Lambda Function:", square_lambda(5))


# Lambda with two arguments
add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Lambda with condition
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print("Number Check:", check(10))
print("Number Check:", check(7))
