#---------------problem statement-----------------------
'''program to deploy elements at odd positions in a list of 10 numbers'''




#-----------------coding-----------------------
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

# Extract elements at odd positions (1, 3, 5, ...)
odd_position_elements = [numbers[i] for i in range(1, 10, 2)]
print("Elements at odd positions:", odd_position_elements)
#-----------------output-----------------------

'''--------------------
Enter 10 numbers:
Enter number 1: 5
Enter number 2: 10
Enter number 3: 15
Enter number 4: 20
Enter number 5: 25
Enter number 6: 30
Enter number 7: 35
Enter number 8: 40
Enter number 9: 45
Enter number 10: 50
Original list: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
Elements at odd positions: [10, 20, 30, 40, 50]
---------------------------'''