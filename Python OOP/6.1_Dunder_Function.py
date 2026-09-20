# __str__( ) Dunder Method

class Teacher:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)


s1 = Teacher("Reza", 22)

print(s1)

# __add__( ) Dunder Method

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(80)
s2 = Student(90)

print(s1 + s2)