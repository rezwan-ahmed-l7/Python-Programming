class Person:

    def __init__(self, age, name):
        self.age = age
        self.name = name


class Student(Person):

    def __init__(self, age, name, gpa):
        super().__init__(age, name)         # Inherit person class constructor using super keyword
        self.gpa = gpa

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("GPA:", self.gpa)


s1 = Student(22, "Rezwan", 3.89)
s1.show()