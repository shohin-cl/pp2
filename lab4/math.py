import math

"""
Python Math library
1)Write a Python program to convert degree to radian.
2)Write a Python program to calculate the area of a trapezoid.
3)Write a Python program to calculate the area of regular polygon.
4)Write a Python program to calculate the area of a parallelogram.
"""


#Task 1
degree  = int(input())
radian = math.radians(degree)

print("Input degree: ", degree)
print("Output radian: ", radian)


#Task 2
height = int(input())
base1 = int(input())
base2 = int(input())

area = 0.5 * (base1 + base2) * height

print("Height: ", height)
print("Base, first value: ", base1)
print("Base, second value: ", base2)
print("Expected Output: ", area)

#Task 3
import math

numsid = int(input("Input number of sides: "))
sidlen = float(input("Input the length of a side: "))
apothem = sidlen / (2 * math.tan(math.pi / numsid))
area = 0.5 * numsid * sidlen * apothem
print("The area of the polygon is:", area)


#Task 4
base = int(input())
height = int(input())

area = base * height

print("Length of base: ", base)
print("Height of parallelogram: ", height)
print("Expected Output: ", area)
