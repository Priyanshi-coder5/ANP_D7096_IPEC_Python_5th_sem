# Program to find remaining pizza slices after equal distribution

# Input: Total Pizza Slices and Number of Children
total_slices = int(input("Enter the total number of pizza slices: "))
children = int(input("Enter the number of children: "))


remaining_slices = total_slices % children

# Output: Remaining Slices
print("Remaining slices after distribution:", remaining_slices)

Enter the total number of pizza slices: 8
Enter the number of children: 4
Remaining slices after distribution: 0
