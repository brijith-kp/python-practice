# Python Abstraction

from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Child Class
class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


# Creating object
car = Car()

car.start()
car.stop()
