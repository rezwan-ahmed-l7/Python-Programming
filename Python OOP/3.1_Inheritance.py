class Person:                  # Parent Class

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):          # Child Class

    def __init__(self, gpa, id):
        self.gpa = gpa
        self.id = id

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("GPA:", self.gpa)
        print("ID:", self.id)


s1 = Student(3.89, 20)

s1.name = "Rezwan"
s1.age = 22

s1.show()