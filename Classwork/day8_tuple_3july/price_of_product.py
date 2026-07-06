#----------------problem statement------------------
'''Write a python program to take product name, price per unit and quantity from user and calculate total price.'''


#----------------coding----------------------
# Step 1: Take input from user
product_name = input("Enter product name: ")
price_per_unit = float(input("Enter price per unit: "))
quantity = int(input("Enter quantity: "))

# Step 2: Calculate total price
total_price = price_per_unit * quantity

# Step 3: Display result
print("\nProduct:", product_name)
print("Price per unit:", price_per_unit)
print("Quantity:", quantity)
print("Total Price =", total_price)

#----------output---------------------------
'''Enter product name: Rice
Enter price per unit: 50
Enter quantity: 10
----------------------
Product: Rice
Price per unit: 50.0
Quantity: 10
Total Price = 500.0
'''