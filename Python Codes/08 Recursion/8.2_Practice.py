n = int(input("Enter Number: "))

def sum(n):
    if n == 1:  # Changed from n == 0 to n == 1
        return 1
    else:
        return n + sum(n-1)
    
total = sum(n)
print(total)

# Print the elements from list using recursion

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show(lis, index):
    if index == len(lis):
        return
    else:
        print(lis[index], end = "")
        total = show(lis, index + 1)
        return total

show(lis, 0)