''' A child class can inherit from multiple parent classes '''

class Person:           # Parent 1

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:          # Parent 2

    def __init__(self, id, gpa):
        self.id = id
        self.gpa = gpa


class UniversityStudent(Person, Student):           # Child of parent 1 and parent 2

    def __init__(self, name, age, id, gpa):
        Person.__init__(self, name, age)
        Student.__init__(self, id, gpa)

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.id)
        print("GPA:", self.gpa)


s1 = UniversityStudent("Rezwan", 22, 20, 3.89)

s1.show()