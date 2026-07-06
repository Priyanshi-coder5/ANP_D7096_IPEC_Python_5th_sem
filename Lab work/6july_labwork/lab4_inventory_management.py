'''create a dictionary to maintain the stock of products in a shop.
Example:
{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10
}
----------------------------------
Implement the following:
• Add a new product.
• Update the stock of an existing product.
• Remove a product from inventory.
• Display products having stock less than 20.
• Display the total number of items available in the inventory.
----------------------------------'''
#-----------coding----------------------
# Lab: Shop Inventory Management

# Step 1: Create dictionary with initial stock
inventory = {
    'Laptop': 15,
    'Mouse': 40,
    'Keyboard': 25,
    'Monitor': 10
}

# Step 2: Display all products
print("Current Inventory:")
for product, stock in inventory.items():
    print(product, ":", stock)

# Step 3: Add a new product
new_product = input("\nEnter new product name: ")
new_stock = int(input("Enter stock quantity: "))
inventory[new_product] = new_stock
print("\nAfter adding new product:", inventory)

# Step 4: Update stock of an existing product
update_product = input("\nEnter product name to update stock: ")
if update_product in inventory:
    new_stock = int(input("Enter updated stock: "))
    inventory[update_product] = new_stock
    print(update_product, "stock updated to", new_stock)
else:
    print("Product not found!")

# Step 5: Remove a product
remove_product = input("\nEnter product name to remove: ")
if remove_product in inventory:
    del inventory[remove_product]
    print(remove_product, "removed successfully!")
else:
    print("Product not found!")

print("\nRemaining Inventory:", inventory)

# Step 6: Display products with stock less than 20
print("\nProducts with stock less than 20:")
for product, stock in inventory.items():
    if stock < 20:
        print(product, ":", stock)

# Step 7: Display total number of items in inventory
total_items = sum(inventory.values())
print("\nTotal number of items in inventory:", total_items)

#----------------output---------------------------
'''Current Inventory:
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10
Enter new product name: Printer
Enter stock quantity: 30
After adding new product: {'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Printer': 30}
Enter product name to update stock: Mouse
Enter updated stock: 35
Mouse stock updated to 35
Enter product name to remove: Monitor
Monitor removed successfully!
Remaining Inventory: {'Laptop': 15, 'Mouse': 35, 'Keyboard': 25, 'Printer': 30}
Products with stock less than 20:
Laptop : 15
Total number of items in inventory: 105
'''