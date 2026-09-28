class Teacher:

    def __init__(self, name):
        self.name = name

class Department:

    def __init__(self, teachers):
        self.teachers = teachers

    def show(self):
        for teacher in self.teachers:
            print(teacher.name)

t1 = Teacher("Rahman")
t2 = Teacher("Karim")
t3 = Teacher("Hasan")

teachers = [t1, t2, t3]

d1 = Department(teachers)

d1.show()