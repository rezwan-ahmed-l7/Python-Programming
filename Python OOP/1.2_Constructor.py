''' Constructor in Python: 
We must use __init__ method to create a constructor
and self is the first parameter of __init__ method '''

# Constructor with parameters
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

c = Car("Nissan", "Red")
print(c.brand)
print(c.color)  

# Constructor with short parameters 

class Car1:
    def __init__(self, b, c):
        self.brand = b
        self.color = c

c1 = Car1("Honda", "White")
print(c1.brand)
print(c1.color)

# Default Constructor or Constructor without parameters

class Car2:
    def __init__(self):
        self.brand = "Dodge"
        self.color = "Black"

c2 = Car2()
print(c2.brand)
print(c2.color)