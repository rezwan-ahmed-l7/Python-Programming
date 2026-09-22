class Student:

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


s1 = Student(20)
s2 = Student(20)

print(s1 == s2)