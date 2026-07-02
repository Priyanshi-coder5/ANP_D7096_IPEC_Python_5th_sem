#-------problem statement-----------
''' Program to reverse the order of elements in a list'''

#----------------coding-----------------------

# Step 1: Input list size and elements
n = int(input("Enter how many elements you want in the list: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

# Step 2: Reverse the list
reversed_list = numbers[::-1]   # slicing method

print("Reversed list:", reversed_list)

#-----------------output-----------------------
'''--------------------
Enter how many elements you want in the list: 5
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
Enter element 5: 50
Original list: [10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]
---------------------------'''
