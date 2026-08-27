class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0

        for val in self.marks:
            sum += val
        print("Name: ", self.name)
        print("Average Number: ", sum/3)

s1 = Student("Rex", [99,96,95])
s1.avg()

s1.name = "Lex"
s1.avg()
