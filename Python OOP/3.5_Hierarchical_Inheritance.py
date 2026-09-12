''' Multiple classes can inherit from a single class '''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):              # Inherit Person

    def __init__(self, name, age, id, gpa):
        super().__init__(name, age)
        self.id = id
        self.gpa = gpa

    def show(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student ID:", self.id)
        print("Student GPA:", self.gpa)


class Teacher(Person):              # Inherit Person

    def __init__(self, name, age, rank, dept):
        super().__init__(name, age)
        self.rank = rank
        self.dept = dept

    def show(self):
        print("Teacher Name:", self.name)
        print("Teacher Age:", self.age)
        print("Teacher Rank:", self.rank)
        print("Teacher Department:", self.dept)


s1 = Student("Rezwan", 22, 20, 3.89)

t1 = Teacher("Rahman", 45, "Assistant Professor", "CSE")

s1.show()

print()

t1.show()