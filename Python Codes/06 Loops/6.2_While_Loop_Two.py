# Print the table of number from user

j = int(input("Enter Number: "))
i = 1

while i <= 10:
    print(i*j)
    i += 1

print()


# Print the elements of a list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

while index < len(list):
    print(list[index])
    index += 1

print()


# Find and print the element of a tuple

key = int(input("Enter Number: "))
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
index2 = 0

while index2 < len(tup):
    if tup[index] == key:
        print("Found")
        break               # Break the loop
    else:
        print("Not Found")
    index2 += 1