# Python Map, Filter and Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1. Map: Square every number
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# 2. Filter: Select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# 3. Reduce: Calculate the sum
total = reduce(lambda x, y: x + y, numbers)
print("Total:", total)
