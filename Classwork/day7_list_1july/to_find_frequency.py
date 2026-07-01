#---------------problem statement-----------------------
'''Program to find the frequency of each element in a list'''


#-----------------coding-----------------------
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers entered:", numbers)

# Find frequency of each element
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency of each element:")
for num, freq in frequency.items():
    print(f"{num}: {freq}")
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
Numbers entered: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
Frequency of each element:
5: 1
10: 1
15: 1
20: 1
25: 1
30: 1
35: 1
40: 1
45: 1
50: 1
---------------------------'''