'''Assign access levels based on:
Roles:
• Admin
• Manager
• Employee
• Guest
Conditions:
• Admin + Security Clearance ≥ 5 → Full Access
• Manager + Experience > 5 Years → Department Access
• Employee + Experience > 2 Years → Limited Access
• Guest → Read-Only Access
• Inactive Account → No Access
--------------------------------
Sample Input
Role: Admin
Security Clearance: 6
Account Status: Active
--------------------------------
Sample Output
Access Level: FULL ACCESS'''
#----------------code-------------------
# Access Level Assignment Program

# Input
role = input("Role: ").strip().capitalize()
account_status = input("Account Status (Active/Inactive): ").strip().capitalize()

# Extra inputs depending on role
security_clearance = 0
experience = 0

if role == "Admin":
    security_clearance = int(input("Security Clearance: "))
elif role in ["Manager", "Employee"]:
    experience = int(input("Experience (Years): "))

# Logic
if account_status == "Inactive":
    access = "No Access"
elif role == "Admin" and security_clearance >= 5:
    access = "Full Access"
elif role == "Manager" and experience > 5:
    access = "Department Access"
elif role == "Employee" and experience > 2:
    access = "Limited Access"
elif role == "Guest":
    access = "Read-Only Access"
else:
    access = "No Access"

# Output
print("Access Level:", access.upper())
#--------output------------
'''
Role: admin
Account Status (Active/Inactive): active
Security Clearance: 6
Access Level: FULL ACCESS 
----------------------  '''
