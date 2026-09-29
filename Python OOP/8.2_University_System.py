class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show(self):
        print(self.name, "-", self.subject)

class Department:

    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers

    def show(self):
        print("Department:", self.name)

        for teacher in self.teachers:
            teacher.show()

t1 = Teacher("Rahman", "DSA")
t2 = Teacher("Karim", "DBMS")
t3 = Teacher("Hasan", "OOP")

teachers = [t1, t2, t3]

cse = Department("CSE", teachers)

cse.show()