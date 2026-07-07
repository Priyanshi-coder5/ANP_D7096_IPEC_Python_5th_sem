''' Program to calculate Simple Interest'''

# Step 1: Take inputs from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (per annum): "))
time = float(input("Enter Time (in years): "))

# Step 2: Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Step 3: Display result
print("Simple Interest =", simple_interest)


#--------------output----------------------------
'''Enter Principal Amount: 5000
Enter Rate of Interest (per annum): 10
Enter Time (in years): 2
Simple Interest = 1000.0
'''
