# Function with no return value

def info(name, age):
    print("Name: ", name)
    print("Age: ", age)

info("Paris", 25)

print()


# Function with default parameters

def info1(name, age = 25):
    print("Name: ", name)
    print("Age: ", age)

info1("Paris")

print()


# Function with variable length arguments

def info2(*args):
    print("Name: ", args[0])
    print("Age: ", args[1])
    print("GPA: ", args[2])

info2("Paris", 25, 3.5)