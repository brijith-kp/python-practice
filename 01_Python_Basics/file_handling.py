# Python File Handling

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello Brijith!\n")
    file.write("Learning Python File Handling.")

print("File created successfully")


# Reading a file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)


# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nLearning Data Science.")

print("New content added")
