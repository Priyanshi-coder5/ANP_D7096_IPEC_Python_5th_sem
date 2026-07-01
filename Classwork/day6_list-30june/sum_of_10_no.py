#--------problem statement-------
''' Program to find the sum of 10 numbers'''

total = 0

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print("The sum of 10 numbers is:", total)
#------------------coding-----------------------
'''Enter 10 numbers:
Enter number 1: 5
Enter number 2: 10
Enter number 3: 15
Enter number 4: 20
Enter number 5: 25  
Enter number 6: 30
Enter number 7: 35
Enter number 8: 40
Enter number 9: 45
Enter number 10: 20
The sum of 10 numbers is: 120
'''