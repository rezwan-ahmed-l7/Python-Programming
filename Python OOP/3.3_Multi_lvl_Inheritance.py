''' Child can inherit from 2nd parent class and 2nd parent class can inherit from 1st parent class '''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):          # 1st level Inherit Person

    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id


class UniStudent(Student):      # 2nd level Inherit Student

    def __init__(self, name, age, id, gpa):
        super().__init__(name, age, id)
        self.gpa = gpa

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.id)
        print("GPA:", self.gpa)


s1 = UniStudent("Rezwan", 22, 20, 3.89)
s1.show()