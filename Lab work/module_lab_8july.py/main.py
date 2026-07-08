#----------------problem statement------------------
'''Create another Python file named operations.py that imports the twodfigures module and performs
the following tasks:
1. Display a menu for selecting one of the following figures:
o Square
o Circle
o Triangle
o Rectangle
2. Based on the user's choice, ask for the required dimensions of the selected figure.
Example:
▪ Circle → Radius
▪ Square → Side
▪ Rectangle → Length and Breadth
▪ Triangle → Three sides (for perimeter) and Base & Height (for area)
3. Display a second menu to choose the required operation:
o Area
o Perimeter
4. Call the appropriate function from the twodfigures module based on the user's selections.
5. Display the calculated result in a user-friendly format.
6. Allow the user to perform multiple calculations until they choose to exit the application'''

#-------------coding----------------------
# main.py
import twodfigures

def main():
    while True:
        print("\n--- Geometry Calculator ---")
        print("1. Square")
        print("2. Circle")
        print("3. Triangle")
        print("4. Rectangle")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:  # Square
            side = float(input("Enter side of square: "))
            print("1. Area")
            print("2. Perimeter")
            op = int(input("Choose operation: "))
            if op == 1:
                print("Area of Square =", twodfigures.square_area(side))
            else:
                print("Perimeter of Square =", twodfigures.square_perimeter(side))

        elif choice == 2:  # Circle
            radius = float(input("Enter radius of circle: "))
            print("1. Area")
            print("2. Circumference")
            op = int(input("Choose operation: "))
            if op == 1:
                print("Area of Circle =", twodfigures.circle_area(radius))
            else:
                print("Circumference of Circle =", twodfigures.circle_circumference(radius))

        elif choice == 3:  # Triangle
            print("1. Area")
            print("2. Perimeter")
            op = int(input("Choose operation: "))
            if op == 1:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print("Area of Triangle =", twodfigures.triangle_area(base, height))
            else:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                print("Perimeter of Triangle =", twodfigures.triangle_perimeter(a, b, c))

        elif choice == 4:  # Rectangle
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            print("1. Area")
            print("2. Perimeter")
            op = int(input("Choose operation: "))
            if op == 1:
                print("Area of Rectangle =", twodfigures.rectangle_area(length, breadth))
            else:
                print("Perimeter of Rectangle =", twodfigures.rectangle_perimeter(length, breadth))

        elif choice == 5:  # Exit
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
