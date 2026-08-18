# Basic Recursion

def fact(n):
    if n == 0:  # Base Case
        return
    print(n, end = " ")
    fact(n-1)   # Recursive Case

fact(5)
print()

print()
# Factorial using Recursion 

def fact2 (m):
    if (m == 1):    # Base Case
        return 1
    else:
        return m * fact2(m-1) # Recursive Case

print(fact2(5))

''' Remember Recursion works from bottom to top or backward.
    It's like a loop where you have begin from from the end and go back to the start. '''