#-----------problem statement----------------------- 
'''Program to create a list of 10 numbers and delete an element at a given index'''

numbers = []

# Input 10 numbers from the user
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Ask the user for the index to delete
index = int(input("Enter the index (0-9) of the element to delete: "))

# Check if the index is valid
if 0 <= index < len(numbers):
    deleted = numbers.pop(index)
    print("Deleted element:", deleted)
    print("Updated List:", numbers)
else:
    print("Invalid index! Please enter an index between 0 and 9.")


#--------------output-----------------------
'''--------------------
 Enter 10 numbers:
 Enter number 1: 52
 Enter number 2: 10
 Enter number 3: 15
 Enter number 4: 20
 Enter number 5: 25
 Enter number 6: 30
 Enter number 7: 35
 Enter number 8: 40
 Enter number 9: 45
 Enter number 10: 50
 Original List: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
 Enter the index (0-9) of the element to delete: 4
 Deleted element: 25
 Updated List: [5, 10, 15, 20, 30, 35, 40, 45, 50]
 ---------------------'''