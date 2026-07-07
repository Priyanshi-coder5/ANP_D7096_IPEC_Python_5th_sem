#--------Calculate electricity bill using selection statements----------
'''Units Rate
0-100 ₹5/unit
101-300 ₹7/unit
Above 300 ₹10/unit
Additional Rules:
 Commercial consumers pay 20% extra.
 Bills above ₹5000 attract 5% surcharge.
 Senior citizens receive 10% discount.
 --------------------------------
Sample Input
Units Consumed: 450
Consumer Type (Residential/Commercial): Commercial
Senior Citizen (Y/N): Y
--------------------------------
Sample Output
Base Bill: ₹4500
Commercial Charge: ₹900
Surcharge: ₹270
Senior Citizen Discount: ₹567
Final Bill Amount: ₹5103
--------------------------------'''
#----------------code-------------------
# Electricity Bill Calculation Program

# Input
units = int(input("Units Consumed: "))
consumer_type = input("Consumer Type (Residential/Commercial): ").strip().capitalize()
senior_citizen = input("Senior Citizen (Y/N): ").strip().upper()

# Step 1: Calculate Base Bill
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + (units - 100) * 7
else:
    base_bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# Step 2: Commercial Charge
commercial_charge = 0
if consumer_type == "Commercial":
    commercial_charge = base_bill * 0.20

# Step 3: Surcharge (if bill > 5000)
surcharge = 0
if base_bill + commercial_charge > 5000:
    surcharge = (base_bill + commercial_charge) * 0.05

# Step 4: Senior Citizen Discount
discount = 0
if senior_citizen == "Y":
    discount = (base_bill + commercial_charge + surcharge) * 0.10

# Step 5: Final Bill
final_bill = base_bill + commercial_charge + surcharge - discount

# Output
print("Base Bill: ₹", base_bill)
print("Commercial Charge: ₹", commercial_charge)
print("Surcharge: ₹", surcharge)
print("Senior Citizen Discount: ₹", discount)
print("Final Bill Amount: ₹", final_bill)
#--------output------------
'''
Units Consumed: 450
Consumer Type (Residential/Commercial): Commercial
Senior Citizen (Y/N): Y
--------------------
Base Bill: ₹4500
Commercial Charge: ₹900
Surcharge: ₹270
Senior Citizen Discount: ₹567
Final Bill Amount: ₹5103
--------------------------------'''
