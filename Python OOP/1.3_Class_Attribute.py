''' Class Attribute '''

class Student:
    school = "S.T Philips High School"      # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Paris", 15)
print(s.name)
print(s.age)
print(s.school)     # Accessing class attribute
print( )

#  Example 

class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Company: ", self.company)

e = Employee("Paris", 100000)
e.show()
        