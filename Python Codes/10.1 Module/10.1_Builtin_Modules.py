''' Build in Modules of Python
math
random
datetime
os
sys
json
re 
collections
itertools '''

import math

radius = float(input("Enter radius: "))

area = math.pi * radius * radius

print("Area of circle:", area)

print()

# Rounded Average

bangla = 78
english = 81
math_mark = 85

average = (bangla + english + math_mark) / 3

print("Average:", average)
print("Rounded Average:", math.ceil(average))