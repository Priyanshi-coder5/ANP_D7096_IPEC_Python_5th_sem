#----------------problem statement------------------
'''Write a python program to count the number of vowels in a string.'''


#----------------coding----------------------
# Step 1: Take input from user
string = input("Enter a string: ")

# Step 2: Initialize vowel count
vowel_count = 0

# Step 3: Define vowels
vowels = "aeiouAEIOU"

# Step 4: Count vowels
for char in string:
    if char in vowels:
        vowel_count += 1

# Step 5: Display result
print("Number of vowels in the string:", vowel_count)


# Step 2: Calculate total price
total_price = price_per_unit * quantity

# Step 3: Display result
print("\nProduct:", product_name)
print("Price per unit:", price_per_unit)
print("Quantity:", quantity)
print("Total Price =", total_price)
  

#----------output---------------------------
'''Enter a string: Hello World
Number of vowels in the string: 3
'''