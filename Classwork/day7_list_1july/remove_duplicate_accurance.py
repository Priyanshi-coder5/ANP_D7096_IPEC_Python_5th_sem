# Program to create a list of 20 numbers and remove duplicates of a given number

# Input 20 numbers from the user
numbers = []
print("Enter 20 numbers")
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

# Ask user for another number
target = int(input("\nEnter a number to remove its duplicate occurrences: "))

#Remove all duplicate occurrences (keep only one if present)
if target in numbers:
    # Count how many times it appears
    count = numbers.count(target)
    if count > 1:
        # Remove all occurrences
        numbers = [x for x in numbers if x != target]
        # Add back a single occurrence
        numbers.append(target)
        print(f"\nRemoved {count-1} duplicate(s) of {target}.")
    else:
        print(f"\n{target} occurs only once, no duplicates to remove.")
else:
    print(f"\n{target} is not present in the list.")

# Step 4: Show final list
print("Updated list:", numbers)
#--------------output-----------------------
'''--------------------
Enter 20 numbers
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
Enter number 11: 55
Enter number 12: 60
Enter number 13: 65
Enter number 14: 70
Enter number 15: 75
Enter number 16: 80
Enter number 17: 85
Enter number 18: 90
Enter number 19: 95
Enter number 20: 100
Original list: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
Enter a number to remove its duplicate occurrences: 25
Removed 1 duplicate of 25.
Updated list: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
---------------------------'''