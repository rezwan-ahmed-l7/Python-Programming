with open("practice.txt", "w") as f:
    f.write("Hi, everyone!\n")
    f.write("We are learning Files.\n")
    f.write("Using Python.\n")
    f.write("Python is very easy.\n")

# Replace Java with Python

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
