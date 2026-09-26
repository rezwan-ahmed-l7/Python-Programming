class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):                         # Operator
        return self.length * self.width

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):                         # Operator Overloading
        return 3.1416 * self.radius * self.radius

r1 = Rectangle(10, 5)
c1 = Circle(7)

print("Rectangle Area:", r1.area())
print("Circle Area:", c1.area())