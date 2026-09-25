class Rectangle:

    def area(self, a, b):
        return a * b


class Square(Rectangle):

    def area(self, a, b):
        return a * a


r1 = Rectangle()
s1 = Square()

print("Rectangle:", r1.area(10, 5))
print("Square:", s1.area(10, 5))