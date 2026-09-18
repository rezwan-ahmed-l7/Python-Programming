class Student:

    university = "BAUST"

    def __init__(self, name):
        self.name = name

    @classmethod
    def changeUniversity(cls, university):
        cls.university = university

    def show(self):
        print("Name:", self.name)
        print("University:", self.university)


s1 = Student("Rezwan")

s1.show()

Student.changeUniversity("BUET")

s1.show()