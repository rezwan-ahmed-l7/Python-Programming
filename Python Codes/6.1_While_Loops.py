# Print numbers from 1 to 10
n = 1

while n <= 10:
    print(n)
    n += 1

print("--------------")


# Continue statement is used for skipping the iteration (corrected)

q = 0

while q <= 10:
    q += 1                  # Move increment before the condition check
    if q % 2 == 0:
        continue            # Skip the iteration for even numbers
    else:
        print(q)

print("--------------")


# Alternative way: increment at the end (with careful placement)

q = 0

while q <= 10:
    if q % 2 == 0:
        q += 1              # Increment before continue
        continue
    else:
        print(q)
        q += 1

print("--------------")


# Reverse numbers from 10 to 1

m = 10

while m >= 1:
    print(m)
    m -= 1