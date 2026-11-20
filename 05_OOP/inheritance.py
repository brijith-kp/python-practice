# Python Inheritance

# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


# Creating an object
student1 = Student("Brijith", 22, "Data Science")

student1.display()
student1.show_course()
