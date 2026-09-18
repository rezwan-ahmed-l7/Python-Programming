class Person:
    name = "anonymous"

    @classmethod
    def name(cls, name):
        cls.name = name

p = Person()
p.name("Alif")
print(p.name)
print(Person.name)