with open("practice.txt", "w") as f:
    f.write("Hi, everyone!\n")
    f.write("We are learning Files.\n")
    f.write("Using Python.\n")
    f.write("Python is very easy.\n")

# Find the word learning

def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_for_word()
