#-----------university scholarship system-----------
'''Scholarship is awarded based on percentage:
Percentage Scholarship
95+ 100%
90-94 75%
85-89 50%
80-84 25%
---------------------------
Below 80 No Scholarship
Conditions:
Family income must be below ₹8,00,000. Students with disciplinary actions receive no scholarship.
--------------------
Sample Input
Percentage: 92
Family Income: 500000
Disciplinary Action (Y/N): N
------------------------
Sample Output
Scholarship Awarded: 75%
--------------------------'''
#----------------code-------------------
# Scholarship Award Program

# Input
percentage = float(input("Percentage: "))
family_income = int(input("Family Income: "))
disciplinary_action = input("Disciplinary Action (Y/N): ").strip().upper()

# Logic
scholarship = "No Scholarship"

if family_income >= 800000:
    scholarship = "No Scholarship (Income above limit)"
elif disciplinary_action == "Y":
    scholarship = "No Scholarship (Disciplinary Action)"
else:
    if percentage >= 95:
        scholarship = "100%"
    elif percentage >= 90:
        scholarship = "75%"
    elif percentage >= 85:
        scholarship = "50%"
    elif percentage >= 80:
        scholarship = "25%"
    else:
        scholarship = "No Scholarship"

# Output
print("Scholarship Awarded:", scholarship)
#--------output------------
'''
Percentage: 92
Family Income: 500000
Disciplinary Action (Y/N): N
Scholarship Awarded: 75%
-----------------------------'''