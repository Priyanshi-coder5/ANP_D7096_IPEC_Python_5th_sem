#-----------problem statement-----------------------
'''program to find all odd numbers in a list of 10 numbers'''

#-----------------coding-----------------------


numbers = []
print("Enter 10 numbers ")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

print("Odd numbers are:")
for num in numbers:
    if num % 2 != 0:   # check if odd
        print(num)
#-----------------output-----------------------
'''--------------------
Enter 10 numbers
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
Odd numbers are: 5, 15, 25, 35, 45
---------------------------'''

