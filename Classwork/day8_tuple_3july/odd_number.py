#-----------problem statement----------------
'''Write a python program to create a tuple with numbers and print one by one all the odd'''

#--------coding----------------------

# Step 1: Take input from user
numbers = []
for i in range(15):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 2: Convert list to tuple
num_tuple = tuple(numbers)

# Step 3: Display odd numbers
print("\nTuple created:", num_tuple)
print("Odd numbers in the tuple are:")

for n in num_tuple:
    if n % 2 != 0:
        print(n, end=" ")



#----------------------output---------------------------
'''Enter number 1: 10
Enter number 2: 15
Enter number 3: 22
---------------------
Enter number 15: 33

Tuple created: (10, 15, 22, ..., 33)
Odd numbers in the tuple are:
15 33
-----------'''