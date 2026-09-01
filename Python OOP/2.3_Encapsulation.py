class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private
    
    def show(self):
        print("Name: ", self.name)
        print("Age: ", self.__age)

p1 = Person("Sara", 25)
p1.show()