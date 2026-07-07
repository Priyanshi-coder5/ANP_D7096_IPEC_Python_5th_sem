#-----------e-commerce membership system-----------

'''A customer becomes Premium Member if:
 Total Purchases > ₹50,000
 Orders Completed ≥ 20
 Customer Rating ≥ 4.5
Special Case:
 Purchases above ₹1,00,000 automatically qualify.
 ---------------------------------------
Sample Input
Total Purchases: 120000
Orders Completed: 10
Customer Rating: 4.0
---------------------------------------
Sample Output
Premium Membership Status: Eligible
Reason: Purchase amount exceeded ₹100000.
-----------------------------------------'''
#----------------code-------------------
# Premium Membership Validation Program

# Input
purchases = int(input("Total Purchases: "))
orders = int(input("Orders Completed: "))
rating = float(input("Customer Rating: "))

# Logic
if purchases > 100000:
    status = "Eligible"
    reason = "Purchase amount exceeded ₹100000."
elif purchases > 50000 and orders >= 20 and rating >= 4.5:
    status = "Eligible"
    reason = "All conditions satisfied (Purchases > 50000, Orders ≥ 20, Rating ≥ 4.5)."
else:
    status = "Not Eligible"
    reason = "Conditions not satisfied."

# Output
print("Premium Membership Status:", status)
print("Reason:", reason)
#--------output------------
'''
Total Purchases: 120000
Orders Completed: 10
Customer Rating: 4.0
Premium Membership Status: Eligible
Reason: Purchase amount exceeded ₹100000.
-----------------------------------------'''

