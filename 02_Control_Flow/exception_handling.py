# Python Exception Handling

# Example 1: ZeroDivisionError

try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# Example 2: ValueError

try:
    number = int("hello")
    print(number)

except ValueError:
    print("Invalid input")


# Example 3: Finally

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program completed")
  
