''' Static Method in Python: 
We must use @staticmethod decorator to create a static method
and self is the first parameter of static method '''

class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Company: ", self.company)

    @staticmethod
    def info():
        print("Google: A tech giant")

e = Employee("Paris", 100000)
e.show()
e.info() 