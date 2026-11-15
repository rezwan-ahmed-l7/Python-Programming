with open("practice.txt", "w") as f:
    f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

# Question 5

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

nums = data.split(",")
for val in nums:
    if(int(val) % 2 == 0):
        print(val)  # Show even numbers
        count += 1

print("Total even numbers: ", count)