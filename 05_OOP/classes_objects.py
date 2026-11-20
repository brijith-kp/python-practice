# Python Classes and Objects

# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    # Method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)


# Creating an object
student1 = Student("Brijith", 22, 8.5)

# Calling method
student1.display_details()
