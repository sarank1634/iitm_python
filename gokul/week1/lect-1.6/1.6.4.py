# 1. write a python code that takes radius of circle as input and prints the area of the circle
from math import pi
r = float(input("enter ht rdius of the circle:"))

area = pi *r ** 2

# print(f"the area of the circle is: {area}")
print("The area of the circle with radius " + str(r) + " is: " + str(area))
