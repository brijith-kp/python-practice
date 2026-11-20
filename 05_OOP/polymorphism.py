# Python Polymorphism

# First class
class Dog:

    def sound(self):
        print("Dog barks")


# Second class
class Cat:

    def sound(self):
        print("Cat meows")


# Third class
class Cow:

    def sound(self):
        print("Cow moos")


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the same method
dog.sound()
cat.sound()
cow.sound()
