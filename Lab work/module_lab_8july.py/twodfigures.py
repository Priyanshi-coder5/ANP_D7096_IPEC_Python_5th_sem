#--------------problem statement-----------------
'''Develop a menu-driven Python application that demonstrates the use of User-Defined
Modules and Functions.
Requirements
You are required to create a Python module named twodfigures.py that contains functions to perform
the following calculations for different two-dimensional shapes:
• Triangle
o Calculate Area
o Calculate Perimeter
• Circle
o Calculate Area
o Calculate Circumference (Perimeter)
• Square
o Calculate Area
o Calculate Perimeter
• Rectangle
o Calculate Area
o Calculate Perimeter
-----------------------------------------'''

#------------coding----------------------
import math


# --- Triangle ---
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

# --- Circle ---
def circle_area(radius):
    return math.pi * radius * radius

def circle_circumference(radius):
    return 2 * math.pi * radius

# --- Square ---
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

# --- Rectangle ---
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

