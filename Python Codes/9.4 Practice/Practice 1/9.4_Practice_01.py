# Question 1

with open("zzz.txt", "w") as f:
    f.write("Hi, everyone!\n")
    f.write("We are learning Files.\n")
    f.write("Using Python.\n")

# This part is to show the output

with open("zzz.txt", "r") as f:
    print(f.read())