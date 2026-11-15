with open("practice.txt", "w") as f:
    f.write("Hi, everyone!\n")
    f.write("We are learning Files.\n")
    f.write("Using Python.\n")
    f.write("Python is very easy.\n")

# Find the word learning

def check():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

def check2():
    word = "learning"
    data = True
    line = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(f"Found at line {line}")
                return line  # Return the line number when found
            line += 1
    print("not found")
    return -1

# Call the functions
check()
check2()