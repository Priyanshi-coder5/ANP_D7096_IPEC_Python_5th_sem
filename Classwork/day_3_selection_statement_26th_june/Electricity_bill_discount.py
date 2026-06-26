#Problem Statement------------------------------------------------------------
'''An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000
or more. Otherwise, no discount is applied.
Write a Python program to accept the total bill amount from the user and display the final amount to
be paid. 
--------------------------------------------------------------

Enter the electricity bill amount: 6200
---------------------------
Sample Output 1
Discount Applied!
Final Bill Amount: ₹5580.0
----------------------------
Sample Input 2
Enter the electricity bill amount: 4200
--------------------------
Sample Output 2
No Discount Applied!
Final Bill Amount: ₹4200
---------------------------------------------------------------'''
# ---------coding------------------------------------------------------

# Program to calculate electricity bill with discount

# Input: Total bill amount
bill_amount = float(input("Enter the electricity bill amount: ₹"))

# Check discount condition
if bill_amount >= 5000:
    discount = bill_amount * 0.10   # 10% discount
    final_amount = bill_amount - discount
    print("Discount Applied!")
else:
    final_amount = bill_amount
    print("No Discount Applied!")

# Output
print("Final Bill Amount: ₹", final_amount)
#-------------------------------------------------------------
'''Output: 
Enter the electricity bill amount: 6200
Discount Applied!
Final Bill Amount: ₹ 5580.0'''
'''Output:
Enter the electricity bill amount: 4200
No Discount Applied!
Final Bill Amount: ₹ 4200.0'''

