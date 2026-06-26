# Program to calculate area and perimeter of a rectangle

# Input: length and width of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculations
area = length * width
perimeter = 2 * (length + width)

# Output
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


'''output - Enter the length of the rectangle: 25
Enter the width of the rectangle: 25
Area of the rectangle: 625.0
Perimeter of the rectangle: 100.0