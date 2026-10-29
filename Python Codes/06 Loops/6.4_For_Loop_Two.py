# Print the elements from list

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0

for index in lis:
    print(index)
    index += 1

print()


# Find and print number from tuple

key = int(input("Enter Number: "))
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
index = 0

for index in tup:
    if key == index:
        print("Found")
        break
    else:
        print("Not Found")
    index += 1

print()

