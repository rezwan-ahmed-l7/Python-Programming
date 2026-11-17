''' We must use " from abc import ABC, abstractmethod " to create abstract class and abstract method '''

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

r1 = Rectangle(10, 5)
c1 = Circle(7)

print("Rectangle Area:", r1.area())
print("Circle Area:", c1.area())