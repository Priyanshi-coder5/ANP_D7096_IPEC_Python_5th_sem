#----problem statement------------------
'''Create a dictionary where:
• Employee ID is the key.
• Value is another dictionary containing:
--------------------------------------------
o Name
o Department
o Salary
-------------------------------------------
Perform the following operations:
• Display all employee details.
• Search for an employee using Employee ID.
• Increase the salary of all employees by 10%.
• Display employees belonging to a specific department entered by the user.
---------------------------------------'''
#-----------coding----------------------


# Step 1: Create dictionary with Employee ID as key
employees = {
    101: {"Name": "Aman", "Department": "HR", "Salary": 30000},
    102: {"Name": "Priya", "Department": "IT", "Salary": 45000},
    103: {"Name": "Rohit", "Department": "Finance", "Salary": 40000},
    104: {"Name": "Sneha", "Department": "IT", "Salary": 50000},
    105: {"Name": "Karan", "Department": "Sales", "Salary": 35000}
}

# Step 2: Display all employee details
print("All Employee Details:")
for emp_id, details in employees.items():
    print("ID:", emp_id, "=>", details)

# Step 3: Search employee by ID
search_id = int(input("\nEnter Employee ID to search: "))
if search_id in employees:
    print("Employee Found:", employees[search_id])
else:
    print("Employee not found!")

# Step 4: Increase salary of all employees by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] *= 1.10

print("\nAfter 10% Salary Increment:")
for emp_id, details in employees.items():
    print("ID:", emp_id, "=>", details)

# Step 5: Display employees of a specific department
dept = input("\nEnter department name to filter employees: ")
print(f"Employees in {dept} Department:")
for emp_id, details in employees.items():
    if details["Department"].lower() == dept.lower():
        print("ID:", emp_id, "=>", details)

#----------------output---------------------------
'''All Employee Details:
ID: 101 => {'Name': 'Aman', 'Department': 'HR', 'Salary': 30000}
ID: 102 => {'Name': 'Priya', 'Department': 'IT', 'Salary': 45000}
ID: 103 => {'Name': 'Rohit', 'Department': 'Finance', 'Salary': 40000}
ID: 104 => {'Name': 'Sneha', 'Department': 'IT', 'Salary': 50000}
ID: 105 => {'Name': 'Karan', 'Department': 'Sales', 'Salary': 35000}
--------------------------------'''