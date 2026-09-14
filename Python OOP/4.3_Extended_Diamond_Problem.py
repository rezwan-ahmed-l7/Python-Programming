''' Diamond Inheritance with an extended child class 
Must use **kwargs when we use super() method '''

class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def showPerson(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, id, gpa, **kwargs):
        super().__init__(name=name, age=age, **kwargs)
        self.id = id
        self.gpa = gpa

    def showStudent(self):
        print("Student ID:", self.id)
        print("Student GPA:", self.gpa)

class Teacher(Person):
    def __init__(self, name, age, rank, dept, **kwargs):
        super().__init__(name=name, age=age, **kwargs)
        self.rank = rank
        self.dept = dept

    def showTeacher(self):
        print("Teacher Rank:", self.rank)
        print("Teacher Department:", self.dept)

class Professor(Student, Teacher):
    def __init__(self, name, age, id, gpa, rank, dept, **kwargs):
        super().__init__(name=name, age=age, id=id, gpa=gpa, rank=rank, dept=dept, **kwargs)

# Passes everything as keyword args so it fans out correctly
# across the MRO: Professor -> Student -> Teacher -> Person

    def showProfessor(self):
        self.showPerson()
        self.showStudent()
        self.showTeacher()

class Researcher(Professor):
    def __init__(self, name, age, id, gpa, rank, dept, research, **kwargs):
        super().__init__(name, age, id, gpa, rank, dept, **kwargs)
        self.research = research

    def showResearcher(self):
        self.showProfessor()
        print("Research:", self.research)

r1 = Researcher("Paris", 22, 70902, 3.89, "Professor", "CSE", "AI")
r1.showResearcher()
print()

s1 = Student("Rafi", 20, 12345, 3.75)
s1.showPerson()
s1.showStudent()
print()


t1 = Teacher("Karim Sir", 45, "Associate Professor", "EEE")
t1.showPerson()
t1.showTeacher()
print()

p1 = Professor("Nusrat", 35, 99887, 3.95, "Assistant Professor", "CSE")
p1.showProfessor()