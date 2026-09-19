class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


s1 = Student("Rezwan", 22)

s1.setAge(23)

print("Name:", s1.name)
print("Age:", s1.getAge())