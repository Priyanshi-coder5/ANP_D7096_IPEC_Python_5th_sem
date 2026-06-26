#Problem Statement 
''' A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or moreOtherwise,
 the customer must pay a parking fee of ₹100. Write a Python program to accept the purchase amount and display whether the parking fee is
 waived or payable '''
#---------------------coding------------------------------------------------------
# Program to check parking fee waiver with validation

# Input: Purchase amount
try:
    purchase_amount = float(input("Enter the purchase amount: ₹"))

    # Validation: purchase amount must be non-negative
    if purchase_amount < 0:
        print("Invalid input! Purchase amount cannot be negative.")
    else:
        # Check condition for parking fee
        if purchase_amount >= 2000:
            print("Parking Fee Waived!")
            print("Parking Fee: ₹0")
        else:
            print("Parking Fee Applicable!")
            print("Parking Fee: ₹100")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

 #--------------------------------------------------------------
 # Output:
'''Enter the purchase amount: 2500
Parking Fee Waived!
Parking Fee: ₹0 '''

'''Enter the purchase amount: 1500
Parking Fee Applicable!
Parking Fee: ₹100 '''
 
'''Enter the purchase amount: -500
Invalid input! Purchase amount cannot be negative.'''



