#---------problem statement-----------
''' Program to return frequency of a given element in a list'''

#----------------coding-----------------------

# Step 1: Input list size and elements
n = int(input("Enter how many elements you want in the list: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

# Step 2: Ask user for the element whose frequency is to be found
target = int(input("\nEnter the element to find its frequency: "))

# Step 3: Calculate frequency
frequency = numbers.count(target)

# Step 4: Display result
if frequency > 0:
    print(f"\nThe element {target} occurs {frequency} time(s) in the list.")
else:
    print(f"\nThe element {target} is not present in the list.")


#-----------------output-----------------------
'''--------------------
Enter how many elements you want in the list: 5
Enter element 1: 10
Enter element 2: 20
Enter element 3: 10
Enter element 4: 30
Enter element 5: 10
Original list: [10, 20, 10, 30, 10]
Enter the element to find its frequency: 10
The element 10 occurs 3 time(s) in the list.
---------------------------'''
