# Length of a list

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show(num):
    print("Length: ",len(num))

show(num)

print()
# Print the elements from list

num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
def show2(num2):
    for index in num2:
        print(index, end = " ")

show2(num2)
print()

print()
# Whatever you want to do just put it in a function

def result(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    print("Factorial: ", fact)

result(5)

print()
# Cont to BDT

taka = float(input("Enter Taka: "))

def conv(taka):
    dollar = taka / 120
    print("Dollar: ", dollar)
    print("BDT: ", taka, "Taka = ", dollar, "USD")

conv(taka)
print()

# Check Even or Odd using function

num3 = int(input("Enter Number: "))

def check(num3):
    if (num3 % 2) == 0:
        print("Even")
    else:
        print("Odd")

check(num3)