#--------problem statement-----------
''' Program to arrange elements in ascending order'''

# Step 1: Input list size and elements
n = int(input("Enter how many elements you want in the list: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

# Step 2: Sort the list in ascending order
numbers.sort()   # in-place sorting

print("List in ascending order:", numbers)
#-----------------output-----------------------
'''--------------------
Enter how many elements you want in the list: 5
Enter element 1: 30
Enter element 2: 10
Enter element 3: 50
Enter element 4: 20
Enter element 5: 40
Original list: [30, 10, 50, 20, 40]
List in ascending order: [10, 20, 30, 40, 50]
---------------------------'''
