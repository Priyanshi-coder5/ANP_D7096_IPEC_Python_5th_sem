#-------Problem Statement---------
'''A hospital prioritizes patients based on:
 Critical Condition
 Age
 Oxygen Level
Rules:
 Critical condition → Immediate Treatment
 Oxygen below 90 → High Priority
Age above 65 → Medium Prioritizes 
Others → Normal Priority '''
#----------------code-------------------
# Hospital Patient Prioritization Program

# Input
critical = input("Critical Condition (Y/N): ").strip().upper()
age = int(input("Age: "))
oxygen = int(input("Oxygen Level: "))

# Logic
if critical == "Y":
    priority = "Immediate Treatment"
    reason = "Critical Condition"
elif oxygen < 90:
    priority = "High Priority"
    reason = "Low Oxygen Level"
elif age > 65:
    priority = "Medium Priority"
    reason = "Senior Citizen"
else:
    priority = "Normal Priority"
    reason = "Stable Condition"

# Output
print("Patient Priority:", priority)
print("Reason:", reason)
#--------output------------
'''
Critical Condition (Y/N): n
Age: 70
Oxygen Level: 94
Patient Priority: Medium Priority
Reason: Senior Citizen
----------------------'''

