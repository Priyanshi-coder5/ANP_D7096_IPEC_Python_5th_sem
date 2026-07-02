#----------problem statement----------
'''Program to update an element in a list'''
#---------------coding-----------------------
# Create a sample list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

#Ask user which position to update
position = int(input("Enter the position (index) you want to update (0-4): "))

#Ask user for the new value
new_value = int(input("Enter the new value: "))

# Update the list
numbers[position] = new_value

# Display updated list
print("Updated list:", numbers)
#-----------------output-----------------------
'''--------------------
Original list: [10, 20, 30, 40, 50]
Enter the position (index) you want to update (0-4): 2
Enter the new value: 35
Updated list: [10, 20, 35, 40, 50]
'''
