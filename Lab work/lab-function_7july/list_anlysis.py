'''Problem Statement 2: List Analysis using Functions
Write a Python program that defines the following functions:
• find_max(numbers)
• find_min(numbers)
• find_average(numbers)
---------------------------------------
The program should:
• Accept a list of 10 integers from the user.
• Call all three functions.
• Display the maximum value, minimum value, and average of the list.
---------------------------------------'''
#--------------------------coding----------------------
# Function to find maximum value
def find_max(numbers):
    return max(numbers)

# Function to find minimum value
def find_min(numbers):
    return min(numbers)

# Function to find average value
def find_average(numbers):
    return sum(numbers) / len(numbers)

# Main program
numbers = []  # empty list

# Accept 10 integers from user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Call functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display results
print("Numbers entered:", numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Average value:", average)

#--------------output---------------------------
'''Numbers entered: [12, 45, 7, 89, 23, 56, 34, 78, 15, 67]
Maximum value: 89
Minimum value: 7
Average value: 42.6'''
 