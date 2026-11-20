# Python Dictionaries

# Creating a dictionary
student = {
    "name": "Brijith",
    "age": 22,
    "cgpa": 8.5,
    "course": "B.Tech"
}

# Display dictionary
print("Student Details:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["college"] = "LBS College of Engineering"
print("After adding:", student)

# Updating a value
student["age"] = 23
print("After updating:", student)

# Removing a key-value pair
student.pop("course")
print("After removing:", student)

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
